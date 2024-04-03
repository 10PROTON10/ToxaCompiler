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
        4,1,15,64,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,0,5,0,18,8,0,10,0,12,0,21,9,0,1,1,1,1,1,1,1,1,1,1,1,
        1,1,2,1,2,1,2,5,2,32,8,2,10,2,12,2,35,9,2,1,3,1,3,1,3,5,3,40,8,3,
        10,3,12,3,43,9,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,52,8,4,1,5,1,5,
        1,5,1,5,3,5,58,8,5,1,5,1,5,1,6,1,6,1,6,0,0,7,0,2,4,6,8,10,12,0,3,
        1,0,3,4,1,0,5,6,1,0,11,12,65,0,19,1,0,0,0,2,22,1,0,0,0,4,28,1,0,
        0,0,6,36,1,0,0,0,8,51,1,0,0,0,10,53,1,0,0,0,12,61,1,0,0,0,14,18,
        3,10,5,0,15,18,3,2,1,0,16,18,3,4,2,0,17,14,1,0,0,0,17,15,1,0,0,0,
        17,16,1,0,0,0,18,21,1,0,0,0,19,17,1,0,0,0,19,20,1,0,0,0,20,1,1,0,
        0,0,21,19,1,0,0,0,22,23,5,10,0,0,23,24,5,7,0,0,24,25,3,4,2,0,25,
        26,5,8,0,0,26,27,5,15,0,0,27,3,1,0,0,0,28,33,3,6,3,0,29,30,7,0,0,
        0,30,32,3,6,3,0,31,29,1,0,0,0,32,35,1,0,0,0,33,31,1,0,0,0,33,34,
        1,0,0,0,34,5,1,0,0,0,35,33,1,0,0,0,36,41,3,8,4,0,37,38,7,1,0,0,38,
        40,3,8,4,0,39,37,1,0,0,0,40,43,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,
        0,42,7,1,0,0,0,43,41,1,0,0,0,44,52,5,1,0,0,45,52,5,2,0,0,46,47,5,
        7,0,0,47,48,3,4,2,0,48,49,5,8,0,0,49,52,1,0,0,0,50,52,5,13,0,0,51,
        44,1,0,0,0,51,45,1,0,0,0,51,46,1,0,0,0,51,50,1,0,0,0,52,9,1,0,0,
        0,53,54,3,12,6,0,54,57,5,13,0,0,55,56,5,9,0,0,56,58,3,4,2,0,57,55,
        1,0,0,0,57,58,1,0,0,0,58,59,1,0,0,0,59,60,5,15,0,0,60,11,1,0,0,0,
        61,62,7,2,0,0,62,13,1,0,0,0,6,17,19,33,41,51,57
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

        def assignStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ToxaLanguageParser.AssignStatementContext)
            else:
                return self.getTypedRuleContext(ToxaLanguageParser.AssignStatementContext,i)


        def printStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ToxaLanguageParser.PrintStatementContext)
            else:
                return self.getTypedRuleContext(ToxaLanguageParser.PrintStatementContext,i)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ToxaLanguageParser.ExprContext)
            else:
                return self.getTypedRuleContext(ToxaLanguageParser.ExprContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 15494) != 0):
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

                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            self.state = 22
            self.match(ToxaLanguageParser.PRINT)
            self.state = 23
            self.match(ToxaLanguageParser.LPAREN)
            self.state = 24
            self.expr()
            self.state = 25
            self.match(ToxaLanguageParser.RPAREN)
            self.state = 26
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
            self.state = 28
            self.term()
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3 or _la==4:
                self.state = 29
                _la = self._input.LA(1)
                if not(_la==3 or _la==4):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 30
                self.term()
                self.state = 35
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
            self.state = 36
            self.factor()
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5 or _la==6:
                self.state = 37
                _la = self._input.LA(1)
                if not(_la==5 or _la==6):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 38
                self.factor()
                self.state = 43
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
            self.state = 51
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 44
                self.match(ToxaLanguageParser.INT)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 45
                self.match(ToxaLanguageParser.FLOAT)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 46
                self.match(ToxaLanguageParser.LPAREN)
                self.state = 47
                self.expr()
                self.state = 48
                self.match(ToxaLanguageParser.RPAREN)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 50
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
            self.state = 53
            self.type_()
            self.state = 54
            self.match(ToxaLanguageParser.ID)
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 55
                self.match(ToxaLanguageParser.ASSIGN)
                self.state = 56
                self.expr()


            self.state = 59
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
            self.state = 61
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





