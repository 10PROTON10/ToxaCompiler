from antlr4 import *
from ToxaLanguageLexer import ToxaLanguageLexer
from ToxaLanguageParser import ToxaLanguageParser
from ToxaLanguageListener import ToxaLanguageListener
from antlr4.error.ErrorListener import ErrorListener

class MyListener(ToxaLanguageListener):
    def enterEveryRule(self, ctx):
        print("Вход в правило:", ToxaLanguageParser.ruleNames[ctx.getRuleIndex()])

    def enterExpression(self, ctx):
        print("Выражение:", ctx.getText())

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print("Ошибка синтаксиса на строке", line, "и столбце", column, ":", msg)

def main():
    input_stream = FileStream("input_program.txt")  # Путь к вашему входному файлу с кодом

    lexer = ToxaLanguageLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ToxaLanguageParser(token_stream)
    listener = MyListener()

    parser.removeErrorListeners()  # Удаляем стандартных слушателей ошибок
    lexer.removeErrorListeners()
    parser.addErrorListener(listener)  # Добавляем наш собственный слушатель ошибок
    lexer.addErrorListener(listener)

    tree = parser.expression()  # Парсим входной файл с использованием правила expression
    walker = ParseTreeWalker()
    walker.walk(listener, tree)  # Обходим дерево разбора с нашим слушателем

if __name__ == '__main__':
    main()


