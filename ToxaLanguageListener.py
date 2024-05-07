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


    # Enter a parse tree produced by ToxaLanguageParser#ifBlock.
    def enterIfBlock(self, ctx:ToxaLanguageParser.IfBlockContext):
        pass

    # Exit a parse tree produced by ToxaLanguageParser#ifBlock.
    def exitIfBlock(self, ctx:ToxaLanguageParser.IfBlockContext):
        pass


    # Enter a parse tree produced by ToxaLanguageParser#ifElseStatement.
    def enterIfElseStatement(self, ctx:ToxaLanguageParser.IfElseStatementContext):
        pass

    # Exit a parse tree produced by ToxaLanguageParser#ifElseStatement.
    def exitIfElseStatement(self, ctx:ToxaLanguageParser.IfElseStatementContext):
        pass


    # Enter a parse tree produced by ToxaLanguageParser#elseBlock.
    def enterElseBlock(self, ctx:ToxaLanguageParser.ElseBlockContext):
        pass

    # Exit a parse tree produced by ToxaLanguageParser#elseBlock.
    def exitElseBlock(self, ctx:ToxaLanguageParser.ElseBlockContext):
        pass


    # Enter a parse tree produced by ToxaLanguageParser#forStatement.
    def enterForStatement(self, ctx:ToxaLanguageParser.ForStatementContext):
        pass

    # Exit a parse tree produced by ToxaLanguageParser#forStatement.
    def exitForStatement(self, ctx:ToxaLanguageParser.ForStatementContext):
        pass


    # Enter a parse tree produced by ToxaLanguageParser#forBlock.
    def enterForBlock(self, ctx:ToxaLanguageParser.ForBlockContext):
        pass

    # Exit a parse tree produced by ToxaLanguageParser#forBlock.
    def exitForBlock(self, ctx:ToxaLanguageParser.ForBlockContext):
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


    # Enter a parse tree produced by ToxaLanguageParser#incrementOrDecrement.
    def enterIncrementOrDecrement(self, ctx:ToxaLanguageParser.IncrementOrDecrementContext):
        pass

    # Exit a parse tree produced by ToxaLanguageParser#incrementOrDecrement.
    def exitIncrementOrDecrement(self, ctx:ToxaLanguageParser.IncrementOrDecrementContext):
        pass


    # Enter a parse tree produced by ToxaLanguageParser#whileStatement.
    def enterWhileStatement(self, ctx:ToxaLanguageParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by ToxaLanguageParser#whileStatement.
    def exitWhileStatement(self, ctx:ToxaLanguageParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by ToxaLanguageParser#whileBlock.
    def enterWhileBlock(self, ctx:ToxaLanguageParser.WhileBlockContext):
        pass

    # Exit a parse tree produced by ToxaLanguageParser#whileBlock.
    def exitWhileBlock(self, ctx:ToxaLanguageParser.WhileBlockContext):
        pass


    # Enter a parse tree produced by ToxaLanguageParser#functionStatement.
    def enterFunctionStatement(self, ctx:ToxaLanguageParser.FunctionStatementContext):
        pass

    # Exit a parse tree produced by ToxaLanguageParser#functionStatement.
    def exitFunctionStatement(self, ctx:ToxaLanguageParser.FunctionStatementContext):
        pass


    # Enter a parse tree produced by ToxaLanguageParser#functionBlock.
    def enterFunctionBlock(self, ctx:ToxaLanguageParser.FunctionBlockContext):
        pass

    # Exit a parse tree produced by ToxaLanguageParser#functionBlock.
    def exitFunctionBlock(self, ctx:ToxaLanguageParser.FunctionBlockContext):
        pass


    # Enter a parse tree produced by ToxaLanguageParser#returnStatement.
    def enterReturnStatement(self, ctx:ToxaLanguageParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by ToxaLanguageParser#returnStatement.
    def exitReturnStatement(self, ctx:ToxaLanguageParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by ToxaLanguageParser#functionCall.
    def enterFunctionCall(self, ctx:ToxaLanguageParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by ToxaLanguageParser#functionCall.
    def exitFunctionCall(self, ctx:ToxaLanguageParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by ToxaLanguageParser#paramsCall.
    def enterParamsCall(self, ctx:ToxaLanguageParser.ParamsCallContext):
        pass

    # Exit a parse tree produced by ToxaLanguageParser#paramsCall.
    def exitParamsCall(self, ctx:ToxaLanguageParser.ParamsCallContext):
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


    # Enter a parse tree produced by ToxaLanguageParser#comparison.
    def enterComparison(self, ctx:ToxaLanguageParser.ComparisonContext):
        pass

    # Exit a parse tree produced by ToxaLanguageParser#comparison.
    def exitComparison(self, ctx:ToxaLanguageParser.ComparisonContext):
        pass


    # Enter a parse tree produced by ToxaLanguageParser#arithmetic.
    def enterArithmetic(self, ctx:ToxaLanguageParser.ArithmeticContext):
        pass

    # Exit a parse tree produced by ToxaLanguageParser#arithmetic.
    def exitArithmetic(self, ctx:ToxaLanguageParser.ArithmeticContext):
        pass


    # Enter a parse tree produced by ToxaLanguageParser#logical.
    def enterLogical(self, ctx:ToxaLanguageParser.LogicalContext):
        pass

    # Exit a parse tree produced by ToxaLanguageParser#logical.
    def exitLogical(self, ctx:ToxaLanguageParser.LogicalContext):
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