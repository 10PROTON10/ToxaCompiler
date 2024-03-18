import json
from antlr4 import FileStream, CommonTokenStream
from ToxaLanguageLexer import ToxaLanguageLexer
from ToxaLanguageVisitor import ToxaLanguageVisitor
from ToxaLanguageParser import ToxaLanguageParser

# Создаем класс посетителя для обхода дерева разбора и создания AST
class ASTBuilder(ToxaLanguageVisitor):
    def __init__(self):
        self.ast = []

    # Обход узлов expression
    def visitExpression(self, ctx: ToxaLanguageParser.ExpressionContext):
        if ctx.INT():
            node = {"type": "INT", "value": int(ctx.INT().getText())}
            self.add_ast_node(node)
            return node
        elif ctx.PLUS():
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            node = {"type": "PLUS", "left": left, "right": right}
            self.add_ast_node(node)
            return node
        elif ctx.MULT():
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            node = {"type": "MULT", "left": left, "right": right}
            self.add_ast_node(node)
            return node
        elif ctx.OPEN_PAREN():
            return self.visit(ctx.expression(0))
        else:
            return None

    # Добавление новых узлов AST
    def add_ast_node(self, node):
        self.ast.append(node)

    # Сохранение AST в JSON файл
    def save_ast_to_json(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.ast, file, indent=4)

if __name__ == "__main__":
    input_code = FileStream("input_program.txt")
    lexer = ToxaLanguageLexer(input_code)
    tokens = CommonTokenStream(lexer)
    parser = ToxaLanguageParser(tokens)
    tree = parser.expression()

    ast_builder = ASTBuilder()
    ast_builder.visit(tree)
    ast_builder.save_ast_to_json("ast.json")
