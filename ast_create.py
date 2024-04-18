import json
from antlr4 import FileStream, CommonTokenStream
from ToxaLanguageLexer import ToxaLanguageLexer
from ToxaLanguageParser import ToxaLanguageParser
from ToxaLanguageVisitor import ToxaLanguageVisitor

class ASTBuilder(ToxaLanguageVisitor):
    def __init__(self):
        self.ast = []

    def visitAssignmentStatement(self, ctx: ToxaLanguageParser.AssignmentStatementContext):
        variable_type = ctx.type_().getText()
        variable_name = ctx.ID().getText()
        assigned_value = self.visit(ctx.expression())
        end_state = ctx.END_STATE().getText()
        node = {
            "type": "ASSIGNMENT",
            "variable_type": variable_type,
            "variable_name": variable_name,
            "value": assigned_value,  # Используем посещенное значение выражения
            "END_STATE": end_state
        }
        self.ast.append(node)

    def visitPrintStatement(self, ctx: ToxaLanguageParser.PrintStatementContext):
        value_to_print = self.visit(ctx.expression())
        node = {"type": "PRINT", "value": value_to_print}
        self.ast.append(node)

    def visitIfStatement(self, ctx: ToxaLanguageParser.IfStatementContext):
        condition = self.visit(ctx.expression())
        block = [self.visit(statement) for statement in ctx.block().statement()]
        else_block = None
        if ctx.elseStatement():
            else_block = [self.visit(statement) for statement in ctx.elseStatement().block().statement()]
        node = {"type": "IF", "condition": condition, "block": block, "else_block": else_block}
        self.ast.append(node)

    def visitWhileStatement(self, ctx: ToxaLanguageParser.WhileStatementContext):
        condition = self.visit(ctx.expression())
        block = [self.visit(statement) for statement in ctx.block().statement()]
        node = {"type": "WHILE", "condition": condition, "block": block}
        self.ast.append(node)

    def visitForStatement(self, ctx: ToxaLanguageParser.ForStatementContext):
        init = self.visit(ctx.forInitializer())
        condition = self.visit(ctx.forCondition()) if ctx.forCondition() else None
        update = self.visit(ctx.forUpdate())
        block = [self.visit(statement) for statement in ctx.block().statement()]
        node = {"type": "FOR", "init": init, "condition": condition, "update": update, "block": block}
        self.ast.append(node)

    def visitFunctionDeclaration(self, ctx: ToxaLanguageParser.FunctionDeclarationContext):
        function_name = ctx.ID().getText()
        parameters = [self.visit(param) for param in ctx.params().expression()]
        block = [self.visit(statement) for statement in ctx.block().statement()]
        node = {"type": "FUNCTION", "function_name": function_name, "parameters": parameters, "block": block}
        self.ast.append(node)

    def visitReturnStatement(self, ctx: ToxaLanguageParser.ReturnStatementContext):
        value = self.visit(ctx.expression()) if ctx.expression() else None
        node = {"type": "RETURN", "value": value}
        self.ast.append(node)

    def visitExpression(self, ctx: ToxaLanguageParser.ExpressionContext):
        if ctx.operand():
            return self.visit(ctx.operand())
        elif ctx.LPAREN():
            return {"type": "PAREN_EXPR",
                    "value": {"LPAREN": "(", "expr": self.visit(ctx.expression(0)), "RPAREN": ")"}}
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
    def visitOperand(self, ctx: ToxaLanguageParser.OperandContext):
        if ctx.INT():
            return {"type": "INT", "value": int(ctx.INT().getText())}
        elif ctx.FLOAT():
            return {"type": "FLOAT", "value": float(ctx.FLOAT().getText())}
        elif ctx.ID():
            return {"type": "ID", "value": ctx.ID().getText()}
        elif ctx.functionCall():
            return self.visit(ctx.functionCall())

    def get_ast(self):
        return self.ast

    def save_ast_to_json(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.ast, file, indent=4)

def ast_create(input_filename="input_program.txt", output_filename="ast.json"):
    input_stream = FileStream(input_filename)
    lexer = ToxaLanguageLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ToxaLanguageParser(token_stream)
    tree = parser.program()

    ast_builder = ASTBuilder()
    ast_builder.visit(tree)
    ast_builder.save_ast_to_json(output_filename)

if __name__ == "__main__":
    ast_create()
