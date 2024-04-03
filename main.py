from antlr4 import *
from ToxaLanguageLexer import ToxaLanguageLexer
from ToxaLanguageParser import ToxaLanguageParser
from ToxaLanguageListener import ToxaLanguageListener
from antlr4.error.ErrorListener import ErrorListener
import json
from ast_create import ASTBuilder

class MyListener(ToxaLanguageListener):
    def enterEveryRule(self, ctx):
        print("Вход в правило:", ToxaLanguageParser.ruleNames[ctx.getRuleIndex()])

    def enterAssignStatement(self, ctx):
        print("Присваивание:", ctx.getText())

    def enterPrintStatement(self, ctx):
        print("Вывод:", ctx.getText())

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print("Ошибка синтаксиса на строке", line, "и столбце", column, ":", msg)

    def exitExpr(self, ctx):
        children = ctx.children
        for child in children:
            if isinstance(child, TerminalNode):
                if child.symbol.type == ToxaLanguageParser.ID:
                    print("Идентификатор:", child.getText())
                elif child.symbol.type == ToxaLanguageParser.INT:
                    print("Целое число:", child.getText())
                elif child.symbol.type == ToxaLanguageParser.FLOAT:
                    print("Число с плавающей точкой:", child.getText())
                elif child.symbol.type == ToxaLanguageParser.PLUS:
                    print("Операция сложения")
                elif child.symbol.type == ToxaLanguageParser.MINUS:
                    print("Операция вычитания")
                elif child.symbol.type == ToxaLanguageParser.MULT:
                    print("Операция умножения")
                elif child.symbol.type == ToxaLanguageParser.DIV:
                    print("Операция деления")
                elif child.symbol.type == ToxaLanguageParser.LPAREN:
                    print("Левая скобка")
                elif child.symbol.type == ToxaLanguageParser.RPAREN:
                    print("Правая скобка")

def main():
    input_stream = FileStream("input_program.txt")
    lexer = ToxaLanguageLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ToxaLanguageParser(token_stream)
    listener = MyListener()

    parser.removeErrorListeners()
    lexer.removeErrorListeners()
    parser.addErrorListener(listener)
    lexer.addErrorListener(listener)

    tree = parser.prog()  # Используем правило prog для парсинга
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    ast_builder = ASTBuilder()
    ast_builder.visit(tree)
    ast_builder.save_ast_to_json("ast.json")

if __name__ == '__main__':
    main()












