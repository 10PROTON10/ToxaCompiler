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
            "statement": {
                "assignmentStatement": {
                    "type": ctx.type_().getText(),
                    "ID": ctx.ID().getText(),
                    "expr": self.visit(ctx.expression()),
                    "END_STATE": ";"
                }
            }
        }
        return assignment

    def visitPrintStatement(self, ctx: ToxaLanguageParser.PrintStatementContext):
        return {
            "statement": {
                "printStatement": {
                    "expression": self.visit(ctx.expression()),
                    "END_STATE": ";"
                }
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
        elif ctx.LPAREN():
            return self.visit(ctx.expression(0))

    def visitOperand(self, ctx: ToxaLanguageParser.OperandContext):
        if ctx.INT():
            return {"type": "INT", "value": int(ctx.INT().getText())}
        elif ctx.FLOAT():
            return {"type": "FLOAT", "value": float(ctx.FLOAT().getText())}
        elif ctx.ID():
            return {"type": "ID", "value": ctx.ID().getText()}
        elif ctx.functionCall():
            return self.visit(ctx.functionCall())

    def visitIfStatement(self, ctx: ToxaLanguageParser.IfStatementContext):
        condition = self.visit(ctx.expression())
        block = [self.visit(statement) for statement in ctx.ifBlock().statement()]
        node = {
            "statement": {
                "ifStatement": {
                    "condition": condition,
                    "if_body": block
                }
            }
        }
        return node

    def visitIfElseStatement(self, ctx: ToxaLanguageParser.IfElseStatementContext):
        if_else_statement = {
            "type": "if_else",
            "condition": self.visit(ctx.expression()),
            "if_body": self.visit(ctx.ifBlock()),
            "else_body": self.visit(ctx.elseBlock())
        }
        return if_else_statement

    def visitForStatement(self, ctx: ToxaLanguageParser.ForStatementContext):
        for_statement = {
            "type": "for",
            "initializer": self.visit(ctx.forInitializer()),
            "condition": self.visit(ctx.forCondition()) if ctx.forCondition() else None,
            "update": self.visitForUpdate(ctx.forUpdate()),  # Обработка оператора обновления
            "body": self.visit(ctx.forBlock())
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
            "type": "while",
            "condition": self.visit(ctx.expression()),
            "body": self.visit(ctx.whileBlock())
        }
        return while_statement

    def visitFunctionStatement(self, ctx: ToxaLanguageParser.FunctionStatementContext):
        function_statement = {
            "type": "function",
            "name": ctx.ID().getText(),
            "params": [self.visit(param) for param in ctx.params().expression()] if ctx.params() else [],
            "body": self.visit(ctx.functionBlock())
        }
        return function_statement

    def visitReturnStatement(self, ctx: ToxaLanguageParser.ReturnStatementContext):
        return_statement = {
            "type": "return",
            "value": self.visit(ctx.expression()) if ctx.expression() else None
        }
        return return_statement

    def visitComparison(self, ctx: ToxaLanguageParser.ComparisonContext):
        left = self.visit(ctx.operand(0))
        right = self.visit(ctx.operand(1))
        operator = ctx.children[1].getText()  # Получаем оператор сравнения
        return {"comparison": operator, "left": left, "right": right}

    def visitArithmetic(self, ctx: ToxaLanguageParser.ArithmeticContext):
        left = self.visit(ctx.operand(0))
        right = self.visit(ctx.operand(1))
        operator = ctx.children[1].getText()  # Получаем арифметический оператор
        return {"arithmetic": operator, "left": left, "right": right}

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
