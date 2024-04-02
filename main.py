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
        if ctx.PLUS():
            print("Операция сложения")
        elif ctx.MINUS():
            print("Операция вычитания")
        elif ctx.MULT():
            print("Операция умножения")
        elif ctx.DIV():
            print("Операция деления")
        elif ctx.FLOAT():
            print("Число с плавающей точкой:", ctx.FLOAT().getText())
        elif ctx.INT():
            print("Целое число:", ctx.INT().getText())

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











