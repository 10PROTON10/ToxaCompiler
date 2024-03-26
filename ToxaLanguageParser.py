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
        4,1,9,23,2,0,7,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,3,0,10,8,0,1,0,1,0,
        1,0,1,0,1,0,1,0,5,0,18,8,0,10,0,12,0,21,9,0,1,0,0,1,0,1,0,0,2,1,
        0,5,6,1,0,3,4,25,0,9,1,0,0,0,2,3,6,0,-1,0,3,10,5,1,0,0,4,10,5,2,
        0,0,5,6,5,7,0,0,6,7,3,0,0,0,7,8,5,8,0,0,8,10,1,0,0,0,9,2,1,0,0,0,
        9,4,1,0,0,0,9,5,1,0,0,0,10,19,1,0,0,0,11,12,10,5,0,0,12,13,7,0,0,
        0,13,18,3,0,0,6,14,15,10,4,0,0,15,16,7,1,0,0,16,18,3,0,0,5,17,11,
        1,0,0,0,17,14,1,0,0,0,18,21,1,0,0,0,19,17,1,0,0,0,19,20,1,0,0,0,
        20,1,1,0,0,0,21,19,1,0,0,0,3,9,17,19
    ]

class ToxaLanguageParser ( Parser ):

    grammarFileName = "ToxaLanguage.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'+'", "'-'", 
                     "'*'", "'/'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "INT", "FLOAT", "PLUS", "MINUS", "MULT", 
                      "DIV", "LPAREN", "RPAREN", "WS" ]

    RULE_expr = 0

    ruleNames =  [ "expr" ]

    EOF = Token.EOF
    INT=1
    FLOAT=2
    PLUS=3
    MINUS=4
    MULT=5
    DIV=6
    LPAREN=7
    RPAREN=8
    WS=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExprContext(ParserRuleContext):
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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ToxaLanguageParser.ExprContext)
            else:
                return self.getTypedRuleContext(ToxaLanguageParser.ExprContext,i)


        def RPAREN(self):
            return self.getToken(ToxaLanguageParser.RPAREN, 0)

        def MULT(self):
            return self.getToken(ToxaLanguageParser.MULT, 0)

        def DIV(self):
            return self.getToken(ToxaLanguageParser.DIV, 0)

        def PLUS(self):
            return self.getToken(ToxaLanguageParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(ToxaLanguageParser.MINUS, 0)

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



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ToxaLanguageParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.state = 3
                self.match(ToxaLanguageParser.INT)
                pass
            elif token in [2]:
                self.state = 4
                self.match(ToxaLanguageParser.FLOAT)
                pass
            elif token in [7]:
                self.state = 5
                self.match(ToxaLanguageParser.LPAREN)
                self.state = 6
                self.expr(0)
                self.state = 7
                self.match(ToxaLanguageParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 19
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 17
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = ToxaLanguageParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 11
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 12
                        _la = self._input.LA(1)
                        if not(_la==5 or _la==6):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 13
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = ToxaLanguageParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 14
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 15
                        _la = self._input.LA(1)
                        if not(_la==3 or _la==4):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 16
                        self.expr(5)
                        pass

             
                self.state = 21
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




