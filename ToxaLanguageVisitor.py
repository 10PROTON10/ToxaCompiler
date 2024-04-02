# Generated from ToxaLanguage.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ToxaLanguageParser import ToxaLanguageParser
else:
    from ToxaLanguageParser import ToxaLanguageParser

# This class defines a complete generic visitor for a parse tree produced by ToxaLanguageParser.

class ToxaLanguageVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ToxaLanguageParser#prog.
    def visitProg(self, ctx:ToxaLanguageParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ToxaLanguageParser#printStatement.
    def visitPrintStatement(self, ctx:ToxaLanguageParser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ToxaLanguageParser#expr.
    def visitExpr(self, ctx:ToxaLanguageParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ToxaLanguageParser#term.
    def visitTerm(self, ctx:ToxaLanguageParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ToxaLanguageParser#factor.
    def visitFactor(self, ctx:ToxaLanguageParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ToxaLanguageParser#assignStatement.
    def visitAssignStatement(self, ctx:ToxaLanguageParser.AssignStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ToxaLanguageParser#type.
    def visitType(self, ctx:ToxaLanguageParser.TypeContext):
        return self.visitChildren(ctx)



del ToxaLanguageParser