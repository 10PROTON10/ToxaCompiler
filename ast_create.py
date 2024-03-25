import json
from antlr4 import FileStream, CommonTokenStream
from ToxaLanguageLexer import ToxaLanguageLexer
from ToxaLanguageVisitor import ToxaLanguageVisitor
from ToxaLanguageParser import ToxaLanguageParser

# Создаем класс посетителя для обхода дерева разбора и создания AST
class ASTBuilder(ToxaLanguageVisitor):
    def __init__(self):
        self.ast = []

    # Добавление узла в AST
    def add_ast_node(self, node):
        self.ast.append(node)

    # Обход узлов multExpr (умножение и деление)
    def visitMultExpr(self, ctx: ToxaLanguageParser.MultExprContext):
        if ctx.MULT():
            left = self.visit(ctx.multExpr())
            right = self.visit(ctx.atom())
            node = {"type": "MULT", "left": left, "right": right}
            return node
        elif ctx.DIV():
            left = self.visit(ctx.multExpr())
            right = self.visit(ctx.atom())
            node = {"type": "DIV", "left": left, "right": right}
            return node
        else:
            return self.visit(ctx.atom())

    # Обход узлов expression (сложение и вычитание)
    def visitExpression(self, ctx: ToxaLanguageParser.ExpressionContext):
        if ctx.PLUS():
            left = self.visit(ctx.expression())
            right = self.visit(ctx.multExpr())
            node = {"type": "PLUS", "left": left, "right": right}
            return node
        elif ctx.MINUS():
            left = self.visit(ctx.expression())
            right = self.visit(ctx.multExpr())
            node = {"type": "MINUS", "left": left, "right": right}
            return node
        else:
            return self.visit(ctx.multExpr())

    # Обход узлов atom (числа и скобки)
    def visitAtom(self, ctx: ToxaLanguageParser.AtomContext):
        if ctx.INT():
            return {"type": "INT", "value": int(ctx.INT().getText())}
        elif ctx.FLOAT():
            return {"type": "FLOAT", "value": float(ctx.FLOAT().getText())}
        elif ctx.OPEN_PAREN():
            return self.visit(ctx.expression())
        else:
            return None

    # Сохранение AST в JSON файл
    def save_ast_to_json(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.ast, file, indent=4)

# Функция для создания AST и сохранения в JSON
def create_ast_and_save_to_json(input_file, output_file="ast.json"):
    input_code = FileStream(input_file)
    lexer = ToxaLanguageLexer(input_code)
    tokens = CommonTokenStream(lexer)
    parser = ToxaLanguageParser(tokens)
    tree = parser.expression()

    ast_builder = ASTBuilder()
    ast_builder.add_ast_node(ast_builder.visit(tree))  # Добавляем корневой узел AST
    ast_builder.save_ast_to_json(output_file)

if __name__ == "__main__":
    create_ast_and_save_to_json("input_program.txt")
