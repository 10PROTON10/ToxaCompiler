# Generated from ToxaLanguage.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ToxaLanguageParser import ToxaLanguageParser
else:
    from ToxaLanguageParser import ToxaLanguageParser

# This class defines a complete listener for a parse tree produced by ToxaLanguageParser.
class ToxaLanguageListener(ParseTreeListener):

    # Enter a parse tree produced by ToxaLanguageParser#expr.
    def enterExpr(self, ctx:ToxaLanguageParser.ExprContext):
        pass

    # Exit a parse tree produced by ToxaLanguageParser#expr.
    def exitExpr(self, ctx:ToxaLanguageParser.ExprContext):
        pass



del ToxaLanguageParser