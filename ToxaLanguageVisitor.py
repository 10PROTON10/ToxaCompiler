# Generated from ToxaLanguage.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ToxaLanguageParser import ToxaLanguageParser
else:
    from ToxaLanguageParser import ToxaLanguageParser

# This class defines a complete generic visitor for a parse tree produced by MyLanguageParser.

class ToxaLanguageVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MyLanguageParser#expression.
    def visitExpression(self, ctx:ToxaLanguageParser.ExpressionContext):
        return self.visitChildren(ctx)



del ToxaLanguageParser