# Generated from ToxaLanguage.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,40,231,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        1,0,1,0,5,0,57,8,0,10,0,12,0,60,9,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,3,1,74,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,
        3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,5,5,98,8,5,
        10,5,12,5,101,9,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        7,5,7,115,8,7,10,7,12,7,118,9,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,9,5,9,134,8,9,10,9,12,9,137,9,9,1,10,1,10,
        1,10,1,10,1,10,1,11,1,11,1,12,1,12,1,12,1,13,1,13,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,15,5,15,161,8,15,10,15,12,15,164,
        9,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,17,5,17,
        177,8,17,10,17,12,17,180,9,17,1,18,1,18,1,18,1,18,1,19,1,19,1,19,
        1,19,1,19,1,20,3,20,192,8,20,1,20,1,20,5,20,196,8,20,10,20,12,20,
        199,9,20,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,3,21,209,8,21,1,
        22,1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,25,1,
        25,1,25,1,25,3,25,227,8,25,1,26,1,26,1,26,0,0,27,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,0,5,
        1,0,11,12,2,0,28,28,32,37,1,0,23,27,1,0,38,39,1,0,9,10,226,0,54,
        1,0,0,0,2,73,1,0,0,0,4,75,1,0,0,0,6,81,1,0,0,0,8,87,1,0,0,0,10,99,
        1,0,0,0,12,102,1,0,0,0,14,116,1,0,0,0,16,119,1,0,0,0,18,135,1,0,
        0,0,20,138,1,0,0,0,22,143,1,0,0,0,24,145,1,0,0,0,26,148,1,0,0,0,
        28,150,1,0,0,0,30,162,1,0,0,0,32,165,1,0,0,0,34,178,1,0,0,0,36,181,
        1,0,0,0,38,185,1,0,0,0,40,191,1,0,0,0,42,208,1,0,0,0,44,210,1,0,
        0,0,46,214,1,0,0,0,48,218,1,0,0,0,50,226,1,0,0,0,52,228,1,0,0,0,
        54,58,5,13,0,0,55,57,3,2,1,0,56,55,1,0,0,0,57,60,1,0,0,0,58,56,1,
        0,0,0,58,59,1,0,0,0,59,61,1,0,0,0,60,58,1,0,0,0,61,62,5,14,0,0,62,
        63,5,0,0,1,63,1,1,0,0,0,64,74,3,4,2,0,65,74,3,6,3,0,66,74,3,8,4,
        0,67,74,3,12,6,0,68,74,3,28,14,0,69,74,3,16,8,0,70,74,3,32,16,0,
        71,74,3,36,18,0,72,74,3,42,21,0,73,64,1,0,0,0,73,65,1,0,0,0,73,66,
        1,0,0,0,73,67,1,0,0,0,73,68,1,0,0,0,73,69,1,0,0,0,73,70,1,0,0,0,
        73,71,1,0,0,0,73,72,1,0,0,0,74,3,1,0,0,0,75,76,3,52,26,0,76,77,5,
        22,0,0,77,78,5,28,0,0,78,79,3,42,21,0,79,80,5,31,0,0,80,5,1,0,0,
        0,81,82,5,1,0,0,82,83,5,29,0,0,83,84,3,42,21,0,84,85,5,30,0,0,85,
        86,5,31,0,0,86,7,1,0,0,0,87,88,5,2,0,0,88,89,5,29,0,0,89,90,3,42,
        21,0,90,91,5,30,0,0,91,92,5,15,0,0,92,93,3,10,5,0,93,94,5,16,0,0,
        94,95,5,31,0,0,95,9,1,0,0,0,96,98,3,2,1,0,97,96,1,0,0,0,98,101,1,
        0,0,0,99,97,1,0,0,0,99,100,1,0,0,0,100,11,1,0,0,0,101,99,1,0,0,0,
        102,103,5,2,0,0,103,104,5,29,0,0,104,105,3,42,21,0,105,106,5,30,
        0,0,106,107,5,15,0,0,107,108,3,10,5,0,108,109,5,3,0,0,109,110,3,
        14,7,0,110,111,5,16,0,0,111,112,5,31,0,0,112,13,1,0,0,0,113,115,
        3,2,1,0,114,113,1,0,0,0,115,118,1,0,0,0,116,114,1,0,0,0,116,117,
        1,0,0,0,117,15,1,0,0,0,118,116,1,0,0,0,119,120,5,4,0,0,120,121,5,
        29,0,0,121,122,3,20,10,0,122,123,5,31,0,0,123,124,3,22,11,0,124,
        125,5,31,0,0,125,126,3,24,12,0,126,127,5,30,0,0,127,128,5,15,0,0,
        128,129,3,18,9,0,129,130,5,17,0,0,130,131,5,31,0,0,131,17,1,0,0,
        0,132,134,3,2,1,0,133,132,1,0,0,0,134,137,1,0,0,0,135,133,1,0,0,
        0,135,136,1,0,0,0,136,19,1,0,0,0,137,135,1,0,0,0,138,139,3,52,26,
        0,139,140,5,22,0,0,140,141,5,28,0,0,141,142,3,42,21,0,142,21,1,0,
        0,0,143,144,3,42,21,0,144,23,1,0,0,0,145,146,5,22,0,0,146,147,3,
        26,13,0,147,25,1,0,0,0,148,149,7,0,0,0,149,27,1,0,0,0,150,151,5,
        5,0,0,151,152,5,29,0,0,152,153,3,42,21,0,153,154,5,30,0,0,154,155,
        5,15,0,0,155,156,3,30,15,0,156,157,5,18,0,0,157,158,5,31,0,0,158,
        29,1,0,0,0,159,161,3,2,1,0,160,159,1,0,0,0,161,164,1,0,0,0,162,160,
        1,0,0,0,162,163,1,0,0,0,163,31,1,0,0,0,164,162,1,0,0,0,165,166,5,
        6,0,0,166,167,5,22,0,0,167,168,5,29,0,0,168,169,3,40,20,0,169,170,
        5,30,0,0,170,171,5,15,0,0,171,172,3,34,17,0,172,173,5,19,0,0,173,
        174,5,31,0,0,174,33,1,0,0,0,175,177,3,2,1,0,176,175,1,0,0,0,177,
        180,1,0,0,0,178,176,1,0,0,0,178,179,1,0,0,0,179,35,1,0,0,0,180,178,
        1,0,0,0,181,182,5,7,0,0,182,183,3,42,21,0,183,184,5,31,0,0,184,37,
        1,0,0,0,185,186,5,22,0,0,186,187,5,29,0,0,187,188,3,40,20,0,188,
        189,5,30,0,0,189,39,1,0,0,0,190,192,3,42,21,0,191,190,1,0,0,0,191,
        192,1,0,0,0,192,197,1,0,0,0,193,194,5,8,0,0,194,196,3,42,21,0,195,
        193,1,0,0,0,196,199,1,0,0,0,197,195,1,0,0,0,197,198,1,0,0,0,198,
        41,1,0,0,0,199,197,1,0,0,0,200,209,3,46,23,0,201,209,3,44,22,0,202,
        209,3,48,24,0,203,209,3,50,25,0,204,205,5,29,0,0,205,206,3,42,21,
        0,206,207,5,30,0,0,207,209,1,0,0,0,208,200,1,0,0,0,208,201,1,0,0,
        0,208,202,1,0,0,0,208,203,1,0,0,0,208,204,1,0,0,0,209,43,1,0,0,0,
        210,211,3,50,25,0,211,212,7,1,0,0,212,213,3,50,25,0,213,45,1,0,0,
        0,214,215,3,50,25,0,215,216,7,2,0,0,216,217,3,50,25,0,217,47,1,0,
        0,0,218,219,3,50,25,0,219,220,7,3,0,0,220,221,3,50,25,0,221,49,1,
        0,0,0,222,227,5,20,0,0,223,227,5,21,0,0,224,227,5,22,0,0,225,227,
        3,38,19,0,226,222,1,0,0,0,226,223,1,0,0,0,226,224,1,0,0,0,226,225,
        1,0,0,0,227,51,1,0,0,0,228,229,7,4,0,0,229,53,1,0,0,0,11,58,73,99,
        116,135,162,178,191,197,208,226
    ]

class ToxaLanguageParser ( Parser ):

    grammarFileName = "ToxaLanguage.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'print'", "'if'", "'else'", "'for'", 
                     "'while'", "'function'", "'return'", "','", "'int'", 
                     "'float'", "<INVALID>", "<INVALID>", "'start'", "'finish'", 
                     "'then'", "'endif'", "'endfor'", "'endwhile'", "'endfunction'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'*'", "'%'", 
                     "'/'", "'+'", "'-'", "'='", "'('", "')'", "';'", "'>'", 
                     "'<'", "'>='", "'<='", "'=='", "'!='", "'&&'", "'||'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "INCREMENT", 
                      "DECREMENT", "START_STATEMENT", "FINISH_STATEMENT", 
                      "THEN", "ENDIF", "ENDFOR", "ENDWHILE", "ENDFUNCTION", 
                      "INT", "FLOAT", "ID", "MUL", "REM", "DIV", "PLUS", 
                      "MINUS", "EQ", "LPAREN", "RPAREN", "END_STATE", "GT", 
                      "LT", "GE", "LE", "EQEQ", "NE", "AND", "OR", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assignmentStatement = 2
    RULE_printStatement = 3
    RULE_ifStatement = 4
    RULE_ifBlock = 5
    RULE_ifElseStatement = 6
    RULE_elseBlock = 7
    RULE_forStatement = 8
    RULE_forBlock = 9
    RULE_forInitializer = 10
    RULE_forCondition = 11
    RULE_forUpdate = 12
    RULE_incrementOrDecrement = 13
    RULE_whileStatement = 14
    RULE_whileBlock = 15
    RULE_functionStatement = 16
    RULE_functionBlock = 17
    RULE_returnStatement = 18
    RULE_functionCall = 19
    RULE_params = 20
    RULE_expression = 21
    RULE_comparison = 22
    RULE_arithmetic = 23
    RULE_logical = 24
    RULE_operand = 25
    RULE_type = 26

    ruleNames =  [ "program", "statement", "assignmentStatement", "printStatement", 
                   "ifStatement", "ifBlock", "ifElseStatement", "elseBlock", 
                   "forStatement", "forBlock", "forInitializer", "forCondition", 
                   "forUpdate", "incrementOrDecrement", "whileStatement", 
                   "whileBlock", "functionStatement", "functionBlock", "returnStatement", 
                   "functionCall", "params", "expression", "comparison", 
                   "arithmetic", "logical", "operand", "type" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    INCREMENT=11
    DECREMENT=12
    START_STATEMENT=13
    FINISH_STATEMENT=14
    THEN=15
    ENDIF=16
    ENDFOR=17
    ENDWHILE=18
    ENDFUNCTION=19
    INT=20
    FLOAT=21
    ID=22
    MUL=23
    REM=24
    DIV=25
    PLUS=26
    MINUS=27
    EQ=28
    LPAREN=29
    RPAREN=30
    END_STATE=31
    GT=32
    LT=33
    GE=34
    LE=35
    EQEQ=36
    NE=37
    AND=38
    OR=39
    WS=40

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def START_STATEMENT(self):
            return self.getToken(ToxaLanguageParser.START_STATEMENT, 0)

        def FINISH_STATEMENT(self):
            return self.getToken(ToxaLanguageParser.FINISH_STATEMENT, 0)

        def EOF(self):
            return self.getToken(ToxaLanguageParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ToxaLanguageParser.StatementContext)
            else:
                return self.getTypedRuleContext(ToxaLanguageParser.StatementContext,i)


        def getRuleIndex(self):
            return ToxaLanguageParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ToxaLanguageParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(ToxaLanguageParser.START_STATEMENT)
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 544212726) != 0):
                self.state = 55
                self.statement()
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 61
            self.match(ToxaLanguageParser.FINISH_STATEMENT)
            self.state = 62
            self.match(ToxaLanguageParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignmentStatement(self):
            return self.getTypedRuleContext(ToxaLanguageParser.AssignmentStatementContext,0)


        def printStatement(self):
            return self.getTypedRuleContext(ToxaLanguageParser.PrintStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(ToxaLanguageParser.IfStatementContext,0)


        def ifElseStatement(self):
            return self.getTypedRuleContext(ToxaLanguageParser.IfElseStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(ToxaLanguageParser.WhileStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(ToxaLanguageParser.ForStatementContext,0)


        def functionStatement(self):
            return self.getTypedRuleContext(ToxaLanguageParser.FunctionStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(ToxaLanguageParser.ReturnStatementContext,0)


        def expression(self):
            return self.getTypedRuleContext(ToxaLanguageParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ToxaLanguageParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ToxaLanguageParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.assignmentStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self.printStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 66
                self.ifStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 67
                self.ifElseStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 68
                self.whileStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 69
                self.forStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 70
                self.functionStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 71
                self.returnStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 72
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(ToxaLanguageParser.TypeContext,0)


        def ID(self):
            return self.getToken(ToxaLanguageParser.ID, 0)

        def EQ(self):
            return self.getToken(ToxaLanguageParser.EQ, 0)

        def expression(self):
            return self.getTypedRuleContext(ToxaLanguageParser.ExpressionContext,0)


        def END_STATE(self):
            return self.getToken(ToxaLanguageParser.END_STATE, 0)

        def getRuleIndex(self):
            return ToxaLanguageParser.RULE_assignmentStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentStatement" ):
                listener.enterAssignmentStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentStatement" ):
                listener.exitAssignmentStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentStatement" ):
                return visitor.visitAssignmentStatement(self)
            else:
                return visitor.visitChildren(self)




    def assignmentStatement(self):

        localctx = ToxaLanguageParser.AssignmentStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignmentStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.type_()
            self.state = 76
            self.match(ToxaLanguageParser.ID)
            self.state = 77
            self.match(ToxaLanguageParser.EQ)
            self.state = 78
            self.expression()
            self.state = 79
            self.match(ToxaLanguageParser.END_STATE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(ToxaLanguageParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(ToxaLanguageParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(ToxaLanguageParser.RPAREN, 0)

        def END_STATE(self):
            return self.getToken(ToxaLanguageParser.END_STATE, 0)

        def getRuleIndex(self):
            return ToxaLanguageParser.RULE_printStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStatement" ):
                listener.enterPrintStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStatement" ):
                listener.exitPrintStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStatement" ):
                return visitor.visitPrintStatement(self)
            else:
                return visitor.visitChildren(self)




    def printStatement(self):

        localctx = ToxaLanguageParser.PrintStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_printStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(ToxaLanguageParser.T__0)
            self.state = 82
            self.match(ToxaLanguageParser.LPAREN)
            self.state = 83
            self.expression()
            self.state = 84
            self.match(ToxaLanguageParser.RPAREN)
            self.state = 85
            self.match(ToxaLanguageParser.END_STATE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(ToxaLanguageParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(ToxaLanguageParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(ToxaLanguageParser.RPAREN, 0)

        def THEN(self):
            return self.getToken(ToxaLanguageParser.THEN, 0)

        def ifBlock(self):
            return self.getTypedRuleContext(ToxaLanguageParser.IfBlockContext,0)


        def ENDIF(self):
            return self.getToken(ToxaLanguageParser.ENDIF, 0)

        def END_STATE(self):
            return self.getToken(ToxaLanguageParser.END_STATE, 0)

        def getRuleIndex(self):
            return ToxaLanguageParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = ToxaLanguageParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(ToxaLanguageParser.T__1)
            self.state = 88
            self.match(ToxaLanguageParser.LPAREN)
            self.state = 89
            self.expression()
            self.state = 90
            self.match(ToxaLanguageParser.RPAREN)
            self.state = 91
            self.match(ToxaLanguageParser.THEN)
            self.state = 92
            self.ifBlock()
            self.state = 93
            self.match(ToxaLanguageParser.ENDIF)
            self.state = 94
            self.match(ToxaLanguageParser.END_STATE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ToxaLanguageParser.StatementContext)
            else:
                return self.getTypedRuleContext(ToxaLanguageParser.StatementContext,i)


        def getRuleIndex(self):
            return ToxaLanguageParser.RULE_ifBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfBlock" ):
                listener.enterIfBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfBlock" ):
                listener.exitIfBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfBlock" ):
                return visitor.visitIfBlock(self)
            else:
                return visitor.visitChildren(self)




    def ifBlock(self):

        localctx = ToxaLanguageParser.IfBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ifBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 544212726) != 0):
                self.state = 96
                self.statement()
                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfElseStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(ToxaLanguageParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(ToxaLanguageParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(ToxaLanguageParser.RPAREN, 0)

        def THEN(self):
            return self.getToken(ToxaLanguageParser.THEN, 0)

        def ifBlock(self):
            return self.getTypedRuleContext(ToxaLanguageParser.IfBlockContext,0)


        def elseBlock(self):
            return self.getTypedRuleContext(ToxaLanguageParser.ElseBlockContext,0)


        def ENDIF(self):
            return self.getToken(ToxaLanguageParser.ENDIF, 0)

        def END_STATE(self):
            return self.getToken(ToxaLanguageParser.END_STATE, 0)

        def getRuleIndex(self):
            return ToxaLanguageParser.RULE_ifElseStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfElseStatement" ):
                listener.enterIfElseStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfElseStatement" ):
                listener.exitIfElseStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfElseStatement" ):
                return visitor.visitIfElseStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifElseStatement(self):

        localctx = ToxaLanguageParser.IfElseStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_ifElseStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(ToxaLanguageParser.T__1)
            self.state = 103
            self.match(ToxaLanguageParser.LPAREN)
            self.state = 104
            self.expression()
            self.state = 105
            self.match(ToxaLanguageParser.RPAREN)
            self.state = 106
            self.match(ToxaLanguageParser.THEN)
            self.state = 107
            self.ifBlock()
            self.state = 108
            self.match(ToxaLanguageParser.T__2)
            self.state = 109
            self.elseBlock()
            self.state = 110
            self.match(ToxaLanguageParser.ENDIF)
            self.state = 111
            self.match(ToxaLanguageParser.END_STATE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ToxaLanguageParser.StatementContext)
            else:
                return self.getTypedRuleContext(ToxaLanguageParser.StatementContext,i)


        def getRuleIndex(self):
            return ToxaLanguageParser.RULE_elseBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseBlock" ):
                listener.enterElseBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseBlock" ):
                listener.exitElseBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseBlock" ):
                return visitor.visitElseBlock(self)
            else:
                return visitor.visitChildren(self)




    def elseBlock(self):

        localctx = ToxaLanguageParser.ElseBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_elseBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 544212726) != 0):
                self.state = 113
                self.statement()
                self.state = 118
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(ToxaLanguageParser.LPAREN, 0)

        def forInitializer(self):
            return self.getTypedRuleContext(ToxaLanguageParser.ForInitializerContext,0)


        def END_STATE(self, i:int=None):
            if i is None:
                return self.getTokens(ToxaLanguageParser.END_STATE)
            else:
                return self.getToken(ToxaLanguageParser.END_STATE, i)

        def forCondition(self):
            return self.getTypedRuleContext(ToxaLanguageParser.ForConditionContext,0)


        def forUpdate(self):
            return self.getTypedRuleContext(ToxaLanguageParser.ForUpdateContext,0)


        def RPAREN(self):
            return self.getToken(ToxaLanguageParser.RPAREN, 0)

        def THEN(self):
            return self.getToken(ToxaLanguageParser.THEN, 0)

        def forBlock(self):
            return self.getTypedRuleContext(ToxaLanguageParser.ForBlockContext,0)


        def ENDFOR(self):
            return self.getToken(ToxaLanguageParser.ENDFOR, 0)

        def getRuleIndex(self):
            return ToxaLanguageParser.RULE_forStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = ToxaLanguageParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_forStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(ToxaLanguageParser.T__3)
            self.state = 120
            self.match(ToxaLanguageParser.LPAREN)
            self.state = 121
            self.forInitializer()
            self.state = 122
            self.match(ToxaLanguageParser.END_STATE)
            self.state = 123
            self.forCondition()
            self.state = 124
            self.match(ToxaLanguageParser.END_STATE)
            self.state = 125
            self.forUpdate()
            self.state = 126
            self.match(ToxaLanguageParser.RPAREN)
            self.state = 127
            self.match(ToxaLanguageParser.THEN)
            self.state = 128
            self.forBlock()
            self.state = 129
            self.match(ToxaLanguageParser.ENDFOR)
            self.state = 130
            self.match(ToxaLanguageParser.END_STATE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ToxaLanguageParser.StatementContext)
            else:
                return self.getTypedRuleContext(ToxaLanguageParser.StatementContext,i)


        def getRuleIndex(self):
            return ToxaLanguageParser.RULE_forBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForBlock" ):
                listener.enterForBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForBlock" ):
                listener.exitForBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForBlock" ):
                return visitor.visitForBlock(self)
            else:
                return visitor.visitChildren(self)




    def forBlock(self):

        localctx = ToxaLanguageParser.ForBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_forBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 544212726) != 0):
                self.state = 132
                self.statement()
                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForInitializerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(ToxaLanguageParser.TypeContext,0)


        def ID(self):
            return self.getToken(ToxaLanguageParser.ID, 0)

        def EQ(self):
            return self.getToken(ToxaLanguageParser.EQ, 0)

        def expression(self):
            return self.getTypedRuleContext(ToxaLanguageParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ToxaLanguageParser.RULE_forInitializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForInitializer" ):
                listener.enterForInitializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForInitializer" ):
                listener.exitForInitializer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForInitializer" ):
                return visitor.visitForInitializer(self)
            else:
                return visitor.visitChildren(self)




    def forInitializer(self):

        localctx = ToxaLanguageParser.ForInitializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_forInitializer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.type_()
            self.state = 139
            self.match(ToxaLanguageParser.ID)
            self.state = 140
            self.match(ToxaLanguageParser.EQ)
            self.state = 141
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ToxaLanguageParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ToxaLanguageParser.RULE_forCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForCondition" ):
                listener.enterForCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForCondition" ):
                listener.exitForCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForCondition" ):
                return visitor.visitForCondition(self)
            else:
                return visitor.visitChildren(self)




    def forCondition(self):

        localctx = ToxaLanguageParser.ForConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_forCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForUpdateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ToxaLanguageParser.ID, 0)

        def incrementOrDecrement(self):
            return self.getTypedRuleContext(ToxaLanguageParser.IncrementOrDecrementContext,0)


        def getRuleIndex(self):
            return ToxaLanguageParser.RULE_forUpdate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForUpdate" ):
                listener.enterForUpdate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForUpdate" ):
                listener.exitForUpdate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForUpdate" ):
                return visitor.visitForUpdate(self)
            else:
                return visitor.visitChildren(self)




    def forUpdate(self):

        localctx = ToxaLanguageParser.ForUpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_forUpdate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(ToxaLanguageParser.ID)
            self.state = 146
            self.incrementOrDecrement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IncrementOrDecrementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INCREMENT(self):
            return self.getToken(ToxaLanguageParser.INCREMENT, 0)

        def DECREMENT(self):
            return self.getToken(ToxaLanguageParser.DECREMENT, 0)

        def getRuleIndex(self):
            return ToxaLanguageParser.RULE_incrementOrDecrement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIncrementOrDecrement" ):
                listener.enterIncrementOrDecrement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIncrementOrDecrement" ):
                listener.exitIncrementOrDecrement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIncrementOrDecrement" ):
                return visitor.visitIncrementOrDecrement(self)
            else:
                return visitor.visitChildren(self)




    def incrementOrDecrement(self):

        localctx = ToxaLanguageParser.IncrementOrDecrementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_incrementOrDecrement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            _la = self._input.LA(1)
            if not(_la==11 or _la==12):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(ToxaLanguageParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(ToxaLanguageParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(ToxaLanguageParser.RPAREN, 0)

        def THEN(self):
            return self.getToken(ToxaLanguageParser.THEN, 0)

        def whileBlock(self):
            return self.getTypedRuleContext(ToxaLanguageParser.WhileBlockContext,0)


        def ENDWHILE(self):
            return self.getToken(ToxaLanguageParser.ENDWHILE, 0)

        def END_STATE(self):
            return self.getToken(ToxaLanguageParser.END_STATE, 0)

        def getRuleIndex(self):
            return ToxaLanguageParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = ToxaLanguageParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(ToxaLanguageParser.T__4)
            self.state = 151
            self.match(ToxaLanguageParser.LPAREN)
            self.state = 152
            self.expression()
            self.state = 153
            self.match(ToxaLanguageParser.RPAREN)
            self.state = 154
            self.match(ToxaLanguageParser.THEN)
            self.state = 155
            self.whileBlock()
            self.state = 156
            self.match(ToxaLanguageParser.ENDWHILE)
            self.state = 157
            self.match(ToxaLanguageParser.END_STATE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ToxaLanguageParser.StatementContext)
            else:
                return self.getTypedRuleContext(ToxaLanguageParser.StatementContext,i)


        def getRuleIndex(self):
            return ToxaLanguageParser.RULE_whileBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileBlock" ):
                listener.enterWhileBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileBlock" ):
                listener.exitWhileBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileBlock" ):
                return visitor.visitWhileBlock(self)
            else:
                return visitor.visitChildren(self)




    def whileBlock(self):

        localctx = ToxaLanguageParser.WhileBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_whileBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 544212726) != 0):
                self.state = 159
                self.statement()
                self.state = 164
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ToxaLanguageParser.ID, 0)

        def LPAREN(self):
            return self.getToken(ToxaLanguageParser.LPAREN, 0)

        def params(self):
            return self.getTypedRuleContext(ToxaLanguageParser.ParamsContext,0)


        def RPAREN(self):
            return self.getToken(ToxaLanguageParser.RPAREN, 0)

        def THEN(self):
            return self.getToken(ToxaLanguageParser.THEN, 0)

        def functionBlock(self):
            return self.getTypedRuleContext(ToxaLanguageParser.FunctionBlockContext,0)


        def ENDFUNCTION(self):
            return self.getToken(ToxaLanguageParser.ENDFUNCTION, 0)

        def END_STATE(self):
            return self.getToken(ToxaLanguageParser.END_STATE, 0)

        def getRuleIndex(self):
            return ToxaLanguageParser.RULE_functionStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionStatement" ):
                listener.enterFunctionStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionStatement" ):
                listener.exitFunctionStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionStatement" ):
                return visitor.visitFunctionStatement(self)
            else:
                return visitor.visitChildren(self)




    def functionStatement(self):

        localctx = ToxaLanguageParser.FunctionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_functionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(ToxaLanguageParser.T__5)
            self.state = 166
            self.match(ToxaLanguageParser.ID)
            self.state = 167
            self.match(ToxaLanguageParser.LPAREN)
            self.state = 168
            self.params()
            self.state = 169
            self.match(ToxaLanguageParser.RPAREN)
            self.state = 170
            self.match(ToxaLanguageParser.THEN)
            self.state = 171
            self.functionBlock()
            self.state = 172
            self.match(ToxaLanguageParser.ENDFUNCTION)
            self.state = 173
            self.match(ToxaLanguageParser.END_STATE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ToxaLanguageParser.StatementContext)
            else:
                return self.getTypedRuleContext(ToxaLanguageParser.StatementContext,i)


        def getRuleIndex(self):
            return ToxaLanguageParser.RULE_functionBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionBlock" ):
                listener.enterFunctionBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionBlock" ):
                listener.exitFunctionBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionBlock" ):
                return visitor.visitFunctionBlock(self)
            else:
                return visitor.visitChildren(self)




    def functionBlock(self):

        localctx = ToxaLanguageParser.FunctionBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_functionBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 544212726) != 0):
                self.state = 175
                self.statement()
                self.state = 180
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ToxaLanguageParser.ExpressionContext,0)


        def END_STATE(self):
            return self.getToken(ToxaLanguageParser.END_STATE, 0)

        def getRuleIndex(self):
            return ToxaLanguageParser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = ToxaLanguageParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(ToxaLanguageParser.T__6)
            self.state = 182
            self.expression()
            self.state = 183
            self.match(ToxaLanguageParser.END_STATE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ToxaLanguageParser.ID, 0)

        def LPAREN(self):
            return self.getToken(ToxaLanguageParser.LPAREN, 0)

        def params(self):
            return self.getTypedRuleContext(ToxaLanguageParser.ParamsContext,0)


        def RPAREN(self):
            return self.getToken(ToxaLanguageParser.RPAREN, 0)

        def getRuleIndex(self):
            return ToxaLanguageParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = ToxaLanguageParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_functionCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.match(ToxaLanguageParser.ID)
            self.state = 186
            self.match(ToxaLanguageParser.LPAREN)
            self.state = 187
            self.params()
            self.state = 188
            self.match(ToxaLanguageParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ToxaLanguageParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ToxaLanguageParser.ExpressionContext,i)


        def getRuleIndex(self):
            return ToxaLanguageParser.RULE_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams" ):
                listener.enterParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams" ):
                listener.exitParams(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = ToxaLanguageParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 544210944) != 0):
                self.state = 190
                self.expression()


            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 193
                self.match(ToxaLanguageParser.T__7)
                self.state = 194
                self.expression()
                self.state = 199
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arithmetic(self):
            return self.getTypedRuleContext(ToxaLanguageParser.ArithmeticContext,0)


        def comparison(self):
            return self.getTypedRuleContext(ToxaLanguageParser.ComparisonContext,0)


        def logical(self):
            return self.getTypedRuleContext(ToxaLanguageParser.LogicalContext,0)


        def operand(self):
            return self.getTypedRuleContext(ToxaLanguageParser.OperandContext,0)


        def LPAREN(self):
            return self.getToken(ToxaLanguageParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(ToxaLanguageParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(ToxaLanguageParser.RPAREN, 0)

        def getRuleIndex(self):
            return ToxaLanguageParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = ToxaLanguageParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_expression)
        try:
            self.state = 208
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.arithmetic()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 201
                self.comparison()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 202
                self.logical()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 203
                self.operand()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 204
                self.match(ToxaLanguageParser.LPAREN)
                self.state = 205
                self.expression()
                self.state = 206
                self.match(ToxaLanguageParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ToxaLanguageParser.OperandContext)
            else:
                return self.getTypedRuleContext(ToxaLanguageParser.OperandContext,i)


        def GT(self):
            return self.getToken(ToxaLanguageParser.GT, 0)

        def LT(self):
            return self.getToken(ToxaLanguageParser.LT, 0)

        def GE(self):
            return self.getToken(ToxaLanguageParser.GE, 0)

        def LE(self):
            return self.getToken(ToxaLanguageParser.LE, 0)

        def EQ(self):
            return self.getToken(ToxaLanguageParser.EQ, 0)

        def EQEQ(self):
            return self.getToken(ToxaLanguageParser.EQEQ, 0)

        def NE(self):
            return self.getToken(ToxaLanguageParser.NE, 0)

        def getRuleIndex(self):
            return ToxaLanguageParser.RULE_comparison

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparison" ):
                return visitor.visitComparison(self)
            else:
                return visitor.visitChildren(self)




    def comparison(self):

        localctx = ToxaLanguageParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_comparison)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.operand()
            self.state = 211
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 270851375104) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 212
            self.operand()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArithmeticContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ToxaLanguageParser.OperandContext)
            else:
                return self.getTypedRuleContext(ToxaLanguageParser.OperandContext,i)


        def MUL(self):
            return self.getToken(ToxaLanguageParser.MUL, 0)

        def DIV(self):
            return self.getToken(ToxaLanguageParser.DIV, 0)

        def REM(self):
            return self.getToken(ToxaLanguageParser.REM, 0)

        def PLUS(self):
            return self.getToken(ToxaLanguageParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(ToxaLanguageParser.MINUS, 0)

        def getRuleIndex(self):
            return ToxaLanguageParser.RULE_arithmetic

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmetic" ):
                listener.enterArithmetic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmetic" ):
                listener.exitArithmetic(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmetic" ):
                return visitor.visitArithmetic(self)
            else:
                return visitor.visitChildren(self)




    def arithmetic(self):

        localctx = ToxaLanguageParser.ArithmeticContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_arithmetic)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.operand()
            self.state = 215
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 260046848) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 216
            self.operand()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ToxaLanguageParser.OperandContext)
            else:
                return self.getTypedRuleContext(ToxaLanguageParser.OperandContext,i)


        def AND(self):
            return self.getToken(ToxaLanguageParser.AND, 0)

        def OR(self):
            return self.getToken(ToxaLanguageParser.OR, 0)

        def getRuleIndex(self):
            return ToxaLanguageParser.RULE_logical

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogical" ):
                listener.enterLogical(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogical" ):
                listener.exitLogical(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical" ):
                return visitor.visitLogical(self)
            else:
                return visitor.visitChildren(self)




    def logical(self):

        localctx = ToxaLanguageParser.LogicalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_logical)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.operand()
            self.state = 219
            _la = self._input.LA(1)
            if not(_la==38 or _la==39):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 220
            self.operand()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(ToxaLanguageParser.INT, 0)

        def FLOAT(self):
            return self.getToken(ToxaLanguageParser.FLOAT, 0)

        def ID(self):
            return self.getToken(ToxaLanguageParser.ID, 0)

        def functionCall(self):
            return self.getTypedRuleContext(ToxaLanguageParser.FunctionCallContext,0)


        def getRuleIndex(self):
            return ToxaLanguageParser.RULE_operand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperand" ):
                listener.enterOperand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperand" ):
                listener.exitOperand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = ToxaLanguageParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_operand)
        try:
            self.state = 226
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 222
                self.match(ToxaLanguageParser.INT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 223
                self.match(ToxaLanguageParser.FLOAT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 224
                self.match(ToxaLanguageParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 225
                self.functionCall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ToxaLanguageParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = ToxaLanguageParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            _la = self._input.LA(1)
            if not(_la==9 or _la==10):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





