# Generated from ToxaLanguage.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ToxaLanguageParser import ToxaLanguageParser
else:
    from ToxaLanguageParser import ToxaLanguageParser

# This class defines a complete generic visitor for a parse tree produced by ToxaLanguageParser.

class ToxaLanguageVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ToxaLanguageParser#expression.
    def visitExpression(self, ctx:ToxaLanguageParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ToxaLanguageParser#multExpr.
    def visitMultExpr(self, ctx:ToxaLanguageParser.MultExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ToxaLanguageParser#atom.
    def visitAtom(self, ctx:ToxaLanguageParser.AtomContext):
        return self.visitChildren(ctx)



del ToxaLanguageParser