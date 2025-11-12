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
        4,1,75,598,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,3,0,106,8,0,1,0,
        5,0,109,8,0,10,0,12,0,112,9,0,3,0,114,8,0,1,1,1,1,1,1,5,1,119,8,
        1,10,1,12,1,122,9,1,1,2,1,2,1,2,5,2,127,8,2,10,2,12,2,130,9,2,1,
        3,1,3,1,3,1,3,3,3,136,8,3,1,3,1,3,3,3,140,8,3,1,3,1,3,1,4,1,4,3,
        4,146,8,4,1,5,4,5,149,8,5,11,5,12,5,150,1,5,1,5,1,6,1,6,1,6,1,6,
        1,6,1,6,3,6,161,8,6,1,7,1,7,1,8,3,8,166,8,8,1,8,1,8,1,8,3,8,171,
        8,8,1,8,1,8,3,8,175,8,8,3,8,177,8,8,1,8,1,8,3,8,181,8,8,1,8,1,8,
        1,8,1,8,3,8,187,8,8,1,9,1,9,1,9,1,9,3,9,193,8,9,1,9,1,9,3,9,197,
        8,9,1,9,1,9,5,9,201,8,9,10,9,12,9,204,9,9,1,9,1,9,1,10,1,10,1,10,
        1,10,5,10,212,8,10,10,10,12,10,215,9,10,1,10,1,10,1,11,3,11,220,
        8,11,1,11,1,11,3,11,224,8,11,1,11,1,11,3,11,228,8,11,1,11,1,11,1,
        11,3,11,233,8,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,242,8,12,
        1,12,1,12,5,12,246,8,12,10,12,12,12,249,9,12,1,12,1,12,1,13,1,13,
        1,13,1,13,1,13,1,13,5,13,259,8,13,10,13,12,13,262,9,13,1,13,1,13,
        1,14,1,14,1,14,5,14,269,8,14,10,14,12,14,272,9,14,1,14,1,14,1,15,
        1,15,1,15,1,15,3,15,280,8,15,1,15,1,15,1,16,3,16,285,8,16,1,16,1,
        16,1,16,1,16,1,16,1,16,1,16,3,16,294,8,16,1,16,1,16,5,16,298,8,16,
        10,16,12,16,301,9,16,1,16,1,16,1,17,1,17,1,17,5,17,308,8,17,10,17,
        12,17,311,9,17,3,17,313,8,17,1,18,1,18,1,18,1,18,1,19,1,19,5,19,
        321,8,19,10,19,12,19,324,9,19,1,19,1,19,1,20,1,20,1,20,1,20,1,21,
        1,21,1,22,1,22,1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,23,1,23,
        1,23,1,23,5,23,348,8,23,10,23,12,23,351,9,23,1,24,1,24,1,24,1,24,
        1,24,1,24,1,24,1,24,1,24,1,24,3,24,363,8,24,1,25,1,25,1,25,1,25,
        1,25,1,25,1,25,1,25,3,25,373,8,25,3,25,375,8,25,1,26,1,26,5,26,379,
        8,26,10,26,12,26,382,9,26,1,26,1,26,1,27,1,27,5,27,388,8,27,10,27,
        12,27,391,9,27,1,27,1,27,1,28,1,28,1,28,1,28,1,28,1,28,5,28,401,
        8,28,10,28,12,28,404,9,28,1,28,1,28,1,29,1,29,1,29,1,29,1,29,1,29,
        1,29,1,29,1,29,1,29,1,29,1,29,3,29,420,8,29,1,30,1,30,5,30,424,8,
        30,10,30,12,30,427,9,30,1,30,1,30,1,31,1,31,1,31,1,31,1,32,1,32,
        1,32,3,32,438,8,32,1,32,1,32,3,32,442,8,32,1,32,1,32,3,32,446,8,
        32,1,32,1,32,1,32,5,32,451,8,32,10,32,12,32,454,9,32,1,32,1,32,1,
        33,1,33,3,33,460,8,33,1,34,1,34,3,34,464,8,34,1,35,1,35,1,35,1,35,
        1,35,1,35,1,35,3,35,473,8,35,1,35,1,35,1,36,1,36,1,36,1,36,1,36,
        5,36,482,8,36,10,36,12,36,485,9,36,1,36,1,36,1,37,1,37,1,37,1,37,
        3,37,493,8,37,1,37,1,37,3,37,497,8,37,1,38,1,38,1,38,1,38,1,39,1,
        39,1,39,5,39,506,8,39,10,39,12,39,509,9,39,1,40,1,40,1,40,1,40,1,
        40,1,40,1,40,3,40,518,8,40,1,41,1,41,3,41,522,8,41,1,41,1,41,1,41,
        1,41,1,41,1,41,3,41,530,8,41,1,41,1,41,3,41,534,8,41,1,41,3,41,537,
        8,41,1,41,1,41,1,41,1,41,1,41,1,41,1,41,1,41,3,41,547,8,41,1,41,
        3,41,550,8,41,5,41,552,8,41,10,41,12,41,555,9,41,1,42,1,42,1,42,
        1,42,3,42,561,8,42,1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,42,
        1,42,3,42,573,8,42,1,43,1,43,3,43,577,8,43,1,43,1,43,1,44,1,44,1,
        44,3,44,584,8,44,1,44,1,44,1,45,1,45,1,45,5,45,591,8,45,10,45,12,
        45,594,9,45,1,46,1,46,1,46,0,0,47,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,
        68,70,72,74,76,78,80,82,84,86,88,90,92,0,7,2,0,35,35,46,46,1,0,3,
        4,2,0,50,50,69,69,2,0,38,42,59,59,4,0,24,27,29,37,43,44,46,48,3,
        0,33,34,45,45,49,49,3,0,20,20,62,67,69,70,651,0,113,1,0,0,0,2,115,
        1,0,0,0,4,123,1,0,0,0,6,131,1,0,0,0,8,145,1,0,0,0,10,148,1,0,0,0,
        12,160,1,0,0,0,14,162,1,0,0,0,16,186,1,0,0,0,18,188,1,0,0,0,20,207,
        1,0,0,0,22,232,1,0,0,0,24,234,1,0,0,0,26,252,1,0,0,0,28,265,1,0,
        0,0,30,275,1,0,0,0,32,284,1,0,0,0,34,312,1,0,0,0,36,314,1,0,0,0,
        38,318,1,0,0,0,40,327,1,0,0,0,42,331,1,0,0,0,44,333,1,0,0,0,46,338,
        1,0,0,0,48,362,1,0,0,0,50,364,1,0,0,0,52,376,1,0,0,0,54,385,1,0,
        0,0,56,394,1,0,0,0,58,419,1,0,0,0,60,421,1,0,0,0,62,430,1,0,0,0,
        64,434,1,0,0,0,66,459,1,0,0,0,68,463,1,0,0,0,70,465,1,0,0,0,72,476,
        1,0,0,0,74,488,1,0,0,0,76,498,1,0,0,0,78,502,1,0,0,0,80,517,1,0,
        0,0,82,521,1,0,0,0,84,572,1,0,0,0,86,574,1,0,0,0,88,580,1,0,0,0,
        90,587,1,0,0,0,92,595,1,0,0,0,94,95,5,56,0,0,95,96,3,0,0,0,96,97,
        5,51,0,0,97,98,3,78,39,0,98,99,5,57,0,0,99,114,1,0,0,0,100,105,3,
        2,1,0,101,102,5,56,0,0,102,103,3,4,2,0,103,104,5,57,0,0,104,106,
        1,0,0,0,105,101,1,0,0,0,105,106,1,0,0,0,106,110,1,0,0,0,107,109,
        7,0,0,0,108,107,1,0,0,0,109,112,1,0,0,0,110,108,1,0,0,0,110,111,
        1,0,0,0,111,114,1,0,0,0,112,110,1,0,0,0,113,94,1,0,0,0,113,100,1,
        0,0,0,114,1,1,0,0,0,115,120,5,68,0,0,116,117,5,60,0,0,117,119,5,
        68,0,0,118,116,1,0,0,0,119,122,1,0,0,0,120,118,1,0,0,0,120,121,1,
        0,0,0,121,3,1,0,0,0,122,120,1,0,0,0,123,128,3,8,4,0,124,125,5,61,
        0,0,125,127,3,8,4,0,126,124,1,0,0,0,127,130,1,0,0,0,128,126,1,0,
        0,0,128,129,1,0,0,0,129,5,1,0,0,0,130,128,1,0,0,0,131,132,7,1,0,
        0,132,135,5,68,0,0,133,134,5,58,0,0,134,136,3,0,0,0,135,133,1,0,
        0,0,135,136,1,0,0,0,136,139,1,0,0,0,137,138,5,59,0,0,138,140,3,78,
        39,0,139,137,1,0,0,0,139,140,1,0,0,0,140,141,1,0,0,0,141,142,5,51,
        0,0,142,7,1,0,0,0,143,146,3,0,0,0,144,146,3,92,46,0,145,143,1,0,
        0,0,145,144,1,0,0,0,146,9,1,0,0,0,147,149,3,12,6,0,148,147,1,0,0,
        0,149,150,1,0,0,0,150,148,1,0,0,0,150,151,1,0,0,0,151,152,1,0,0,
        0,152,153,5,0,0,1,153,11,1,0,0,0,154,161,3,30,15,0,155,161,3,38,
        19,0,156,161,3,18,9,0,157,161,3,20,10,0,158,161,3,32,16,0,159,161,
        3,72,36,0,160,154,1,0,0,0,160,155,1,0,0,0,160,156,1,0,0,0,160,157,
        1,0,0,0,160,158,1,0,0,0,160,159,1,0,0,0,161,13,1,0,0,0,162,163,5,
        16,0,0,163,15,1,0,0,0,164,166,3,14,7,0,165,164,1,0,0,0,165,166,1,
        0,0,0,166,167,1,0,0,0,167,187,3,6,3,0,168,170,5,11,0,0,169,171,3,
        14,7,0,170,169,1,0,0,0,170,171,1,0,0,0,171,177,1,0,0,0,172,174,3,
        14,7,0,173,175,5,11,0,0,174,173,1,0,0,0,174,175,1,0,0,0,175,177,
        1,0,0,0,176,168,1,0,0,0,176,172,1,0,0,0,177,178,1,0,0,0,178,187,
        3,24,12,0,179,181,3,14,7,0,180,179,1,0,0,0,180,181,1,0,0,0,181,182,
        1,0,0,0,182,187,3,26,13,0,183,187,3,24,12,0,184,187,3,28,14,0,185,
        187,3,38,19,0,186,165,1,0,0,0,186,176,1,0,0,0,186,180,1,0,0,0,186,
        183,1,0,0,0,186,184,1,0,0,0,186,185,1,0,0,0,187,17,1,0,0,0,188,189,
        5,6,0,0,189,192,5,68,0,0,190,191,5,58,0,0,191,193,5,68,0,0,192,190,
        1,0,0,0,192,193,1,0,0,0,193,196,1,0,0,0,194,195,5,18,0,0,195,197,
        3,4,2,0,196,194,1,0,0,0,196,197,1,0,0,0,197,198,1,0,0,0,198,202,
        5,54,0,0,199,201,3,16,8,0,200,199,1,0,0,0,201,204,1,0,0,0,202,200,
        1,0,0,0,202,203,1,0,0,0,203,205,1,0,0,0,204,202,1,0,0,0,205,206,
        5,55,0,0,206,19,1,0,0,0,207,208,5,7,0,0,208,209,5,68,0,0,209,213,
        5,54,0,0,210,212,3,22,11,0,211,210,1,0,0,0,212,215,1,0,0,0,213,211,
        1,0,0,0,213,214,1,0,0,0,214,216,1,0,0,0,215,213,1,0,0,0,216,217,
        5,55,0,0,217,21,1,0,0,0,218,220,3,14,7,0,219,218,1,0,0,0,219,220,
        1,0,0,0,220,221,1,0,0,0,221,233,3,6,3,0,222,224,3,14,7,0,223,222,
        1,0,0,0,223,224,1,0,0,0,224,225,1,0,0,0,225,233,3,24,12,0,226,228,
        3,14,7,0,227,226,1,0,0,0,227,228,1,0,0,0,228,229,1,0,0,0,229,233,
        3,26,13,0,230,233,3,28,14,0,231,233,3,38,19,0,232,219,1,0,0,0,232,
        223,1,0,0,0,232,227,1,0,0,0,232,230,1,0,0,0,232,231,1,0,0,0,233,
        23,1,0,0,0,234,235,5,2,0,0,235,236,5,68,0,0,236,237,5,52,0,0,237,
        238,3,34,17,0,238,241,5,53,0,0,239,240,5,28,0,0,240,242,3,0,0,0,
        241,239,1,0,0,0,241,242,1,0,0,0,242,243,1,0,0,0,243,247,5,54,0,0,
        244,246,3,58,29,0,245,244,1,0,0,0,246,249,1,0,0,0,247,245,1,0,0,
        0,247,248,1,0,0,0,248,250,1,0,0,0,249,247,1,0,0,0,250,251,5,55,0,
        0,251,25,1,0,0,0,252,253,5,8,0,0,253,254,5,52,0,0,254,255,3,34,17,
        0,255,256,5,53,0,0,256,260,5,54,0,0,257,259,3,58,29,0,258,257,1,
        0,0,0,259,262,1,0,0,0,260,258,1,0,0,0,260,261,1,0,0,0,261,263,1,
        0,0,0,262,260,1,0,0,0,263,264,5,55,0,0,264,27,1,0,0,0,265,266,5,
        9,0,0,266,270,5,54,0,0,267,269,3,58,29,0,268,267,1,0,0,0,269,272,
        1,0,0,0,270,268,1,0,0,0,270,271,1,0,0,0,271,273,1,0,0,0,272,270,
        1,0,0,0,273,274,5,55,0,0,274,29,1,0,0,0,275,276,5,1,0,0,276,279,
        7,2,0,0,277,278,5,19,0,0,278,280,5,68,0,0,279,277,1,0,0,0,279,280,
        1,0,0,0,280,281,1,0,0,0,281,282,5,51,0,0,282,31,1,0,0,0,283,285,
        5,11,0,0,284,283,1,0,0,0,284,285,1,0,0,0,285,286,1,0,0,0,286,287,
        5,2,0,0,287,288,5,68,0,0,288,289,5,52,0,0,289,290,3,34,17,0,290,
        293,5,53,0,0,291,292,5,28,0,0,292,294,3,0,0,0,293,291,1,0,0,0,293,
        294,1,0,0,0,294,295,1,0,0,0,295,299,5,54,0,0,296,298,3,58,29,0,297,
        296,1,0,0,0,298,301,1,0,0,0,299,297,1,0,0,0,299,300,1,0,0,0,300,
        302,1,0,0,0,301,299,1,0,0,0,302,303,5,55,0,0,303,33,1,0,0,0,304,
        309,3,36,18,0,305,306,5,61,0,0,306,308,3,36,18,0,307,305,1,0,0,0,
        308,311,1,0,0,0,309,307,1,0,0,0,309,310,1,0,0,0,310,313,1,0,0,0,
        311,309,1,0,0,0,312,304,1,0,0,0,312,313,1,0,0,0,313,35,1,0,0,0,314,
        315,5,68,0,0,315,316,5,58,0,0,316,317,3,0,0,0,317,37,1,0,0,0,318,
        322,5,23,0,0,319,321,5,75,0,0,320,319,1,0,0,0,321,324,1,0,0,0,322,
        320,1,0,0,0,322,323,1,0,0,0,323,325,1,0,0,0,324,322,1,0,0,0,325,
        326,5,74,0,0,326,39,1,0,0,0,327,328,5,5,0,0,328,329,3,78,39,0,329,
        330,5,51,0,0,330,41,1,0,0,0,331,332,7,3,0,0,332,43,1,0,0,0,333,334,
        3,46,23,0,334,335,3,42,21,0,335,336,3,78,39,0,336,337,5,51,0,0,337,
        45,1,0,0,0,338,349,3,48,24,0,339,340,5,60,0,0,340,348,5,68,0,0,341,
        342,5,56,0,0,342,343,3,78,39,0,343,344,5,57,0,0,344,348,1,0,0,0,
        345,346,5,28,0,0,346,348,5,68,0,0,347,339,1,0,0,0,347,341,1,0,0,
        0,347,345,1,0,0,0,348,351,1,0,0,0,349,347,1,0,0,0,349,350,1,0,0,
        0,350,47,1,0,0,0,351,349,1,0,0,0,352,363,5,68,0,0,353,363,5,10,0,
        0,354,355,5,35,0,0,355,363,3,48,24,0,356,357,5,46,0,0,357,363,3,
        48,24,0,358,359,5,52,0,0,359,360,3,46,23,0,360,361,5,53,0,0,361,
        363,1,0,0,0,362,352,1,0,0,0,362,353,1,0,0,0,362,354,1,0,0,0,362,
        356,1,0,0,0,362,358,1,0,0,0,363,49,1,0,0,0,364,365,5,12,0,0,365,
        366,5,52,0,0,366,367,3,78,39,0,367,368,5,53,0,0,368,374,3,52,26,
        0,369,372,5,13,0,0,370,373,3,50,25,0,371,373,3,54,27,0,372,370,1,
        0,0,0,372,371,1,0,0,0,373,375,1,0,0,0,374,369,1,0,0,0,374,375,1,
        0,0,0,375,51,1,0,0,0,376,380,5,54,0,0,377,379,3,58,29,0,378,377,
        1,0,0,0,379,382,1,0,0,0,380,378,1,0,0,0,380,381,1,0,0,0,381,383,
        1,0,0,0,382,380,1,0,0,0,383,384,5,55,0,0,384,53,1,0,0,0,385,389,
        5,54,0,0,386,388,3,58,29,0,387,386,1,0,0,0,388,391,1,0,0,0,389,387,
        1,0,0,0,389,390,1,0,0,0,390,392,1,0,0,0,391,389,1,0,0,0,392,393,
        5,55,0,0,393,55,1,0,0,0,394,395,5,14,0,0,395,396,5,52,0,0,396,397,
        3,78,39,0,397,398,5,53,0,0,398,402,5,54,0,0,399,401,3,58,29,0,400,
        399,1,0,0,0,401,404,1,0,0,0,402,400,1,0,0,0,402,403,1,0,0,0,403,
        405,1,0,0,0,404,402,1,0,0,0,405,406,5,55,0,0,406,57,1,0,0,0,407,
        420,3,6,3,0,408,420,3,44,22,0,409,420,3,40,20,0,410,411,3,78,39,
        0,411,412,5,51,0,0,412,420,1,0,0,0,413,420,3,38,19,0,414,420,3,50,
        25,0,415,420,3,56,28,0,416,420,3,62,31,0,417,420,3,64,32,0,418,420,
        3,60,30,0,419,407,1,0,0,0,419,408,1,0,0,0,419,409,1,0,0,0,419,410,
        1,0,0,0,419,413,1,0,0,0,419,414,1,0,0,0,419,415,1,0,0,0,419,416,
        1,0,0,0,419,417,1,0,0,0,419,418,1,0,0,0,420,59,1,0,0,0,421,425,5,
        54,0,0,422,424,3,58,29,0,423,422,1,0,0,0,424,427,1,0,0,0,425,423,
        1,0,0,0,425,426,1,0,0,0,426,428,1,0,0,0,427,425,1,0,0,0,428,429,
        5,55,0,0,429,61,1,0,0,0,430,431,5,22,0,0,431,432,3,78,39,0,432,433,
        5,51,0,0,433,63,1,0,0,0,434,435,5,15,0,0,435,437,5,52,0,0,436,438,
        3,66,33,0,437,436,1,0,0,0,437,438,1,0,0,0,438,439,1,0,0,0,439,441,
        5,51,0,0,440,442,3,78,39,0,441,440,1,0,0,0,441,442,1,0,0,0,442,443,
        1,0,0,0,443,445,5,51,0,0,444,446,3,68,34,0,445,444,1,0,0,0,445,446,
        1,0,0,0,446,447,1,0,0,0,447,448,5,53,0,0,448,452,5,54,0,0,449,451,
        3,58,29,0,450,449,1,0,0,0,451,454,1,0,0,0,452,450,1,0,0,0,452,453,
        1,0,0,0,453,455,1,0,0,0,454,452,1,0,0,0,455,456,5,55,0,0,456,65,
        1,0,0,0,457,460,3,74,37,0,458,460,3,76,38,0,459,457,1,0,0,0,459,
        458,1,0,0,0,460,67,1,0,0,0,461,464,3,76,38,0,462,464,3,78,39,0,463,
        461,1,0,0,0,463,462,1,0,0,0,464,69,1,0,0,0,465,466,5,2,0,0,466,467,
        5,68,0,0,467,468,5,52,0,0,468,469,3,34,17,0,469,472,5,53,0,0,470,
        471,5,28,0,0,471,473,3,0,0,0,472,470,1,0,0,0,472,473,1,0,0,0,473,
        474,1,0,0,0,474,475,5,51,0,0,475,71,1,0,0,0,476,477,5,17,0,0,477,
        478,5,68,0,0,478,483,5,54,0,0,479,482,3,70,35,0,480,482,3,38,19,
        0,481,479,1,0,0,0,481,480,1,0,0,0,482,485,1,0,0,0,483,481,1,0,0,
        0,483,484,1,0,0,0,484,486,1,0,0,0,485,483,1,0,0,0,486,487,5,55,0,
        0,487,73,1,0,0,0,488,489,7,1,0,0,489,492,5,68,0,0,490,491,5,58,0,
        0,491,493,3,0,0,0,492,490,1,0,0,0,492,493,1,0,0,0,493,496,1,0,0,
        0,494,495,5,59,0,0,495,497,3,78,39,0,496,494,1,0,0,0,496,497,1,0,
        0,0,497,75,1,0,0,0,498,499,3,46,23,0,499,500,3,42,21,0,500,501,3,
        78,39,0,501,77,1,0,0,0,502,507,3,80,40,0,503,504,7,4,0,0,504,506,
        3,80,40,0,505,503,1,0,0,0,506,509,1,0,0,0,507,505,1,0,0,0,507,508,
        1,0,0,0,508,79,1,0,0,0,509,507,1,0,0,0,510,511,7,5,0,0,511,518,3,
        80,40,0,512,513,5,46,0,0,513,518,3,80,40,0,514,515,5,35,0,0,515,
        518,3,80,40,0,516,518,3,82,41,0,517,510,1,0,0,0,517,512,1,0,0,0,
        517,514,1,0,0,0,517,516,1,0,0,0,518,81,1,0,0,0,519,522,3,84,42,0,
        520,522,3,88,44,0,521,519,1,0,0,0,521,520,1,0,0,0,522,553,1,0,0,
        0,523,524,5,60,0,0,524,529,5,68,0,0,525,526,5,56,0,0,526,527,3,4,
        2,0,527,528,5,57,0,0,528,530,1,0,0,0,529,525,1,0,0,0,529,530,1,0,
        0,0,530,536,1,0,0,0,531,533,5,52,0,0,532,534,3,90,45,0,533,532,1,
        0,0,0,533,534,1,0,0,0,534,535,1,0,0,0,535,537,5,53,0,0,536,531,1,
        0,0,0,536,537,1,0,0,0,537,552,1,0,0,0,538,539,5,56,0,0,539,540,3,
        78,39,0,540,541,5,57,0,0,541,552,1,0,0,0,542,543,5,28,0,0,543,549,
        5,68,0,0,544,546,5,52,0,0,545,547,3,90,45,0,546,545,1,0,0,0,546,
        547,1,0,0,0,547,548,1,0,0,0,548,550,5,53,0,0,549,544,1,0,0,0,549,
        550,1,0,0,0,550,552,1,0,0,0,551,523,1,0,0,0,551,538,1,0,0,0,551,
        542,1,0,0,0,552,555,1,0,0,0,553,551,1,0,0,0,553,554,1,0,0,0,554,
        83,1,0,0,0,555,553,1,0,0,0,556,557,5,21,0,0,557,558,3,2,1,0,558,
        560,5,52,0,0,559,561,3,90,45,0,560,559,1,0,0,0,560,561,1,0,0,0,561,
        562,1,0,0,0,562,563,5,53,0,0,563,573,1,0,0,0,564,573,3,92,46,0,565,
        573,3,86,43,0,566,573,5,68,0,0,567,573,5,10,0,0,568,569,5,52,0,0,
        569,570,3,78,39,0,570,571,5,53,0,0,571,573,1,0,0,0,572,556,1,0,0,
        0,572,564,1,0,0,0,572,565,1,0,0,0,572,566,1,0,0,0,572,567,1,0,0,
        0,572,568,1,0,0,0,573,85,1,0,0,0,574,576,5,54,0,0,575,577,3,90,45,
        0,576,575,1,0,0,0,576,577,1,0,0,0,577,578,1,0,0,0,578,579,5,55,0,
        0,579,87,1,0,0,0,580,581,5,68,0,0,581,583,5,52,0,0,582,584,3,90,
        45,0,583,582,1,0,0,0,583,584,1,0,0,0,584,585,1,0,0,0,585,586,5,53,
        0,0,586,89,1,0,0,0,587,592,3,78,39,0,588,589,5,61,0,0,589,591,3,
        78,39,0,590,588,1,0,0,0,591,594,1,0,0,0,592,590,1,0,0,0,592,593,
        1,0,0,0,593,91,1,0,0,0,594,592,1,0,0,0,595,596,7,6,0,0,596,93,1,
        0,0,0,71,105,110,113,120,128,135,139,145,150,160,165,170,174,176,
        180,186,192,196,202,213,219,223,227,232,241,247,260,270,279,284,
        293,299,309,312,322,347,349,362,372,374,380,389,402,419,425,437,
        441,445,452,459,463,472,481,483,492,496,507,517,521,529,533,536,
        546,549,551,553,560,572,576,583,592
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
            self.state = 113
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [56]:
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
                pass
            elif token in [68]:
                self.enterOuterAlt(localctx, 2)
                self.state = 100
                self.baseType()
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==56:
                    self.state = 101
                    self.match(ChronoParser.LBRACK)
                    self.state = 102
                    self.typeList()
                    self.state = 103
                    self.match(ChronoParser.RBRACK)


                self.state = 110
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==35 or _la==46:
                    self.state = 107
                    _la = self._input.LA(1)
                    if not(_la==35 or _la==46):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 112
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
            self.state = 115
            self.match(ChronoParser.IDENTIFIER)
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==60:
                self.state = 116
                self.match(ChronoParser.DOT)
                self.state = 117
                self.match(ChronoParser.IDENTIFIER)
                self.state = 122
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
            self.state = 123
            self.templateArgument()
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==61:
                self.state = 124
                self.match(ChronoParser.COMMA)
                self.state = 125
                self.templateArgument()
                self.state = 130
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
            self.state = 131
            _la = self._input.LA(1)
            if not(_la==3 or _la==4):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 132
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==58:
                self.state = 133
                self.match(ChronoParser.COLON)
                self.state = 134
                localctx.typeName = self.typeSpecifier()


            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==59:
                self.state = 137
                self.match(ChronoParser.ASSIGN)
                self.state = 138
                self.expression()


            self.state = 141
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
            self.state = 145
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [56, 68]:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self.typeSpecifier()
                pass
            elif token in [20, 62, 63, 64, 65, 66, 67, 69, 70]:
                self.enterOuterAlt(localctx, 2)
                self.state = 144
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
            self.state = 148 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 147
                self.topLevelStatement()
                self.state = 150 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 8521926) != 0)):
                    break

            self.state = 152
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
            self.state = 160
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                self.importDirective()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.cppBlock()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 156
                self.classDefinition()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 4)
                self.state = 157
                self.structDefinition()
                pass
            elif token in [2, 11]:
                self.enterOuterAlt(localctx, 5)
                self.state = 158
                self.functionDefinition()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 6)
                self.state = 159
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
            self.state = 162
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
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 164
                    self.accessModifier()


                self.state = 167
                self.variableDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 176
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [11]:
                    self.state = 168
                    self.match(ChronoParser.STATIC)
                    self.state = 170
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==16:
                        self.state = 169
                        self.accessModifier()


                    pass
                elif token in [16]:
                    self.state = 172
                    self.accessModifier()
                    self.state = 174
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==11:
                        self.state = 173
                        self.match(ChronoParser.STATIC)


                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 178
                self.methodDefinition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 180
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 179
                    self.accessModifier()


                self.state = 182
                self.initDefinition()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 183
                self.methodDefinition()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 184
                self.deinitBlock()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 185
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
            self.state = 188
            self.match(ChronoParser.CLASS)
            self.state = 189
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==58:
                self.state = 190
                self.match(ChronoParser.COLON)
                self.state = 191
                localctx.base = self.match(ChronoParser.IDENTIFIER)


            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 194
                self.match(ChronoParser.IMPL)
                self.state = 195
                localctx.interfaces = self.typeList()


            self.state = 198
            self.match(ChronoParser.LBRACE)
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8456988) != 0):
                self.state = 199
                self.classBodyStatement()
                self.state = 204
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 205
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
            self.state = 207
            self.match(ChronoParser.STRUCT)
            self.state = 208
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 209
            self.match(ChronoParser.LBRACE)
            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8454940) != 0):
                self.state = 210
                self.structBodyStatement()
                self.state = 215
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 216
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
            self.state = 232
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 218
                    self.accessModifier()


                self.state = 221
                self.variableDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 223
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 222
                    self.accessModifier()


                self.state = 225
                self.methodDefinition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 227
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 226
                    self.accessModifier()


                self.state = 229
                self.initDefinition()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 230
                self.deinitBlock()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 231
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
            self.state = 234
            self.match(ChronoParser.FUNC)
            self.state = 235
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 236
            self.match(ChronoParser.LPAREN)
            self.state = 237
            self.parameters()
            self.state = 238
            self.match(ChronoParser.RPAREN)
            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 239
                self.match(ChronoParser.ARROW)
                self.state = 240
                localctx.returnType = self.typeSpecifier()


            self.state = 243
            self.match(ChronoParser.LBRACE)
            self.state = 247
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -4588499457075522504) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 127) != 0):
                self.state = 244
                self.statement()
                self.state = 249
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 250
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
            self.state = 252
            self.match(ChronoParser.INIT)
            self.state = 253
            self.match(ChronoParser.LPAREN)
            self.state = 254
            self.parameters()
            self.state = 255
            self.match(ChronoParser.RPAREN)
            self.state = 256
            self.match(ChronoParser.LBRACE)
            self.state = 260
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -4588499457075522504) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 127) != 0):
                self.state = 257
                self.statement()
                self.state = 262
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 263
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
            self.state = 265
            self.match(ChronoParser.DEINIT)
            self.state = 266
            self.match(ChronoParser.LBRACE)
            self.state = 270
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -4588499457075522504) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 127) != 0):
                self.state = 267
                self.statement()
                self.state = 272
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 273
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
            self.state = 275
            self.match(ChronoParser.IMPORT)
            self.state = 276
            localctx.path = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==50 or _la==69):
                localctx.path = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 279
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 277
                self.match(ChronoParser.AS)
                self.state = 278
                localctx.alias = self.match(ChronoParser.IDENTIFIER)


            self.state = 281
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
            self.state = 284
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 283
                self.match(ChronoParser.STATIC)


            self.state = 286
            self.match(ChronoParser.FUNC)
            self.state = 287
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 288
            self.match(ChronoParser.LPAREN)
            self.state = 289
            self.parameters()
            self.state = 290
            self.match(ChronoParser.RPAREN)
            self.state = 293
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 291
                self.match(ChronoParser.ARROW)
                self.state = 292
                localctx.returnType = self.typeSpecifier()


            self.state = 295
            self.match(ChronoParser.LBRACE)
            self.state = 299
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -4588499457075522504) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 127) != 0):
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
            self.state = 312
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==68:
                self.state = 304
                self.parameter()
                self.state = 309
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==61:
                    self.state = 305
                    self.match(ChronoParser.COMMA)
                    self.state = 306
                    self.parameter()
                    self.state = 311
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
            self.state = 314
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 315
            self.match(ChronoParser.COLON)
            self.state = 316
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
            self.state = 318
            self.match(ChronoParser.AT_CPP)
            self.state = 322
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==75:
                self.state = 319
                self.match(ChronoParser.CPP_BODY)
                self.state = 324
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 325
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
            self.state = 327
            self.match(ChronoParser.RETURN)
            self.state = 328
            self.expression()
            self.state = 329
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
            self.state = 331
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
            self.state = 333
            self.assignableExpression()
            self.state = 334
            self.assignmentOperator()
            self.state = 335
            self.expression()
            self.state = 336
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
            self.state = 338
            self.assignablePrimary()
            self.state = 349
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1224979098913210368) != 0):
                self.state = 347
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [60]:
                    self.state = 339
                    self.match(ChronoParser.DOT)
                    self.state = 340
                    self.match(ChronoParser.IDENTIFIER)
                    pass
                elif token in [56]:
                    self.state = 341
                    self.match(ChronoParser.LBRACK)
                    self.state = 342
                    self.expression()
                    self.state = 343
                    self.match(ChronoParser.RBRACK)
                    pass
                elif token in [28]:
                    self.state = 345
                    self.match(ChronoParser.ARROW)
                    self.state = 346
                    self.match(ChronoParser.IDENTIFIER)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 351
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
            self.state = 362
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [68]:
                self.enterOuterAlt(localctx, 1)
                self.state = 352
                self.match(ChronoParser.IDENTIFIER)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 353
                self.match(ChronoParser.THIS)
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 3)
                self.state = 354
                self.match(ChronoParser.STAR)
                self.state = 355
                self.assignablePrimary()
                pass
            elif token in [46]:
                self.enterOuterAlt(localctx, 4)
                self.state = 356
                self.match(ChronoParser.BIT_AND)
                self.state = 357
                self.assignablePrimary()
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 5)
                self.state = 358
                self.match(ChronoParser.LPAREN)
                self.state = 359
                self.assignableExpression()
                self.state = 360
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
            self.state = 364
            self.match(ChronoParser.IF)
            self.state = 365
            self.match(ChronoParser.LPAREN)
            self.state = 366
            self.expression()
            self.state = 367
            self.match(ChronoParser.RPAREN)
            self.state = 368
            localctx.if_block = self.ifBlock()
            self.state = 374
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 369
                self.match(ChronoParser.ELSE)
                self.state = 372
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [12]:
                    self.state = 370
                    localctx.else_if = self.ifStatement()
                    pass
                elif token in [54]:
                    self.state = 371
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
            self.state = 376
            self.match(ChronoParser.LBRACE)
            self.state = 380
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -4588499457075522504) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 127) != 0):
                self.state = 377
                self.statement()
                self.state = 382
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 383
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
            self.state = 385
            self.match(ChronoParser.LBRACE)
            self.state = 389
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -4588499457075522504) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 127) != 0):
                self.state = 386
                self.statement()
                self.state = 391
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 392
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
            self.state = 394
            self.match(ChronoParser.WHILE)
            self.state = 395
            self.match(ChronoParser.LPAREN)
            self.state = 396
            self.expression()
            self.state = 397
            self.match(ChronoParser.RPAREN)
            self.state = 398
            self.match(ChronoParser.LBRACE)
            self.state = 402
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -4588499457075522504) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 127) != 0):
                self.state = 399
                self.statement()
                self.state = 404
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 405
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
            self.state = 419
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 407
                self.variableDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 408
                self.assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 409
                self.returnStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 410
                self.expression()
                self.state = 411
                self.match(ChronoParser.SEMIC_TOKEN)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 413
                self.cppBlock()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 414
                self.ifStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 415
                self.whileStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 416
                self.deleteStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 417
                self.forStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 418
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
            self.state = 421
            self.match(ChronoParser.LBRACE)
            self.state = 425
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -4588499457075522504) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 127) != 0):
                self.state = 422
                self.statement()
                self.state = 427
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 428
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
            self.state = 430
            self.match(ChronoParser.DELETE)
            self.state = 431
            self.expression()
            self.state = 432
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
            self.state = 434
            self.match(ChronoParser.FOR)
            self.state = 435
            self.match(ChronoParser.LPAREN)
            self.state = 437
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4574002731287576) != 0) or _la==68:
                self.state = 436
                localctx.init = self.forInit()


            self.state = 439
            self.match(ChronoParser.SEMIC_TOKEN)
            self.state = 441
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & 2301362052712631297) != 0):
                self.state = 440
                localctx.cond = self.expression()


            self.state = 443
            self.match(ChronoParser.SEMIC_TOKEN)
            self.state = 445
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & 2301362052712631297) != 0):
                self.state = 444
                localctx.incr = self.forIncrement()


            self.state = 447
            self.match(ChronoParser.RPAREN)
            self.state = 448
            self.match(ChronoParser.LBRACE)
            self.state = 452
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -4588499457075522504) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 127) != 0):
                self.state = 449
                self.statement()
                self.state = 454
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 455
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
            self.state = 459
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 457
                self.variableDeclaration_no_semicolon()
                pass
            elif token in [10, 35, 46, 52, 68]:
                self.enterOuterAlt(localctx, 2)
                self.state = 458
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
            self.state = 463
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 461
                self.assignment_no_semicolon()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 462
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
            self.state = 465
            self.match(ChronoParser.FUNC)
            self.state = 466
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 467
            self.match(ChronoParser.LPAREN)
            self.state = 468
            self.parameters()
            self.state = 469
            self.match(ChronoParser.RPAREN)
            self.state = 472
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 470
                self.match(ChronoParser.ARROW)
                self.state = 471
                localctx.returnType = self.typeSpecifier()


            self.state = 474
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
            self.state = 476
            self.match(ChronoParser.INTERFACE)
            self.state = 477
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 478
            self.match(ChronoParser.LBRACE)
            self.state = 483
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2 or _la==23:
                self.state = 481
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [2]:
                    self.state = 479
                    self.methodSignature()
                    pass
                elif token in [23]:
                    self.state = 480
                    self.cppBlock()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 485
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 486
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
            self.state = 488
            _la = self._input.LA(1)
            if not(_la==3 or _la==4):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 489
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 492
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==58:
                self.state = 490
                self.match(ChronoParser.COLON)
                self.state = 491
                localctx.typeName = self.typeSpecifier()


            self.state = 496
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==59:
                self.state = 494
                self.match(ChronoParser.ASSIGN)
                self.state = 495
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
            self.state = 498
            self.assignableExpression()
            self.state = 499
            self.assignmentOperator()
            self.state = 500
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
            self.state = 502
            self.unaryExpression()
            self.state = 507
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 519244081004544) != 0):
                self.state = 503
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 519244081004544) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 504
                self.unaryExpression()
                self.state = 509
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
            self.state = 517
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33, 34, 45, 49]:
                self.enterOuterAlt(localctx, 1)
                self.state = 510
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 598160095313920) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 511
                self.unaryExpression()
                pass
            elif token in [46]:
                self.enterOuterAlt(localctx, 2)
                self.state = 512
                self.match(ChronoParser.BIT_AND)
                self.state = 513
                self.unaryExpression()
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 3)
                self.state = 514
                self.match(ChronoParser.STAR)
                self.state = 515
                self.unaryExpression()
                pass
            elif token in [10, 20, 21, 52, 54, 62, 63, 64, 65, 66, 67, 68, 69, 70]:
                self.enterOuterAlt(localctx, 4)
                self.state = 516
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
            self.state = 521
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
            if la_ == 1:
                self.state = 519
                self.primary()
                pass

            elif la_ == 2:
                self.state = 520
                self.functionCallExpression()
                pass


            self.state = 553
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1224979098913210368) != 0):
                self.state = 551
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [60]:
                    self.state = 523
                    self.match(ChronoParser.DOT)
                    self.state = 524
                    self.match(ChronoParser.IDENTIFIER)
                    self.state = 529
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
                    if la_ == 1:
                        self.state = 525
                        self.match(ChronoParser.LBRACK)
                        self.state = 526
                        self.typeList()
                        self.state = 527
                        self.match(ChronoParser.RBRACK)


                    self.state = 536
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==52:
                        self.state = 531
                        self.match(ChronoParser.LPAREN)
                        self.state = 533
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & 2301362052712631297) != 0):
                            self.state = 532
                            self.expressionList()


                        self.state = 535
                        self.match(ChronoParser.RPAREN)


                    pass
                elif token in [56]:
                    self.state = 538
                    self.match(ChronoParser.LBRACK)
                    self.state = 539
                    self.expression()
                    self.state = 540
                    self.match(ChronoParser.RBRACK)
                    pass
                elif token in [28]:
                    self.state = 542
                    self.match(ChronoParser.ARROW)
                    self.state = 543
                    self.match(ChronoParser.IDENTIFIER)
                    self.state = 549
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==52:
                        self.state = 544
                        self.match(ChronoParser.LPAREN)
                        self.state = 546
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & 2301362052712631297) != 0):
                            self.state = 545
                            self.expressionList()


                        self.state = 548
                        self.match(ChronoParser.RPAREN)


                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 555
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
        self.enterRule(localctx, 84, self.RULE_primary)
        self._la = 0 # Token type
        try:
            self.state = 572
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 556
                self.match(ChronoParser.NEW)
                self.state = 557
                self.baseType()
                self.state = 558
                self.match(ChronoParser.LPAREN)
                self.state = 560
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & 2301362052712631297) != 0):
                    self.state = 559
                    self.expressionList()


                self.state = 562
                self.match(ChronoParser.RPAREN)
                pass
            elif token in [20, 62, 63, 64, 65, 66, 67, 69, 70]:
                self.enterOuterAlt(localctx, 2)
                self.state = 564
                self.literal()
                pass
            elif token in [54]:
                self.enterOuterAlt(localctx, 3)
                self.state = 565
                self.initializerList()
                pass
            elif token in [68]:
                self.enterOuterAlt(localctx, 4)
                self.state = 566
                self.match(ChronoParser.IDENTIFIER)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 5)
                self.state = 567
                self.match(ChronoParser.THIS)
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 6)
                self.state = 568
                self.match(ChronoParser.LPAREN)
                self.state = 569
                self.expression()
                self.state = 570
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
            self.state = 574
            self.match(ChronoParser.LBRACE)
            self.state = 576
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & 2301362052712631297) != 0):
                self.state = 575
                self.expressionList()


            self.state = 578
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
        self.enterRule(localctx, 88, self.RULE_functionCallExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 580
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 581
            self.match(ChronoParser.LPAREN)
            self.state = 583
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & 2301362052712631297) != 0):
                self.state = 582
                self.expressionList()


            self.state = 585
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
            self.state = 587
            self.expression()
            self.state = 592
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==61:
                self.state = 588
                self.match(ChronoParser.COMMA)
                self.state = 589
                self.expression()
                self.state = 594
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
            self.state = 595
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





