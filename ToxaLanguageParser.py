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
        4,1,9,43,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,
        1,0,5,0,16,8,0,10,0,12,0,19,9,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,5,1,30,8,1,10,1,12,1,33,9,1,1,2,1,2,1,2,1,2,1,2,1,2,3,2,41,8,
        2,1,2,0,2,0,2,3,0,2,4,0,0,45,0,6,1,0,0,0,2,20,1,0,0,0,4,40,1,0,0,
        0,6,7,6,0,-1,0,7,8,3,2,1,0,8,17,1,0,0,0,9,10,10,2,0,0,10,11,5,3,
        0,0,11,16,3,2,1,0,12,13,10,1,0,0,13,14,5,4,0,0,14,16,3,2,1,0,15,
        9,1,0,0,0,15,12,1,0,0,0,16,19,1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,
        0,18,1,1,0,0,0,19,17,1,0,0,0,20,21,6,1,-1,0,21,22,3,4,2,0,22,31,
        1,0,0,0,23,24,10,2,0,0,24,25,5,5,0,0,25,30,3,4,2,0,26,27,10,1,0,
        0,27,28,5,6,0,0,28,30,3,4,2,0,29,23,1,0,0,0,29,26,1,0,0,0,30,33,
        1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,3,1,0,0,0,33,31,1,0,0,0,34,
        41,5,1,0,0,35,41,5,2,0,0,36,37,5,7,0,0,37,38,3,0,0,0,38,39,5,8,0,
        0,39,41,1,0,0,0,40,34,1,0,0,0,40,35,1,0,0,0,40,36,1,0,0,0,41,5,1,
        0,0,0,5,15,17,29,31,40
    ]

class ToxaLanguageParser ( Parser ):

    grammarFileName = "ToxaLanguage.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'+'", "'-'", 
                     "'*'", "'/'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "INT", "FLOAT", "PLUS", "MINUS", "MULT", 
                      "DIV", "OPEN_PAREN", "CLOSE_PAREN", "WS" ]

    RULE_expression = 0
    RULE_multExpr = 1
    RULE_atom = 2

    ruleNames =  [ "expression", "multExpr", "atom" ]

    EOF = Token.EOF
    INT=1
    FLOAT=2
    PLUS=3
    MINUS=4
    MULT=5
    DIV=6
    OPEN_PAREN=7
    CLOSE_PAREN=8
    WS=9

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

        def multExpr(self):
            return self.getTypedRuleContext(ToxaLanguageParser.MultExprContext,0)


        def expression(self):
            return self.getTypedRuleContext(ToxaLanguageParser.ExpressionContext,0)


        def PLUS(self):
            return self.getToken(ToxaLanguageParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(ToxaLanguageParser.MINUS, 0)

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



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ToxaLanguageParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7
            self.multExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 17
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 15
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                    if la_ == 1:
                        localctx = ToxaLanguageParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 9
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 10
                        self.match(ToxaLanguageParser.PLUS)
                        self.state = 11
                        self.multExpr(0)
                        pass

                    elif la_ == 2:
                        localctx = ToxaLanguageParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 12
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 13
                        self.match(ToxaLanguageParser.MINUS)
                        self.state = 14
                        self.multExpr(0)
                        pass

             
                self.state = 19
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class MultExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(ToxaLanguageParser.AtomContext,0)


        def multExpr(self):
            return self.getTypedRuleContext(ToxaLanguageParser.MultExprContext,0)


        def MULT(self):
            return self.getToken(ToxaLanguageParser.MULT, 0)

        def DIV(self):
            return self.getToken(ToxaLanguageParser.DIV, 0)

        def getRuleIndex(self):
            return ToxaLanguageParser.RULE_multExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultExpr" ):
                listener.enterMultExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultExpr" ):
                listener.exitMultExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultExpr" ):
                return visitor.visitMultExpr(self)
            else:
                return visitor.visitChildren(self)



    def multExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ToxaLanguageParser.MultExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_multExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self.atom()
            self._ctx.stop = self._input.LT(-1)
            self.state = 31
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 29
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = ToxaLanguageParser.MultExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_multExpr)
                        self.state = 23
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 24
                        self.match(ToxaLanguageParser.MULT)
                        self.state = 25
                        self.atom()
                        pass

                    elif la_ == 2:
                        localctx = ToxaLanguageParser.MultExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_multExpr)
                        self.state = 26
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 27
                        self.match(ToxaLanguageParser.DIV)
                        self.state = 28
                        self.atom()
                        pass

             
                self.state = 33
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(ToxaLanguageParser.INT, 0)

        def FLOAT(self):
            return self.getToken(ToxaLanguageParser.FLOAT, 0)

        def OPEN_PAREN(self):
            return self.getToken(ToxaLanguageParser.OPEN_PAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(ToxaLanguageParser.ExpressionContext,0)


        def CLOSE_PAREN(self):
            return self.getToken(ToxaLanguageParser.CLOSE_PAREN, 0)

        def getRuleIndex(self):
            return ToxaLanguageParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = ToxaLanguageParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_atom)
        try:
            self.state = 40
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.match(ToxaLanguageParser.INT)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 35
                self.match(ToxaLanguageParser.FLOAT)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 36
                self.match(ToxaLanguageParser.OPEN_PAREN)
                self.state = 37
                self.expression(0)
                self.state = 38
                self.match(ToxaLanguageParser.CLOSE_PAREN)
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.expression_sempred
        self._predicates[1] = self.multExpr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         

    def multExpr_sempred(self, localctx:MultExprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         




