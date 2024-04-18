# Generated from ToxaLanguage.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ToxaLanguageParser import ToxaLanguageParser
else:
    from ToxaLanguageParser import ToxaLanguageParser

# This class defines a complete generic visitor for a parse tree produced by ToxaLanguageParser.

class ToxaLanguageVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ToxaLanguageParser#program.
    def visitProgram(self, ctx:ToxaLanguageParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ToxaLanguageParser#statement.
    def visitStatement(self, ctx:ToxaLanguageParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ToxaLanguageParser#assignmentStatement.
    def visitAssignmentStatement(self, ctx:ToxaLanguageParser.AssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ToxaLanguageParser#printStatement.
    def visitPrintStatement(self, ctx:ToxaLanguageParser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ToxaLanguageParser#ifStatement.
    def visitIfStatement(self, ctx:ToxaLanguageParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ToxaLanguageParser#elseStatement.
    def visitElseStatement(self, ctx:ToxaLanguageParser.ElseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ToxaLanguageParser#block.
    def visitBlock(self, ctx:ToxaLanguageParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ToxaLanguageParser#forStatement.
    def visitForStatement(self, ctx:ToxaLanguageParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ToxaLanguageParser#whileStatement.
    def visitWhileStatement(self, ctx:ToxaLanguageParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ToxaLanguageParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:ToxaLanguageParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ToxaLanguageParser#returnStatement.
    def visitReturnStatement(self, ctx:ToxaLanguageParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ToxaLanguageParser#forInitializer.
    def visitForInitializer(self, ctx:ToxaLanguageParser.ForInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ToxaLanguageParser#forCondition.
    def visitForCondition(self, ctx:ToxaLanguageParser.ForConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ToxaLanguageParser#forUpdate.
    def visitForUpdate(self, ctx:ToxaLanguageParser.ForUpdateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ToxaLanguageParser#functionCall.
    def visitFunctionCall(self, ctx:ToxaLanguageParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ToxaLanguageParser#params.
    def visitParams(self, ctx:ToxaLanguageParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ToxaLanguageParser#expression.
    def visitExpression(self, ctx:ToxaLanguageParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ToxaLanguageParser#operand.
    def visitOperand(self, ctx:ToxaLanguageParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ToxaLanguageParser#type.
    def visitType(self, ctx:ToxaLanguageParser.TypeContext):
        return self.visitChildren(ctx)



del ToxaLanguageParser