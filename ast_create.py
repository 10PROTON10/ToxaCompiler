import json
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from ToxaLanguageLexer import ToxaLanguageLexer
from ToxaLanguageParser import ToxaLanguageParser
from ToxaLanguageVisitor import ToxaLanguageVisitor
from antlr4.error.ErrorListener import ErrorListener
from antlr4 import *

class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print("Ошибка синтаксиса на строке", line, "и столбце", column, ":", msg)

class ASTbuilder(ToxaLanguageVisitor):
    def __init__(self):
        self.ast = []

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
        elif ctx.LPAREN():
            expr_node = self.visit(ctx.expr())  # Обработка выражений в скобках
            lparen = ctx.LPAREN().getText()
            rparen = ctx.RPAREN().getText()
            if lparen != "(" or rparen != ")":
                error_node = {"type": "ERROR", "message": "Mismatched parentheses"}
                return error_node
            return {"type": "PAREN_EXPR", "value": {"LPAREN": "(", "expr": expr_node, "RPAREN": ")"}}
        else:
            return self.visit(ctx.expr())

    def visitAssignStatement(self, ctx: ToxaLanguageParser.AssignStatementContext):
        try:
            variable_type = ctx.type_().getText()
            variable_name = ctx.ID().getText()
            assigned_value = self.visit(ctx.expr())
            if assigned_value.get("type") == "ERROR":
                self.ast.append(assigned_value)
                return
            end_state = ctx.END_STATE().getText()
            node = {"type": "ASSIGNMENT", "variable_type": variable_type,
                    "variable_name": variable_name, "value": assigned_value, "END_STATE": end_state}
            self.ast.append(node)
        except AttributeError:
            error_node = {"type": "ERROR", "message": "Mismatched parentheses"}
            self.ast.append(error_node)

    def visitPrintStatement(self, ctx: ToxaLanguageParser.PrintStatementContext):
        try:
            value_to_print = self.visit(ctx.expr())
            if value_to_print.get("type") == "ERROR":
                self.ast.append(value_to_print)
                return
            node = {"type": "PRINT", "value": value_to_print}
            self.ast.append(node)
        except AttributeError:
            error_node = {"type": "ERROR", "message": "Mismatched parentheses"}
            self.ast.append(error_node)

    def check_parenthesis_matching(self, ctx: ToxaLanguageParser.ProgContext):
        text = ctx.getText()
        stack = []
        for char in text:
            if char == '(':
                stack.append('(')
            elif char == ')':
                if not stack:
                    return False
                stack.pop()
        return not stack

    def visitProg(self, ctx: ToxaLanguageParser.ProgContext):
        if not self.check_parenthesis_matching(ctx):
            error_node = {"type": "ERROR", "message": "Mismatched parentheses"}
            self.ast.append(error_node)
            return self.ast

        self.visitChildren(ctx)
        return self.ast

    def save_ast_to_json(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.ast, file, indent=4)

def parse_input_file(input_filename):
    try:
        input_code = FileStream(input_filename)
        lexer = ToxaLanguageLexer(input_code)
        tokens = CommonTokenStream(lexer)
        parser = ToxaLanguageParser(tokens)
        parser.removeErrorListeners()  # Удаляем стандартные ErrorListener'ы
        error_listener = MyErrorListener()  # Создаем свой ErrorListener
        parser.addErrorListener(error_listener)  # Добавляем свой ErrorListener к парсеру
        tree = parser.prog()
        return tree
    except ValueError as e:
        error_info = {"type": "ERROR", "message": str(e)}
        return error_info
    except AttributeError as e:
        error_node = {"type": "ERROR", "message": "Mismatched parentheses"}
        return error_node

def ast_create():
    input_filename = "input_program.txt"
    ast_or_error = parse_input_file(input_filename)
    ast_builder = ASTbuilder()
    ast_builder.visit(ast_or_error)
    ast_builder.save_ast_to_json("ast.json")

if __name__ == "__main__":
    ast_create()
