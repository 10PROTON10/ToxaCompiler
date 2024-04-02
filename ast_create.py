import json
from antlr4 import FileStream, CommonTokenStream
from ToxaLanguageLexer import ToxaLanguageLexer
from ToxaLanguageVisitor import ToxaLanguageVisitor
from ToxaLanguageParser import ToxaLanguageParser

class ASTBuilder(ToxaLanguageVisitor):
    def __init__(self):
        self.ast = None

    def visitExpr(self, ctx: ToxaLanguageParser.ExprContext):
        if ctx.PLUS():
            left = self.visit(ctx.term(0))
            right = self.visit(ctx.term(1))
            node = {"type": "PLUS", "left": left, "right": right}
            return node
        elif ctx.MINUS():
            left = self.visit(ctx.term(0))
            right = self.visit(ctx.term(1))
            node = {"type": "MINUS", "left": left, "right": right}
            return node
        else:
            return self.visit(ctx.term(0))

    def visitTerm(self, ctx: ToxaLanguageParser.TermContext):
        if ctx.MULT():
            left = self.visit(ctx.factor(0))
            right = self.visit(ctx.factor(1))
            node = {"type": "MULT", "left": left, "right": right}
            return node
        elif ctx.DIV():
            left = self.visit(ctx.factor(0))
            right = self.visit(ctx.factor(1))
            node = {"type": "DIV", "left": left, "right": right}
            return node
        else:
            return self.visit(ctx.factor(0))

    def visitFactor(self, ctx: ToxaLanguageParser.FactorContext):
        if ctx.INT():
            node = {"type": "INT", "value": int(ctx.INT().getText())}
            return node
        elif ctx.FLOAT():
            node = {"type": "FLOAT", "value": float(ctx.FLOAT().getText())}
            return node
        elif ctx.ID():
            node = {"type": "ID", "value": ctx.ID().getText()}
            return node
        else:
            return self.visit(ctx.expr())

    def visitAssignStatement(self, ctx: ToxaLanguageParser.AssignStatementContext):
        variable_type = ctx.type_().getText()
        variable_name = ctx.ID().getText()
        assigned_value = self.visit(ctx.expr())
        end_state = ctx.END_STATE().getText()
        node = {"type": "ASSIGNMENT", "variable_type": variable_type,
                "variable_name": variable_name, "value": assigned_value, "END_STATE": end_state}
        return node

    def visitPrintStatement(self, ctx: ToxaLanguageParser.PrintStatementContext):
        value_to_print = self.visit(ctx.expr())
        node = {"type": "PRINT", "value": value_to_print}
        return node

    def visitProg(self, ctx: ToxaLanguageParser.ProgContext):
        self.ast = self.visitChildren(ctx)
        return self.ast

    def save_ast_to_json(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.ast, file, indent=4)

if __name__ == "__main__":
    input_code = FileStream("input_program.txt")
    lexer = ToxaLanguageLexer(input_code)
    tokens = CommonTokenStream(lexer)
    parser = ToxaLanguageParser(tokens)
    tree = parser.prog()

    ast_builder = ASTBuilder()
    ast_builder.visit(tree)
    ast_builder.save_ast_to_json("ast.json")






