import json
from antlr4 import FileStream, CommonTokenStream
from ToxaLanguageLexer import ToxaLanguageLexer
from ToxaLanguageParser import ToxaLanguageParser
from ToxaLanguageVisitor import ToxaLanguageVisitor
from antlr4.error.ErrorListener import ErrorListener

class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception("Ошибка на строке " + str(line) + ":" + str(column) + " " + msg)

class ASTBuilder(ToxaLanguageVisitor):
    def __init__(self):
        self.ast = []

    def visitStatement(self, ctx: ToxaLanguageParser.StatementContext):
        return self.visitChildren(ctx)

    def visitProgram(self, ctx: ToxaLanguageParser.ProgramContext):
        for statement_ctx in ctx.statement():
            self.ast.append(self.visit(statement_ctx))
        return self.ast

    def visitAssignmentStatement(self, ctx: ToxaLanguageParser.AssignmentStatementContext):
        assignment = {
            "assignmentStatement": {
                "type": ctx.type_().getText(),
                "ID": ctx.ID().getText(),
                "expression": self.visit(ctx.expression()),
                "END_STATE": ";"
            }
        }
        return assignment

    def visitPrintStatement(self, ctx: ToxaLanguageParser.PrintStatementContext):
        return {
            "printStatement": {
                "expression": self.visit(ctx.expression()),
                "END_STATE": ";"
            }
        }

    def visitExpression(self, ctx: ToxaLanguageParser.ExpressionContext):
        if ctx.arithmetic():
            return self.visit(ctx.arithmetic())
        elif ctx.comparison():
            return self.visit(ctx.comparison())
        elif ctx.logical():
            return self.visit(ctx.logical())
        elif ctx.operand():
            return self.visit(ctx.operand())
        elif ctx.functionCall():
            return self.visit(ctx.functionCall())

    def visitOperand(self, ctx: ToxaLanguageParser.OperandContext):
        if ctx.INT():
            return {"type": "INT", "value": int(ctx.INT().getText())}
        elif ctx.FLOAT():
            return {"type": "FLOAT", "value": float(ctx.FLOAT().getText())}
        elif ctx.ID():
            return {"type": "ID", "value": ctx.ID().getText()}
        elif ctx.functionCall():
            return self.visit(ctx.functionCall())
        elif ctx.LPAREN() and ctx.RPAREN():  # Если операнд является выражением в скобках
            return self.visit(ctx.expression())  # Посещаем выражение внутри скобок

    def visitIfStatement(self, ctx: ToxaLanguageParser.IfStatementContext):
        condition = self.visit(ctx.expression())
        block = [self.visit(statement) for statement in ctx.ifBlock().statement()]
        node = {
            "ifStatement": {
                "condition": condition,
                "if_body": block
            }
        }
        return node

    def visitIfElseStatement(self, ctx: ToxaLanguageParser.IfElseStatementContext):
        if_else_statement = {
            "ifElseStatement": {
                "condition": self.visit(ctx.expression()),
                "if_body": self.visit(ctx.ifBlock()),
                "else_body": self.visit(ctx.elseBlock())
            }
        }
        return if_else_statement

    def visitForStatement(self, ctx: ToxaLanguageParser.ForStatementContext):
        for_statement = {
            "forStatement": {
                "initializer": self.visit(ctx.forInitializer()),
                "condition": self.visit(ctx.forCondition()) if ctx.forCondition() else None,
                "update": self.visitForUpdate(ctx.forUpdate()),  # Обработка оператора обновления
                "body": self.visit(ctx.forBlock())
            }
        }
        return for_statement

    def visitForInitializer(self, ctx: ToxaLanguageParser.ForInitializerContext):
        initializer = {
            "type": "INT",
            "ID": ctx.ID().getText(),  # Получаем имя переменной
            "value": self.visit(ctx.expression())  # Обрабатываем выражение для значения переменной
        }
        return initializer

    def visitForUpdate(self, ctx: ToxaLanguageParser.ForUpdateContext):
        id_name = ctx.ID().getText()  # Получаем имя переменной
        operation = ctx.incrementOrDecrement().getText()  # Получаем оператор инкремента или декремента
        return {"ID": id_name, "operation": operation}

    def visitWhileStatement(self, ctx: ToxaLanguageParser.WhileStatementContext):
        while_statement = {
            "whileStatement": {
                "condition": self.visit(ctx.expression()),
                "body": self.visit(ctx.whileBlock())
            }
        }
        return while_statement

    def visitFunctionStatement(self, ctx: ToxaLanguageParser.FunctionStatementContext):
        params = []
        if ctx.params():
            params = [self.visit(param) for param in ctx.params().operand()]
        function_statement = {
            "functionStatement": {
                "name": ctx.ID().getText(),
                "params": params,
                "body": self.visit(ctx.functionBlock())
            }
        }
        return function_statement

    def visitFunctionCall(self, ctx: ToxaLanguageParser.FunctionCallContext):
        name = ctx.ID().getText()
        params = [self.visit(param) for param in ctx.paramsCall().operand()] if ctx.paramsCall() else []
        return {"functionCall": {"name": name, "params": params}}

    def visitReturnStatement(self, ctx: ToxaLanguageParser.ReturnStatementContext):
        return_statement = {
            "returnStatement": {
                "value": self.visit(ctx.expression()) if ctx.expression() else None
            }
        }
        return return_statement

    def visitComparison(self, ctx: ToxaLanguageParser.ComparisonContext):
        left = self.visit(ctx.operand(0))
        right = self.visit(ctx.operand(1))
        operator = ctx.children[1].getText()  # Получаем оператор сравнения
        return {"comparison": operator, "left": left, "right": right}

    def visitArithmetic(self, ctx: ToxaLanguageParser.ArithmeticContext):
        operands = [self.visit(operand_ctx) for operand_ctx in ctx.operand()]
        operators = [ctx.children[i].getText() for i in range(1, len(ctx.children), 2)]

        # Переводим символьные представления операторов в соответствующие ключи
        operator_mapping = {
            "+": "PLUS",
            "-": "MINUS",
            "*": "MUL",
            "/": "DIV",
            "^": "POW"
        }

        # Инициализируем переменную result значением первого операнда
        result = operands[0]

        # Перебираем операторы и операнды, чтобы вычислить результат
        for i in range(1, len(operands)):
            operator = operator_mapping[operators[i - 1]]
            right = operands[i]

            # Строим вложенную структуру с использованием вычисленного результата и следующего операнда
            result = {"arithmetic": {"operator": operator, "left": result, "right": right}}

        # Возвращаем вычисленный результат
        return result

    def visitLogical(self, ctx: ToxaLanguageParser.LogicalContext):
        left = self.visit(ctx.operand(0))
        right = self.visit(ctx.operand(1))
        operator = ctx.children[1].getText()  # Получаем логический оператор
        return {"logical": operator, "left": left, "right": right}

# Код для запуска парсера и создания AST
def main():
    input_file = "input_program.txt"
    output_file = "ast.json"

    input_stream = FileStream(input_file)
    lexer = ToxaLanguageLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(MyErrorListener())
    stream = CommonTokenStream(lexer)
    parser = ToxaLanguageParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(MyErrorListener())
    tree = parser.program()

    ast_builder = ASTBuilder()
    ast = ast_builder.visit(tree)

    with open(output_file, "w") as f:
        json.dump(ast, f, indent=4)

if __name__ == '__main__':
    main()
