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


    # Visit a parse tree produced by ToxaLanguageParser#ifBlock.
    def visitIfBlock(self, ctx:ToxaLanguageParser.IfBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ToxaLanguageParser#ifElseStatement.
    def visitIfElseStatement(self, ctx:ToxaLanguageParser.IfElseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ToxaLanguageParser#elseBlock.
    def visitElseBlock(self, ctx:ToxaLanguageParser.ElseBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ToxaLanguageParser#forStatement.
    def visitForStatement(self, ctx:ToxaLanguageParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ToxaLanguageParser#forBlock.
    def visitForBlock(self, ctx:ToxaLanguageParser.ForBlockContext):
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


    # Visit a parse tree produced by ToxaLanguageParser#incrementOrDecrement.
    def visitIncrementOrDecrement(self, ctx:ToxaLanguageParser.IncrementOrDecrementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ToxaLanguageParser#whileStatement.
    def visitWhileStatement(self, ctx:ToxaLanguageParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ToxaLanguageParser#whileBlock.
    def visitWhileBlock(self, ctx:ToxaLanguageParser.WhileBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ToxaLanguageParser#functionStatement.
    def visitFunctionStatement(self, ctx:ToxaLanguageParser.FunctionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ToxaLanguageParser#functionBlock.
    def visitFunctionBlock(self, ctx:ToxaLanguageParser.FunctionBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ToxaLanguageParser#returnStatement.
    def visitReturnStatement(self, ctx:ToxaLanguageParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ToxaLanguageParser#functionCall.
    def visitFunctionCall(self, ctx:ToxaLanguageParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ToxaLanguageParser#paramsCall.
    def visitParamsCall(self, ctx:ToxaLanguageParser.ParamsCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ToxaLanguageParser#params.
    def visitParams(self, ctx:ToxaLanguageParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ToxaLanguageParser#expression.
    def visitExpression(self, ctx:ToxaLanguageParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ToxaLanguageParser#comparison.
    def visitComparison(self, ctx:ToxaLanguageParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ToxaLanguageParser#arithmetic.
    def visitArithmetic(self, ctx:ToxaLanguageParser.ArithmeticContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ToxaLanguageParser#logical.
    def visitLogical(self, ctx:ToxaLanguageParser.LogicalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ToxaLanguageParser#operand.
    def visitOperand(self, ctx:ToxaLanguageParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ToxaLanguageParser#type.
    def visitType(self, ctx:ToxaLanguageParser.TypeContext):
        return self.visitChildren(ctx)



del ToxaLanguageParser