# Generated from src/parser/ChronoParser.g4 by ANTLR 4.13.2
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
        4,1,81,637,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,1,0,1,0,1,0,1,0,1,0,1,0,1,0,5,0,102,8,0,10,0,12,0,105,9,0,1,
        0,1,0,1,0,1,0,1,0,3,0,112,8,0,1,0,5,0,115,8,0,10,0,12,0,118,9,0,
        1,0,1,0,3,0,122,8,0,1,0,1,0,1,0,1,0,1,0,1,0,3,0,130,8,0,1,0,5,0,
        133,8,0,10,0,12,0,136,9,0,3,0,138,8,0,1,1,1,1,1,1,5,1,143,8,1,10,
        1,12,1,146,9,1,1,1,1,1,1,1,3,1,151,8,1,1,2,1,2,1,2,5,2,156,8,2,10,
        2,12,2,159,9,2,1,3,1,3,1,3,1,3,3,3,165,8,3,1,3,1,3,3,3,169,8,3,1,
        3,1,3,1,4,1,4,3,4,175,8,4,1,5,4,5,178,8,5,11,5,12,5,179,1,5,1,5,
        1,6,1,6,1,6,1,6,1,6,1,6,3,6,190,8,6,1,7,1,7,1,8,3,8,195,8,8,1,8,
        1,8,1,8,3,8,200,8,8,1,8,1,8,3,8,204,8,8,3,8,206,8,8,1,8,1,8,3,8,
        210,8,8,1,8,1,8,1,8,1,8,3,8,216,8,8,1,9,1,9,1,9,1,9,3,9,222,8,9,
        1,9,1,9,3,9,226,8,9,1,9,1,9,5,9,230,8,9,10,9,12,9,233,9,9,1,9,1,
        9,1,10,1,10,1,10,1,10,5,10,241,8,10,10,10,12,10,244,9,10,1,10,1,
        10,1,11,3,11,249,8,11,1,11,1,11,3,11,253,8,11,1,11,1,11,3,11,257,
        8,11,1,11,1,11,1,11,3,11,262,8,11,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,3,12,271,8,12,1,12,1,12,5,12,275,8,12,10,12,12,12,278,9,12,
        1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,5,13,288,8,13,10,13,12,13,
        291,9,13,1,13,1,13,1,14,1,14,1,14,5,14,298,8,14,10,14,12,14,301,
        9,14,1,14,1,14,1,15,1,15,1,15,1,15,3,15,309,8,15,1,15,1,15,1,16,
        3,16,314,8,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,323,8,16,1,
        16,1,16,5,16,327,8,16,10,16,12,16,330,9,16,1,16,1,16,1,17,1,17,1,
        17,5,17,337,8,17,10,17,12,17,340,9,17,3,17,342,8,17,1,18,1,18,1,
        18,1,18,1,19,1,19,5,19,350,8,19,10,19,12,19,353,9,19,1,19,1,19,1,
        20,1,20,1,20,1,20,1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,23,1,23,1,
        23,1,23,1,23,1,23,1,23,1,23,1,23,5,23,377,8,23,10,23,12,23,380,9,
        23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,3,24,392,8,
        24,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,3,25,402,8,25,3,25,404,
        8,25,1,26,1,26,5,26,408,8,26,10,26,12,26,411,9,26,1,26,1,26,1,27,
        1,27,5,27,417,8,27,10,27,12,27,420,9,27,1,27,1,27,1,28,1,28,1,28,
        1,28,1,28,1,28,5,28,430,8,28,10,28,12,28,433,9,28,1,28,1,28,1,29,
        1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,3,29,449,
        8,29,1,30,1,30,5,30,453,8,30,10,30,12,30,456,9,30,1,30,1,30,1,31,
        1,31,1,31,1,31,1,32,1,32,1,32,3,32,467,8,32,1,32,1,32,3,32,471,8,
        32,1,32,1,32,3,32,475,8,32,1,32,1,32,1,32,5,32,480,8,32,10,32,12,
        32,483,9,32,1,32,1,32,1,33,1,33,3,33,489,8,33,1,34,1,34,3,34,493,
        8,34,1,35,1,35,1,35,1,35,1,35,1,35,1,35,3,35,502,8,35,1,35,1,35,
        1,36,1,36,1,36,1,36,1,36,5,36,511,8,36,10,36,12,36,514,9,36,1,36,
        1,36,1,37,1,37,1,37,1,37,3,37,522,8,37,1,37,1,37,3,37,526,8,37,1,
        38,1,38,1,38,1,38,1,39,1,39,1,39,5,39,535,8,39,10,39,12,39,538,9,
        39,1,40,1,40,1,40,1,40,1,40,1,40,1,40,3,40,547,8,40,1,41,1,41,3,
        41,551,8,41,1,41,1,41,1,41,1,41,1,41,1,41,3,41,559,8,41,1,41,1,41,
        3,41,563,8,41,1,41,3,41,566,8,41,1,41,1,41,1,41,1,41,1,41,1,41,1,
        41,1,41,3,41,576,8,41,1,41,3,41,579,8,41,5,41,581,8,41,10,41,12,
        41,584,9,41,1,42,1,42,1,42,1,42,3,42,590,8,42,1,42,1,42,1,42,1,42,
        1,42,1,42,1,42,1,42,3,42,600,8,42,1,42,1,42,1,42,1,42,1,42,1,42,
        1,42,1,42,1,42,1,42,3,42,612,8,42,1,43,1,43,3,43,616,8,43,1,43,1,
        43,1,44,1,44,1,44,3,44,623,8,44,1,44,1,44,1,45,1,45,1,45,5,45,630,
        8,45,10,45,12,45,633,9,45,1,46,1,46,1,46,0,0,47,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,
        58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,0,9,2,0,41,
        41,52,52,1,0,3,4,2,0,56,56,75,75,2,0,44,48,65,65,4,0,30,33,35,43,
        49,50,52,54,3,0,39,40,51,51,55,55,1,0,23,24,2,0,25,25,74,74,3,0,
        26,26,68,73,75,76,700,0,137,1,0,0,0,2,150,1,0,0,0,4,152,1,0,0,0,
        6,160,1,0,0,0,8,174,1,0,0,0,10,177,1,0,0,0,12,189,1,0,0,0,14,191,
        1,0,0,0,16,215,1,0,0,0,18,217,1,0,0,0,20,236,1,0,0,0,22,261,1,0,
        0,0,24,263,1,0,0,0,26,281,1,0,0,0,28,294,1,0,0,0,30,304,1,0,0,0,
        32,313,1,0,0,0,34,341,1,0,0,0,36,343,1,0,0,0,38,347,1,0,0,0,40,356,
        1,0,0,0,42,360,1,0,0,0,44,362,1,0,0,0,46,367,1,0,0,0,48,391,1,0,
        0,0,50,393,1,0,0,0,52,405,1,0,0,0,54,414,1,0,0,0,56,423,1,0,0,0,
        58,448,1,0,0,0,60,450,1,0,0,0,62,459,1,0,0,0,64,463,1,0,0,0,66,488,
        1,0,0,0,68,492,1,0,0,0,70,494,1,0,0,0,72,505,1,0,0,0,74,517,1,0,
        0,0,76,527,1,0,0,0,78,531,1,0,0,0,80,546,1,0,0,0,82,550,1,0,0,0,
        84,611,1,0,0,0,86,613,1,0,0,0,88,619,1,0,0,0,90,626,1,0,0,0,92,634,
        1,0,0,0,94,95,5,62,0,0,95,96,3,0,0,0,96,97,5,57,0,0,97,98,3,78,39,
        0,98,99,5,63,0,0,99,103,1,0,0,0,100,102,7,0,0,0,101,100,1,0,0,0,
        102,105,1,0,0,0,103,101,1,0,0,0,103,104,1,0,0,0,104,138,1,0,0,0,
        105,103,1,0,0,0,106,111,3,2,1,0,107,108,5,62,0,0,108,109,3,4,2,0,
        109,110,5,63,0,0,110,112,1,0,0,0,111,107,1,0,0,0,111,112,1,0,0,0,
        112,116,1,0,0,0,113,115,7,0,0,0,114,113,1,0,0,0,115,118,1,0,0,0,
        116,114,1,0,0,0,116,117,1,0,0,0,117,138,1,0,0,0,118,116,1,0,0,0,
        119,129,5,58,0,0,120,122,3,4,2,0,121,120,1,0,0,0,121,122,1,0,0,0,
        122,123,1,0,0,0,123,124,5,59,0,0,124,125,5,34,0,0,125,130,3,0,0,
        0,126,127,3,0,0,0,127,128,5,59,0,0,128,130,1,0,0,0,129,121,1,0,0,
        0,129,126,1,0,0,0,130,134,1,0,0,0,131,133,7,0,0,0,132,131,1,0,0,
        0,133,136,1,0,0,0,134,132,1,0,0,0,134,135,1,0,0,0,135,138,1,0,0,
        0,136,134,1,0,0,0,137,94,1,0,0,0,137,106,1,0,0,0,137,119,1,0,0,0,
        138,1,1,0,0,0,139,144,5,74,0,0,140,141,5,66,0,0,141,143,5,74,0,0,
        142,140,1,0,0,0,143,146,1,0,0,0,144,142,1,0,0,0,144,145,1,0,0,0,
        145,151,1,0,0,0,146,144,1,0,0,0,147,151,5,20,0,0,148,151,5,21,0,
        0,149,151,5,22,0,0,150,139,1,0,0,0,150,147,1,0,0,0,150,148,1,0,0,
        0,150,149,1,0,0,0,151,3,1,0,0,0,152,157,3,8,4,0,153,154,5,67,0,0,
        154,156,3,8,4,0,155,153,1,0,0,0,156,159,1,0,0,0,157,155,1,0,0,0,
        157,158,1,0,0,0,158,5,1,0,0,0,159,157,1,0,0,0,160,161,7,1,0,0,161,
        164,5,74,0,0,162,163,5,64,0,0,163,165,3,0,0,0,164,162,1,0,0,0,164,
        165,1,0,0,0,165,168,1,0,0,0,166,167,5,65,0,0,167,169,3,78,39,0,168,
        166,1,0,0,0,168,169,1,0,0,0,169,170,1,0,0,0,170,171,5,57,0,0,171,
        7,1,0,0,0,172,175,3,0,0,0,173,175,3,92,46,0,174,172,1,0,0,0,174,
        173,1,0,0,0,175,9,1,0,0,0,176,178,3,12,6,0,177,176,1,0,0,0,178,179,
        1,0,0,0,179,177,1,0,0,0,179,180,1,0,0,0,180,181,1,0,0,0,181,182,
        5,0,0,1,182,11,1,0,0,0,183,190,3,30,15,0,184,190,3,38,19,0,185,190,
        3,18,9,0,186,190,3,20,10,0,187,190,3,32,16,0,188,190,3,72,36,0,189,
        183,1,0,0,0,189,184,1,0,0,0,189,185,1,0,0,0,189,186,1,0,0,0,189,
        187,1,0,0,0,189,188,1,0,0,0,190,13,1,0,0,0,191,192,5,16,0,0,192,
        15,1,0,0,0,193,195,3,14,7,0,194,193,1,0,0,0,194,195,1,0,0,0,195,
        196,1,0,0,0,196,216,3,6,3,0,197,199,5,11,0,0,198,200,3,14,7,0,199,
        198,1,0,0,0,199,200,1,0,0,0,200,206,1,0,0,0,201,203,3,14,7,0,202,
        204,5,11,0,0,203,202,1,0,0,0,203,204,1,0,0,0,204,206,1,0,0,0,205,
        197,1,0,0,0,205,201,1,0,0,0,206,207,1,0,0,0,207,216,3,24,12,0,208,
        210,3,14,7,0,209,208,1,0,0,0,209,210,1,0,0,0,210,211,1,0,0,0,211,
        216,3,26,13,0,212,216,3,24,12,0,213,216,3,28,14,0,214,216,3,38,19,
        0,215,194,1,0,0,0,215,205,1,0,0,0,215,209,1,0,0,0,215,212,1,0,0,
        0,215,213,1,0,0,0,215,214,1,0,0,0,216,17,1,0,0,0,217,218,5,6,0,0,
        218,221,5,74,0,0,219,220,5,64,0,0,220,222,5,74,0,0,221,219,1,0,0,
        0,221,222,1,0,0,0,222,225,1,0,0,0,223,224,5,18,0,0,224,226,3,4,2,
        0,225,223,1,0,0,0,225,226,1,0,0,0,226,227,1,0,0,0,227,231,5,60,0,
        0,228,230,3,16,8,0,229,228,1,0,0,0,230,233,1,0,0,0,231,229,1,0,0,
        0,231,232,1,0,0,0,232,234,1,0,0,0,233,231,1,0,0,0,234,235,5,61,0,
        0,235,19,1,0,0,0,236,237,5,7,0,0,237,238,5,74,0,0,238,242,5,60,0,
        0,239,241,3,22,11,0,240,239,1,0,0,0,241,244,1,0,0,0,242,240,1,0,
        0,0,242,243,1,0,0,0,243,245,1,0,0,0,244,242,1,0,0,0,245,246,5,61,
        0,0,246,21,1,0,0,0,247,249,3,14,7,0,248,247,1,0,0,0,248,249,1,0,
        0,0,249,250,1,0,0,0,250,262,3,6,3,0,251,253,3,14,7,0,252,251,1,0,
        0,0,252,253,1,0,0,0,253,254,1,0,0,0,254,262,3,24,12,0,255,257,3,
        14,7,0,256,255,1,0,0,0,256,257,1,0,0,0,257,258,1,0,0,0,258,262,3,
        26,13,0,259,262,3,28,14,0,260,262,3,38,19,0,261,248,1,0,0,0,261,
        252,1,0,0,0,261,256,1,0,0,0,261,259,1,0,0,0,261,260,1,0,0,0,262,
        23,1,0,0,0,263,264,5,2,0,0,264,265,5,74,0,0,265,266,5,58,0,0,266,
        267,3,34,17,0,267,270,5,59,0,0,268,269,5,34,0,0,269,271,3,0,0,0,
        270,268,1,0,0,0,270,271,1,0,0,0,271,272,1,0,0,0,272,276,5,60,0,0,
        273,275,3,58,29,0,274,273,1,0,0,0,275,278,1,0,0,0,276,274,1,0,0,
        0,276,277,1,0,0,0,277,279,1,0,0,0,278,276,1,0,0,0,279,280,5,61,0,
        0,280,25,1,0,0,0,281,282,5,8,0,0,282,283,5,58,0,0,283,284,3,34,17,
        0,284,285,5,59,0,0,285,289,5,60,0,0,286,288,3,58,29,0,287,286,1,
        0,0,0,288,291,1,0,0,0,289,287,1,0,0,0,289,290,1,0,0,0,290,292,1,
        0,0,0,291,289,1,0,0,0,292,293,5,61,0,0,293,27,1,0,0,0,294,295,5,
        9,0,0,295,299,5,60,0,0,296,298,3,58,29,0,297,296,1,0,0,0,298,301,
        1,0,0,0,299,297,1,0,0,0,299,300,1,0,0,0,300,302,1,0,0,0,301,299,
        1,0,0,0,302,303,5,61,0,0,303,29,1,0,0,0,304,305,5,1,0,0,305,308,
        7,2,0,0,306,307,5,19,0,0,307,309,5,74,0,0,308,306,1,0,0,0,308,309,
        1,0,0,0,309,310,1,0,0,0,310,311,5,57,0,0,311,31,1,0,0,0,312,314,
        5,11,0,0,313,312,1,0,0,0,313,314,1,0,0,0,314,315,1,0,0,0,315,316,
        5,2,0,0,316,317,5,74,0,0,317,318,5,58,0,0,318,319,3,34,17,0,319,
        322,5,59,0,0,320,321,5,34,0,0,321,323,3,0,0,0,322,320,1,0,0,0,322,
        323,1,0,0,0,323,324,1,0,0,0,324,328,5,60,0,0,325,327,3,58,29,0,326,
        325,1,0,0,0,327,330,1,0,0,0,328,326,1,0,0,0,328,329,1,0,0,0,329,
        331,1,0,0,0,330,328,1,0,0,0,331,332,5,61,0,0,332,33,1,0,0,0,333,
        338,3,36,18,0,334,335,5,67,0,0,335,337,3,36,18,0,336,334,1,0,0,0,
        337,340,1,0,0,0,338,336,1,0,0,0,338,339,1,0,0,0,339,342,1,0,0,0,
        340,338,1,0,0,0,341,333,1,0,0,0,341,342,1,0,0,0,342,35,1,0,0,0,343,
        344,5,74,0,0,344,345,5,64,0,0,345,346,3,0,0,0,346,37,1,0,0,0,347,
        351,5,29,0,0,348,350,5,81,0,0,349,348,1,0,0,0,350,353,1,0,0,0,351,
        349,1,0,0,0,351,352,1,0,0,0,352,354,1,0,0,0,353,351,1,0,0,0,354,
        355,5,80,0,0,355,39,1,0,0,0,356,357,5,5,0,0,357,358,3,78,39,0,358,
        359,5,57,0,0,359,41,1,0,0,0,360,361,7,3,0,0,361,43,1,0,0,0,362,363,
        3,46,23,0,363,364,3,42,21,0,364,365,3,78,39,0,365,366,5,57,0,0,366,
        45,1,0,0,0,367,378,3,48,24,0,368,369,5,66,0,0,369,377,5,74,0,0,370,
        371,5,62,0,0,371,372,3,78,39,0,372,373,5,63,0,0,373,377,1,0,0,0,
        374,375,5,34,0,0,375,377,5,74,0,0,376,368,1,0,0,0,376,370,1,0,0,
        0,376,374,1,0,0,0,377,380,1,0,0,0,378,376,1,0,0,0,378,379,1,0,0,
        0,379,47,1,0,0,0,380,378,1,0,0,0,381,392,5,74,0,0,382,392,5,10,0,
        0,383,384,5,41,0,0,384,392,3,48,24,0,385,386,5,52,0,0,386,392,3,
        48,24,0,387,388,5,58,0,0,388,389,3,46,23,0,389,390,5,59,0,0,390,
        392,1,0,0,0,391,381,1,0,0,0,391,382,1,0,0,0,391,383,1,0,0,0,391,
        385,1,0,0,0,391,387,1,0,0,0,392,49,1,0,0,0,393,394,5,12,0,0,394,
        395,5,58,0,0,395,396,3,78,39,0,396,397,5,59,0,0,397,403,3,52,26,
        0,398,401,5,13,0,0,399,402,3,50,25,0,400,402,3,54,27,0,401,399,1,
        0,0,0,401,400,1,0,0,0,402,404,1,0,0,0,403,398,1,0,0,0,403,404,1,
        0,0,0,404,51,1,0,0,0,405,409,5,60,0,0,406,408,3,58,29,0,407,406,
        1,0,0,0,408,411,1,0,0,0,409,407,1,0,0,0,409,410,1,0,0,0,410,412,
        1,0,0,0,411,409,1,0,0,0,412,413,5,61,0,0,413,53,1,0,0,0,414,418,
        5,60,0,0,415,417,3,58,29,0,416,415,1,0,0,0,417,420,1,0,0,0,418,416,
        1,0,0,0,418,419,1,0,0,0,419,421,1,0,0,0,420,418,1,0,0,0,421,422,
        5,61,0,0,422,55,1,0,0,0,423,424,5,14,0,0,424,425,5,58,0,0,425,426,
        3,78,39,0,426,427,5,59,0,0,427,431,5,60,0,0,428,430,3,58,29,0,429,
        428,1,0,0,0,430,433,1,0,0,0,431,429,1,0,0,0,431,432,1,0,0,0,432,
        434,1,0,0,0,433,431,1,0,0,0,434,435,5,61,0,0,435,57,1,0,0,0,436,
        449,3,6,3,0,437,449,3,44,22,0,438,449,3,40,20,0,439,440,3,78,39,
        0,440,441,5,57,0,0,441,449,1,0,0,0,442,449,3,38,19,0,443,449,3,50,
        25,0,444,449,3,56,28,0,445,449,3,62,31,0,446,449,3,64,32,0,447,449,
        3,60,30,0,448,436,1,0,0,0,448,437,1,0,0,0,448,438,1,0,0,0,448,439,
        1,0,0,0,448,442,1,0,0,0,448,443,1,0,0,0,448,444,1,0,0,0,448,445,
        1,0,0,0,448,446,1,0,0,0,448,447,1,0,0,0,449,59,1,0,0,0,450,454,5,
        60,0,0,451,453,3,58,29,0,452,451,1,0,0,0,453,456,1,0,0,0,454,452,
        1,0,0,0,454,455,1,0,0,0,455,457,1,0,0,0,456,454,1,0,0,0,457,458,
        5,61,0,0,458,61,1,0,0,0,459,460,5,28,0,0,460,461,3,78,39,0,461,462,
        5,57,0,0,462,63,1,0,0,0,463,464,5,15,0,0,464,466,5,58,0,0,465,467,
        3,66,33,0,466,465,1,0,0,0,466,467,1,0,0,0,467,468,1,0,0,0,468,470,
        5,57,0,0,469,471,3,78,39,0,470,469,1,0,0,0,470,471,1,0,0,0,471,472,
        1,0,0,0,472,474,5,57,0,0,473,475,3,68,34,0,474,473,1,0,0,0,474,475,
        1,0,0,0,475,476,1,0,0,0,476,477,5,59,0,0,477,481,5,60,0,0,478,480,
        3,58,29,0,479,478,1,0,0,0,480,483,1,0,0,0,481,479,1,0,0,0,481,482,
        1,0,0,0,482,484,1,0,0,0,483,481,1,0,0,0,484,485,5,61,0,0,485,65,
        1,0,0,0,486,489,3,74,37,0,487,489,3,76,38,0,488,486,1,0,0,0,488,
        487,1,0,0,0,489,67,1,0,0,0,490,493,3,76,38,0,491,493,3,78,39,0,492,
        490,1,0,0,0,492,491,1,0,0,0,493,69,1,0,0,0,494,495,5,2,0,0,495,496,
        5,74,0,0,496,497,5,58,0,0,497,498,3,34,17,0,498,501,5,59,0,0,499,
        500,5,34,0,0,500,502,3,0,0,0,501,499,1,0,0,0,501,502,1,0,0,0,502,
        503,1,0,0,0,503,504,5,57,0,0,504,71,1,0,0,0,505,506,5,17,0,0,506,
        507,5,74,0,0,507,512,5,60,0,0,508,511,3,70,35,0,509,511,3,38,19,
        0,510,508,1,0,0,0,510,509,1,0,0,0,511,514,1,0,0,0,512,510,1,0,0,
        0,512,513,1,0,0,0,513,515,1,0,0,0,514,512,1,0,0,0,515,516,5,61,0,
        0,516,73,1,0,0,0,517,518,7,1,0,0,518,521,5,74,0,0,519,520,5,64,0,
        0,520,522,3,0,0,0,521,519,1,0,0,0,521,522,1,0,0,0,522,525,1,0,0,
        0,523,524,5,65,0,0,524,526,3,78,39,0,525,523,1,0,0,0,525,526,1,0,
        0,0,526,75,1,0,0,0,527,528,3,46,23,0,528,529,3,42,21,0,529,530,3,
        78,39,0,530,77,1,0,0,0,531,536,3,80,40,0,532,533,7,4,0,0,533,535,
        3,80,40,0,534,532,1,0,0,0,535,538,1,0,0,0,536,534,1,0,0,0,536,537,
        1,0,0,0,537,79,1,0,0,0,538,536,1,0,0,0,539,540,7,5,0,0,540,547,3,
        80,40,0,541,542,5,52,0,0,542,547,3,80,40,0,543,544,5,41,0,0,544,
        547,3,80,40,0,545,547,3,82,41,0,546,539,1,0,0,0,546,541,1,0,0,0,
        546,543,1,0,0,0,546,545,1,0,0,0,547,81,1,0,0,0,548,551,3,84,42,0,
        549,551,3,88,44,0,550,548,1,0,0,0,550,549,1,0,0,0,551,582,1,0,0,
        0,552,553,5,66,0,0,553,558,5,74,0,0,554,555,5,62,0,0,555,556,3,4,
        2,0,556,557,5,63,0,0,557,559,1,0,0,0,558,554,1,0,0,0,558,559,1,0,
        0,0,559,565,1,0,0,0,560,562,5,58,0,0,561,563,3,90,45,0,562,561,1,
        0,0,0,562,563,1,0,0,0,563,564,1,0,0,0,564,566,5,59,0,0,565,560,1,
        0,0,0,565,566,1,0,0,0,566,581,1,0,0,0,567,568,5,62,0,0,568,569,3,
        78,39,0,569,570,5,63,0,0,570,581,1,0,0,0,571,572,5,34,0,0,572,578,
        5,74,0,0,573,575,5,58,0,0,574,576,3,90,45,0,575,574,1,0,0,0,575,
        576,1,0,0,0,576,577,1,0,0,0,577,579,5,59,0,0,578,573,1,0,0,0,578,
        579,1,0,0,0,579,581,1,0,0,0,580,552,1,0,0,0,580,567,1,0,0,0,580,
        571,1,0,0,0,581,584,1,0,0,0,582,580,1,0,0,0,582,583,1,0,0,0,583,
        83,1,0,0,0,584,582,1,0,0,0,585,586,5,27,0,0,586,587,3,2,1,0,587,
        589,5,58,0,0,588,590,3,90,45,0,589,588,1,0,0,0,589,590,1,0,0,0,590,
        591,1,0,0,0,591,592,5,59,0,0,592,612,1,0,0,0,593,594,7,6,0,0,594,
        595,5,62,0,0,595,596,3,0,0,0,596,597,5,63,0,0,597,599,5,58,0,0,598,
        600,3,90,45,0,599,598,1,0,0,0,599,600,1,0,0,0,600,601,1,0,0,0,601,
        602,5,59,0,0,602,612,1,0,0,0,603,612,3,92,46,0,604,612,3,86,43,0,
        605,612,5,74,0,0,606,612,5,10,0,0,607,608,5,58,0,0,608,609,3,78,
        39,0,609,610,5,59,0,0,610,612,1,0,0,0,611,585,1,0,0,0,611,593,1,
        0,0,0,611,603,1,0,0,0,611,604,1,0,0,0,611,605,1,0,0,0,611,606,1,
        0,0,0,611,607,1,0,0,0,612,85,1,0,0,0,613,615,5,60,0,0,614,616,3,
        90,45,0,615,614,1,0,0,0,615,616,1,0,0,0,616,617,1,0,0,0,617,618,
        5,61,0,0,618,87,1,0,0,0,619,620,7,7,0,0,620,622,5,58,0,0,621,623,
        3,90,45,0,622,621,1,0,0,0,622,623,1,0,0,0,623,624,1,0,0,0,624,625,
        5,59,0,0,625,89,1,0,0,0,626,631,3,78,39,0,627,628,5,67,0,0,628,630,
        3,78,39,0,629,627,1,0,0,0,630,633,1,0,0,0,631,629,1,0,0,0,631,632,
        1,0,0,0,632,91,1,0,0,0,633,631,1,0,0,0,634,635,7,8,0,0,635,93,1,
        0,0,0,77,103,111,116,121,129,134,137,144,150,157,164,168,174,179,
        189,194,199,203,205,209,215,221,225,231,242,248,252,256,261,270,
        276,289,299,308,313,322,328,338,341,351,376,378,391,401,403,409,
        418,431,448,454,466,470,474,481,488,492,501,510,512,521,525,536,
        546,550,558,562,565,575,578,580,582,589,599,611,615,622,631
    ]

class ChronoParser ( Parser ):

    grammarFileName = "ChronoParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'import'", "'func'", "'var'", "'const'", 
                     "'return'", "'class'", "'struct'", "'init'", "'deinit'", 
                     "'this'", "'static'", "'if'", "'else'", "'while'", 
                     "'for'", "'public'", "'interface'", "'impl'", "'as'", 
                     "'unique'", "'shared'", "'weak'", "'@make'", "'@make_shared'", 
                     "'@move'", "<INVALID>", "'new'", "'delete'", "'@cpp'", 
                     "'=='", "'!='", "'<='", "'>='", "'->'", "'&&'", "'||'", 
                     "'<<'", "'>>'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'+='", "'-='", "'*='", "'/='", "'%='", "'<'", "'>'", 
                     "'!'", "'&'", "'|'", "'^'", "'~'", "<INVALID>", "';'", 
                     "'('", "')'", "'{'", "'}'", "'['", "']'", "':'", "'='", 
                     "'.'", "','", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'@end'" ]

    symbolicNames = [ "<INVALID>", "IMPORT", "FUNC", "VAR", "CONST", "RETURN", 
                      "CLASS", "STRUCT", "INIT", "DEINIT", "THIS", "STATIC", 
                      "IF", "ELSE", "WHILE", "FOR", "PUBLIC", "INTERFACE", 
                      "IMPL", "AS", "UNIQUE_KW", "SHARED_KW", "WEAK_KW", 
                      "AT_MAKE_UNIQUE", "AT_MAKE_SHARED", "AT_MOVE", "BOOL_LITERAL", 
                      "NEW", "DELETE", "AT_CPP", "EQ", "NEQ", "LTE", "GTE", 
                      "ARROW", "AND_OP", "OR_OP", "LSHIFT", "RSHIFT", "PLUS", 
                      "MINUS", "STAR", "SLASH", "MODULO", "PLUS_ASSIGN", 
                      "MINUS_ASSIGN", "STAR_ASSIGN", "SLASH_ASSIGN", "MOD_ASSIGN", 
                      "LT", "GT", "NOT_OP", "BIT_AND", "BIT_OR", "BIT_XOR", 
                      "BIT_NOT", "INCLUDE_PATH", "SEMIC_TOKEN", "LPAREN", 
                      "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", 
                      "COLON", "ASSIGN", "DOT", "COMMA", "HEX_LITERAL", 
                      "BINARY_LITERAL", "OCTAL_LITERAL", "FLOAT_LITERAL", 
                      "DECIMAL_LITERAL", "BYTE_LITERAL", "IDENTIFIER", "STRING_LITERAL", 
                      "CHAR_LITERAL", "LINE_COMMENT", "WHITESPACE", "NEWLINE", 
                      "AT_END", "CPP_BODY" ]

    RULE_typeSpecifier = 0
    RULE_baseType = 1
    RULE_typeList = 2
    RULE_variableDeclaration = 3
    RULE_templateArgument = 4
    RULE_program = 5
    RULE_topLevelStatement = 6
    RULE_accessModifier = 7
    RULE_classBodyStatement = 8
    RULE_classDefinition = 9
    RULE_structDefinition = 10
    RULE_structBodyStatement = 11
    RULE_methodDefinition = 12
    RULE_initDefinition = 13
    RULE_deinitBlock = 14
    RULE_importDirective = 15
    RULE_functionDefinition = 16
    RULE_parameters = 17
    RULE_parameter = 18
    RULE_cppBlock = 19
    RULE_returnStatement = 20
    RULE_assignmentOperator = 21
    RULE_assignment = 22
    RULE_assignableExpression = 23
    RULE_assignablePrimary = 24
    RULE_ifStatement = 25
    RULE_ifBlock = 26
    RULE_elseBlock = 27
    RULE_whileStatement = 28
    RULE_statement = 29
    RULE_blockStatement = 30
    RULE_deleteStatement = 31
    RULE_forStatement = 32
    RULE_forInit = 33
    RULE_forIncrement = 34
    RULE_methodSignature = 35
    RULE_interfaceDefinition = 36
    RULE_variableDeclaration_no_semicolon = 37
    RULE_assignment_no_semicolon = 38
    RULE_expression = 39
    RULE_unaryExpression = 40
    RULE_simpleExpression = 41
    RULE_primary = 42
    RULE_initializerList = 43
    RULE_functionCallExpression = 44
    RULE_expressionList = 45
    RULE_literal = 46

    ruleNames =  [ "typeSpecifier", "baseType", "typeList", "variableDeclaration", 
                   "templateArgument", "program", "topLevelStatement", "accessModifier", 
                   "classBodyStatement", "classDefinition", "structDefinition", 
                   "structBodyStatement", "methodDefinition", "initDefinition", 
                   "deinitBlock", "importDirective", "functionDefinition", 
                   "parameters", "parameter", "cppBlock", "returnStatement", 
                   "assignmentOperator", "assignment", "assignableExpression", 
                   "assignablePrimary", "ifStatement", "ifBlock", "elseBlock", 
                   "whileStatement", "statement", "blockStatement", "deleteStatement", 
                   "forStatement", "forInit", "forIncrement", "methodSignature", 
                   "interfaceDefinition", "variableDeclaration_no_semicolon", 
                   "assignment_no_semicolon", "expression", "unaryExpression", 
                   "simpleExpression", "primary", "initializerList", "functionCallExpression", 
                   "expressionList", "literal" ]

    EOF = Token.EOF
    IMPORT=1
    FUNC=2
    VAR=3
    CONST=4
    RETURN=5
    CLASS=6
    STRUCT=7
    INIT=8
    DEINIT=9
    THIS=10
    STATIC=11
    IF=12
    ELSE=13
    WHILE=14
    FOR=15
    PUBLIC=16
    INTERFACE=17
    IMPL=18
    AS=19
    UNIQUE_KW=20
    SHARED_KW=21
    WEAK_KW=22
    AT_MAKE_UNIQUE=23
    AT_MAKE_SHARED=24
    AT_MOVE=25
    BOOL_LITERAL=26
    NEW=27
    DELETE=28
    AT_CPP=29
    EQ=30
    NEQ=31
    LTE=32
    GTE=33
    ARROW=34
    AND_OP=35
    OR_OP=36
    LSHIFT=37
    RSHIFT=38
    PLUS=39
    MINUS=40
    STAR=41
    SLASH=42
    MODULO=43
    PLUS_ASSIGN=44
    MINUS_ASSIGN=45
    STAR_ASSIGN=46
    SLASH_ASSIGN=47
    MOD_ASSIGN=48
    LT=49
    GT=50
    NOT_OP=51
    BIT_AND=52
    BIT_OR=53
    BIT_XOR=54
    BIT_NOT=55
    INCLUDE_PATH=56
    SEMIC_TOKEN=57
    LPAREN=58
    RPAREN=59
    LBRACE=60
    RBRACE=61
    LBRACK=62
    RBRACK=63
    COLON=64
    ASSIGN=65
    DOT=66
    COMMA=67
    HEX_LITERAL=68
    BINARY_LITERAL=69
    OCTAL_LITERAL=70
    FLOAT_LITERAL=71
    DECIMAL_LITERAL=72
    BYTE_LITERAL=73
    IDENTIFIER=74
    STRING_LITERAL=75
    CHAR_LITERAL=76
    LINE_COMMENT=77
    WHITESPACE=78
    NEWLINE=79
    AT_END=80
    CPP_BODY=81

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class TypeSpecifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.params = None # TypeListContext
            self.returnType = None # TypeSpecifierContext
            self.nested = None # TypeSpecifierContext

        def LBRACK(self):
            return self.getToken(ChronoParser.LBRACK, 0)

        def typeSpecifier(self):
            return self.getTypedRuleContext(ChronoParser.TypeSpecifierContext,0)


        def SEMIC_TOKEN(self):
            return self.getToken(ChronoParser.SEMIC_TOKEN, 0)

        def expression(self):
            return self.getTypedRuleContext(ChronoParser.ExpressionContext,0)


        def RBRACK(self):
            return self.getToken(ChronoParser.RBRACK, 0)

        def STAR(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.STAR)
            else:
                return self.getToken(ChronoParser.STAR, i)

        def BIT_AND(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.BIT_AND)
            else:
                return self.getToken(ChronoParser.BIT_AND, i)

        def baseType(self):
            return self.getTypedRuleContext(ChronoParser.BaseTypeContext,0)


        def typeList(self):
            return self.getTypedRuleContext(ChronoParser.TypeListContext,0)


        def LPAREN(self):
            return self.getToken(ChronoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ChronoParser.RPAREN, 0)

        def ARROW(self):
            return self.getToken(ChronoParser.ARROW, 0)

        def getRuleIndex(self):
            return ChronoParser.RULE_typeSpecifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeSpecifier" ):
                listener.enterTypeSpecifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeSpecifier" ):
                listener.exitTypeSpecifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeSpecifier" ):
                return visitor.visitTypeSpecifier(self)
            else:
                return visitor.visitChildren(self)




    def typeSpecifier(self):

        localctx = ChronoParser.TypeSpecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_typeSpecifier)
        self._la = 0 # Token type
        try:
            self.state = 137
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [62]:
                self.enterOuterAlt(localctx, 1)
                self.state = 94
                self.match(ChronoParser.LBRACK)
                self.state = 95
                self.typeSpecifier()
                self.state = 96
                self.match(ChronoParser.SEMIC_TOKEN)
                self.state = 97
                self.expression()
                self.state = 98
                self.match(ChronoParser.RBRACK)
                self.state = 103
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 100
                        _la = self._input.LA(1)
                        if not(_la==41 or _la==52):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume() 
                    self.state = 105
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

                pass
            elif token in [20, 21, 22, 74]:
                self.enterOuterAlt(localctx, 2)
                self.state = 106
                self.baseType()
                self.state = 111
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==62:
                    self.state = 107
                    self.match(ChronoParser.LBRACK)
                    self.state = 108
                    self.typeList()
                    self.state = 109
                    self.match(ChronoParser.RBRACK)


                self.state = 116
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 113
                        _la = self._input.LA(1)
                        if not(_la==41 or _la==52):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume() 
                    self.state = 118
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                pass
            elif token in [58]:
                self.enterOuterAlt(localctx, 3)
                self.state = 119
                self.match(ChronoParser.LPAREN)
                self.state = 129
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 121
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if ((((_la - 20)) & ~0x3f) == 0 and ((1 << (_la - 20)) & 143838386023563335) != 0):
                        self.state = 120
                        localctx.params = self.typeList()


                    self.state = 123
                    self.match(ChronoParser.RPAREN)
                    self.state = 124
                    self.match(ChronoParser.ARROW)
                    self.state = 125
                    localctx.returnType = self.typeSpecifier()
                    pass

                elif la_ == 2:
                    self.state = 126
                    localctx.nested = self.typeSpecifier()
                    self.state = 127
                    self.match(ChronoParser.RPAREN)
                    pass


                self.state = 134
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 131
                        _la = self._input.LA(1)
                        if not(_la==41 or _la==52):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume() 
                    self.state = 136
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

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


    class BaseTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.IDENTIFIER)
            else:
                return self.getToken(ChronoParser.IDENTIFIER, i)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.DOT)
            else:
                return self.getToken(ChronoParser.DOT, i)

        def UNIQUE_KW(self):
            return self.getToken(ChronoParser.UNIQUE_KW, 0)

        def SHARED_KW(self):
            return self.getToken(ChronoParser.SHARED_KW, 0)

        def WEAK_KW(self):
            return self.getToken(ChronoParser.WEAK_KW, 0)

        def getRuleIndex(self):
            return ChronoParser.RULE_baseType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBaseType" ):
                listener.enterBaseType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBaseType" ):
                listener.exitBaseType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBaseType" ):
                return visitor.visitBaseType(self)
            else:
                return visitor.visitChildren(self)




    def baseType(self):

        localctx = ChronoParser.BaseTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_baseType)
        self._la = 0 # Token type
        try:
            self.state = 150
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [74]:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.match(ChronoParser.IDENTIFIER)
                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==66:
                    self.state = 140
                    self.match(ChronoParser.DOT)
                    self.state = 141
                    self.match(ChronoParser.IDENTIFIER)
                    self.state = 146
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 147
                self.match(ChronoParser.UNIQUE_KW)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 3)
                self.state = 148
                self.match(ChronoParser.SHARED_KW)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 4)
                self.state = 149
                self.match(ChronoParser.WEAK_KW)
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


    class TypeListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def templateArgument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChronoParser.TemplateArgumentContext)
            else:
                return self.getTypedRuleContext(ChronoParser.TemplateArgumentContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.COMMA)
            else:
                return self.getToken(ChronoParser.COMMA, i)

        def getRuleIndex(self):
            return ChronoParser.RULE_typeList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeList" ):
                listener.enterTypeList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeList" ):
                listener.exitTypeList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeList" ):
                return visitor.visitTypeList(self)
            else:
                return visitor.visitChildren(self)




    def typeList(self):

        localctx = ChronoParser.TypeListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_typeList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.templateArgument()
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==67:
                self.state = 153
                self.match(ChronoParser.COMMA)
                self.state = 154
                self.templateArgument()
                self.state = 159
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token
            self.typeName = None # TypeSpecifierContext

        def SEMIC_TOKEN(self):
            return self.getToken(ChronoParser.SEMIC_TOKEN, 0)

        def CONST(self):
            return self.getToken(ChronoParser.CONST, 0)

        def VAR(self):
            return self.getToken(ChronoParser.VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(ChronoParser.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(ChronoParser.COLON, 0)

        def ASSIGN(self):
            return self.getToken(ChronoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ChronoParser.ExpressionContext,0)


        def typeSpecifier(self):
            return self.getTypedRuleContext(ChronoParser.TypeSpecifierContext,0)


        def getRuleIndex(self):
            return ChronoParser.RULE_variableDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclaration" ):
                listener.enterVariableDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclaration" ):
                listener.exitVariableDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclaration" ):
                return visitor.visitVariableDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclaration(self):

        localctx = ChronoParser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variableDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            _la = self._input.LA(1)
            if not(_la==3 or _la==4):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 161
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==64:
                self.state = 162
                self.match(ChronoParser.COLON)
                self.state = 163
                localctx.typeName = self.typeSpecifier()


            self.state = 168
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==65:
                self.state = 166
                self.match(ChronoParser.ASSIGN)
                self.state = 167
                self.expression()


            self.state = 170
            self.match(ChronoParser.SEMIC_TOKEN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TemplateArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeSpecifier(self):
            return self.getTypedRuleContext(ChronoParser.TypeSpecifierContext,0)


        def literal(self):
            return self.getTypedRuleContext(ChronoParser.LiteralContext,0)


        def getRuleIndex(self):
            return ChronoParser.RULE_templateArgument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTemplateArgument" ):
                listener.enterTemplateArgument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTemplateArgument" ):
                listener.exitTemplateArgument(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTemplateArgument" ):
                return visitor.visitTemplateArgument(self)
            else:
                return visitor.visitChildren(self)




    def templateArgument(self):

        localctx = ChronoParser.TemplateArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_templateArgument)
        try:
            self.state = 174
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20, 21, 22, 58, 62, 74]:
                self.enterOuterAlt(localctx, 1)
                self.state = 172
                self.typeSpecifier()
                pass
            elif token in [26, 68, 69, 70, 71, 72, 73, 75, 76]:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
                self.literal()
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


    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ChronoParser.EOF, 0)

        def topLevelStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChronoParser.TopLevelStatementContext)
            else:
                return self.getTypedRuleContext(ChronoParser.TopLevelStatementContext,i)


        def getRuleIndex(self):
            return ChronoParser.RULE_program

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

        localctx = ChronoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 176
                self.topLevelStatement()
                self.state = 179 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 537004230) != 0)):
                    break

            self.state = 181
            self.match(ChronoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TopLevelStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def importDirective(self):
            return self.getTypedRuleContext(ChronoParser.ImportDirectiveContext,0)


        def cppBlock(self):
            return self.getTypedRuleContext(ChronoParser.CppBlockContext,0)


        def classDefinition(self):
            return self.getTypedRuleContext(ChronoParser.ClassDefinitionContext,0)


        def structDefinition(self):
            return self.getTypedRuleContext(ChronoParser.StructDefinitionContext,0)


        def functionDefinition(self):
            return self.getTypedRuleContext(ChronoParser.FunctionDefinitionContext,0)


        def interfaceDefinition(self):
            return self.getTypedRuleContext(ChronoParser.InterfaceDefinitionContext,0)


        def getRuleIndex(self):
            return ChronoParser.RULE_topLevelStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTopLevelStatement" ):
                listener.enterTopLevelStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTopLevelStatement" ):
                listener.exitTopLevelStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTopLevelStatement" ):
                return visitor.visitTopLevelStatement(self)
            else:
                return visitor.visitChildren(self)




    def topLevelStatement(self):

        localctx = ChronoParser.TopLevelStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_topLevelStatement)
        try:
            self.state = 189
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.importDirective()
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
                self.cppBlock()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 185
                self.classDefinition()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 4)
                self.state = 186
                self.structDefinition()
                pass
            elif token in [2, 11]:
                self.enterOuterAlt(localctx, 5)
                self.state = 187
                self.functionDefinition()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 6)
                self.state = 188
                self.interfaceDefinition()
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


    class AccessModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PUBLIC(self):
            return self.getToken(ChronoParser.PUBLIC, 0)

        def getRuleIndex(self):
            return ChronoParser.RULE_accessModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAccessModifier" ):
                listener.enterAccessModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAccessModifier" ):
                listener.exitAccessModifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAccessModifier" ):
                return visitor.visitAccessModifier(self)
            else:
                return visitor.visitChildren(self)




    def accessModifier(self):

        localctx = ChronoParser.AccessModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_accessModifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(ChronoParser.PUBLIC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassBodyStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self):
            return self.getTypedRuleContext(ChronoParser.VariableDeclarationContext,0)


        def accessModifier(self):
            return self.getTypedRuleContext(ChronoParser.AccessModifierContext,0)


        def methodDefinition(self):
            return self.getTypedRuleContext(ChronoParser.MethodDefinitionContext,0)


        def STATIC(self):
            return self.getToken(ChronoParser.STATIC, 0)

        def initDefinition(self):
            return self.getTypedRuleContext(ChronoParser.InitDefinitionContext,0)


        def deinitBlock(self):
            return self.getTypedRuleContext(ChronoParser.DeinitBlockContext,0)


        def cppBlock(self):
            return self.getTypedRuleContext(ChronoParser.CppBlockContext,0)


        def getRuleIndex(self):
            return ChronoParser.RULE_classBodyStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassBodyStatement" ):
                listener.enterClassBodyStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassBodyStatement" ):
                listener.exitClassBodyStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassBodyStatement" ):
                return visitor.visitClassBodyStatement(self)
            else:
                return visitor.visitChildren(self)




    def classBodyStatement(self):

        localctx = ChronoParser.ClassBodyStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_classBodyStatement)
        self._la = 0 # Token type
        try:
            self.state = 215
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 193
                    self.accessModifier()


                self.state = 196
                self.variableDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 205
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [11]:
                    self.state = 197
                    self.match(ChronoParser.STATIC)
                    self.state = 199
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==16:
                        self.state = 198
                        self.accessModifier()


                    pass
                elif token in [16]:
                    self.state = 201
                    self.accessModifier()
                    self.state = 203
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==11:
                        self.state = 202
                        self.match(ChronoParser.STATIC)


                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 207
                self.methodDefinition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 209
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 208
                    self.accessModifier()


                self.state = 211
                self.initDefinition()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 212
                self.methodDefinition()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 213
                self.deinitBlock()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 214
                self.cppBlock()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token
            self.base = None # Token
            self.interfaces = None # TypeListContext

        def CLASS(self):
            return self.getToken(ChronoParser.CLASS, 0)

        def LBRACE(self):
            return self.getToken(ChronoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(ChronoParser.RBRACE, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.IDENTIFIER)
            else:
                return self.getToken(ChronoParser.IDENTIFIER, i)

        def COLON(self):
            return self.getToken(ChronoParser.COLON, 0)

        def IMPL(self):
            return self.getToken(ChronoParser.IMPL, 0)

        def classBodyStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChronoParser.ClassBodyStatementContext)
            else:
                return self.getTypedRuleContext(ChronoParser.ClassBodyStatementContext,i)


        def typeList(self):
            return self.getTypedRuleContext(ChronoParser.TypeListContext,0)


        def getRuleIndex(self):
            return ChronoParser.RULE_classDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassDefinition" ):
                listener.enterClassDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassDefinition" ):
                listener.exitClassDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassDefinition" ):
                return visitor.visitClassDefinition(self)
            else:
                return visitor.visitChildren(self)




    def classDefinition(self):

        localctx = ChronoParser.ClassDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_classDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(ChronoParser.CLASS)
            self.state = 218
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==64:
                self.state = 219
                self.match(ChronoParser.COLON)
                self.state = 220
                localctx.base = self.match(ChronoParser.IDENTIFIER)


            self.state = 225
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 223
                self.match(ChronoParser.IMPL)
                self.state = 224
                localctx.interfaces = self.typeList()


            self.state = 227
            self.match(ChronoParser.LBRACE)
            self.state = 231
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 536939292) != 0):
                self.state = 228
                self.classBodyStatement()
                self.state = 233
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 234
            self.match(ChronoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token

        def STRUCT(self):
            return self.getToken(ChronoParser.STRUCT, 0)

        def LBRACE(self):
            return self.getToken(ChronoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(ChronoParser.RBRACE, 0)

        def IDENTIFIER(self):
            return self.getToken(ChronoParser.IDENTIFIER, 0)

        def structBodyStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChronoParser.StructBodyStatementContext)
            else:
                return self.getTypedRuleContext(ChronoParser.StructBodyStatementContext,i)


        def getRuleIndex(self):
            return ChronoParser.RULE_structDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStructDefinition" ):
                listener.enterStructDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStructDefinition" ):
                listener.exitStructDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructDefinition" ):
                return visitor.visitStructDefinition(self)
            else:
                return visitor.visitChildren(self)




    def structDefinition(self):

        localctx = ChronoParser.StructDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_structDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.match(ChronoParser.STRUCT)
            self.state = 237
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 238
            self.match(ChronoParser.LBRACE)
            self.state = 242
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 536937244) != 0):
                self.state = 239
                self.structBodyStatement()
                self.state = 244
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 245
            self.match(ChronoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructBodyStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self):
            return self.getTypedRuleContext(ChronoParser.VariableDeclarationContext,0)


        def accessModifier(self):
            return self.getTypedRuleContext(ChronoParser.AccessModifierContext,0)


        def methodDefinition(self):
            return self.getTypedRuleContext(ChronoParser.MethodDefinitionContext,0)


        def initDefinition(self):
            return self.getTypedRuleContext(ChronoParser.InitDefinitionContext,0)


        def deinitBlock(self):
            return self.getTypedRuleContext(ChronoParser.DeinitBlockContext,0)


        def cppBlock(self):
            return self.getTypedRuleContext(ChronoParser.CppBlockContext,0)


        def getRuleIndex(self):
            return ChronoParser.RULE_structBodyStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStructBodyStatement" ):
                listener.enterStructBodyStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStructBodyStatement" ):
                listener.exitStructBodyStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructBodyStatement" ):
                return visitor.visitStructBodyStatement(self)
            else:
                return visitor.visitChildren(self)




    def structBodyStatement(self):

        localctx = ChronoParser.StructBodyStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_structBodyStatement)
        self._la = 0 # Token type
        try:
            self.state = 261
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 247
                    self.accessModifier()


                self.state = 250
                self.variableDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 252
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 251
                    self.accessModifier()


                self.state = 254
                self.methodDefinition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 256
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 255
                    self.accessModifier()


                self.state = 258
                self.initDefinition()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 259
                self.deinitBlock()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 260
                self.cppBlock()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token
            self.returnType = None # TypeSpecifierContext

        def FUNC(self):
            return self.getToken(ChronoParser.FUNC, 0)

        def LPAREN(self):
            return self.getToken(ChronoParser.LPAREN, 0)

        def parameters(self):
            return self.getTypedRuleContext(ChronoParser.ParametersContext,0)


        def RPAREN(self):
            return self.getToken(ChronoParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(ChronoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(ChronoParser.RBRACE, 0)

        def IDENTIFIER(self):
            return self.getToken(ChronoParser.IDENTIFIER, 0)

        def ARROW(self):
            return self.getToken(ChronoParser.ARROW, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChronoParser.StatementContext)
            else:
                return self.getTypedRuleContext(ChronoParser.StatementContext,i)


        def typeSpecifier(self):
            return self.getTypedRuleContext(ChronoParser.TypeSpecifierContext,0)


        def getRuleIndex(self):
            return ChronoParser.RULE_methodDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodDefinition" ):
                listener.enterMethodDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodDefinition" ):
                listener.exitMethodDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDefinition" ):
                return visitor.visitMethodDefinition(self)
            else:
                return visitor.visitChildren(self)




    def methodDefinition(self):

        localctx = ChronoParser.MethodDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_methodDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.match(ChronoParser.FUNC)
            self.state = 264
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 265
            self.match(ChronoParser.LPAREN)
            self.state = 266
            self.parameters()
            self.state = 267
            self.match(ChronoParser.RPAREN)
            self.state = 270
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 268
                self.match(ChronoParser.ARROW)
                self.state = 269
                localctx.returnType = self.typeSpecifier()


            self.state = 272
            self.match(ChronoParser.LBRACE)
            self.state = 276
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1483939926574683192) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & 511) != 0):
                self.state = 273
                self.statement()
                self.state = 278
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 279
            self.match(ChronoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INIT(self):
            return self.getToken(ChronoParser.INIT, 0)

        def LPAREN(self):
            return self.getToken(ChronoParser.LPAREN, 0)

        def parameters(self):
            return self.getTypedRuleContext(ChronoParser.ParametersContext,0)


        def RPAREN(self):
            return self.getToken(ChronoParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(ChronoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(ChronoParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChronoParser.StatementContext)
            else:
                return self.getTypedRuleContext(ChronoParser.StatementContext,i)


        def getRuleIndex(self):
            return ChronoParser.RULE_initDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitDefinition" ):
                listener.enterInitDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitDefinition" ):
                listener.exitInitDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitDefinition" ):
                return visitor.visitInitDefinition(self)
            else:
                return visitor.visitChildren(self)




    def initDefinition(self):

        localctx = ChronoParser.InitDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_initDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(ChronoParser.INIT)
            self.state = 282
            self.match(ChronoParser.LPAREN)
            self.state = 283
            self.parameters()
            self.state = 284
            self.match(ChronoParser.RPAREN)
            self.state = 285
            self.match(ChronoParser.LBRACE)
            self.state = 289
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1483939926574683192) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & 511) != 0):
                self.state = 286
                self.statement()
                self.state = 291
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 292
            self.match(ChronoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeinitBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEINIT(self):
            return self.getToken(ChronoParser.DEINIT, 0)

        def LBRACE(self):
            return self.getToken(ChronoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(ChronoParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChronoParser.StatementContext)
            else:
                return self.getTypedRuleContext(ChronoParser.StatementContext,i)


        def getRuleIndex(self):
            return ChronoParser.RULE_deinitBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeinitBlock" ):
                listener.enterDeinitBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeinitBlock" ):
                listener.exitDeinitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeinitBlock" ):
                return visitor.visitDeinitBlock(self)
            else:
                return visitor.visitChildren(self)




    def deinitBlock(self):

        localctx = ChronoParser.DeinitBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_deinitBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.match(ChronoParser.DEINIT)
            self.state = 295
            self.match(ChronoParser.LBRACE)
            self.state = 299
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1483939926574683192) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & 511) != 0):
                self.state = 296
                self.statement()
                self.state = 301
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 302
            self.match(ChronoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImportDirectiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.path = None # Token
            self.alias = None # Token

        def IMPORT(self):
            return self.getToken(ChronoParser.IMPORT, 0)

        def SEMIC_TOKEN(self):
            return self.getToken(ChronoParser.SEMIC_TOKEN, 0)

        def STRING_LITERAL(self):
            return self.getToken(ChronoParser.STRING_LITERAL, 0)

        def INCLUDE_PATH(self):
            return self.getToken(ChronoParser.INCLUDE_PATH, 0)

        def AS(self):
            return self.getToken(ChronoParser.AS, 0)

        def IDENTIFIER(self):
            return self.getToken(ChronoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return ChronoParser.RULE_importDirective

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImportDirective" ):
                listener.enterImportDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImportDirective" ):
                listener.exitImportDirective(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImportDirective" ):
                return visitor.visitImportDirective(self)
            else:
                return visitor.visitChildren(self)




    def importDirective(self):

        localctx = ChronoParser.ImportDirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_importDirective)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.match(ChronoParser.IMPORT)
            self.state = 305
            localctx.path = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==56 or _la==75):
                localctx.path = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 308
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 306
                self.match(ChronoParser.AS)
                self.state = 307
                localctx.alias = self.match(ChronoParser.IDENTIFIER)


            self.state = 310
            self.match(ChronoParser.SEMIC_TOKEN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token
            self.returnType = None # TypeSpecifierContext

        def FUNC(self):
            return self.getToken(ChronoParser.FUNC, 0)

        def LPAREN(self):
            return self.getToken(ChronoParser.LPAREN, 0)

        def parameters(self):
            return self.getTypedRuleContext(ChronoParser.ParametersContext,0)


        def RPAREN(self):
            return self.getToken(ChronoParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(ChronoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(ChronoParser.RBRACE, 0)

        def IDENTIFIER(self):
            return self.getToken(ChronoParser.IDENTIFIER, 0)

        def STATIC(self):
            return self.getToken(ChronoParser.STATIC, 0)

        def ARROW(self):
            return self.getToken(ChronoParser.ARROW, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChronoParser.StatementContext)
            else:
                return self.getTypedRuleContext(ChronoParser.StatementContext,i)


        def typeSpecifier(self):
            return self.getTypedRuleContext(ChronoParser.TypeSpecifierContext,0)


        def getRuleIndex(self):
            return ChronoParser.RULE_functionDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDefinition" ):
                listener.enterFunctionDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDefinition" ):
                listener.exitFunctionDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDefinition" ):
                return visitor.visitFunctionDefinition(self)
            else:
                return visitor.visitChildren(self)




    def functionDefinition(self):

        localctx = ChronoParser.FunctionDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_functionDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 312
                self.match(ChronoParser.STATIC)


            self.state = 315
            self.match(ChronoParser.FUNC)
            self.state = 316
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 317
            self.match(ChronoParser.LPAREN)
            self.state = 318
            self.parameters()
            self.state = 319
            self.match(ChronoParser.RPAREN)
            self.state = 322
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 320
                self.match(ChronoParser.ARROW)
                self.state = 321
                localctx.returnType = self.typeSpecifier()


            self.state = 324
            self.match(ChronoParser.LBRACE)
            self.state = 328
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1483939926574683192) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & 511) != 0):
                self.state = 325
                self.statement()
                self.state = 330
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 331
            self.match(ChronoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChronoParser.ParameterContext)
            else:
                return self.getTypedRuleContext(ChronoParser.ParameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.COMMA)
            else:
                return self.getToken(ChronoParser.COMMA, i)

        def getRuleIndex(self):
            return ChronoParser.RULE_parameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameters" ):
                listener.enterParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameters" ):
                listener.exitParameters(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameters" ):
                return visitor.visitParameters(self)
            else:
                return visitor.visitChildren(self)




    def parameters(self):

        localctx = ChronoParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==74:
                self.state = 333
                self.parameter()
                self.state = 338
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==67:
                    self.state = 334
                    self.match(ChronoParser.COMMA)
                    self.state = 335
                    self.parameter()
                    self.state = 340
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token
            self.typeName = None # TypeSpecifierContext

        def COLON(self):
            return self.getToken(ChronoParser.COLON, 0)

        def IDENTIFIER(self):
            return self.getToken(ChronoParser.IDENTIFIER, 0)

        def typeSpecifier(self):
            return self.getTypedRuleContext(ChronoParser.TypeSpecifierContext,0)


        def getRuleIndex(self):
            return ChronoParser.RULE_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter" ):
                listener.enterParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter" ):
                listener.exitParameter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = ChronoParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 344
            self.match(ChronoParser.COLON)
            self.state = 345
            localctx.typeName = self.typeSpecifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CppBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AT_CPP(self):
            return self.getToken(ChronoParser.AT_CPP, 0)

        def AT_END(self):
            return self.getToken(ChronoParser.AT_END, 0)

        def CPP_BODY(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.CPP_BODY)
            else:
                return self.getToken(ChronoParser.CPP_BODY, i)

        def getRuleIndex(self):
            return ChronoParser.RULE_cppBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCppBlock" ):
                listener.enterCppBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCppBlock" ):
                listener.exitCppBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCppBlock" ):
                return visitor.visitCppBlock(self)
            else:
                return visitor.visitChildren(self)




    def cppBlock(self):

        localctx = ChronoParser.CppBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_cppBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.match(ChronoParser.AT_CPP)
            self.state = 351
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==81:
                self.state = 348
                self.match(ChronoParser.CPP_BODY)
                self.state = 353
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 354
            self.match(ChronoParser.AT_END)
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

        def RETURN(self):
            return self.getToken(ChronoParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(ChronoParser.ExpressionContext,0)


        def SEMIC_TOKEN(self):
            return self.getToken(ChronoParser.SEMIC_TOKEN, 0)

        def getRuleIndex(self):
            return ChronoParser.RULE_returnStatement

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

        localctx = ChronoParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            self.match(ChronoParser.RETURN)
            self.state = 357
            self.expression()
            self.state = 358
            self.match(ChronoParser.SEMIC_TOKEN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(ChronoParser.ASSIGN, 0)

        def PLUS_ASSIGN(self):
            return self.getToken(ChronoParser.PLUS_ASSIGN, 0)

        def MINUS_ASSIGN(self):
            return self.getToken(ChronoParser.MINUS_ASSIGN, 0)

        def STAR_ASSIGN(self):
            return self.getToken(ChronoParser.STAR_ASSIGN, 0)

        def SLASH_ASSIGN(self):
            return self.getToken(ChronoParser.SLASH_ASSIGN, 0)

        def MOD_ASSIGN(self):
            return self.getToken(ChronoParser.MOD_ASSIGN, 0)

        def getRuleIndex(self):
            return ChronoParser.RULE_assignmentOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentOperator" ):
                listener.enterAssignmentOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentOperator" ):
                listener.exitAssignmentOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentOperator" ):
                return visitor.visitAssignmentOperator(self)
            else:
                return visitor.visitChildren(self)




    def assignmentOperator(self):

        localctx = ChronoParser.AssignmentOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            _la = self._input.LA(1)
            if not(((((_la - 44)) & ~0x3f) == 0 and ((1 << (_la - 44)) & 2097183) != 0)):
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


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignableExpression(self):
            return self.getTypedRuleContext(ChronoParser.AssignableExpressionContext,0)


        def assignmentOperator(self):
            return self.getTypedRuleContext(ChronoParser.AssignmentOperatorContext,0)


        def expression(self):
            return self.getTypedRuleContext(ChronoParser.ExpressionContext,0)


        def SEMIC_TOKEN(self):
            return self.getToken(ChronoParser.SEMIC_TOKEN, 0)

        def getRuleIndex(self):
            return ChronoParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = ChronoParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self.assignableExpression()
            self.state = 363
            self.assignmentOperator()
            self.state = 364
            self.expression()
            self.state = 365
            self.match(ChronoParser.SEMIC_TOKEN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignableExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignablePrimary(self):
            return self.getTypedRuleContext(ChronoParser.AssignablePrimaryContext,0)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.DOT)
            else:
                return self.getToken(ChronoParser.DOT, i)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.IDENTIFIER)
            else:
                return self.getToken(ChronoParser.IDENTIFIER, i)

        def LBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.LBRACK)
            else:
                return self.getToken(ChronoParser.LBRACK, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChronoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ChronoParser.ExpressionContext,i)


        def RBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.RBRACK)
            else:
                return self.getToken(ChronoParser.RBRACK, i)

        def ARROW(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.ARROW)
            else:
                return self.getToken(ChronoParser.ARROW, i)

        def getRuleIndex(self):
            return ChronoParser.RULE_assignableExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignableExpression" ):
                listener.enterAssignableExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignableExpression" ):
                listener.exitAssignableExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignableExpression" ):
                return visitor.visitAssignableExpression(self)
            else:
                return visitor.visitChildren(self)




    def assignableExpression(self):

        localctx = ChronoParser.AssignableExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_assignableExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.assignablePrimary()
            self.state = 378
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 34)) & ~0x3f) == 0 and ((1 << (_la - 34)) & 4563402753) != 0):
                self.state = 376
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [66]:
                    self.state = 368
                    self.match(ChronoParser.DOT)
                    self.state = 369
                    self.match(ChronoParser.IDENTIFIER)
                    pass
                elif token in [62]:
                    self.state = 370
                    self.match(ChronoParser.LBRACK)
                    self.state = 371
                    self.expression()
                    self.state = 372
                    self.match(ChronoParser.RBRACK)
                    pass
                elif token in [34]:
                    self.state = 374
                    self.match(ChronoParser.ARROW)
                    self.state = 375
                    self.match(ChronoParser.IDENTIFIER)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 380
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignablePrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ChronoParser.IDENTIFIER, 0)

        def THIS(self):
            return self.getToken(ChronoParser.THIS, 0)

        def STAR(self):
            return self.getToken(ChronoParser.STAR, 0)

        def assignablePrimary(self):
            return self.getTypedRuleContext(ChronoParser.AssignablePrimaryContext,0)


        def BIT_AND(self):
            return self.getToken(ChronoParser.BIT_AND, 0)

        def LPAREN(self):
            return self.getToken(ChronoParser.LPAREN, 0)

        def assignableExpression(self):
            return self.getTypedRuleContext(ChronoParser.AssignableExpressionContext,0)


        def RPAREN(self):
            return self.getToken(ChronoParser.RPAREN, 0)

        def getRuleIndex(self):
            return ChronoParser.RULE_assignablePrimary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignablePrimary" ):
                listener.enterAssignablePrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignablePrimary" ):
                listener.exitAssignablePrimary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignablePrimary" ):
                return visitor.visitAssignablePrimary(self)
            else:
                return visitor.visitChildren(self)




    def assignablePrimary(self):

        localctx = ChronoParser.AssignablePrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_assignablePrimary)
        try:
            self.state = 391
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [74]:
                self.enterOuterAlt(localctx, 1)
                self.state = 381
                self.match(ChronoParser.IDENTIFIER)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 382
                self.match(ChronoParser.THIS)
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 3)
                self.state = 383
                self.match(ChronoParser.STAR)
                self.state = 384
                self.assignablePrimary()
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 4)
                self.state = 385
                self.match(ChronoParser.BIT_AND)
                self.state = 386
                self.assignablePrimary()
                pass
            elif token in [58]:
                self.enterOuterAlt(localctx, 5)
                self.state = 387
                self.match(ChronoParser.LPAREN)
                self.state = 388
                self.assignableExpression()
                self.state = 389
                self.match(ChronoParser.RPAREN)
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


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.if_block = None # IfBlockContext
            self.else_if = None # IfStatementContext
            self.else_block = None # ElseBlockContext

        def IF(self):
            return self.getToken(ChronoParser.IF, 0)

        def LPAREN(self):
            return self.getToken(ChronoParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(ChronoParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(ChronoParser.RPAREN, 0)

        def ifBlock(self):
            return self.getTypedRuleContext(ChronoParser.IfBlockContext,0)


        def ELSE(self):
            return self.getToken(ChronoParser.ELSE, 0)

        def ifStatement(self):
            return self.getTypedRuleContext(ChronoParser.IfStatementContext,0)


        def elseBlock(self):
            return self.getTypedRuleContext(ChronoParser.ElseBlockContext,0)


        def getRuleIndex(self):
            return ChronoParser.RULE_ifStatement

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

        localctx = ChronoParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.match(ChronoParser.IF)
            self.state = 394
            self.match(ChronoParser.LPAREN)
            self.state = 395
            self.expression()
            self.state = 396
            self.match(ChronoParser.RPAREN)
            self.state = 397
            localctx.if_block = self.ifBlock()
            self.state = 403
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 398
                self.match(ChronoParser.ELSE)
                self.state = 401
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [12]:
                    self.state = 399
                    localctx.else_if = self.ifStatement()
                    pass
                elif token in [60]:
                    self.state = 400
                    localctx.else_block = self.elseBlock()
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


    class IfBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(ChronoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(ChronoParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChronoParser.StatementContext)
            else:
                return self.getTypedRuleContext(ChronoParser.StatementContext,i)


        def getRuleIndex(self):
            return ChronoParser.RULE_ifBlock

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

        localctx = ChronoParser.IfBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_ifBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            self.match(ChronoParser.LBRACE)
            self.state = 409
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1483939926574683192) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & 511) != 0):
                self.state = 406
                self.statement()
                self.state = 411
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 412
            self.match(ChronoParser.RBRACE)
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

        def LBRACE(self):
            return self.getToken(ChronoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(ChronoParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChronoParser.StatementContext)
            else:
                return self.getTypedRuleContext(ChronoParser.StatementContext,i)


        def getRuleIndex(self):
            return ChronoParser.RULE_elseBlock

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

        localctx = ChronoParser.ElseBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_elseBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
            self.match(ChronoParser.LBRACE)
            self.state = 418
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1483939926574683192) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & 511) != 0):
                self.state = 415
                self.statement()
                self.state = 420
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 421
            self.match(ChronoParser.RBRACE)
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

        def WHILE(self):
            return self.getToken(ChronoParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(ChronoParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(ChronoParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(ChronoParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(ChronoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(ChronoParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChronoParser.StatementContext)
            else:
                return self.getTypedRuleContext(ChronoParser.StatementContext,i)


        def getRuleIndex(self):
            return ChronoParser.RULE_whileStatement

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

        localctx = ChronoParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_whileStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 423
            self.match(ChronoParser.WHILE)
            self.state = 424
            self.match(ChronoParser.LPAREN)
            self.state = 425
            self.expression()
            self.state = 426
            self.match(ChronoParser.RPAREN)
            self.state = 427
            self.match(ChronoParser.LBRACE)
            self.state = 431
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1483939926574683192) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & 511) != 0):
                self.state = 428
                self.statement()
                self.state = 433
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 434
            self.match(ChronoParser.RBRACE)
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

        def variableDeclaration(self):
            return self.getTypedRuleContext(ChronoParser.VariableDeclarationContext,0)


        def assignment(self):
            return self.getTypedRuleContext(ChronoParser.AssignmentContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(ChronoParser.ReturnStatementContext,0)


        def expression(self):
            return self.getTypedRuleContext(ChronoParser.ExpressionContext,0)


        def SEMIC_TOKEN(self):
            return self.getToken(ChronoParser.SEMIC_TOKEN, 0)

        def cppBlock(self):
            return self.getTypedRuleContext(ChronoParser.CppBlockContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(ChronoParser.IfStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(ChronoParser.WhileStatementContext,0)


        def deleteStatement(self):
            return self.getTypedRuleContext(ChronoParser.DeleteStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(ChronoParser.ForStatementContext,0)


        def blockStatement(self):
            return self.getTypedRuleContext(ChronoParser.BlockStatementContext,0)


        def getRuleIndex(self):
            return ChronoParser.RULE_statement

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

        localctx = ChronoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_statement)
        try:
            self.state = 448
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 436
                self.variableDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 437
                self.assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 438
                self.returnStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 439
                self.expression()
                self.state = 440
                self.match(ChronoParser.SEMIC_TOKEN)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 442
                self.cppBlock()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 443
                self.ifStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 444
                self.whileStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 445
                self.deleteStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 446
                self.forStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 447
                self.blockStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(ChronoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(ChronoParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChronoParser.StatementContext)
            else:
                return self.getTypedRuleContext(ChronoParser.StatementContext,i)


        def getRuleIndex(self):
            return ChronoParser.RULE_blockStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockStatement" ):
                listener.enterBlockStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockStatement" ):
                listener.exitBlockStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockStatement" ):
                return visitor.visitBlockStatement(self)
            else:
                return visitor.visitChildren(self)




    def blockStatement(self):

        localctx = ChronoParser.BlockStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_blockStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 450
            self.match(ChronoParser.LBRACE)
            self.state = 454
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1483939926574683192) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & 511) != 0):
                self.state = 451
                self.statement()
                self.state = 456
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 457
            self.match(ChronoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeleteStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DELETE(self):
            return self.getToken(ChronoParser.DELETE, 0)

        def expression(self):
            return self.getTypedRuleContext(ChronoParser.ExpressionContext,0)


        def SEMIC_TOKEN(self):
            return self.getToken(ChronoParser.SEMIC_TOKEN, 0)

        def getRuleIndex(self):
            return ChronoParser.RULE_deleteStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeleteStatement" ):
                listener.enterDeleteStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeleteStatement" ):
                listener.exitDeleteStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeleteStatement" ):
                return visitor.visitDeleteStatement(self)
            else:
                return visitor.visitChildren(self)




    def deleteStatement(self):

        localctx = ChronoParser.DeleteStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_deleteStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 459
            self.match(ChronoParser.DELETE)
            self.state = 460
            self.expression()
            self.state = 461
            self.match(ChronoParser.SEMIC_TOKEN)
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
            self.init = None # ForInitContext
            self.cond = None # ExpressionContext
            self.incr = None # ForIncrementContext

        def FOR(self):
            return self.getToken(ChronoParser.FOR, 0)

        def LPAREN(self):
            return self.getToken(ChronoParser.LPAREN, 0)

        def SEMIC_TOKEN(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.SEMIC_TOKEN)
            else:
                return self.getToken(ChronoParser.SEMIC_TOKEN, i)

        def RPAREN(self):
            return self.getToken(ChronoParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(ChronoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(ChronoParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChronoParser.StatementContext)
            else:
                return self.getTypedRuleContext(ChronoParser.StatementContext,i)


        def forInit(self):
            return self.getTypedRuleContext(ChronoParser.ForInitContext,0)


        def expression(self):
            return self.getTypedRuleContext(ChronoParser.ExpressionContext,0)


        def forIncrement(self):
            return self.getTypedRuleContext(ChronoParser.ForIncrementContext,0)


        def getRuleIndex(self):
            return ChronoParser.RULE_forStatement

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

        localctx = ChronoParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 463
            self.match(ChronoParser.FOR)
            self.state = 464
            self.match(ChronoParser.LPAREN)
            self.state = 466
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 292736174802338840) != 0) or _la==74:
                self.state = 465
                localctx.init = self.forInit()


            self.state = 468
            self.match(ChronoParser.SEMIC_TOKEN)
            self.state = 470
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1483939925769323520) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & 511) != 0):
                self.state = 469
                localctx.cond = self.expression()


            self.state = 472
            self.match(ChronoParser.SEMIC_TOKEN)
            self.state = 474
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1483939925769323520) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & 511) != 0):
                self.state = 473
                localctx.incr = self.forIncrement()


            self.state = 476
            self.match(ChronoParser.RPAREN)
            self.state = 477
            self.match(ChronoParser.LBRACE)
            self.state = 481
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1483939926574683192) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & 511) != 0):
                self.state = 478
                self.statement()
                self.state = 483
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 484
            self.match(ChronoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration_no_semicolon(self):
            return self.getTypedRuleContext(ChronoParser.VariableDeclaration_no_semicolonContext,0)


        def assignment_no_semicolon(self):
            return self.getTypedRuleContext(ChronoParser.Assignment_no_semicolonContext,0)


        def getRuleIndex(self):
            return ChronoParser.RULE_forInit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForInit" ):
                listener.enterForInit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForInit" ):
                listener.exitForInit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForInit" ):
                return visitor.visitForInit(self)
            else:
                return visitor.visitChildren(self)




    def forInit(self):

        localctx = ChronoParser.ForInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_forInit)
        try:
            self.state = 488
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 486
                self.variableDeclaration_no_semicolon()
                pass
            elif token in [10, 41, 52, 58, 74]:
                self.enterOuterAlt(localctx, 2)
                self.state = 487
                self.assignment_no_semicolon()
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


    class ForIncrementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment_no_semicolon(self):
            return self.getTypedRuleContext(ChronoParser.Assignment_no_semicolonContext,0)


        def expression(self):
            return self.getTypedRuleContext(ChronoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ChronoParser.RULE_forIncrement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForIncrement" ):
                listener.enterForIncrement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForIncrement" ):
                listener.exitForIncrement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForIncrement" ):
                return visitor.visitForIncrement(self)
            else:
                return visitor.visitChildren(self)




    def forIncrement(self):

        localctx = ChronoParser.ForIncrementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_forIncrement)
        try:
            self.state = 492
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 490
                self.assignment_no_semicolon()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 491
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodSignatureContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token
            self.returnType = None # TypeSpecifierContext

        def FUNC(self):
            return self.getToken(ChronoParser.FUNC, 0)

        def LPAREN(self):
            return self.getToken(ChronoParser.LPAREN, 0)

        def parameters(self):
            return self.getTypedRuleContext(ChronoParser.ParametersContext,0)


        def RPAREN(self):
            return self.getToken(ChronoParser.RPAREN, 0)

        def SEMIC_TOKEN(self):
            return self.getToken(ChronoParser.SEMIC_TOKEN, 0)

        def IDENTIFIER(self):
            return self.getToken(ChronoParser.IDENTIFIER, 0)

        def ARROW(self):
            return self.getToken(ChronoParser.ARROW, 0)

        def typeSpecifier(self):
            return self.getTypedRuleContext(ChronoParser.TypeSpecifierContext,0)


        def getRuleIndex(self):
            return ChronoParser.RULE_methodSignature

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodSignature" ):
                listener.enterMethodSignature(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodSignature" ):
                listener.exitMethodSignature(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodSignature" ):
                return visitor.visitMethodSignature(self)
            else:
                return visitor.visitChildren(self)




    def methodSignature(self):

        localctx = ChronoParser.MethodSignatureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_methodSignature)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 494
            self.match(ChronoParser.FUNC)
            self.state = 495
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 496
            self.match(ChronoParser.LPAREN)
            self.state = 497
            self.parameters()
            self.state = 498
            self.match(ChronoParser.RPAREN)
            self.state = 501
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 499
                self.match(ChronoParser.ARROW)
                self.state = 500
                localctx.returnType = self.typeSpecifier()


            self.state = 503
            self.match(ChronoParser.SEMIC_TOKEN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token

        def INTERFACE(self):
            return self.getToken(ChronoParser.INTERFACE, 0)

        def LBRACE(self):
            return self.getToken(ChronoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(ChronoParser.RBRACE, 0)

        def IDENTIFIER(self):
            return self.getToken(ChronoParser.IDENTIFIER, 0)

        def methodSignature(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChronoParser.MethodSignatureContext)
            else:
                return self.getTypedRuleContext(ChronoParser.MethodSignatureContext,i)


        def cppBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChronoParser.CppBlockContext)
            else:
                return self.getTypedRuleContext(ChronoParser.CppBlockContext,i)


        def getRuleIndex(self):
            return ChronoParser.RULE_interfaceDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterfaceDefinition" ):
                listener.enterInterfaceDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterfaceDefinition" ):
                listener.exitInterfaceDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceDefinition" ):
                return visitor.visitInterfaceDefinition(self)
            else:
                return visitor.visitChildren(self)




    def interfaceDefinition(self):

        localctx = ChronoParser.InterfaceDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_interfaceDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 505
            self.match(ChronoParser.INTERFACE)
            self.state = 506
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 507
            self.match(ChronoParser.LBRACE)
            self.state = 512
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2 or _la==29:
                self.state = 510
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [2]:
                    self.state = 508
                    self.methodSignature()
                    pass
                elif token in [29]:
                    self.state = 509
                    self.cppBlock()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 514
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 515
            self.match(ChronoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclaration_no_semicolonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token
            self.typeName = None # TypeSpecifierContext

        def CONST(self):
            return self.getToken(ChronoParser.CONST, 0)

        def VAR(self):
            return self.getToken(ChronoParser.VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(ChronoParser.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(ChronoParser.COLON, 0)

        def ASSIGN(self):
            return self.getToken(ChronoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ChronoParser.ExpressionContext,0)


        def typeSpecifier(self):
            return self.getTypedRuleContext(ChronoParser.TypeSpecifierContext,0)


        def getRuleIndex(self):
            return ChronoParser.RULE_variableDeclaration_no_semicolon

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclaration_no_semicolon" ):
                listener.enterVariableDeclaration_no_semicolon(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclaration_no_semicolon" ):
                listener.exitVariableDeclaration_no_semicolon(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclaration_no_semicolon" ):
                return visitor.visitVariableDeclaration_no_semicolon(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclaration_no_semicolon(self):

        localctx = ChronoParser.VariableDeclaration_no_semicolonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_variableDeclaration_no_semicolon)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 517
            _la = self._input.LA(1)
            if not(_la==3 or _la==4):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 518
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 521
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==64:
                self.state = 519
                self.match(ChronoParser.COLON)
                self.state = 520
                localctx.typeName = self.typeSpecifier()


            self.state = 525
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==65:
                self.state = 523
                self.match(ChronoParser.ASSIGN)
                self.state = 524
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_no_semicolonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignableExpression(self):
            return self.getTypedRuleContext(ChronoParser.AssignableExpressionContext,0)


        def assignmentOperator(self):
            return self.getTypedRuleContext(ChronoParser.AssignmentOperatorContext,0)


        def expression(self):
            return self.getTypedRuleContext(ChronoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ChronoParser.RULE_assignment_no_semicolon

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment_no_semicolon" ):
                listener.enterAssignment_no_semicolon(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment_no_semicolon" ):
                listener.exitAssignment_no_semicolon(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_no_semicolon" ):
                return visitor.visitAssignment_no_semicolon(self)
            else:
                return visitor.visitChildren(self)




    def assignment_no_semicolon(self):

        localctx = ChronoParser.Assignment_no_semicolonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_assignment_no_semicolon)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 527
            self.assignableExpression()
            self.state = 528
            self.assignmentOperator()
            self.state = 529
            self.expression()
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

        def unaryExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChronoParser.UnaryExpressionContext)
            else:
                return self.getTypedRuleContext(ChronoParser.UnaryExpressionContext,i)


        def EQ(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.EQ)
            else:
                return self.getToken(ChronoParser.EQ, i)

        def NEQ(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.NEQ)
            else:
                return self.getToken(ChronoParser.NEQ, i)

        def LT(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.LT)
            else:
                return self.getToken(ChronoParser.LT, i)

        def GT(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.GT)
            else:
                return self.getToken(ChronoParser.GT, i)

        def LTE(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.LTE)
            else:
                return self.getToken(ChronoParser.LTE, i)

        def GTE(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.GTE)
            else:
                return self.getToken(ChronoParser.GTE, i)

        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.PLUS)
            else:
                return self.getToken(ChronoParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.MINUS)
            else:
                return self.getToken(ChronoParser.MINUS, i)

        def STAR(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.STAR)
            else:
                return self.getToken(ChronoParser.STAR, i)

        def SLASH(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.SLASH)
            else:
                return self.getToken(ChronoParser.SLASH, i)

        def MODULO(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.MODULO)
            else:
                return self.getToken(ChronoParser.MODULO, i)

        def AND_OP(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.AND_OP)
            else:
                return self.getToken(ChronoParser.AND_OP, i)

        def OR_OP(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.OR_OP)
            else:
                return self.getToken(ChronoParser.OR_OP, i)

        def BIT_AND(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.BIT_AND)
            else:
                return self.getToken(ChronoParser.BIT_AND, i)

        def BIT_OR(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.BIT_OR)
            else:
                return self.getToken(ChronoParser.BIT_OR, i)

        def BIT_XOR(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.BIT_XOR)
            else:
                return self.getToken(ChronoParser.BIT_XOR, i)

        def LSHIFT(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.LSHIFT)
            else:
                return self.getToken(ChronoParser.LSHIFT, i)

        def RSHIFT(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.RSHIFT)
            else:
                return self.getToken(ChronoParser.RSHIFT, i)

        def getRuleIndex(self):
            return ChronoParser.RULE_expression

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

        localctx = ChronoParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 531
            self.unaryExpression()
            self.state = 536
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 33231621184290816) != 0):
                self.state = 532
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 33231621184290816) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 533
                self.unaryExpression()
                self.state = 538
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpression(self):
            return self.getTypedRuleContext(ChronoParser.UnaryExpressionContext,0)


        def PLUS(self):
            return self.getToken(ChronoParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(ChronoParser.MINUS, 0)

        def NOT_OP(self):
            return self.getToken(ChronoParser.NOT_OP, 0)

        def BIT_NOT(self):
            return self.getToken(ChronoParser.BIT_NOT, 0)

        def BIT_AND(self):
            return self.getToken(ChronoParser.BIT_AND, 0)

        def STAR(self):
            return self.getToken(ChronoParser.STAR, 0)

        def simpleExpression(self):
            return self.getTypedRuleContext(ChronoParser.SimpleExpressionContext,0)


        def getRuleIndex(self):
            return ChronoParser.RULE_unaryExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryExpression" ):
                listener.enterUnaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryExpression" ):
                listener.exitUnaryExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpression" ):
                return visitor.visitUnaryExpression(self)
            else:
                return visitor.visitChildren(self)




    def unaryExpression(self):

        localctx = ChronoParser.UnaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_unaryExpression)
        self._la = 0 # Token type
        try:
            self.state = 546
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [39, 40, 51, 55]:
                self.enterOuterAlt(localctx, 1)
                self.state = 539
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 38282246100090880) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 540
                self.unaryExpression()
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 2)
                self.state = 541
                self.match(ChronoParser.BIT_AND)
                self.state = 542
                self.unaryExpression()
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 3)
                self.state = 543
                self.match(ChronoParser.STAR)
                self.state = 544
                self.unaryExpression()
                pass
            elif token in [10, 23, 24, 25, 26, 27, 58, 60, 68, 69, 70, 71, 72, 73, 74, 75, 76]:
                self.enterOuterAlt(localctx, 4)
                self.state = 545
                self.simpleExpression()
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


    class SimpleExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary(self):
            return self.getTypedRuleContext(ChronoParser.PrimaryContext,0)


        def functionCallExpression(self):
            return self.getTypedRuleContext(ChronoParser.FunctionCallExpressionContext,0)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.DOT)
            else:
                return self.getToken(ChronoParser.DOT, i)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.IDENTIFIER)
            else:
                return self.getToken(ChronoParser.IDENTIFIER, i)

        def LBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.LBRACK)
            else:
                return self.getToken(ChronoParser.LBRACK, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChronoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ChronoParser.ExpressionContext,i)


        def RBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.RBRACK)
            else:
                return self.getToken(ChronoParser.RBRACK, i)

        def ARROW(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.ARROW)
            else:
                return self.getToken(ChronoParser.ARROW, i)

        def typeList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChronoParser.TypeListContext)
            else:
                return self.getTypedRuleContext(ChronoParser.TypeListContext,i)


        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.LPAREN)
            else:
                return self.getToken(ChronoParser.LPAREN, i)

        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.RPAREN)
            else:
                return self.getToken(ChronoParser.RPAREN, i)

        def expressionList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChronoParser.ExpressionListContext)
            else:
                return self.getTypedRuleContext(ChronoParser.ExpressionListContext,i)


        def getRuleIndex(self):
            return ChronoParser.RULE_simpleExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleExpression" ):
                listener.enterSimpleExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleExpression" ):
                listener.exitSimpleExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleExpression" ):
                return visitor.visitSimpleExpression(self)
            else:
                return visitor.visitChildren(self)




    def simpleExpression(self):

        localctx = ChronoParser.SimpleExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_simpleExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 550
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
            if la_ == 1:
                self.state = 548
                self.primary()
                pass

            elif la_ == 2:
                self.state = 549
                self.functionCallExpression()
                pass


            self.state = 582
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 34)) & ~0x3f) == 0 and ((1 << (_la - 34)) & 4563402753) != 0):
                self.state = 580
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [66]:
                    self.state = 552
                    self.match(ChronoParser.DOT)
                    self.state = 553
                    self.match(ChronoParser.IDENTIFIER)
                    self.state = 558
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
                    if la_ == 1:
                        self.state = 554
                        self.match(ChronoParser.LBRACK)
                        self.state = 555
                        self.typeList()
                        self.state = 556
                        self.match(ChronoParser.RBRACK)


                    self.state = 565
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==58:
                        self.state = 560
                        self.match(ChronoParser.LPAREN)
                        self.state = 562
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1483939925769323520) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & 511) != 0):
                            self.state = 561
                            self.expressionList()


                        self.state = 564
                        self.match(ChronoParser.RPAREN)


                    pass
                elif token in [62]:
                    self.state = 567
                    self.match(ChronoParser.LBRACK)
                    self.state = 568
                    self.expression()
                    self.state = 569
                    self.match(ChronoParser.RBRACK)
                    pass
                elif token in [34]:
                    self.state = 571
                    self.match(ChronoParser.ARROW)
                    self.state = 572
                    self.match(ChronoParser.IDENTIFIER)
                    self.state = 578
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==58:
                        self.state = 573
                        self.match(ChronoParser.LPAREN)
                        self.state = 575
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1483939925769323520) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & 511) != 0):
                            self.state = 574
                            self.expressionList()


                        self.state = 577
                        self.match(ChronoParser.RPAREN)


                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 584
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(ChronoParser.NEW, 0)

        def baseType(self):
            return self.getTypedRuleContext(ChronoParser.BaseTypeContext,0)


        def LPAREN(self):
            return self.getToken(ChronoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ChronoParser.RPAREN, 0)

        def expressionList(self):
            return self.getTypedRuleContext(ChronoParser.ExpressionListContext,0)


        def LBRACK(self):
            return self.getToken(ChronoParser.LBRACK, 0)

        def typeSpecifier(self):
            return self.getTypedRuleContext(ChronoParser.TypeSpecifierContext,0)


        def RBRACK(self):
            return self.getToken(ChronoParser.RBRACK, 0)

        def AT_MAKE_UNIQUE(self):
            return self.getToken(ChronoParser.AT_MAKE_UNIQUE, 0)

        def AT_MAKE_SHARED(self):
            return self.getToken(ChronoParser.AT_MAKE_SHARED, 0)

        def literal(self):
            return self.getTypedRuleContext(ChronoParser.LiteralContext,0)


        def initializerList(self):
            return self.getTypedRuleContext(ChronoParser.InitializerListContext,0)


        def IDENTIFIER(self):
            return self.getToken(ChronoParser.IDENTIFIER, 0)

        def THIS(self):
            return self.getToken(ChronoParser.THIS, 0)

        def expression(self):
            return self.getTypedRuleContext(ChronoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ChronoParser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary" ):
                return visitor.visitPrimary(self)
            else:
                return visitor.visitChildren(self)




    def primary(self):

        localctx = ChronoParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_primary)
        self._la = 0 # Token type
        try:
            self.state = 611
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 585
                self.match(ChronoParser.NEW)
                self.state = 586
                self.baseType()
                self.state = 587
                self.match(ChronoParser.LPAREN)
                self.state = 589
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1483939925769323520) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & 511) != 0):
                    self.state = 588
                    self.expressionList()


                self.state = 591
                self.match(ChronoParser.RPAREN)
                pass
            elif token in [23, 24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 593
                _la = self._input.LA(1)
                if not(_la==23 or _la==24):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 594
                self.match(ChronoParser.LBRACK)
                self.state = 595
                self.typeSpecifier()
                self.state = 596
                self.match(ChronoParser.RBRACK)
                self.state = 597
                self.match(ChronoParser.LPAREN)
                self.state = 599
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1483939925769323520) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & 511) != 0):
                    self.state = 598
                    self.expressionList()


                self.state = 601
                self.match(ChronoParser.RPAREN)
                pass
            elif token in [26, 68, 69, 70, 71, 72, 73, 75, 76]:
                self.enterOuterAlt(localctx, 3)
                self.state = 603
                self.literal()
                pass
            elif token in [60]:
                self.enterOuterAlt(localctx, 4)
                self.state = 604
                self.initializerList()
                pass
            elif token in [74]:
                self.enterOuterAlt(localctx, 5)
                self.state = 605
                self.match(ChronoParser.IDENTIFIER)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 6)
                self.state = 606
                self.match(ChronoParser.THIS)
                pass
            elif token in [58]:
                self.enterOuterAlt(localctx, 7)
                self.state = 607
                self.match(ChronoParser.LPAREN)
                self.state = 608
                self.expression()
                self.state = 609
                self.match(ChronoParser.RPAREN)
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


    class InitializerListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(ChronoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(ChronoParser.RBRACE, 0)

        def expressionList(self):
            return self.getTypedRuleContext(ChronoParser.ExpressionListContext,0)


        def getRuleIndex(self):
            return ChronoParser.RULE_initializerList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitializerList" ):
                listener.enterInitializerList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitializerList" ):
                listener.exitInitializerList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitializerList" ):
                return visitor.visitInitializerList(self)
            else:
                return visitor.visitChildren(self)




    def initializerList(self):

        localctx = ChronoParser.InitializerListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_initializerList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 613
            self.match(ChronoParser.LBRACE)
            self.state = 615
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1483939925769323520) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & 511) != 0):
                self.state = 614
                self.expressionList()


            self.state = 617
            self.match(ChronoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.funcName = None # Token

        def LPAREN(self):
            return self.getToken(ChronoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ChronoParser.RPAREN, 0)

        def IDENTIFIER(self):
            return self.getToken(ChronoParser.IDENTIFIER, 0)

        def AT_MOVE(self):
            return self.getToken(ChronoParser.AT_MOVE, 0)

        def expressionList(self):
            return self.getTypedRuleContext(ChronoParser.ExpressionListContext,0)


        def getRuleIndex(self):
            return ChronoParser.RULE_functionCallExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCallExpression" ):
                listener.enterFunctionCallExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCallExpression" ):
                listener.exitFunctionCallExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCallExpression" ):
                return visitor.visitFunctionCallExpression(self)
            else:
                return visitor.visitChildren(self)




    def functionCallExpression(self):

        localctx = ChronoParser.FunctionCallExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_functionCallExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 619
            localctx.funcName = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==25 or _la==74):
                localctx.funcName = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 620
            self.match(ChronoParser.LPAREN)
            self.state = 622
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1483939925769323520) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & 511) != 0):
                self.state = 621
                self.expressionList()


            self.state = 624
            self.match(ChronoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChronoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ChronoParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.COMMA)
            else:
                return self.getToken(ChronoParser.COMMA, i)

        def getRuleIndex(self):
            return ChronoParser.RULE_expressionList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionList" ):
                listener.enterExpressionList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionList" ):
                listener.exitExpressionList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionList" ):
                return visitor.visitExpressionList(self)
            else:
                return visitor.visitChildren(self)




    def expressionList(self):

        localctx = ChronoParser.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 626
            self.expression()
            self.state = 631
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==67:
                self.state = 627
                self.match(ChronoParser.COMMA)
                self.state = 628
                self.expression()
                self.state = 633
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DECIMAL_LITERAL(self):
            return self.getToken(ChronoParser.DECIMAL_LITERAL, 0)

        def HEX_LITERAL(self):
            return self.getToken(ChronoParser.HEX_LITERAL, 0)

        def BINARY_LITERAL(self):
            return self.getToken(ChronoParser.BINARY_LITERAL, 0)

        def OCTAL_LITERAL(self):
            return self.getToken(ChronoParser.OCTAL_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(ChronoParser.FLOAT_LITERAL, 0)

        def BYTE_LITERAL(self):
            return self.getToken(ChronoParser.BYTE_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(ChronoParser.STRING_LITERAL, 0)

        def BOOL_LITERAL(self):
            return self.getToken(ChronoParser.BOOL_LITERAL, 0)

        def CHAR_LITERAL(self):
            return self.getToken(ChronoParser.CHAR_LITERAL, 0)

        def getRuleIndex(self):
            return ChronoParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = ChronoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 634
            _la = self._input.LA(1)
            if not(((((_la - 26)) & ~0x3f) == 0 and ((1 << (_la - 26)) & 1965926790463489) != 0)):
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





