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
            "type": "assignment",
            "variable": ctx.ID().getText(),
            "value": self.visit(ctx.expression())
        }
        return assignment

    def visitPrintStatement(self, ctx: ToxaLanguageParser.PrintStatementContext):
        return {
            "type": "print",
            "value": self.visit(ctx.expression())
        }

    def visitExpression(self, ctx: ToxaLanguageParser.ExpressionContext):
        if ctx.operand():
            return self.visit(ctx.operand())
        elif ctx.GT():
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            return {"type": "GT", "left": left, "right": right}
        elif ctx.LT():
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            return {"type": "LT", "left": left, "right": right}
        elif ctx.GE():
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            return {"type": "GE", "left": left, "right": right}
        elif ctx.LE():
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            return {"type": "LE", "left": left, "right": right}
        elif ctx.EQEQ():
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            return {"type": "EQEQ", "left": left, "right": right}
        elif ctx.NE():
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            return {"type": "NE", "left": left, "right": right}
        elif ctx.AND():
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            return {"type": "AND", "left": left, "right": right}
        elif ctx.OR():
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            return {"type": "OR", "left": left, "right": right}
        elif ctx.PLUS():
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            return {"type": "PLUS", "left": left, "right": right}
        elif ctx.MINUS():
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            return {"type": "MINUS", "left": left, "right": right}
        elif ctx.MUL():
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            return {"type": "MUL", "left": left, "right": right}
        elif ctx.DIV():
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            return {"type": "DIV", "left": left, "right": right}
        elif ctx.REM():
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            return {"type": "REM", "left": left, "right": right}

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
            "type": "IF",
            "condition": condition,
            "block": block
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
            "update": self.visit(ctx.forUpdate()),
            "body": self.visit(ctx.forBlock())
        }
        return for_statement

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
