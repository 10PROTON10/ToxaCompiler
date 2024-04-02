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
        4,1,15,61,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,0,3,0,18,8,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,5,2,
        29,8,2,10,2,12,2,32,9,2,1,3,1,3,1,3,5,3,37,8,3,10,3,12,3,40,9,3,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,49,8,4,1,5,1,5,1,5,1,5,3,5,55,8,
        5,1,5,1,5,1,6,1,6,1,6,0,0,7,0,2,4,6,8,10,12,0,3,1,0,3,4,1,0,5,6,
        1,0,11,12,61,0,17,1,0,0,0,2,19,1,0,0,0,4,25,1,0,0,0,6,33,1,0,0,0,
        8,48,1,0,0,0,10,50,1,0,0,0,12,58,1,0,0,0,14,18,3,10,5,0,15,18,3,
        2,1,0,16,18,3,4,2,0,17,14,1,0,0,0,17,15,1,0,0,0,17,16,1,0,0,0,18,
        1,1,0,0,0,19,20,5,10,0,0,20,21,5,7,0,0,21,22,3,4,2,0,22,23,5,8,0,
        0,23,24,5,15,0,0,24,3,1,0,0,0,25,30,3,6,3,0,26,27,7,0,0,0,27,29,
        3,6,3,0,28,26,1,0,0,0,29,32,1,0,0,0,30,28,1,0,0,0,30,31,1,0,0,0,
        31,5,1,0,0,0,32,30,1,0,0,0,33,38,3,8,4,0,34,35,7,1,0,0,35,37,3,8,
        4,0,36,34,1,0,0,0,37,40,1,0,0,0,38,36,1,0,0,0,38,39,1,0,0,0,39,7,
        1,0,0,0,40,38,1,0,0,0,41,49,5,1,0,0,42,49,5,2,0,0,43,44,5,7,0,0,
        44,45,3,4,2,0,45,46,5,8,0,0,46,49,1,0,0,0,47,49,5,13,0,0,48,41,1,
        0,0,0,48,42,1,0,0,0,48,43,1,0,0,0,48,47,1,0,0,0,49,9,1,0,0,0,50,
        51,3,12,6,0,51,54,5,13,0,0,52,53,5,9,0,0,53,55,3,4,2,0,54,52,1,0,
        0,0,54,55,1,0,0,0,55,56,1,0,0,0,56,57,5,15,0,0,57,11,1,0,0,0,58,
        59,7,2,0,0,59,13,1,0,0,0,5,17,30,38,48,54
    ]

class ToxaLanguageParser ( Parser ):

    grammarFileName = "ToxaLanguage.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'+'", "'-'", 
                     "'*'", "'/'", "'('", "')'", "'='", "'print'", "'int'", 
                     "'float'", "<INVALID>", "<INVALID>", "';'" ]

    symbolicNames = [ "<INVALID>", "INT", "FLOAT", "PLUS", "MINUS", "MULT", 
                      "DIV", "LPAREN", "RPAREN", "ASSIGN", "PRINT", "TYPE_INT", 
                      "TYPE_FLOAT", "ID", "WS", "END_STATE" ]

    RULE_prog = 0
    RULE_printStatement = 1
    RULE_expr = 2
    RULE_term = 3
    RULE_factor = 4
    RULE_assignStatement = 5
    RULE_type = 6

    ruleNames =  [ "prog", "printStatement", "expr", "term", "factor", "assignStatement", 
                   "type" ]

    EOF = Token.EOF
    INT=1
    FLOAT=2
    PLUS=3
    MINUS=4
    MULT=5
    DIV=6
    LPAREN=7
    RPAREN=8
    ASSIGN=9
    PRINT=10
    TYPE_INT=11
    TYPE_FLOAT=12
    ID=13
    WS=14
    END_STATE=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignStatement(self):
            return self.getTypedRuleContext(ToxaLanguageParser.AssignStatementContext,0)


        def printStatement(self):
            return self.getTypedRuleContext(ToxaLanguageParser.PrintStatementContext,0)


        def expr(self):
            return self.getTypedRuleContext(ToxaLanguageParser.ExprContext,0)


        def getRuleIndex(self):
            return ToxaLanguageParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = ToxaLanguageParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 12]:
                self.state = 14
                self.assignStatement()
                pass
            elif token in [10]:
                self.state = 15
                self.printStatement()
                pass
            elif token in [1, 2, 7, 13]:
                self.state = 16
                self.expr()
                pass
            else:
                raise NoViableAltException(self)

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

        def PRINT(self):
            return self.getToken(ToxaLanguageParser.PRINT, 0)

        def LPAREN(self):
            return self.getToken(ToxaLanguageParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(ToxaLanguageParser.ExprContext,0)


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
        self.enterRule(localctx, 2, self.RULE_printStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.match(ToxaLanguageParser.PRINT)
            self.state = 20
            self.match(ToxaLanguageParser.LPAREN)
            self.state = 21
            self.expr()
            self.state = 22
            self.match(ToxaLanguageParser.RPAREN)
            self.state = 23
            self.match(ToxaLanguageParser.END_STATE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ToxaLanguageParser.TermContext)
            else:
                return self.getTypedRuleContext(ToxaLanguageParser.TermContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(ToxaLanguageParser.PLUS)
            else:
                return self.getToken(ToxaLanguageParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(ToxaLanguageParser.MINUS)
            else:
                return self.getToken(ToxaLanguageParser.MINUS, i)

        def getRuleIndex(self):
            return ToxaLanguageParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = ToxaLanguageParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.term()
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3 or _la==4:
                self.state = 26
                _la = self._input.LA(1)
                if not(_la==3 or _la==4):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 27
                self.term()
                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ToxaLanguageParser.FactorContext)
            else:
                return self.getTypedRuleContext(ToxaLanguageParser.FactorContext,i)


        def MULT(self, i:int=None):
            if i is None:
                return self.getTokens(ToxaLanguageParser.MULT)
            else:
                return self.getToken(ToxaLanguageParser.MULT, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(ToxaLanguageParser.DIV)
            else:
                return self.getToken(ToxaLanguageParser.DIV, i)

        def getRuleIndex(self):
            return ToxaLanguageParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = ToxaLanguageParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.factor()
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5 or _la==6:
                self.state = 34
                _la = self._input.LA(1)
                if not(_la==5 or _la==6):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 35
                self.factor()
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(ToxaLanguageParser.INT, 0)

        def FLOAT(self):
            return self.getToken(ToxaLanguageParser.FLOAT, 0)

        def LPAREN(self):
            return self.getToken(ToxaLanguageParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(ToxaLanguageParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(ToxaLanguageParser.RPAREN, 0)

        def ID(self):
            return self.getToken(ToxaLanguageParser.ID, 0)

        def getRuleIndex(self):
            return ToxaLanguageParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = ToxaLanguageParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_factor)
        try:
            self.state = 48
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.match(ToxaLanguageParser.INT)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.match(ToxaLanguageParser.FLOAT)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 43
                self.match(ToxaLanguageParser.LPAREN)
                self.state = 44
                self.expr()
                self.state = 45
                self.match(ToxaLanguageParser.RPAREN)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 47
                self.match(ToxaLanguageParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(ToxaLanguageParser.TypeContext,0)


        def ID(self):
            return self.getToken(ToxaLanguageParser.ID, 0)

        def END_STATE(self):
            return self.getToken(ToxaLanguageParser.END_STATE, 0)

        def ASSIGN(self):
            return self.getToken(ToxaLanguageParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ToxaLanguageParser.ExprContext,0)


        def getRuleIndex(self):
            return ToxaLanguageParser.RULE_assignStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignStatement" ):
                listener.enterAssignStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignStatement" ):
                listener.exitAssignStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStatement" ):
                return visitor.visitAssignStatement(self)
            else:
                return visitor.visitChildren(self)




    def assignStatement(self):

        localctx = ToxaLanguageParser.AssignStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assignStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.type_()
            self.state = 51
            self.match(ToxaLanguageParser.ID)
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 52
                self.match(ToxaLanguageParser.ASSIGN)
                self.state = 53
                self.expr()


            self.state = 56
            self.match(ToxaLanguageParser.END_STATE)
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

        def TYPE_INT(self):
            return self.getToken(ToxaLanguageParser.TYPE_INT, 0)

        def TYPE_FLOAT(self):
            return self.getToken(ToxaLanguageParser.TYPE_FLOAT, 0)

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
        self.enterRule(localctx, 12, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
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





