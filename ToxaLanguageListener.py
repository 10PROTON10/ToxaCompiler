# Generated from ToxaLanguage.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ToxaLanguageParser import ToxaLanguageParser
else:
    from ToxaLanguageParser import ToxaLanguageParser

# This class defines a complete listener for a parse tree produced by ToxaLanguageParser.
class ToxaLanguageListener(ParseTreeListener):

    # Enter a parse tree produced by ToxaLanguageParser#prog.
    def enterProg(self, ctx:ToxaLanguageParser.ProgContext):
        pass

    # Exit a parse tree produced by ToxaLanguageParser#prog.
    def exitProg(self, ctx:ToxaLanguageParser.ProgContext):
        pass


    # Enter a parse tree produced by ToxaLanguageParser#printStatement.
    def enterPrintStatement(self, ctx:ToxaLanguageParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by ToxaLanguageParser#printStatement.
    def exitPrintStatement(self, ctx:ToxaLanguageParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by ToxaLanguageParser#expr.
    def enterExpr(self, ctx:ToxaLanguageParser.ExprContext):
        pass

    # Exit a parse tree produced by ToxaLanguageParser#expr.
    def exitExpr(self, ctx:ToxaLanguageParser.ExprContext):
        pass


    # Enter a parse tree produced by ToxaLanguageParser#term.
    def enterTerm(self, ctx:ToxaLanguageParser.TermContext):
        pass

    # Exit a parse tree produced by ToxaLanguageParser#term.
    def exitTerm(self, ctx:ToxaLanguageParser.TermContext):
        pass


    # Enter a parse tree produced by ToxaLanguageParser#factor.
    def enterFactor(self, ctx:ToxaLanguageParser.FactorContext):
        pass

    # Exit a parse tree produced by ToxaLanguageParser#factor.
    def exitFactor(self, ctx:ToxaLanguageParser.FactorContext):
        pass


    # Enter a parse tree produced by ToxaLanguageParser#assignStatement.
    def enterAssignStatement(self, ctx:ToxaLanguageParser.AssignStatementContext):
        pass

    # Exit a parse tree produced by ToxaLanguageParser#assignStatement.
    def exitAssignStatement(self, ctx:ToxaLanguageParser.AssignStatementContext):
        pass


    # Enter a parse tree produced by ToxaLanguageParser#type.
    def enterType(self, ctx:ToxaLanguageParser.TypeContext):
        pass

    # Exit a parse tree produced by ToxaLanguageParser#type.
    def exitType(self, ctx:ToxaLanguageParser.TypeContext):
        pass



del ToxaLanguageParser