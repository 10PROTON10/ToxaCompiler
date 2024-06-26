import json
from antlr4 import FileStream, CommonTokenStream
from ToxaLanguageLexer import ToxaLanguageLexer
from ToxaLanguageParser import ToxaLanguageParser
from ToxaLanguageVisitor import ToxaLanguageVisitor
from antlr4.error.ErrorListener import ErrorListener

class MyErrorListener(ErrorListener):
    def __init__(self):
        self.has_errors = False

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.has_errors = True
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
                "type": ctx.type_().getText().upper(),
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
        elif ctx.expression():
            left = self.visit(ctx.expression(0))
            operator_text = ctx.getChild(1).getText()
            operator = "AND" if operator_text == "&&" else "OR" if operator_text == "||" else operator_text
            right = self.visit(ctx.expression(1))
            return {"logical": {"operator": operator, "left": left, "right": right}}

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
                "if_body": [self.visit(statement) for statement in ctx.ifBlock().statement()]
            }
        }
        return node

    def visitIfElseStatement(self, ctx: ToxaLanguageParser.IfElseStatementContext):
        if_else_statement = {
            "ifElseStatement": {
                "condition": self.visit(ctx.expression()),
                "if_body": [self.visit(statement) for statement in ctx.ifBlock().statement()],
                "else_body": [self.visit(statement) for statement in ctx.elseBlock().statement()]
            }
        }
        return if_else_statement

    def visitForStatement(self, ctx: ToxaLanguageParser.ForStatementContext):
        for_statement = {
            "forStatement": {
                "initializer": self.visit(ctx.forInitializer()),
                "condition": self.visit(ctx.forCondition()) if ctx.forCondition() else None,
                "update": self.visitForUpdate(ctx.forUpdate()),  # Обработка оператора обновления
                "body": [self.visit(statement) for statement in ctx.forBlock().statement()]
            }
        }
        return for_statement

    def visitForInitializer(self, ctx: ToxaLanguageParser.ForInitializerContext):
        initializer = {
            "type": ctx.type_().getText(),
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
                "body": [self.visit(statement) for statement in ctx.whileBlock().statement()]
            }
        }
        return while_statement

    def visitFunctionStatement(self, ctx: ToxaLanguageParser.FunctionStatementContext):
        params = []
        if ctx.params():
            params = self.visitParams(ctx.params())
        function_statement = {
            "functionStatement": {
                "name": ctx.ID().getText(),
                "params": params,
                "body": [self.visit(statement) for statement in ctx.functionBlock().statement()]
            }
        }
        return function_statement

    def visitParams(self, ctx: ToxaLanguageParser.ParamsContext):
        params = []
        for i in range(len(ctx.type_())):
            param_type = ctx.type_(i).getText()
            param_name = ctx.operand(i).getText()
            params.append({"type": param_type.upper(), "value": param_name})
        return params

    def visitFunctionCall(self, ctx: ToxaLanguageParser.FunctionCallContext):
        name = ctx.ID().getText()
        params = [self.visit(param) for param in ctx.paramsCall().operand()] if ctx.paramsCall() else []
        return {
            "type": "functionCall",
            "functionCall": {
                "name": name,
                "params": params
            }
        }

    def visitReturnStatement(self, ctx: ToxaLanguageParser.ReturnStatementContext):
        return_statement = {
            "returnStatement": {
                "expression": self.visit(ctx.expression()) if ctx.expression() else None
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

        # Функция для обработки операций с более высоким приоритетом
        def handle_high_priority_ops(operands, operators):
            result = []
            i = 0
            while i < len(operators):
                if operators[i] in ("*", "/"):
                    left = operands.pop(i)
                    right = operands.pop(i)
                    op = operator_mapping[operators.pop(i)]
                    operands.insert(i, {"arithmetic": {"operator": op, "left": left, "right": right}})
                else:
                    result.append((operands[i], operators[i]))
                    i += 1
            result.append((operands[i], None))  # Добавляем последний операнд
            return result

        # Обрабатываем операции умножения и деления
        processed = handle_high_priority_ops(operands, operators)

        # Инициализируем переменную result значением первого операнда
        result = processed[0][0]

        # Перебираем операторы и операнды, чтобы вычислить результат
        for i in range(1, len(processed)):
            operator = operator_mapping[processed[i - 1][1]]
            right = processed[i][0]
            # Строим вложенную структуру с использованием вычисленного результата и следующего операнда
            result = {"arithmetic": {"operator": operator, "left": result, "right": right}}

        # Возвращаем вычисленный результат
        return result

    def visitLogical(self, ctx: ToxaLanguageParser.LogicalContext):
        left = self.visit(ctx.operand(0))
        right = self.visit(ctx.operand(1))
        operator = ctx.children[1].getText()  # Получаем логический оператор
        return {"logical": operator, "left": left, "right": right}
#
# # Код для запуска парсера и создания AST
# def main():
#     input_file = "input_program.txt"
#     output_file = "ast.json"
#
#     input_stream = FileStream(input_file)
#     lexer = ToxaLanguageLexer(input_stream)
#     lexer.removeErrorListeners()
#     lexer.addErrorListener(MyErrorListener())
#     stream = CommonTokenStream(lexer)
#     parser = ToxaLanguageParser(stream)
#     parser.removeErrorListeners()
#     parser.addErrorListener(MyErrorListener())
#     tree = parser.program()
#
#     ast_builder = ASTBuilder()
#     ast = ast_builder.visit(tree)
#
#     with open(output_file, "w") as f:
#         json.dump(ast, f, indent=4)
#
# if __name__ == '__main__':
#     main()
