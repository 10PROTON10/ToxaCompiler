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
        4,1,6,22,2,0,7,0,1,0,1,0,1,0,1,0,1,0,1,0,3,0,9,8,0,1,0,1,0,1,0,1,
        0,1,0,1,0,5,0,17,8,0,10,0,12,0,20,9,0,1,0,0,1,0,1,0,0,0,23,0,8,1,
        0,0,0,2,3,6,0,-1,0,3,9,5,1,0,0,4,5,5,4,0,0,5,6,3,0,0,0,6,7,5,5,0,
        0,7,9,1,0,0,0,8,2,1,0,0,0,8,4,1,0,0,0,9,18,1,0,0,0,10,11,10,3,0,
        0,11,12,5,2,0,0,12,17,3,0,0,4,13,14,10,2,0,0,14,15,5,3,0,0,15,17,
        3,0,0,3,16,10,1,0,0,0,16,13,1,0,0,0,17,20,1,0,0,0,18,16,1,0,0,0,
        18,19,1,0,0,0,19,1,1,0,0,0,20,18,1,0,0,0,3,8,16,18
    ]

class ToxaLanguageParser ( Parser ):

    grammarFileName = "ToxaLanguage.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'+'", "'*'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "INT", "PLUS", "MULT", "OPEN_PAREN", 
                      "CLOSE_PAREN", "WS" ]

    RULE_expression = 0

    ruleNames =  [ "expression" ]

    EOF = Token.EOF
    INT=1
    PLUS=2
    MULT=3
    OPEN_PAREN=4
    CLOSE_PAREN=5
    WS=6

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(ToxaLanguageParser.INT, 0)

        def OPEN_PAREN(self):
            return self.getToken(ToxaLanguageParser.OPEN_PAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ToxaLanguageParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ToxaLanguageParser.ExpressionContext,i)


        def CLOSE_PAREN(self):
            return self.getToken(ToxaLanguageParser.CLOSE_PAREN, 0)

        def PLUS(self):
            return self.getToken(ToxaLanguageParser.PLUS, 0)

        def MULT(self):
            return self.getToken(ToxaLanguageParser.MULT, 0)

        def getRuleIndex(self):
            return ToxaLanguageParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ToxaLanguageParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.state = 3
                self.match(ToxaLanguageParser.INT)
                pass
            elif token in [4]:
                self.state = 4
                self.match(ToxaLanguageParser.OPEN_PAREN)
                self.state = 5
                self.expression(0)
                self.state = 6
                self.match(ToxaLanguageParser.CLOSE_PAREN)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 18
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 16
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = ToxaLanguageParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 10
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 11
                        self.match(ToxaLanguageParser.PLUS)
                        self.state = 12
                        self.expression(4)
                        pass

                    elif la_ == 2:
                        localctx = ToxaLanguageParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 13
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 14
                        self.match(ToxaLanguageParser.MULT)
                        self.state = 15
                        self.expression(3)
                        pass

             
                self.state = 20
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
        self._predicates[0] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




