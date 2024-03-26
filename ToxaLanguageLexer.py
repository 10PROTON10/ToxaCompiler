# Generated from ToxaLanguage.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,9,54,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,1,0,4,0,21,8,0,11,0,12,0,22,1,1,4,1,26,8,1,
        11,1,12,1,27,1,1,1,1,4,1,32,8,1,11,1,12,1,33,1,2,1,2,1,3,1,3,1,4,
        1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,4,8,49,8,8,11,8,12,8,50,1,8,1,8,
        0,0,9,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,1,0,2,1,0,48,57,3,
        0,9,10,13,13,32,32,57,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,
        0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,
        0,0,0,1,20,1,0,0,0,3,25,1,0,0,0,5,35,1,0,0,0,7,37,1,0,0,0,9,39,1,
        0,0,0,11,41,1,0,0,0,13,43,1,0,0,0,15,45,1,0,0,0,17,48,1,0,0,0,19,
        21,7,0,0,0,20,19,1,0,0,0,21,22,1,0,0,0,22,20,1,0,0,0,22,23,1,0,0,
        0,23,2,1,0,0,0,24,26,7,0,0,0,25,24,1,0,0,0,26,27,1,0,0,0,27,25,1,
        0,0,0,27,28,1,0,0,0,28,29,1,0,0,0,29,31,5,46,0,0,30,32,7,0,0,0,31,
        30,1,0,0,0,32,33,1,0,0,0,33,31,1,0,0,0,33,34,1,0,0,0,34,4,1,0,0,
        0,35,36,5,43,0,0,36,6,1,0,0,0,37,38,5,45,0,0,38,8,1,0,0,0,39,40,
        5,42,0,0,40,10,1,0,0,0,41,42,5,47,0,0,42,12,1,0,0,0,43,44,5,40,0,
        0,44,14,1,0,0,0,45,46,5,41,0,0,46,16,1,0,0,0,47,49,7,1,0,0,48,47,
        1,0,0,0,49,50,1,0,0,0,50,48,1,0,0,0,50,51,1,0,0,0,51,52,1,0,0,0,
        52,53,6,8,0,0,53,18,1,0,0,0,5,0,22,27,33,50,1,6,0,0
    ]

class ToxaLanguageLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INT = 1
    FLOAT = 2
    PLUS = 3
    MINUS = 4
    MULT = 5
    DIV = 6
    LPAREN = 7
    RPAREN = 8
    WS = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "FLOAT", "PLUS", "MINUS", "MULT", "DIV", "LPAREN", "RPAREN", 
            "WS" ]

    ruleNames = [ "INT", "FLOAT", "PLUS", "MINUS", "MULT", "DIV", "LPAREN", 
                  "RPAREN", "WS" ]

    grammarFileName = "ToxaLanguage.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


