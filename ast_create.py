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
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            node = {"type": "PLUS", "left": left, "right": right}
            self.add_ast_node(node)
            return node
        elif ctx.MINUS():
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            node = {"type": "MINUS", "left": left, "right": right}
            self.add_ast_node(node)
            return node
        elif ctx.INT():
            node = {"type": "INT", "value": int(ctx.INT().getText())}
            return node
        elif ctx.FLOAT():
            node = {"type": "FLOAT", "value": float(ctx.FLOAT().getText())}
            return node
        elif ctx.MULT():
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            node = {"type": "MULT", "left": left, "right": right}
            self.add_ast_node(node)
            return node
        elif ctx.DIV():
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            node = {"type": "DIV", "left": left, "right": right}
            self.add_ast_node(node)
            return node
        elif ctx.LPAREN():
            return self.visit(ctx.expr(0))
        else:
            return None

    def add_ast_node(self, node):
        self.ast = node

    def save_ast_to_json(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.ast, file, indent=4)


if __name__ == "__main__":
    input_code = FileStream("input_program.txt")
    lexer = ToxaLanguageLexer(input_code)
    tokens = CommonTokenStream(lexer)
    parser = ToxaLanguageParser(tokens)
    tree = parser.expr()

    ast_builder = ASTBuilder()
    ast_builder.visit(tree)
    ast_builder.save_ast_to_json("ast.json")
