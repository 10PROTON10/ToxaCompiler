# Generated from ToxaLanguage.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ToxaLanguageParser import ToxaLanguageParser
else:
    from ToxaLanguageParser import ToxaLanguageParser

# This class defines a complete listener for a parse tree produced by ToxaLanguageParser.
class ToxaLanguageListener(ParseTreeListener):

    # Enter a parse tree produced by ToxaLanguageParser#expression.
    def enterExpression(self, ctx:ToxaLanguageParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ToxaLanguageParser#expression.
    def exitExpression(self, ctx:ToxaLanguageParser.ExpressionContext):
        pass


    # Enter a parse tree produced by ToxaLanguageParser#multExpr.
    def enterMultExpr(self, ctx:ToxaLanguageParser.MultExprContext):
        pass

    # Exit a parse tree produced by ToxaLanguageParser#multExpr.
    def exitMultExpr(self, ctx:ToxaLanguageParser.MultExprContext):
        pass


    # Enter a parse tree produced by ToxaLanguageParser#atom.
    def enterAtom(self, ctx:ToxaLanguageParser.AtomContext):
        pass

    # Exit a parse tree produced by ToxaLanguageParser#atom.
    def exitAtom(self, ctx:ToxaLanguageParser.AtomContext):
        pass



del ToxaLanguageParser