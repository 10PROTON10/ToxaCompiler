# Generated from ToxaLanguage.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ToxaLanguageParser import ToxaLanguageParser
else:
    from ToxaLanguageParser import ToxaLanguageParser

# This class defines a complete listener for a parse tree produced by ToxaLanguageParser.
class ToxaLanguageListener(ParseTreeListener):

    # Enter a parse tree produced by ToxaLanguageParser#program.
    def enterProgram(self, ctx:ToxaLanguageParser.ProgramContext):
        pass

    # Exit a parse tree produced by ToxaLanguageParser#program.
    def exitProgram(self, ctx:ToxaLanguageParser.ProgramContext):
        pass


    # Enter a parse tree produced by ToxaLanguageParser#statement.
    def enterStatement(self, ctx:ToxaLanguageParser.StatementContext):
        pass

    # Exit a parse tree produced by ToxaLanguageParser#statement.
    def exitStatement(self, ctx:ToxaLanguageParser.StatementContext):
        pass


    # Enter a parse tree produced by ToxaLanguageParser#assignmentStatement.
    def enterAssignmentStatement(self, ctx:ToxaLanguageParser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by ToxaLanguageParser#assignmentStatement.
    def exitAssignmentStatement(self, ctx:ToxaLanguageParser.AssignmentStatementContext):
        pass


    # Enter a parse tree produced by ToxaLanguageParser#printStatement.
    def enterPrintStatement(self, ctx:ToxaLanguageParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by ToxaLanguageParser#printStatement.
    def exitPrintStatement(self, ctx:ToxaLanguageParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by ToxaLanguageParser#ifStatement.
    def enterIfStatement(self, ctx:ToxaLanguageParser.IfStatementContext):
        pass

    # Exit a parse tree produced by ToxaLanguageParser#ifStatement.
    def exitIfStatement(self, ctx:ToxaLanguageParser.IfStatementContext):
        pass


    # Enter a parse tree produced by ToxaLanguageParser#elseStatement.
    def enterElseStatement(self, ctx:ToxaLanguageParser.ElseStatementContext):
        pass

    # Exit a parse tree produced by ToxaLanguageParser#elseStatement.
    def exitElseStatement(self, ctx:ToxaLanguageParser.ElseStatementContext):
        pass


    # Enter a parse tree produced by ToxaLanguageParser#block.
    def enterBlock(self, ctx:ToxaLanguageParser.BlockContext):
        pass

    # Exit a parse tree produced by ToxaLanguageParser#block.
    def exitBlock(self, ctx:ToxaLanguageParser.BlockContext):
        pass


    # Enter a parse tree produced by ToxaLanguageParser#forStatement.
    def enterForStatement(self, ctx:ToxaLanguageParser.ForStatementContext):
        pass

    # Exit a parse tree produced by ToxaLanguageParser#forStatement.
    def exitForStatement(self, ctx:ToxaLanguageParser.ForStatementContext):
        pass


    # Enter a parse tree produced by ToxaLanguageParser#whileStatement.
    def enterWhileStatement(self, ctx:ToxaLanguageParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by ToxaLanguageParser#whileStatement.
    def exitWhileStatement(self, ctx:ToxaLanguageParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by ToxaLanguageParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:ToxaLanguageParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by ToxaLanguageParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:ToxaLanguageParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by ToxaLanguageParser#returnStatement.
    def enterReturnStatement(self, ctx:ToxaLanguageParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by ToxaLanguageParser#returnStatement.
    def exitReturnStatement(self, ctx:ToxaLanguageParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by ToxaLanguageParser#forInitializer.
    def enterForInitializer(self, ctx:ToxaLanguageParser.ForInitializerContext):
        pass

    # Exit a parse tree produced by ToxaLanguageParser#forInitializer.
    def exitForInitializer(self, ctx:ToxaLanguageParser.ForInitializerContext):
        pass


    # Enter a parse tree produced by ToxaLanguageParser#forCondition.
    def enterForCondition(self, ctx:ToxaLanguageParser.ForConditionContext):
        pass

    # Exit a parse tree produced by ToxaLanguageParser#forCondition.
    def exitForCondition(self, ctx:ToxaLanguageParser.ForConditionContext):
        pass


    # Enter a parse tree produced by ToxaLanguageParser#forUpdate.
    def enterForUpdate(self, ctx:ToxaLanguageParser.ForUpdateContext):
        pass

    # Exit a parse tree produced by ToxaLanguageParser#forUpdate.
    def exitForUpdate(self, ctx:ToxaLanguageParser.ForUpdateContext):
        pass


    # Enter a parse tree produced by ToxaLanguageParser#functionCall.
    def enterFunctionCall(self, ctx:ToxaLanguageParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by ToxaLanguageParser#functionCall.
    def exitFunctionCall(self, ctx:ToxaLanguageParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by ToxaLanguageParser#params.
    def enterParams(self, ctx:ToxaLanguageParser.ParamsContext):
        pass

    # Exit a parse tree produced by ToxaLanguageParser#params.
    def exitParams(self, ctx:ToxaLanguageParser.ParamsContext):
        pass


    # Enter a parse tree produced by ToxaLanguageParser#expression.
    def enterExpression(self, ctx:ToxaLanguageParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ToxaLanguageParser#expression.
    def exitExpression(self, ctx:ToxaLanguageParser.ExpressionContext):
        pass


    # Enter a parse tree produced by ToxaLanguageParser#operand.
    def enterOperand(self, ctx:ToxaLanguageParser.OperandContext):
        pass

    # Exit a parse tree produced by ToxaLanguageParser#operand.
    def exitOperand(self, ctx:ToxaLanguageParser.OperandContext):
        pass


    # Enter a parse tree produced by ToxaLanguageParser#type.
    def enterType(self, ctx:ToxaLanguageParser.TypeContext):
        pass

    # Exit a parse tree produced by ToxaLanguageParser#type.
    def exitType(self, ctx:ToxaLanguageParser.TypeContext):
        pass



del ToxaLanguageParser