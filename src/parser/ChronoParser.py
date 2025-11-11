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
        4,1,75,580,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,1,0,
        1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,3,0,104,8,0,1,0,5,0,107,
        8,0,10,0,12,0,110,9,0,3,0,112,8,0,1,1,1,1,1,1,5,1,117,8,1,10,1,12,
        1,120,9,1,1,2,1,2,1,2,5,2,125,8,2,10,2,12,2,128,9,2,1,3,1,3,1,3,
        1,3,3,3,134,8,3,1,3,1,3,3,3,138,8,3,1,3,1,3,1,4,1,4,3,4,144,8,4,
        1,5,4,5,147,8,5,11,5,12,5,148,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,3,
        6,159,8,6,1,7,1,7,1,8,3,8,164,8,8,1,8,1,8,1,8,3,8,169,8,8,1,8,1,
        8,3,8,173,8,8,3,8,175,8,8,1,8,1,8,3,8,179,8,8,1,8,1,8,1,8,1,8,3,
        8,185,8,8,1,9,1,9,1,9,1,9,3,9,191,8,9,1,9,1,9,3,9,195,8,9,1,9,1,
        9,5,9,199,8,9,10,9,12,9,202,9,9,1,9,1,9,1,10,1,10,1,10,1,10,5,10,
        210,8,10,10,10,12,10,213,9,10,1,10,1,10,1,11,3,11,218,8,11,1,11,
        1,11,3,11,222,8,11,1,11,1,11,3,11,226,8,11,1,11,1,11,1,11,3,11,231,
        8,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,240,8,12,1,12,1,12,
        5,12,244,8,12,10,12,12,12,247,9,12,1,12,1,12,1,13,1,13,1,13,1,13,
        1,13,1,13,5,13,257,8,13,10,13,12,13,260,9,13,1,13,1,13,1,14,1,14,
        1,14,5,14,267,8,14,10,14,12,14,270,9,14,1,14,1,14,1,15,1,15,1,15,
        1,15,3,15,278,8,15,1,15,1,15,1,16,3,16,283,8,16,1,16,1,16,1,16,1,
        16,1,16,1,16,1,16,3,16,292,8,16,1,16,1,16,5,16,296,8,16,10,16,12,
        16,299,9,16,1,16,1,16,1,17,1,17,1,17,5,17,306,8,17,10,17,12,17,309,
        9,17,3,17,311,8,17,1,18,1,18,1,18,1,18,1,19,1,19,5,19,319,8,19,10,
        19,12,19,322,9,19,1,19,1,19,1,20,1,20,1,20,1,20,1,21,1,21,1,22,1,
        22,1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,5,
        23,346,8,23,10,23,12,23,349,9,23,1,24,1,24,1,24,1,24,1,24,1,24,1,
        24,1,24,3,24,359,8,24,3,24,361,8,24,1,25,1,25,5,25,365,8,25,10,25,
        12,25,368,9,25,1,25,1,25,1,26,1,26,5,26,374,8,26,10,26,12,26,377,
        9,26,1,26,1,26,1,27,1,27,1,27,1,27,1,27,1,27,5,27,387,8,27,10,27,
        12,27,390,9,27,1,27,1,27,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,
        1,28,1,28,1,28,1,28,3,28,406,8,28,1,29,1,29,5,29,410,8,29,10,29,
        12,29,413,9,29,1,29,1,29,1,30,1,30,1,30,1,30,1,31,1,31,1,31,3,31,
        424,8,31,1,31,1,31,3,31,428,8,31,1,31,1,31,3,31,432,8,31,1,31,1,
        31,1,31,5,31,437,8,31,10,31,12,31,440,9,31,1,31,1,31,1,32,1,32,3,
        32,446,8,32,1,33,1,33,3,33,450,8,33,1,34,1,34,1,34,1,34,1,34,1,34,
        1,34,3,34,459,8,34,1,34,1,34,1,35,1,35,1,35,1,35,1,35,5,35,468,8,
        35,10,35,12,35,471,9,35,1,35,1,35,1,36,1,36,1,36,1,36,3,36,479,8,
        36,1,36,1,36,3,36,483,8,36,1,37,1,37,1,37,1,37,1,38,1,38,1,38,5,
        38,492,8,38,10,38,12,38,495,9,38,1,39,1,39,1,39,3,39,500,8,39,1,
        40,1,40,3,40,504,8,40,1,40,1,40,1,40,1,40,1,40,1,40,3,40,512,8,40,
        1,40,1,40,3,40,516,8,40,1,40,3,40,519,8,40,1,40,1,40,1,40,1,40,1,
        40,1,40,1,40,1,40,3,40,529,8,40,1,40,3,40,532,8,40,5,40,534,8,40,
        10,40,12,40,537,9,40,1,41,1,41,1,41,1,41,3,41,543,8,41,1,41,1,41,
        1,41,1,41,1,41,1,41,1,41,1,41,1,41,1,41,3,41,555,8,41,1,42,1,42,
        3,42,559,8,42,1,42,1,42,1,43,1,43,1,43,3,43,566,8,43,1,43,1,43,1,
        44,1,44,1,44,5,44,573,8,44,10,44,12,44,576,9,44,1,45,1,45,1,45,0,
        0,46,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,
        44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,
        88,90,0,8,2,0,35,35,46,46,1,0,3,4,2,0,50,50,69,69,2,0,38,42,59,59,
        2,0,10,10,68,68,4,0,24,27,29,37,43,44,46,48,3,0,33,34,45,45,49,49,
        3,0,20,20,62,67,69,70,628,0,111,1,0,0,0,2,113,1,0,0,0,4,121,1,0,
        0,0,6,129,1,0,0,0,8,143,1,0,0,0,10,146,1,0,0,0,12,158,1,0,0,0,14,
        160,1,0,0,0,16,184,1,0,0,0,18,186,1,0,0,0,20,205,1,0,0,0,22,230,
        1,0,0,0,24,232,1,0,0,0,26,250,1,0,0,0,28,263,1,0,0,0,30,273,1,0,
        0,0,32,282,1,0,0,0,34,310,1,0,0,0,36,312,1,0,0,0,38,316,1,0,0,0,
        40,325,1,0,0,0,42,329,1,0,0,0,44,331,1,0,0,0,46,336,1,0,0,0,48,350,
        1,0,0,0,50,362,1,0,0,0,52,371,1,0,0,0,54,380,1,0,0,0,56,405,1,0,
        0,0,58,407,1,0,0,0,60,416,1,0,0,0,62,420,1,0,0,0,64,445,1,0,0,0,
        66,449,1,0,0,0,68,451,1,0,0,0,70,462,1,0,0,0,72,474,1,0,0,0,74,484,
        1,0,0,0,76,488,1,0,0,0,78,499,1,0,0,0,80,503,1,0,0,0,82,554,1,0,
        0,0,84,556,1,0,0,0,86,562,1,0,0,0,88,569,1,0,0,0,90,577,1,0,0,0,
        92,93,5,56,0,0,93,94,3,0,0,0,94,95,5,51,0,0,95,96,3,76,38,0,96,97,
        5,57,0,0,97,112,1,0,0,0,98,103,3,2,1,0,99,100,5,56,0,0,100,101,3,
        4,2,0,101,102,5,57,0,0,102,104,1,0,0,0,103,99,1,0,0,0,103,104,1,
        0,0,0,104,108,1,0,0,0,105,107,7,0,0,0,106,105,1,0,0,0,107,110,1,
        0,0,0,108,106,1,0,0,0,108,109,1,0,0,0,109,112,1,0,0,0,110,108,1,
        0,0,0,111,92,1,0,0,0,111,98,1,0,0,0,112,1,1,0,0,0,113,118,5,68,0,
        0,114,115,5,60,0,0,115,117,5,68,0,0,116,114,1,0,0,0,117,120,1,0,
        0,0,118,116,1,0,0,0,118,119,1,0,0,0,119,3,1,0,0,0,120,118,1,0,0,
        0,121,126,3,8,4,0,122,123,5,61,0,0,123,125,3,8,4,0,124,122,1,0,0,
        0,125,128,1,0,0,0,126,124,1,0,0,0,126,127,1,0,0,0,127,5,1,0,0,0,
        128,126,1,0,0,0,129,130,7,1,0,0,130,133,5,68,0,0,131,132,5,58,0,
        0,132,134,3,0,0,0,133,131,1,0,0,0,133,134,1,0,0,0,134,137,1,0,0,
        0,135,136,5,59,0,0,136,138,3,76,38,0,137,135,1,0,0,0,137,138,1,0,
        0,0,138,139,1,0,0,0,139,140,5,51,0,0,140,7,1,0,0,0,141,144,3,0,0,
        0,142,144,3,90,45,0,143,141,1,0,0,0,143,142,1,0,0,0,144,9,1,0,0,
        0,145,147,3,12,6,0,146,145,1,0,0,0,147,148,1,0,0,0,148,146,1,0,0,
        0,148,149,1,0,0,0,149,150,1,0,0,0,150,151,5,0,0,1,151,11,1,0,0,0,
        152,159,3,30,15,0,153,159,3,38,19,0,154,159,3,18,9,0,155,159,3,20,
        10,0,156,159,3,32,16,0,157,159,3,70,35,0,158,152,1,0,0,0,158,153,
        1,0,0,0,158,154,1,0,0,0,158,155,1,0,0,0,158,156,1,0,0,0,158,157,
        1,0,0,0,159,13,1,0,0,0,160,161,5,16,0,0,161,15,1,0,0,0,162,164,3,
        14,7,0,163,162,1,0,0,0,163,164,1,0,0,0,164,165,1,0,0,0,165,185,3,
        6,3,0,166,168,5,11,0,0,167,169,3,14,7,0,168,167,1,0,0,0,168,169,
        1,0,0,0,169,175,1,0,0,0,170,172,3,14,7,0,171,173,5,11,0,0,172,171,
        1,0,0,0,172,173,1,0,0,0,173,175,1,0,0,0,174,166,1,0,0,0,174,170,
        1,0,0,0,175,176,1,0,0,0,176,185,3,24,12,0,177,179,3,14,7,0,178,177,
        1,0,0,0,178,179,1,0,0,0,179,180,1,0,0,0,180,185,3,26,13,0,181,185,
        3,24,12,0,182,185,3,28,14,0,183,185,3,38,19,0,184,163,1,0,0,0,184,
        174,1,0,0,0,184,178,1,0,0,0,184,181,1,0,0,0,184,182,1,0,0,0,184,
        183,1,0,0,0,185,17,1,0,0,0,186,187,5,6,0,0,187,190,5,68,0,0,188,
        189,5,58,0,0,189,191,5,68,0,0,190,188,1,0,0,0,190,191,1,0,0,0,191,
        194,1,0,0,0,192,193,5,18,0,0,193,195,3,4,2,0,194,192,1,0,0,0,194,
        195,1,0,0,0,195,196,1,0,0,0,196,200,5,54,0,0,197,199,3,16,8,0,198,
        197,1,0,0,0,199,202,1,0,0,0,200,198,1,0,0,0,200,201,1,0,0,0,201,
        203,1,0,0,0,202,200,1,0,0,0,203,204,5,55,0,0,204,19,1,0,0,0,205,
        206,5,7,0,0,206,207,5,68,0,0,207,211,5,54,0,0,208,210,3,22,11,0,
        209,208,1,0,0,0,210,213,1,0,0,0,211,209,1,0,0,0,211,212,1,0,0,0,
        212,214,1,0,0,0,213,211,1,0,0,0,214,215,5,55,0,0,215,21,1,0,0,0,
        216,218,3,14,7,0,217,216,1,0,0,0,217,218,1,0,0,0,218,219,1,0,0,0,
        219,231,3,6,3,0,220,222,3,14,7,0,221,220,1,0,0,0,221,222,1,0,0,0,
        222,223,1,0,0,0,223,231,3,24,12,0,224,226,3,14,7,0,225,224,1,0,0,
        0,225,226,1,0,0,0,226,227,1,0,0,0,227,231,3,26,13,0,228,231,3,28,
        14,0,229,231,3,38,19,0,230,217,1,0,0,0,230,221,1,0,0,0,230,225,1,
        0,0,0,230,228,1,0,0,0,230,229,1,0,0,0,231,23,1,0,0,0,232,233,5,2,
        0,0,233,234,5,68,0,0,234,235,5,52,0,0,235,236,3,34,17,0,236,239,
        5,53,0,0,237,238,5,28,0,0,238,240,3,0,0,0,239,237,1,0,0,0,239,240,
        1,0,0,0,240,241,1,0,0,0,241,245,5,54,0,0,242,244,3,56,28,0,243,242,
        1,0,0,0,244,247,1,0,0,0,245,243,1,0,0,0,245,246,1,0,0,0,246,248,
        1,0,0,0,247,245,1,0,0,0,248,249,5,55,0,0,249,25,1,0,0,0,250,251,
        5,8,0,0,251,252,5,52,0,0,252,253,3,34,17,0,253,254,5,53,0,0,254,
        258,5,54,0,0,255,257,3,56,28,0,256,255,1,0,0,0,257,260,1,0,0,0,258,
        256,1,0,0,0,258,259,1,0,0,0,259,261,1,0,0,0,260,258,1,0,0,0,261,
        262,5,55,0,0,262,27,1,0,0,0,263,264,5,9,0,0,264,268,5,54,0,0,265,
        267,3,56,28,0,266,265,1,0,0,0,267,270,1,0,0,0,268,266,1,0,0,0,268,
        269,1,0,0,0,269,271,1,0,0,0,270,268,1,0,0,0,271,272,5,55,0,0,272,
        29,1,0,0,0,273,274,5,1,0,0,274,277,7,2,0,0,275,276,5,19,0,0,276,
        278,5,68,0,0,277,275,1,0,0,0,277,278,1,0,0,0,278,279,1,0,0,0,279,
        280,5,51,0,0,280,31,1,0,0,0,281,283,5,11,0,0,282,281,1,0,0,0,282,
        283,1,0,0,0,283,284,1,0,0,0,284,285,5,2,0,0,285,286,5,68,0,0,286,
        287,5,52,0,0,287,288,3,34,17,0,288,291,5,53,0,0,289,290,5,28,0,0,
        290,292,3,0,0,0,291,289,1,0,0,0,291,292,1,0,0,0,292,293,1,0,0,0,
        293,297,5,54,0,0,294,296,3,56,28,0,295,294,1,0,0,0,296,299,1,0,0,
        0,297,295,1,0,0,0,297,298,1,0,0,0,298,300,1,0,0,0,299,297,1,0,0,
        0,300,301,5,55,0,0,301,33,1,0,0,0,302,307,3,36,18,0,303,304,5,61,
        0,0,304,306,3,36,18,0,305,303,1,0,0,0,306,309,1,0,0,0,307,305,1,
        0,0,0,307,308,1,0,0,0,308,311,1,0,0,0,309,307,1,0,0,0,310,302,1,
        0,0,0,310,311,1,0,0,0,311,35,1,0,0,0,312,313,5,68,0,0,313,314,5,
        58,0,0,314,315,3,0,0,0,315,37,1,0,0,0,316,320,5,23,0,0,317,319,5,
        75,0,0,318,317,1,0,0,0,319,322,1,0,0,0,320,318,1,0,0,0,320,321,1,
        0,0,0,321,323,1,0,0,0,322,320,1,0,0,0,323,324,5,74,0,0,324,39,1,
        0,0,0,325,326,5,5,0,0,326,327,3,76,38,0,327,328,5,51,0,0,328,41,
        1,0,0,0,329,330,7,3,0,0,330,43,1,0,0,0,331,332,3,46,23,0,332,333,
        3,42,21,0,333,334,3,76,38,0,334,335,5,51,0,0,335,45,1,0,0,0,336,
        347,7,4,0,0,337,338,5,60,0,0,338,346,5,68,0,0,339,340,5,56,0,0,340,
        341,3,76,38,0,341,342,5,57,0,0,342,346,1,0,0,0,343,344,5,28,0,0,
        344,346,5,68,0,0,345,337,1,0,0,0,345,339,1,0,0,0,345,343,1,0,0,0,
        346,349,1,0,0,0,347,345,1,0,0,0,347,348,1,0,0,0,348,47,1,0,0,0,349,
        347,1,0,0,0,350,351,5,12,0,0,351,352,5,52,0,0,352,353,3,76,38,0,
        353,354,5,53,0,0,354,360,3,50,25,0,355,358,5,13,0,0,356,359,3,48,
        24,0,357,359,3,52,26,0,358,356,1,0,0,0,358,357,1,0,0,0,359,361,1,
        0,0,0,360,355,1,0,0,0,360,361,1,0,0,0,361,49,1,0,0,0,362,366,5,54,
        0,0,363,365,3,56,28,0,364,363,1,0,0,0,365,368,1,0,0,0,366,364,1,
        0,0,0,366,367,1,0,0,0,367,369,1,0,0,0,368,366,1,0,0,0,369,370,5,
        55,0,0,370,51,1,0,0,0,371,375,5,54,0,0,372,374,3,56,28,0,373,372,
        1,0,0,0,374,377,1,0,0,0,375,373,1,0,0,0,375,376,1,0,0,0,376,378,
        1,0,0,0,377,375,1,0,0,0,378,379,5,55,0,0,379,53,1,0,0,0,380,381,
        5,14,0,0,381,382,5,52,0,0,382,383,3,76,38,0,383,384,5,53,0,0,384,
        388,5,54,0,0,385,387,3,56,28,0,386,385,1,0,0,0,387,390,1,0,0,0,388,
        386,1,0,0,0,388,389,1,0,0,0,389,391,1,0,0,0,390,388,1,0,0,0,391,
        392,5,55,0,0,392,55,1,0,0,0,393,406,3,6,3,0,394,406,3,44,22,0,395,
        406,3,40,20,0,396,397,3,76,38,0,397,398,5,51,0,0,398,406,1,0,0,0,
        399,406,3,38,19,0,400,406,3,48,24,0,401,406,3,54,27,0,402,406,3,
        60,30,0,403,406,3,62,31,0,404,406,3,58,29,0,405,393,1,0,0,0,405,
        394,1,0,0,0,405,395,1,0,0,0,405,396,1,0,0,0,405,399,1,0,0,0,405,
        400,1,0,0,0,405,401,1,0,0,0,405,402,1,0,0,0,405,403,1,0,0,0,405,
        404,1,0,0,0,406,57,1,0,0,0,407,411,5,54,0,0,408,410,3,56,28,0,409,
        408,1,0,0,0,410,413,1,0,0,0,411,409,1,0,0,0,411,412,1,0,0,0,412,
        414,1,0,0,0,413,411,1,0,0,0,414,415,5,55,0,0,415,59,1,0,0,0,416,
        417,5,22,0,0,417,418,3,76,38,0,418,419,5,51,0,0,419,61,1,0,0,0,420,
        421,5,15,0,0,421,423,5,52,0,0,422,424,3,64,32,0,423,422,1,0,0,0,
        423,424,1,0,0,0,424,425,1,0,0,0,425,427,5,51,0,0,426,428,3,76,38,
        0,427,426,1,0,0,0,427,428,1,0,0,0,428,429,1,0,0,0,429,431,5,51,0,
        0,430,432,3,66,33,0,431,430,1,0,0,0,431,432,1,0,0,0,432,433,1,0,
        0,0,433,434,5,53,0,0,434,438,5,54,0,0,435,437,3,56,28,0,436,435,
        1,0,0,0,437,440,1,0,0,0,438,436,1,0,0,0,438,439,1,0,0,0,439,441,
        1,0,0,0,440,438,1,0,0,0,441,442,5,55,0,0,442,63,1,0,0,0,443,446,
        3,72,36,0,444,446,3,74,37,0,445,443,1,0,0,0,445,444,1,0,0,0,446,
        65,1,0,0,0,447,450,3,74,37,0,448,450,3,76,38,0,449,447,1,0,0,0,449,
        448,1,0,0,0,450,67,1,0,0,0,451,452,5,2,0,0,452,453,5,68,0,0,453,
        454,5,52,0,0,454,455,3,34,17,0,455,458,5,53,0,0,456,457,5,28,0,0,
        457,459,3,0,0,0,458,456,1,0,0,0,458,459,1,0,0,0,459,460,1,0,0,0,
        460,461,5,51,0,0,461,69,1,0,0,0,462,463,5,17,0,0,463,464,5,68,0,
        0,464,469,5,54,0,0,465,468,3,68,34,0,466,468,3,38,19,0,467,465,1,
        0,0,0,467,466,1,0,0,0,468,471,1,0,0,0,469,467,1,0,0,0,469,470,1,
        0,0,0,470,472,1,0,0,0,471,469,1,0,0,0,472,473,5,55,0,0,473,71,1,
        0,0,0,474,475,7,1,0,0,475,478,5,68,0,0,476,477,5,58,0,0,477,479,
        3,0,0,0,478,476,1,0,0,0,478,479,1,0,0,0,479,482,1,0,0,0,480,481,
        5,59,0,0,481,483,3,76,38,0,482,480,1,0,0,0,482,483,1,0,0,0,483,73,
        1,0,0,0,484,485,3,46,23,0,485,486,3,42,21,0,486,487,3,76,38,0,487,
        75,1,0,0,0,488,493,3,78,39,0,489,490,7,5,0,0,490,492,3,78,39,0,491,
        489,1,0,0,0,492,495,1,0,0,0,493,491,1,0,0,0,493,494,1,0,0,0,494,
        77,1,0,0,0,495,493,1,0,0,0,496,497,7,6,0,0,497,500,3,78,39,0,498,
        500,3,80,40,0,499,496,1,0,0,0,499,498,1,0,0,0,500,79,1,0,0,0,501,
        504,3,82,41,0,502,504,3,86,43,0,503,501,1,0,0,0,503,502,1,0,0,0,
        504,535,1,0,0,0,505,506,5,60,0,0,506,511,5,68,0,0,507,508,5,56,0,
        0,508,509,3,4,2,0,509,510,5,57,0,0,510,512,1,0,0,0,511,507,1,0,0,
        0,511,512,1,0,0,0,512,518,1,0,0,0,513,515,5,52,0,0,514,516,3,88,
        44,0,515,514,1,0,0,0,515,516,1,0,0,0,516,517,1,0,0,0,517,519,5,53,
        0,0,518,513,1,0,0,0,518,519,1,0,0,0,519,534,1,0,0,0,520,521,5,56,
        0,0,521,522,3,76,38,0,522,523,5,57,0,0,523,534,1,0,0,0,524,525,5,
        28,0,0,525,531,5,68,0,0,526,528,5,52,0,0,527,529,3,88,44,0,528,527,
        1,0,0,0,528,529,1,0,0,0,529,530,1,0,0,0,530,532,5,53,0,0,531,526,
        1,0,0,0,531,532,1,0,0,0,532,534,1,0,0,0,533,505,1,0,0,0,533,520,
        1,0,0,0,533,524,1,0,0,0,534,537,1,0,0,0,535,533,1,0,0,0,535,536,
        1,0,0,0,536,81,1,0,0,0,537,535,1,0,0,0,538,539,5,21,0,0,539,540,
        3,2,1,0,540,542,5,52,0,0,541,543,3,88,44,0,542,541,1,0,0,0,542,543,
        1,0,0,0,543,544,1,0,0,0,544,545,5,53,0,0,545,555,1,0,0,0,546,555,
        3,90,45,0,547,555,3,84,42,0,548,555,5,68,0,0,549,555,5,10,0,0,550,
        551,5,52,0,0,551,552,3,76,38,0,552,553,5,53,0,0,553,555,1,0,0,0,
        554,538,1,0,0,0,554,546,1,0,0,0,554,547,1,0,0,0,554,548,1,0,0,0,
        554,549,1,0,0,0,554,550,1,0,0,0,555,83,1,0,0,0,556,558,5,54,0,0,
        557,559,3,88,44,0,558,557,1,0,0,0,558,559,1,0,0,0,559,560,1,0,0,
        0,560,561,5,55,0,0,561,85,1,0,0,0,562,563,5,68,0,0,563,565,5,52,
        0,0,564,566,3,88,44,0,565,564,1,0,0,0,565,566,1,0,0,0,566,567,1,
        0,0,0,567,568,5,53,0,0,568,87,1,0,0,0,569,574,3,76,38,0,570,571,
        5,61,0,0,571,573,3,76,38,0,572,570,1,0,0,0,573,576,1,0,0,0,574,572,
        1,0,0,0,574,575,1,0,0,0,575,89,1,0,0,0,576,574,1,0,0,0,577,578,7,
        7,0,0,578,91,1,0,0,0,70,103,108,111,118,126,133,137,143,148,158,
        163,168,172,174,178,184,190,194,200,211,217,221,225,230,239,245,
        258,268,277,282,291,297,307,310,320,345,347,358,360,366,375,388,
        405,411,423,427,431,438,445,449,458,467,469,478,482,493,499,503,
        511,515,518,528,531,533,535,542,554,558,565,574
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
                     "<INVALID>", "'new'", "'delete'", "'@cpp'", "'=='", 
                     "'!='", "'<='", "'>='", "'->'", "'&&'", "'||'", "'<<'", 
                     "'>>'", "'+'", "'-'", "'*'", "'/'", "'%'", "'+='", 
                     "'-='", "'*='", "'/='", "'%='", "'<'", "'>'", "'!'", 
                     "'&'", "'|'", "'^'", "'~'", "<INVALID>", "';'", "'('", 
                     "')'", "'{'", "'}'", "'['", "']'", "':'", "'='", "'.'", 
                     "','", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'@end'" ]

    symbolicNames = [ "<INVALID>", "IMPORT", "FUNC", "VAR", "CONST", "RETURN", 
                      "CLASS", "STRUCT", "INIT", "DEINIT", "THIS", "STATIC", 
                      "IF", "ELSE", "WHILE", "FOR", "PUBLIC", "INTERFACE", 
                      "IMPL", "AS", "BOOL_LITERAL", "NEW", "DELETE", "AT_CPP", 
                      "EQ", "NEQ", "LTE", "GTE", "ARROW", "AND_OP", "OR_OP", 
                      "LSHIFT", "RSHIFT", "PLUS", "MINUS", "STAR", "SLASH", 
                      "MODULO", "PLUS_ASSIGN", "MINUS_ASSIGN", "STAR_ASSIGN", 
                      "SLASH_ASSIGN", "MOD_ASSIGN", "LT", "GT", "NOT_OP", 
                      "BIT_AND", "BIT_OR", "BIT_XOR", "BIT_NOT", "INCLUDE_PATH", 
                      "SEMIC_TOKEN", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                      "LBRACK", "RBRACK", "COLON", "ASSIGN", "DOT", "COMMA", 
                      "HEX_LITERAL", "BINARY_LITERAL", "OCTAL_LITERAL", 
                      "FLOAT_LITERAL", "DECIMAL_LITERAL", "BYTE_LITERAL", 
                      "IDENTIFIER", "STRING_LITERAL", "CHAR_LITERAL", "LINE_COMMENT", 
                      "WHITESPACE", "NEWLINE", "AT_END", "CPP_BODY" ]

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
    RULE_ifStatement = 24
    RULE_ifBlock = 25
    RULE_elseBlock = 26
    RULE_whileStatement = 27
    RULE_statement = 28
    RULE_blockStatement = 29
    RULE_deleteStatement = 30
    RULE_forStatement = 31
    RULE_forInit = 32
    RULE_forIncrement = 33
    RULE_methodSignature = 34
    RULE_interfaceDefinition = 35
    RULE_variableDeclaration_no_semicolon = 36
    RULE_assignment_no_semicolon = 37
    RULE_expression = 38
    RULE_unaryExpression = 39
    RULE_simpleExpression = 40
    RULE_primary = 41
    RULE_initializerList = 42
    RULE_functionCallExpression = 43
    RULE_expressionList = 44
    RULE_literal = 45

    ruleNames =  [ "typeSpecifier", "baseType", "typeList", "variableDeclaration", 
                   "templateArgument", "program", "topLevelStatement", "accessModifier", 
                   "classBodyStatement", "classDefinition", "structDefinition", 
                   "structBodyStatement", "methodDefinition", "initDefinition", 
                   "deinitBlock", "importDirective", "functionDefinition", 
                   "parameters", "parameter", "cppBlock", "returnStatement", 
                   "assignmentOperator", "assignment", "assignableExpression", 
                   "ifStatement", "ifBlock", "elseBlock", "whileStatement", 
                   "statement", "blockStatement", "deleteStatement", "forStatement", 
                   "forInit", "forIncrement", "methodSignature", "interfaceDefinition", 
                   "variableDeclaration_no_semicolon", "assignment_no_semicolon", 
                   "expression", "unaryExpression", "simpleExpression", 
                   "primary", "initializerList", "functionCallExpression", 
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
    BOOL_LITERAL=20
    NEW=21
    DELETE=22
    AT_CPP=23
    EQ=24
    NEQ=25
    LTE=26
    GTE=27
    ARROW=28
    AND_OP=29
    OR_OP=30
    LSHIFT=31
    RSHIFT=32
    PLUS=33
    MINUS=34
    STAR=35
    SLASH=36
    MODULO=37
    PLUS_ASSIGN=38
    MINUS_ASSIGN=39
    STAR_ASSIGN=40
    SLASH_ASSIGN=41
    MOD_ASSIGN=42
    LT=43
    GT=44
    NOT_OP=45
    BIT_AND=46
    BIT_OR=47
    BIT_XOR=48
    BIT_NOT=49
    INCLUDE_PATH=50
    SEMIC_TOKEN=51
    LPAREN=52
    RPAREN=53
    LBRACE=54
    RBRACE=55
    LBRACK=56
    RBRACK=57
    COLON=58
    ASSIGN=59
    DOT=60
    COMMA=61
    HEX_LITERAL=62
    BINARY_LITERAL=63
    OCTAL_LITERAL=64
    FLOAT_LITERAL=65
    DECIMAL_LITERAL=66
    BYTE_LITERAL=67
    IDENTIFIER=68
    STRING_LITERAL=69
    CHAR_LITERAL=70
    LINE_COMMENT=71
    WHITESPACE=72
    NEWLINE=73
    AT_END=74
    CPP_BODY=75

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

        def baseType(self):
            return self.getTypedRuleContext(ChronoParser.BaseTypeContext,0)


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

        def typeList(self):
            return self.getTypedRuleContext(ChronoParser.TypeListContext,0)


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
            self.state = 111
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [56]:
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                self.match(ChronoParser.LBRACK)
                self.state = 93
                self.typeSpecifier()
                self.state = 94
                self.match(ChronoParser.SEMIC_TOKEN)
                self.state = 95
                self.expression()
                self.state = 96
                self.match(ChronoParser.RBRACK)
                pass
            elif token in [68]:
                self.enterOuterAlt(localctx, 2)
                self.state = 98
                self.baseType()
                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==56:
                    self.state = 99
                    self.match(ChronoParser.LBRACK)
                    self.state = 100
                    self.typeList()
                    self.state = 101
                    self.match(ChronoParser.RBRACK)


                self.state = 108
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==35 or _la==46:
                    self.state = 105
                    _la = self._input.LA(1)
                    if not(_la==35 or _la==46):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 110
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

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
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(ChronoParser.IDENTIFIER)
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==60:
                self.state = 114
                self.match(ChronoParser.DOT)
                self.state = 115
                self.match(ChronoParser.IDENTIFIER)
                self.state = 120
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            self.state = 121
            self.templateArgument()
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==61:
                self.state = 122
                self.match(ChronoParser.COMMA)
                self.state = 123
                self.templateArgument()
                self.state = 128
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
            self.state = 129
            _la = self._input.LA(1)
            if not(_la==3 or _la==4):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 130
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==58:
                self.state = 131
                self.match(ChronoParser.COLON)
                self.state = 132
                localctx.typeName = self.typeSpecifier()


            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==59:
                self.state = 135
                self.match(ChronoParser.ASSIGN)
                self.state = 136
                self.expression()


            self.state = 139
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
            self.state = 143
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [56, 68]:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.typeSpecifier()
                pass
            elif token in [20, 62, 63, 64, 65, 66, 67, 69, 70]:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
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
            self.state = 146 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 145
                self.topLevelStatement()
                self.state = 148 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 8521926) != 0)):
                    break

            self.state = 150
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
            self.state = 158
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                self.importDirective()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 153
                self.cppBlock()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 154
                self.classDefinition()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 4)
                self.state = 155
                self.structDefinition()
                pass
            elif token in [2, 11]:
                self.enterOuterAlt(localctx, 5)
                self.state = 156
                self.functionDefinition()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 6)
                self.state = 157
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
            self.state = 160
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
            self.state = 184
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 162
                    self.accessModifier()


                self.state = 165
                self.variableDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 174
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [11]:
                    self.state = 166
                    self.match(ChronoParser.STATIC)
                    self.state = 168
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==16:
                        self.state = 167
                        self.accessModifier()


                    pass
                elif token in [16]:
                    self.state = 170
                    self.accessModifier()
                    self.state = 172
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==11:
                        self.state = 171
                        self.match(ChronoParser.STATIC)


                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 176
                self.methodDefinition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 178
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 177
                    self.accessModifier()


                self.state = 180
                self.initDefinition()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 181
                self.methodDefinition()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 182
                self.deinitBlock()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 183
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
            self.state = 186
            self.match(ChronoParser.CLASS)
            self.state = 187
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==58:
                self.state = 188
                self.match(ChronoParser.COLON)
                self.state = 189
                localctx.base = self.match(ChronoParser.IDENTIFIER)


            self.state = 194
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 192
                self.match(ChronoParser.IMPL)
                self.state = 193
                localctx.interfaces = self.typeList()


            self.state = 196
            self.match(ChronoParser.LBRACE)
            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8456988) != 0):
                self.state = 197
                self.classBodyStatement()
                self.state = 202
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 203
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
            self.state = 205
            self.match(ChronoParser.STRUCT)
            self.state = 206
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 207
            self.match(ChronoParser.LBRACE)
            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8454940) != 0):
                self.state = 208
                self.structBodyStatement()
                self.state = 213
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 214
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
            self.state = 230
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 216
                    self.accessModifier()


                self.state = 219
                self.variableDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 221
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 220
                    self.accessModifier()


                self.state = 223
                self.methodDefinition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 225
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 224
                    self.accessModifier()


                self.state = 227
                self.initDefinition()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 228
                self.deinitBlock()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 229
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
            self.state = 232
            self.match(ChronoParser.FUNC)
            self.state = 233
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 234
            self.match(ChronoParser.LPAREN)
            self.state = 235
            self.parameters()
            self.state = 236
            self.match(ChronoParser.RPAREN)
            self.state = 239
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 237
                self.match(ChronoParser.ARROW)
                self.state = 238
                localctx.returnType = self.typeSpecifier()


            self.state = 241
            self.match(ChronoParser.LBRACE)
            self.state = 245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -4588569860179438536) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 127) != 0):
                self.state = 242
                self.statement()
                self.state = 247
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 248
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
            self.state = 250
            self.match(ChronoParser.INIT)
            self.state = 251
            self.match(ChronoParser.LPAREN)
            self.state = 252
            self.parameters()
            self.state = 253
            self.match(ChronoParser.RPAREN)
            self.state = 254
            self.match(ChronoParser.LBRACE)
            self.state = 258
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -4588569860179438536) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 127) != 0):
                self.state = 255
                self.statement()
                self.state = 260
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 261
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
            self.state = 263
            self.match(ChronoParser.DEINIT)
            self.state = 264
            self.match(ChronoParser.LBRACE)
            self.state = 268
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -4588569860179438536) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 127) != 0):
                self.state = 265
                self.statement()
                self.state = 270
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 271
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
            self.state = 273
            self.match(ChronoParser.IMPORT)
            self.state = 274
            localctx.path = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==50 or _la==69):
                localctx.path = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 277
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 275
                self.match(ChronoParser.AS)
                self.state = 276
                localctx.alias = self.match(ChronoParser.IDENTIFIER)


            self.state = 279
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
            self.state = 282
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 281
                self.match(ChronoParser.STATIC)


            self.state = 284
            self.match(ChronoParser.FUNC)
            self.state = 285
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 286
            self.match(ChronoParser.LPAREN)
            self.state = 287
            self.parameters()
            self.state = 288
            self.match(ChronoParser.RPAREN)
            self.state = 291
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 289
                self.match(ChronoParser.ARROW)
                self.state = 290
                localctx.returnType = self.typeSpecifier()


            self.state = 293
            self.match(ChronoParser.LBRACE)
            self.state = 297
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -4588569860179438536) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 127) != 0):
                self.state = 294
                self.statement()
                self.state = 299
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 300
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
            self.state = 310
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==68:
                self.state = 302
                self.parameter()
                self.state = 307
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==61:
                    self.state = 303
                    self.match(ChronoParser.COMMA)
                    self.state = 304
                    self.parameter()
                    self.state = 309
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
            self.state = 312
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 313
            self.match(ChronoParser.COLON)
            self.state = 314
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
            self.state = 316
            self.match(ChronoParser.AT_CPP)
            self.state = 320
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==75:
                self.state = 317
                self.match(ChronoParser.CPP_BODY)
                self.state = 322
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 323
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
            self.state = 325
            self.match(ChronoParser.RETURN)
            self.state = 326
            self.expression()
            self.state = 327
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
            self.state = 329
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 576469273518538752) != 0)):
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
            self.state = 331
            self.assignableExpression()
            self.state = 332
            self.assignmentOperator()
            self.state = 333
            self.expression()
            self.state = 334
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

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.IDENTIFIER)
            else:
                return self.getToken(ChronoParser.IDENTIFIER, i)

        def THIS(self):
            return self.getToken(ChronoParser.THIS, 0)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.DOT)
            else:
                return self.getToken(ChronoParser.DOT, i)

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
            self.state = 336
            _la = self._input.LA(1)
            if not(_la==10 or _la==68):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 347
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1224979098913210368) != 0):
                self.state = 345
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [60]:
                    self.state = 337
                    self.match(ChronoParser.DOT)
                    self.state = 338
                    self.match(ChronoParser.IDENTIFIER)
                    pass
                elif token in [56]:
                    self.state = 339
                    self.match(ChronoParser.LBRACK)
                    self.state = 340
                    self.expression()
                    self.state = 341
                    self.match(ChronoParser.RBRACK)
                    pass
                elif token in [28]:
                    self.state = 343
                    self.match(ChronoParser.ARROW)
                    self.state = 344
                    self.match(ChronoParser.IDENTIFIER)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 349
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 48, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.match(ChronoParser.IF)
            self.state = 351
            self.match(ChronoParser.LPAREN)
            self.state = 352
            self.expression()
            self.state = 353
            self.match(ChronoParser.RPAREN)
            self.state = 354
            localctx.if_block = self.ifBlock()
            self.state = 360
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 355
                self.match(ChronoParser.ELSE)
                self.state = 358
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [12]:
                    self.state = 356
                    localctx.else_if = self.ifStatement()
                    pass
                elif token in [54]:
                    self.state = 357
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
        self.enterRule(localctx, 50, self.RULE_ifBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self.match(ChronoParser.LBRACE)
            self.state = 366
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -4588569860179438536) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 127) != 0):
                self.state = 363
                self.statement()
                self.state = 368
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 369
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
        self.enterRule(localctx, 52, self.RULE_elseBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            self.match(ChronoParser.LBRACE)
            self.state = 375
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -4588569860179438536) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 127) != 0):
                self.state = 372
                self.statement()
                self.state = 377
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 378
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
        self.enterRule(localctx, 54, self.RULE_whileStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            self.match(ChronoParser.WHILE)
            self.state = 381
            self.match(ChronoParser.LPAREN)
            self.state = 382
            self.expression()
            self.state = 383
            self.match(ChronoParser.RPAREN)
            self.state = 384
            self.match(ChronoParser.LBRACE)
            self.state = 388
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -4588569860179438536) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 127) != 0):
                self.state = 385
                self.statement()
                self.state = 390
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 391
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
        self.enterRule(localctx, 56, self.RULE_statement)
        try:
            self.state = 405
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 393
                self.variableDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 394
                self.assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 395
                self.returnStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 396
                self.expression()
                self.state = 397
                self.match(ChronoParser.SEMIC_TOKEN)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 399
                self.cppBlock()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 400
                self.ifStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 401
                self.whileStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 402
                self.deleteStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 403
                self.forStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 404
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
        self.enterRule(localctx, 58, self.RULE_blockStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            self.match(ChronoParser.LBRACE)
            self.state = 411
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -4588569860179438536) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 127) != 0):
                self.state = 408
                self.statement()
                self.state = 413
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 414
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
        self.enterRule(localctx, 60, self.RULE_deleteStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            self.match(ChronoParser.DELETE)
            self.state = 417
            self.expression()
            self.state = 418
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
        self.enterRule(localctx, 62, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self.match(ChronoParser.FOR)
            self.state = 421
            self.match(ChronoParser.LPAREN)
            self.state = 423
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1048) != 0) or _la==68:
                self.state = 422
                localctx.init = self.forInit()


            self.state = 425
            self.match(ChronoParser.SEMIC_TOKEN)
            self.state = 427
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & 2301361983959600129) != 0):
                self.state = 426
                localctx.cond = self.expression()


            self.state = 429
            self.match(ChronoParser.SEMIC_TOKEN)
            self.state = 431
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & 2301361983959600129) != 0):
                self.state = 430
                localctx.incr = self.forIncrement()


            self.state = 433
            self.match(ChronoParser.RPAREN)
            self.state = 434
            self.match(ChronoParser.LBRACE)
            self.state = 438
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -4588569860179438536) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 127) != 0):
                self.state = 435
                self.statement()
                self.state = 440
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 441
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
        self.enterRule(localctx, 64, self.RULE_forInit)
        try:
            self.state = 445
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 443
                self.variableDeclaration_no_semicolon()
                pass
            elif token in [10, 68]:
                self.enterOuterAlt(localctx, 2)
                self.state = 444
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
        self.enterRule(localctx, 66, self.RULE_forIncrement)
        try:
            self.state = 449
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 447
                self.assignment_no_semicolon()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 448
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
        self.enterRule(localctx, 68, self.RULE_methodSignature)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            self.match(ChronoParser.FUNC)
            self.state = 452
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 453
            self.match(ChronoParser.LPAREN)
            self.state = 454
            self.parameters()
            self.state = 455
            self.match(ChronoParser.RPAREN)
            self.state = 458
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 456
                self.match(ChronoParser.ARROW)
                self.state = 457
                localctx.returnType = self.typeSpecifier()


            self.state = 460
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
        self.enterRule(localctx, 70, self.RULE_interfaceDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 462
            self.match(ChronoParser.INTERFACE)
            self.state = 463
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 464
            self.match(ChronoParser.LBRACE)
            self.state = 469
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2 or _la==23:
                self.state = 467
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [2]:
                    self.state = 465
                    self.methodSignature()
                    pass
                elif token in [23]:
                    self.state = 466
                    self.cppBlock()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 471
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 472
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
        self.enterRule(localctx, 72, self.RULE_variableDeclaration_no_semicolon)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
            _la = self._input.LA(1)
            if not(_la==3 or _la==4):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 475
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 478
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==58:
                self.state = 476
                self.match(ChronoParser.COLON)
                self.state = 477
                localctx.typeName = self.typeSpecifier()


            self.state = 482
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==59:
                self.state = 480
                self.match(ChronoParser.ASSIGN)
                self.state = 481
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
        self.enterRule(localctx, 74, self.RULE_assignment_no_semicolon)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 484
            self.assignableExpression()
            self.state = 485
            self.assignmentOperator()
            self.state = 486
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
        self.enterRule(localctx, 76, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 488
            self.unaryExpression()
            self.state = 493
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 519244081004544) != 0):
                self.state = 489
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 519244081004544) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 490
                self.unaryExpression()
                self.state = 495
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
        self.enterRule(localctx, 78, self.RULE_unaryExpression)
        self._la = 0 # Token type
        try:
            self.state = 499
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33, 34, 45, 49]:
                self.enterOuterAlt(localctx, 1)
                self.state = 496
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 598160095313920) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 497
                self.unaryExpression()
                pass
            elif token in [10, 20, 21, 52, 54, 62, 63, 64, 65, 66, 67, 68, 69, 70]:
                self.enterOuterAlt(localctx, 2)
                self.state = 498
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
        self.enterRule(localctx, 80, self.RULE_simpleExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 503
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
            if la_ == 1:
                self.state = 501
                self.primary()
                pass

            elif la_ == 2:
                self.state = 502
                self.functionCallExpression()
                pass


            self.state = 535
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1224979098913210368) != 0):
                self.state = 533
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [60]:
                    self.state = 505
                    self.match(ChronoParser.DOT)
                    self.state = 506
                    self.match(ChronoParser.IDENTIFIER)
                    self.state = 511
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
                    if la_ == 1:
                        self.state = 507
                        self.match(ChronoParser.LBRACK)
                        self.state = 508
                        self.typeList()
                        self.state = 509
                        self.match(ChronoParser.RBRACK)


                    self.state = 518
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==52:
                        self.state = 513
                        self.match(ChronoParser.LPAREN)
                        self.state = 515
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & 2301361983959600129) != 0):
                            self.state = 514
                            self.expressionList()


                        self.state = 517
                        self.match(ChronoParser.RPAREN)


                    pass
                elif token in [56]:
                    self.state = 520
                    self.match(ChronoParser.LBRACK)
                    self.state = 521
                    self.expression()
                    self.state = 522
                    self.match(ChronoParser.RBRACK)
                    pass
                elif token in [28]:
                    self.state = 524
                    self.match(ChronoParser.ARROW)
                    self.state = 525
                    self.match(ChronoParser.IDENTIFIER)
                    self.state = 531
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==52:
                        self.state = 526
                        self.match(ChronoParser.LPAREN)
                        self.state = 528
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & 2301361983959600129) != 0):
                            self.state = 527
                            self.expressionList()


                        self.state = 530
                        self.match(ChronoParser.RPAREN)


                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 537
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
        self.enterRule(localctx, 82, self.RULE_primary)
        self._la = 0 # Token type
        try:
            self.state = 554
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 538
                self.match(ChronoParser.NEW)
                self.state = 539
                self.baseType()
                self.state = 540
                self.match(ChronoParser.LPAREN)
                self.state = 542
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & 2301361983959600129) != 0):
                    self.state = 541
                    self.expressionList()


                self.state = 544
                self.match(ChronoParser.RPAREN)
                pass
            elif token in [20, 62, 63, 64, 65, 66, 67, 69, 70]:
                self.enterOuterAlt(localctx, 2)
                self.state = 546
                self.literal()
                pass
            elif token in [54]:
                self.enterOuterAlt(localctx, 3)
                self.state = 547
                self.initializerList()
                pass
            elif token in [68]:
                self.enterOuterAlt(localctx, 4)
                self.state = 548
                self.match(ChronoParser.IDENTIFIER)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 5)
                self.state = 549
                self.match(ChronoParser.THIS)
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 6)
                self.state = 550
                self.match(ChronoParser.LPAREN)
                self.state = 551
                self.expression()
                self.state = 552
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
        self.enterRule(localctx, 84, self.RULE_initializerList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 556
            self.match(ChronoParser.LBRACE)
            self.state = 558
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & 2301361983959600129) != 0):
                self.state = 557
                self.expressionList()


            self.state = 560
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
            self.name = None # Token

        def LPAREN(self):
            return self.getToken(ChronoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ChronoParser.RPAREN, 0)

        def IDENTIFIER(self):
            return self.getToken(ChronoParser.IDENTIFIER, 0)

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
        self.enterRule(localctx, 86, self.RULE_functionCallExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 562
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 563
            self.match(ChronoParser.LPAREN)
            self.state = 565
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & 2301361983959600129) != 0):
                self.state = 564
                self.expressionList()


            self.state = 567
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
        self.enterRule(localctx, 88, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 569
            self.expression()
            self.state = 574
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==61:
                self.state = 570
                self.match(ChronoParser.COMMA)
                self.state = 571
                self.expression()
                self.state = 576
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
        self.enterRule(localctx, 90, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 577
            _la = self._input.LA(1)
            if not(((((_la - 20)) & ~0x3f) == 0 and ((1 << (_la - 20)) & 1965926790463489) != 0)):
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





