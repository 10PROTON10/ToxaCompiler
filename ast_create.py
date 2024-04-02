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

    def visitAssignStatement(self, ctx: ToxaLanguageParser.AssignStatementContext):
        variable_type = ctx.type_().getText()  # Получаем тип переменной
        variable_name = ctx.ID().getText()  # Получаем имя переменной
        assigned_value = self.visit(ctx.expr())  # Получаем значение переменной
        node = {"type": "ASSIGNMENT", "variable_type": variable_type,
                "variable_name": variable_name, "value": assigned_value, "END_STATE": ctx.END_STATE().getText()}
        self.add_ast_node(node)
        return node

    def visitPrint(self, ctx: ToxaLanguageParser.ProgContext):
        value_to_print = self.visit(ctx.expr())
        node = {"type": "PRINT", "value": value_to_print, "END_STATE": ctx.END_STATE().getText()}
        self.add_ast_node(node)
        return node

    def visitProg(self, ctx: ToxaLanguageParser.ProgContext):
        return self.visitChildren(ctx)

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
    tree = parser.prog()

    ast_builder = ASTBuilder()
    ast_builder.visit(tree)
    ast_builder.save_ast_to_json("ast.json")



