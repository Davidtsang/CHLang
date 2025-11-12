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
        4,1,81,613,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,3,0,106,8,0,1,0,
        5,0,109,8,0,10,0,12,0,112,9,0,3,0,114,8,0,1,1,1,1,1,1,5,1,119,8,
        1,10,1,12,1,122,9,1,1,1,1,1,1,1,3,1,127,8,1,1,2,1,2,1,2,5,2,132,
        8,2,10,2,12,2,135,9,2,1,3,1,3,1,3,1,3,3,3,141,8,3,1,3,1,3,3,3,145,
        8,3,1,3,1,3,1,4,1,4,3,4,151,8,4,1,5,4,5,154,8,5,11,5,12,5,155,1,
        5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,3,6,166,8,6,1,7,1,7,1,8,3,8,171,8,
        8,1,8,1,8,1,8,3,8,176,8,8,1,8,1,8,3,8,180,8,8,3,8,182,8,8,1,8,1,
        8,3,8,186,8,8,1,8,1,8,1,8,1,8,3,8,192,8,8,1,9,1,9,1,9,1,9,3,9,198,
        8,9,1,9,1,9,3,9,202,8,9,1,9,1,9,5,9,206,8,9,10,9,12,9,209,9,9,1,
        9,1,9,1,10,1,10,1,10,1,10,5,10,217,8,10,10,10,12,10,220,9,10,1,10,
        1,10,1,11,3,11,225,8,11,1,11,1,11,3,11,229,8,11,1,11,1,11,3,11,233,
        8,11,1,11,1,11,1,11,3,11,238,8,11,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,3,12,247,8,12,1,12,1,12,5,12,251,8,12,10,12,12,12,254,9,12,
        1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,5,13,264,8,13,10,13,12,13,
        267,9,13,1,13,1,13,1,14,1,14,1,14,5,14,274,8,14,10,14,12,14,277,
        9,14,1,14,1,14,1,15,1,15,1,15,1,15,3,15,285,8,15,1,15,1,15,1,16,
        3,16,290,8,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,299,8,16,1,
        16,1,16,5,16,303,8,16,10,16,12,16,306,9,16,1,16,1,16,1,17,1,17,1,
        17,5,17,313,8,17,10,17,12,17,316,9,17,3,17,318,8,17,1,18,1,18,1,
        18,1,18,1,19,1,19,5,19,326,8,19,10,19,12,19,329,9,19,1,19,1,19,1,
        20,1,20,1,20,1,20,1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,23,1,23,1,
        23,1,23,1,23,1,23,1,23,1,23,1,23,5,23,353,8,23,10,23,12,23,356,9,
        23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,3,24,368,8,
        24,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,3,25,378,8,25,3,25,380,
        8,25,1,26,1,26,5,26,384,8,26,10,26,12,26,387,9,26,1,26,1,26,1,27,
        1,27,5,27,393,8,27,10,27,12,27,396,9,27,1,27,1,27,1,28,1,28,1,28,
        1,28,1,28,1,28,5,28,406,8,28,10,28,12,28,409,9,28,1,28,1,28,1,29,
        1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,3,29,425,
        8,29,1,30,1,30,5,30,429,8,30,10,30,12,30,432,9,30,1,30,1,30,1,31,
        1,31,1,31,1,31,1,32,1,32,1,32,3,32,443,8,32,1,32,1,32,3,32,447,8,
        32,1,32,1,32,3,32,451,8,32,1,32,1,32,1,32,5,32,456,8,32,10,32,12,
        32,459,9,32,1,32,1,32,1,33,1,33,3,33,465,8,33,1,34,1,34,3,34,469,
        8,34,1,35,1,35,1,35,1,35,1,35,1,35,1,35,3,35,478,8,35,1,35,1,35,
        1,36,1,36,1,36,1,36,1,36,5,36,487,8,36,10,36,12,36,490,9,36,1,36,
        1,36,1,37,1,37,1,37,1,37,3,37,498,8,37,1,37,1,37,3,37,502,8,37,1,
        38,1,38,1,38,1,38,1,39,1,39,1,39,5,39,511,8,39,10,39,12,39,514,9,
        39,1,40,1,40,1,40,1,40,1,40,1,40,1,40,3,40,523,8,40,1,41,1,41,3,
        41,527,8,41,1,41,1,41,1,41,1,41,1,41,1,41,3,41,535,8,41,1,41,1,41,
        3,41,539,8,41,1,41,3,41,542,8,41,1,41,1,41,1,41,1,41,1,41,1,41,1,
        41,1,41,3,41,552,8,41,1,41,3,41,555,8,41,5,41,557,8,41,10,41,12,
        41,560,9,41,1,42,1,42,1,42,1,42,3,42,566,8,42,1,42,1,42,1,42,1,42,
        1,42,1,42,1,42,1,42,3,42,576,8,42,1,42,1,42,1,42,1,42,1,42,1,42,
        1,42,1,42,1,42,1,42,3,42,588,8,42,1,43,1,43,3,43,592,8,43,1,43,1,
        43,1,44,1,44,1,44,3,44,599,8,44,1,44,1,44,1,45,1,45,1,45,5,45,606,
        8,45,10,45,12,45,609,9,45,1,46,1,46,1,46,0,0,47,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,
        58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,0,9,2,0,41,
        41,52,52,1,0,3,4,2,0,56,56,75,75,2,0,44,48,65,65,4,0,30,33,35,43,
        49,50,52,54,3,0,39,40,51,51,55,55,1,0,23,24,2,0,25,25,74,74,3,0,
        26,26,68,73,75,76,671,0,113,1,0,0,0,2,126,1,0,0,0,4,128,1,0,0,0,
        6,136,1,0,0,0,8,150,1,0,0,0,10,153,1,0,0,0,12,165,1,0,0,0,14,167,
        1,0,0,0,16,191,1,0,0,0,18,193,1,0,0,0,20,212,1,0,0,0,22,237,1,0,
        0,0,24,239,1,0,0,0,26,257,1,0,0,0,28,270,1,0,0,0,30,280,1,0,0,0,
        32,289,1,0,0,0,34,317,1,0,0,0,36,319,1,0,0,0,38,323,1,0,0,0,40,332,
        1,0,0,0,42,336,1,0,0,0,44,338,1,0,0,0,46,343,1,0,0,0,48,367,1,0,
        0,0,50,369,1,0,0,0,52,381,1,0,0,0,54,390,1,0,0,0,56,399,1,0,0,0,
        58,424,1,0,0,0,60,426,1,0,0,0,62,435,1,0,0,0,64,439,1,0,0,0,66,464,
        1,0,0,0,68,468,1,0,0,0,70,470,1,0,0,0,72,481,1,0,0,0,74,493,1,0,
        0,0,76,503,1,0,0,0,78,507,1,0,0,0,80,522,1,0,0,0,82,526,1,0,0,0,
        84,587,1,0,0,0,86,589,1,0,0,0,88,595,1,0,0,0,90,602,1,0,0,0,92,610,
        1,0,0,0,94,95,5,62,0,0,95,96,3,0,0,0,96,97,5,57,0,0,97,98,3,78,39,
        0,98,99,5,63,0,0,99,114,1,0,0,0,100,105,3,2,1,0,101,102,5,62,0,0,
        102,103,3,4,2,0,103,104,5,63,0,0,104,106,1,0,0,0,105,101,1,0,0,0,
        105,106,1,0,0,0,106,110,1,0,0,0,107,109,7,0,0,0,108,107,1,0,0,0,
        109,112,1,0,0,0,110,108,1,0,0,0,110,111,1,0,0,0,111,114,1,0,0,0,
        112,110,1,0,0,0,113,94,1,0,0,0,113,100,1,0,0,0,114,1,1,0,0,0,115,
        120,5,74,0,0,116,117,5,66,0,0,117,119,5,74,0,0,118,116,1,0,0,0,119,
        122,1,0,0,0,120,118,1,0,0,0,120,121,1,0,0,0,121,127,1,0,0,0,122,
        120,1,0,0,0,123,127,5,20,0,0,124,127,5,21,0,0,125,127,5,22,0,0,126,
        115,1,0,0,0,126,123,1,0,0,0,126,124,1,0,0,0,126,125,1,0,0,0,127,
        3,1,0,0,0,128,133,3,8,4,0,129,130,5,67,0,0,130,132,3,8,4,0,131,129,
        1,0,0,0,132,135,1,0,0,0,133,131,1,0,0,0,133,134,1,0,0,0,134,5,1,
        0,0,0,135,133,1,0,0,0,136,137,7,1,0,0,137,140,5,74,0,0,138,139,5,
        64,0,0,139,141,3,0,0,0,140,138,1,0,0,0,140,141,1,0,0,0,141,144,1,
        0,0,0,142,143,5,65,0,0,143,145,3,78,39,0,144,142,1,0,0,0,144,145,
        1,0,0,0,145,146,1,0,0,0,146,147,5,57,0,0,147,7,1,0,0,0,148,151,3,
        0,0,0,149,151,3,92,46,0,150,148,1,0,0,0,150,149,1,0,0,0,151,9,1,
        0,0,0,152,154,3,12,6,0,153,152,1,0,0,0,154,155,1,0,0,0,155,153,1,
        0,0,0,155,156,1,0,0,0,156,157,1,0,0,0,157,158,5,0,0,1,158,11,1,0,
        0,0,159,166,3,30,15,0,160,166,3,38,19,0,161,166,3,18,9,0,162,166,
        3,20,10,0,163,166,3,32,16,0,164,166,3,72,36,0,165,159,1,0,0,0,165,
        160,1,0,0,0,165,161,1,0,0,0,165,162,1,0,0,0,165,163,1,0,0,0,165,
        164,1,0,0,0,166,13,1,0,0,0,167,168,5,16,0,0,168,15,1,0,0,0,169,171,
        3,14,7,0,170,169,1,0,0,0,170,171,1,0,0,0,171,172,1,0,0,0,172,192,
        3,6,3,0,173,175,5,11,0,0,174,176,3,14,7,0,175,174,1,0,0,0,175,176,
        1,0,0,0,176,182,1,0,0,0,177,179,3,14,7,0,178,180,5,11,0,0,179,178,
        1,0,0,0,179,180,1,0,0,0,180,182,1,0,0,0,181,173,1,0,0,0,181,177,
        1,0,0,0,182,183,1,0,0,0,183,192,3,24,12,0,184,186,3,14,7,0,185,184,
        1,0,0,0,185,186,1,0,0,0,186,187,1,0,0,0,187,192,3,26,13,0,188,192,
        3,24,12,0,189,192,3,28,14,0,190,192,3,38,19,0,191,170,1,0,0,0,191,
        181,1,0,0,0,191,185,1,0,0,0,191,188,1,0,0,0,191,189,1,0,0,0,191,
        190,1,0,0,0,192,17,1,0,0,0,193,194,5,6,0,0,194,197,5,74,0,0,195,
        196,5,64,0,0,196,198,5,74,0,0,197,195,1,0,0,0,197,198,1,0,0,0,198,
        201,1,0,0,0,199,200,5,18,0,0,200,202,3,4,2,0,201,199,1,0,0,0,201,
        202,1,0,0,0,202,203,1,0,0,0,203,207,5,60,0,0,204,206,3,16,8,0,205,
        204,1,0,0,0,206,209,1,0,0,0,207,205,1,0,0,0,207,208,1,0,0,0,208,
        210,1,0,0,0,209,207,1,0,0,0,210,211,5,61,0,0,211,19,1,0,0,0,212,
        213,5,7,0,0,213,214,5,74,0,0,214,218,5,60,0,0,215,217,3,22,11,0,
        216,215,1,0,0,0,217,220,1,0,0,0,218,216,1,0,0,0,218,219,1,0,0,0,
        219,221,1,0,0,0,220,218,1,0,0,0,221,222,5,61,0,0,222,21,1,0,0,0,
        223,225,3,14,7,0,224,223,1,0,0,0,224,225,1,0,0,0,225,226,1,0,0,0,
        226,238,3,6,3,0,227,229,3,14,7,0,228,227,1,0,0,0,228,229,1,0,0,0,
        229,230,1,0,0,0,230,238,3,24,12,0,231,233,3,14,7,0,232,231,1,0,0,
        0,232,233,1,0,0,0,233,234,1,0,0,0,234,238,3,26,13,0,235,238,3,28,
        14,0,236,238,3,38,19,0,237,224,1,0,0,0,237,228,1,0,0,0,237,232,1,
        0,0,0,237,235,1,0,0,0,237,236,1,0,0,0,238,23,1,0,0,0,239,240,5,2,
        0,0,240,241,5,74,0,0,241,242,5,58,0,0,242,243,3,34,17,0,243,246,
        5,59,0,0,244,245,5,34,0,0,245,247,3,0,0,0,246,244,1,0,0,0,246,247,
        1,0,0,0,247,248,1,0,0,0,248,252,5,60,0,0,249,251,3,58,29,0,250,249,
        1,0,0,0,251,254,1,0,0,0,252,250,1,0,0,0,252,253,1,0,0,0,253,255,
        1,0,0,0,254,252,1,0,0,0,255,256,5,61,0,0,256,25,1,0,0,0,257,258,
        5,8,0,0,258,259,5,58,0,0,259,260,3,34,17,0,260,261,5,59,0,0,261,
        265,5,60,0,0,262,264,3,58,29,0,263,262,1,0,0,0,264,267,1,0,0,0,265,
        263,1,0,0,0,265,266,1,0,0,0,266,268,1,0,0,0,267,265,1,0,0,0,268,
        269,5,61,0,0,269,27,1,0,0,0,270,271,5,9,0,0,271,275,5,60,0,0,272,
        274,3,58,29,0,273,272,1,0,0,0,274,277,1,0,0,0,275,273,1,0,0,0,275,
        276,1,0,0,0,276,278,1,0,0,0,277,275,1,0,0,0,278,279,5,61,0,0,279,
        29,1,0,0,0,280,281,5,1,0,0,281,284,7,2,0,0,282,283,5,19,0,0,283,
        285,5,74,0,0,284,282,1,0,0,0,284,285,1,0,0,0,285,286,1,0,0,0,286,
        287,5,57,0,0,287,31,1,0,0,0,288,290,5,11,0,0,289,288,1,0,0,0,289,
        290,1,0,0,0,290,291,1,0,0,0,291,292,5,2,0,0,292,293,5,74,0,0,293,
        294,5,58,0,0,294,295,3,34,17,0,295,298,5,59,0,0,296,297,5,34,0,0,
        297,299,3,0,0,0,298,296,1,0,0,0,298,299,1,0,0,0,299,300,1,0,0,0,
        300,304,5,60,0,0,301,303,3,58,29,0,302,301,1,0,0,0,303,306,1,0,0,
        0,304,302,1,0,0,0,304,305,1,0,0,0,305,307,1,0,0,0,306,304,1,0,0,
        0,307,308,5,61,0,0,308,33,1,0,0,0,309,314,3,36,18,0,310,311,5,67,
        0,0,311,313,3,36,18,0,312,310,1,0,0,0,313,316,1,0,0,0,314,312,1,
        0,0,0,314,315,1,0,0,0,315,318,1,0,0,0,316,314,1,0,0,0,317,309,1,
        0,0,0,317,318,1,0,0,0,318,35,1,0,0,0,319,320,5,74,0,0,320,321,5,
        64,0,0,321,322,3,0,0,0,322,37,1,0,0,0,323,327,5,29,0,0,324,326,5,
        81,0,0,325,324,1,0,0,0,326,329,1,0,0,0,327,325,1,0,0,0,327,328,1,
        0,0,0,328,330,1,0,0,0,329,327,1,0,0,0,330,331,5,80,0,0,331,39,1,
        0,0,0,332,333,5,5,0,0,333,334,3,78,39,0,334,335,5,57,0,0,335,41,
        1,0,0,0,336,337,7,3,0,0,337,43,1,0,0,0,338,339,3,46,23,0,339,340,
        3,42,21,0,340,341,3,78,39,0,341,342,5,57,0,0,342,45,1,0,0,0,343,
        354,3,48,24,0,344,345,5,66,0,0,345,353,5,74,0,0,346,347,5,62,0,0,
        347,348,3,78,39,0,348,349,5,63,0,0,349,353,1,0,0,0,350,351,5,34,
        0,0,351,353,5,74,0,0,352,344,1,0,0,0,352,346,1,0,0,0,352,350,1,0,
        0,0,353,356,1,0,0,0,354,352,1,0,0,0,354,355,1,0,0,0,355,47,1,0,0,
        0,356,354,1,0,0,0,357,368,5,74,0,0,358,368,5,10,0,0,359,360,5,41,
        0,0,360,368,3,48,24,0,361,362,5,52,0,0,362,368,3,48,24,0,363,364,
        5,58,0,0,364,365,3,46,23,0,365,366,5,59,0,0,366,368,1,0,0,0,367,
        357,1,0,0,0,367,358,1,0,0,0,367,359,1,0,0,0,367,361,1,0,0,0,367,
        363,1,0,0,0,368,49,1,0,0,0,369,370,5,12,0,0,370,371,5,58,0,0,371,
        372,3,78,39,0,372,373,5,59,0,0,373,379,3,52,26,0,374,377,5,13,0,
        0,375,378,3,50,25,0,376,378,3,54,27,0,377,375,1,0,0,0,377,376,1,
        0,0,0,378,380,1,0,0,0,379,374,1,0,0,0,379,380,1,0,0,0,380,51,1,0,
        0,0,381,385,5,60,0,0,382,384,3,58,29,0,383,382,1,0,0,0,384,387,1,
        0,0,0,385,383,1,0,0,0,385,386,1,0,0,0,386,388,1,0,0,0,387,385,1,
        0,0,0,388,389,5,61,0,0,389,53,1,0,0,0,390,394,5,60,0,0,391,393,3,
        58,29,0,392,391,1,0,0,0,393,396,1,0,0,0,394,392,1,0,0,0,394,395,
        1,0,0,0,395,397,1,0,0,0,396,394,1,0,0,0,397,398,5,61,0,0,398,55,
        1,0,0,0,399,400,5,14,0,0,400,401,5,58,0,0,401,402,3,78,39,0,402,
        403,5,59,0,0,403,407,5,60,0,0,404,406,3,58,29,0,405,404,1,0,0,0,
        406,409,1,0,0,0,407,405,1,0,0,0,407,408,1,0,0,0,408,410,1,0,0,0,
        409,407,1,0,0,0,410,411,5,61,0,0,411,57,1,0,0,0,412,425,3,6,3,0,
        413,425,3,44,22,0,414,425,3,40,20,0,415,416,3,78,39,0,416,417,5,
        57,0,0,417,425,1,0,0,0,418,425,3,38,19,0,419,425,3,50,25,0,420,425,
        3,56,28,0,421,425,3,62,31,0,422,425,3,64,32,0,423,425,3,60,30,0,
        424,412,1,0,0,0,424,413,1,0,0,0,424,414,1,0,0,0,424,415,1,0,0,0,
        424,418,1,0,0,0,424,419,1,0,0,0,424,420,1,0,0,0,424,421,1,0,0,0,
        424,422,1,0,0,0,424,423,1,0,0,0,425,59,1,0,0,0,426,430,5,60,0,0,
        427,429,3,58,29,0,428,427,1,0,0,0,429,432,1,0,0,0,430,428,1,0,0,
        0,430,431,1,0,0,0,431,433,1,0,0,0,432,430,1,0,0,0,433,434,5,61,0,
        0,434,61,1,0,0,0,435,436,5,28,0,0,436,437,3,78,39,0,437,438,5,57,
        0,0,438,63,1,0,0,0,439,440,5,15,0,0,440,442,5,58,0,0,441,443,3,66,
        33,0,442,441,1,0,0,0,442,443,1,0,0,0,443,444,1,0,0,0,444,446,5,57,
        0,0,445,447,3,78,39,0,446,445,1,0,0,0,446,447,1,0,0,0,447,448,1,
        0,0,0,448,450,5,57,0,0,449,451,3,68,34,0,450,449,1,0,0,0,450,451,
        1,0,0,0,451,452,1,0,0,0,452,453,5,59,0,0,453,457,5,60,0,0,454,456,
        3,58,29,0,455,454,1,0,0,0,456,459,1,0,0,0,457,455,1,0,0,0,457,458,
        1,0,0,0,458,460,1,0,0,0,459,457,1,0,0,0,460,461,5,61,0,0,461,65,
        1,0,0,0,462,465,3,74,37,0,463,465,3,76,38,0,464,462,1,0,0,0,464,
        463,1,0,0,0,465,67,1,0,0,0,466,469,3,76,38,0,467,469,3,78,39,0,468,
        466,1,0,0,0,468,467,1,0,0,0,469,69,1,0,0,0,470,471,5,2,0,0,471,472,
        5,74,0,0,472,473,5,58,0,0,473,474,3,34,17,0,474,477,5,59,0,0,475,
        476,5,34,0,0,476,478,3,0,0,0,477,475,1,0,0,0,477,478,1,0,0,0,478,
        479,1,0,0,0,479,480,5,57,0,0,480,71,1,0,0,0,481,482,5,17,0,0,482,
        483,5,74,0,0,483,488,5,60,0,0,484,487,3,70,35,0,485,487,3,38,19,
        0,486,484,1,0,0,0,486,485,1,0,0,0,487,490,1,0,0,0,488,486,1,0,0,
        0,488,489,1,0,0,0,489,491,1,0,0,0,490,488,1,0,0,0,491,492,5,61,0,
        0,492,73,1,0,0,0,493,494,7,1,0,0,494,497,5,74,0,0,495,496,5,64,0,
        0,496,498,3,0,0,0,497,495,1,0,0,0,497,498,1,0,0,0,498,501,1,0,0,
        0,499,500,5,65,0,0,500,502,3,78,39,0,501,499,1,0,0,0,501,502,1,0,
        0,0,502,75,1,0,0,0,503,504,3,46,23,0,504,505,3,42,21,0,505,506,3,
        78,39,0,506,77,1,0,0,0,507,512,3,80,40,0,508,509,7,4,0,0,509,511,
        3,80,40,0,510,508,1,0,0,0,511,514,1,0,0,0,512,510,1,0,0,0,512,513,
        1,0,0,0,513,79,1,0,0,0,514,512,1,0,0,0,515,516,7,5,0,0,516,523,3,
        80,40,0,517,518,5,52,0,0,518,523,3,80,40,0,519,520,5,41,0,0,520,
        523,3,80,40,0,521,523,3,82,41,0,522,515,1,0,0,0,522,517,1,0,0,0,
        522,519,1,0,0,0,522,521,1,0,0,0,523,81,1,0,0,0,524,527,3,84,42,0,
        525,527,3,88,44,0,526,524,1,0,0,0,526,525,1,0,0,0,527,558,1,0,0,
        0,528,529,5,66,0,0,529,534,5,74,0,0,530,531,5,62,0,0,531,532,3,4,
        2,0,532,533,5,63,0,0,533,535,1,0,0,0,534,530,1,0,0,0,534,535,1,0,
        0,0,535,541,1,0,0,0,536,538,5,58,0,0,537,539,3,90,45,0,538,537,1,
        0,0,0,538,539,1,0,0,0,539,540,1,0,0,0,540,542,5,59,0,0,541,536,1,
        0,0,0,541,542,1,0,0,0,542,557,1,0,0,0,543,544,5,62,0,0,544,545,3,
        78,39,0,545,546,5,63,0,0,546,557,1,0,0,0,547,548,5,34,0,0,548,554,
        5,74,0,0,549,551,5,58,0,0,550,552,3,90,45,0,551,550,1,0,0,0,551,
        552,1,0,0,0,552,553,1,0,0,0,553,555,5,59,0,0,554,549,1,0,0,0,554,
        555,1,0,0,0,555,557,1,0,0,0,556,528,1,0,0,0,556,543,1,0,0,0,556,
        547,1,0,0,0,557,560,1,0,0,0,558,556,1,0,0,0,558,559,1,0,0,0,559,
        83,1,0,0,0,560,558,1,0,0,0,561,562,5,27,0,0,562,563,3,2,1,0,563,
        565,5,58,0,0,564,566,3,90,45,0,565,564,1,0,0,0,565,566,1,0,0,0,566,
        567,1,0,0,0,567,568,5,59,0,0,568,588,1,0,0,0,569,570,7,6,0,0,570,
        571,5,62,0,0,571,572,3,0,0,0,572,573,5,63,0,0,573,575,5,58,0,0,574,
        576,3,90,45,0,575,574,1,0,0,0,575,576,1,0,0,0,576,577,1,0,0,0,577,
        578,5,59,0,0,578,588,1,0,0,0,579,588,3,92,46,0,580,588,3,86,43,0,
        581,588,5,74,0,0,582,588,5,10,0,0,583,584,5,58,0,0,584,585,3,78,
        39,0,585,586,5,59,0,0,586,588,1,0,0,0,587,561,1,0,0,0,587,569,1,
        0,0,0,587,579,1,0,0,0,587,580,1,0,0,0,587,581,1,0,0,0,587,582,1,
        0,0,0,587,583,1,0,0,0,588,85,1,0,0,0,589,591,5,60,0,0,590,592,3,
        90,45,0,591,590,1,0,0,0,591,592,1,0,0,0,592,593,1,0,0,0,593,594,
        5,61,0,0,594,87,1,0,0,0,595,596,7,7,0,0,596,598,5,58,0,0,597,599,
        3,90,45,0,598,597,1,0,0,0,598,599,1,0,0,0,599,600,1,0,0,0,600,601,
        5,59,0,0,601,89,1,0,0,0,602,607,3,78,39,0,603,604,5,67,0,0,604,606,
        3,78,39,0,605,603,1,0,0,0,606,609,1,0,0,0,607,605,1,0,0,0,607,608,
        1,0,0,0,608,91,1,0,0,0,609,607,1,0,0,0,610,611,7,8,0,0,611,93,1,
        0,0,0,73,105,110,113,120,126,133,140,144,150,155,165,170,175,179,
        181,185,191,197,201,207,218,224,228,232,237,246,252,265,275,284,
        289,298,304,314,317,327,352,354,367,377,379,385,394,407,424,430,
        442,446,450,457,464,468,477,486,488,497,501,512,522,526,534,538,
        541,551,554,556,558,565,575,587,591,598,607
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
                pass
            elif token in [20, 21, 22, 74]:
                self.enterOuterAlt(localctx, 2)
                self.state = 100
                self.baseType()
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==62:
                    self.state = 101
                    self.match(ChronoParser.LBRACK)
                    self.state = 102
                    self.typeList()
                    self.state = 103
                    self.match(ChronoParser.RBRACK)


                self.state = 110
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==41 or _la==52:
                    self.state = 107
                    _la = self._input.LA(1)
                    if not(_la==41 or _la==52):
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
            self.state = 126
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [74]:
                self.enterOuterAlt(localctx, 1)
                self.state = 115
                self.match(ChronoParser.IDENTIFIER)
                self.state = 120
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==66:
                    self.state = 116
                    self.match(ChronoParser.DOT)
                    self.state = 117
                    self.match(ChronoParser.IDENTIFIER)
                    self.state = 122
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 123
                self.match(ChronoParser.UNIQUE_KW)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 3)
                self.state = 124
                self.match(ChronoParser.SHARED_KW)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 4)
                self.state = 125
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
            self.state = 128
            self.templateArgument()
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==67:
                self.state = 129
                self.match(ChronoParser.COMMA)
                self.state = 130
                self.templateArgument()
                self.state = 135
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
            self.state = 136
            _la = self._input.LA(1)
            if not(_la==3 or _la==4):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 137
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==64:
                self.state = 138
                self.match(ChronoParser.COLON)
                self.state = 139
                localctx.typeName = self.typeSpecifier()


            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==65:
                self.state = 142
                self.match(ChronoParser.ASSIGN)
                self.state = 143
                self.expression()


            self.state = 146
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
            self.state = 150
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20, 21, 22, 62, 74]:
                self.enterOuterAlt(localctx, 1)
                self.state = 148
                self.typeSpecifier()
                pass
            elif token in [26, 68, 69, 70, 71, 72, 73, 75, 76]:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
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
            self.state = 153 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 152
                self.topLevelStatement()
                self.state = 155 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 537004230) != 0)):
                    break

            self.state = 157
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
            self.state = 165
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.importDirective()
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 160
                self.cppBlock()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 161
                self.classDefinition()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 4)
                self.state = 162
                self.structDefinition()
                pass
            elif token in [2, 11]:
                self.enterOuterAlt(localctx, 5)
                self.state = 163
                self.functionDefinition()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 6)
                self.state = 164
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
            self.state = 167
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
            self.state = 191
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 169
                    self.accessModifier()


                self.state = 172
                self.variableDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [11]:
                    self.state = 173
                    self.match(ChronoParser.STATIC)
                    self.state = 175
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==16:
                        self.state = 174
                        self.accessModifier()


                    pass
                elif token in [16]:
                    self.state = 177
                    self.accessModifier()
                    self.state = 179
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==11:
                        self.state = 178
                        self.match(ChronoParser.STATIC)


                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 183
                self.methodDefinition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 185
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 184
                    self.accessModifier()


                self.state = 187
                self.initDefinition()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 188
                self.methodDefinition()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 189
                self.deinitBlock()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 190
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
            self.state = 193
            self.match(ChronoParser.CLASS)
            self.state = 194
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==64:
                self.state = 195
                self.match(ChronoParser.COLON)
                self.state = 196
                localctx.base = self.match(ChronoParser.IDENTIFIER)


            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 199
                self.match(ChronoParser.IMPL)
                self.state = 200
                localctx.interfaces = self.typeList()


            self.state = 203
            self.match(ChronoParser.LBRACE)
            self.state = 207
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 536939292) != 0):
                self.state = 204
                self.classBodyStatement()
                self.state = 209
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 210
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
            self.state = 212
            self.match(ChronoParser.STRUCT)
            self.state = 213
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 214
            self.match(ChronoParser.LBRACE)
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 536937244) != 0):
                self.state = 215
                self.structBodyStatement()
                self.state = 220
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 221
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
            self.state = 237
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 224
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 223
                    self.accessModifier()


                self.state = 226
                self.variableDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 228
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 227
                    self.accessModifier()


                self.state = 230
                self.methodDefinition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 232
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 231
                    self.accessModifier()


                self.state = 234
                self.initDefinition()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 235
                self.deinitBlock()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 236
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
            self.state = 239
            self.match(ChronoParser.FUNC)
            self.state = 240
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 241
            self.match(ChronoParser.LPAREN)
            self.state = 242
            self.parameters()
            self.state = 243
            self.match(ChronoParser.RPAREN)
            self.state = 246
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 244
                self.match(ChronoParser.ARROW)
                self.state = 245
                localctx.returnType = self.typeSpecifier()


            self.state = 248
            self.match(ChronoParser.LBRACE)
            self.state = 252
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1483939926574683192) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & 511) != 0):
                self.state = 249
                self.statement()
                self.state = 254
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 255
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
            self.state = 257
            self.match(ChronoParser.INIT)
            self.state = 258
            self.match(ChronoParser.LPAREN)
            self.state = 259
            self.parameters()
            self.state = 260
            self.match(ChronoParser.RPAREN)
            self.state = 261
            self.match(ChronoParser.LBRACE)
            self.state = 265
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1483939926574683192) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & 511) != 0):
                self.state = 262
                self.statement()
                self.state = 267
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 268
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
            self.state = 270
            self.match(ChronoParser.DEINIT)
            self.state = 271
            self.match(ChronoParser.LBRACE)
            self.state = 275
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1483939926574683192) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & 511) != 0):
                self.state = 272
                self.statement()
                self.state = 277
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 278
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
            self.state = 280
            self.match(ChronoParser.IMPORT)
            self.state = 281
            localctx.path = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==56 or _la==75):
                localctx.path = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 284
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 282
                self.match(ChronoParser.AS)
                self.state = 283
                localctx.alias = self.match(ChronoParser.IDENTIFIER)


            self.state = 286
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
            self.state = 289
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 288
                self.match(ChronoParser.STATIC)


            self.state = 291
            self.match(ChronoParser.FUNC)
            self.state = 292
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 293
            self.match(ChronoParser.LPAREN)
            self.state = 294
            self.parameters()
            self.state = 295
            self.match(ChronoParser.RPAREN)
            self.state = 298
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 296
                self.match(ChronoParser.ARROW)
                self.state = 297
                localctx.returnType = self.typeSpecifier()


            self.state = 300
            self.match(ChronoParser.LBRACE)
            self.state = 304
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1483939926574683192) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & 511) != 0):
                self.state = 301
                self.statement()
                self.state = 306
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 307
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
            self.state = 317
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==74:
                self.state = 309
                self.parameter()
                self.state = 314
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==67:
                    self.state = 310
                    self.match(ChronoParser.COMMA)
                    self.state = 311
                    self.parameter()
                    self.state = 316
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
            self.state = 319
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 320
            self.match(ChronoParser.COLON)
            self.state = 321
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
            self.state = 323
            self.match(ChronoParser.AT_CPP)
            self.state = 327
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==81:
                self.state = 324
                self.match(ChronoParser.CPP_BODY)
                self.state = 329
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 330
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
            self.state = 332
            self.match(ChronoParser.RETURN)
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
            self.state = 336
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
            self.state = 338
            self.assignableExpression()
            self.state = 339
            self.assignmentOperator()
            self.state = 340
            self.expression()
            self.state = 341
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
            self.state = 343
            self.assignablePrimary()
            self.state = 354
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 34)) & ~0x3f) == 0 and ((1 << (_la - 34)) & 4563402753) != 0):
                self.state = 352
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [66]:
                    self.state = 344
                    self.match(ChronoParser.DOT)
                    self.state = 345
                    self.match(ChronoParser.IDENTIFIER)
                    pass
                elif token in [62]:
                    self.state = 346
                    self.match(ChronoParser.LBRACK)
                    self.state = 347
                    self.expression()
                    self.state = 348
                    self.match(ChronoParser.RBRACK)
                    pass
                elif token in [34]:
                    self.state = 350
                    self.match(ChronoParser.ARROW)
                    self.state = 351
                    self.match(ChronoParser.IDENTIFIER)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 356
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
            self.state = 367
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [74]:
                self.enterOuterAlt(localctx, 1)
                self.state = 357
                self.match(ChronoParser.IDENTIFIER)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 358
                self.match(ChronoParser.THIS)
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 3)
                self.state = 359
                self.match(ChronoParser.STAR)
                self.state = 360
                self.assignablePrimary()
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 4)
                self.state = 361
                self.match(ChronoParser.BIT_AND)
                self.state = 362
                self.assignablePrimary()
                pass
            elif token in [58]:
                self.enterOuterAlt(localctx, 5)
                self.state = 363
                self.match(ChronoParser.LPAREN)
                self.state = 364
                self.assignableExpression()
                self.state = 365
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
            self.state = 369
            self.match(ChronoParser.IF)
            self.state = 370
            self.match(ChronoParser.LPAREN)
            self.state = 371
            self.expression()
            self.state = 372
            self.match(ChronoParser.RPAREN)
            self.state = 373
            localctx.if_block = self.ifBlock()
            self.state = 379
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 374
                self.match(ChronoParser.ELSE)
                self.state = 377
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [12]:
                    self.state = 375
                    localctx.else_if = self.ifStatement()
                    pass
                elif token in [60]:
                    self.state = 376
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
            self.state = 381
            self.match(ChronoParser.LBRACE)
            self.state = 385
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1483939926574683192) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & 511) != 0):
                self.state = 382
                self.statement()
                self.state = 387
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 388
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
            self.state = 390
            self.match(ChronoParser.LBRACE)
            self.state = 394
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1483939926574683192) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & 511) != 0):
                self.state = 391
                self.statement()
                self.state = 396
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 397
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
            self.state = 399
            self.match(ChronoParser.WHILE)
            self.state = 400
            self.match(ChronoParser.LPAREN)
            self.state = 401
            self.expression()
            self.state = 402
            self.match(ChronoParser.RPAREN)
            self.state = 403
            self.match(ChronoParser.LBRACE)
            self.state = 407
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1483939926574683192) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & 511) != 0):
                self.state = 404
                self.statement()
                self.state = 409
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 410
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
            self.state = 424
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 412
                self.variableDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 413
                self.assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 414
                self.returnStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 415
                self.expression()
                self.state = 416
                self.match(ChronoParser.SEMIC_TOKEN)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 418
                self.cppBlock()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 419
                self.ifStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 420
                self.whileStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 421
                self.deleteStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 422
                self.forStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 423
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
            self.state = 426
            self.match(ChronoParser.LBRACE)
            self.state = 430
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1483939926574683192) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & 511) != 0):
                self.state = 427
                self.statement()
                self.state = 432
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 433
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
            self.state = 435
            self.match(ChronoParser.DELETE)
            self.state = 436
            self.expression()
            self.state = 437
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
            self.state = 439
            self.match(ChronoParser.FOR)
            self.state = 440
            self.match(ChronoParser.LPAREN)
            self.state = 442
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 292736174802338840) != 0) or _la==74:
                self.state = 441
                localctx.init = self.forInit()


            self.state = 444
            self.match(ChronoParser.SEMIC_TOKEN)
            self.state = 446
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1483939925769323520) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & 511) != 0):
                self.state = 445
                localctx.cond = self.expression()


            self.state = 448
            self.match(ChronoParser.SEMIC_TOKEN)
            self.state = 450
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1483939925769323520) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & 511) != 0):
                self.state = 449
                localctx.incr = self.forIncrement()


            self.state = 452
            self.match(ChronoParser.RPAREN)
            self.state = 453
            self.match(ChronoParser.LBRACE)
            self.state = 457
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1483939926574683192) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & 511) != 0):
                self.state = 454
                self.statement()
                self.state = 459
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 460
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
            self.state = 464
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 462
                self.variableDeclaration_no_semicolon()
                pass
            elif token in [10, 41, 52, 58, 74]:
                self.enterOuterAlt(localctx, 2)
                self.state = 463
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
            self.state = 468
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 466
                self.assignment_no_semicolon()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 467
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
            self.state = 470
            self.match(ChronoParser.FUNC)
            self.state = 471
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 472
            self.match(ChronoParser.LPAREN)
            self.state = 473
            self.parameters()
            self.state = 474
            self.match(ChronoParser.RPAREN)
            self.state = 477
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 475
                self.match(ChronoParser.ARROW)
                self.state = 476
                localctx.returnType = self.typeSpecifier()


            self.state = 479
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
            self.state = 481
            self.match(ChronoParser.INTERFACE)
            self.state = 482
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 483
            self.match(ChronoParser.LBRACE)
            self.state = 488
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2 or _la==29:
                self.state = 486
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [2]:
                    self.state = 484
                    self.methodSignature()
                    pass
                elif token in [29]:
                    self.state = 485
                    self.cppBlock()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 490
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 491
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
            self.state = 493
            _la = self._input.LA(1)
            if not(_la==3 or _la==4):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 494
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 497
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==64:
                self.state = 495
                self.match(ChronoParser.COLON)
                self.state = 496
                localctx.typeName = self.typeSpecifier()


            self.state = 501
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==65:
                self.state = 499
                self.match(ChronoParser.ASSIGN)
                self.state = 500
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
            self.state = 503
            self.assignableExpression()
            self.state = 504
            self.assignmentOperator()
            self.state = 505
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
            self.state = 507
            self.unaryExpression()
            self.state = 512
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 33231621184290816) != 0):
                self.state = 508
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 33231621184290816) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 509
                self.unaryExpression()
                self.state = 514
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
            self.state = 522
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [39, 40, 51, 55]:
                self.enterOuterAlt(localctx, 1)
                self.state = 515
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 38282246100090880) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 516
                self.unaryExpression()
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 2)
                self.state = 517
                self.match(ChronoParser.BIT_AND)
                self.state = 518
                self.unaryExpression()
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 3)
                self.state = 519
                self.match(ChronoParser.STAR)
                self.state = 520
                self.unaryExpression()
                pass
            elif token in [10, 23, 24, 25, 26, 27, 58, 60, 68, 69, 70, 71, 72, 73, 74, 75, 76]:
                self.enterOuterAlt(localctx, 4)
                self.state = 521
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
            self.state = 526
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
            if la_ == 1:
                self.state = 524
                self.primary()
                pass

            elif la_ == 2:
                self.state = 525
                self.functionCallExpression()
                pass


            self.state = 558
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 34)) & ~0x3f) == 0 and ((1 << (_la - 34)) & 4563402753) != 0):
                self.state = 556
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [66]:
                    self.state = 528
                    self.match(ChronoParser.DOT)
                    self.state = 529
                    self.match(ChronoParser.IDENTIFIER)
                    self.state = 534
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
                    if la_ == 1:
                        self.state = 530
                        self.match(ChronoParser.LBRACK)
                        self.state = 531
                        self.typeList()
                        self.state = 532
                        self.match(ChronoParser.RBRACK)


                    self.state = 541
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==58:
                        self.state = 536
                        self.match(ChronoParser.LPAREN)
                        self.state = 538
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1483939925769323520) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & 511) != 0):
                            self.state = 537
                            self.expressionList()


                        self.state = 540
                        self.match(ChronoParser.RPAREN)


                    pass
                elif token in [62]:
                    self.state = 543
                    self.match(ChronoParser.LBRACK)
                    self.state = 544
                    self.expression()
                    self.state = 545
                    self.match(ChronoParser.RBRACK)
                    pass
                elif token in [34]:
                    self.state = 547
                    self.match(ChronoParser.ARROW)
                    self.state = 548
                    self.match(ChronoParser.IDENTIFIER)
                    self.state = 554
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==58:
                        self.state = 549
                        self.match(ChronoParser.LPAREN)
                        self.state = 551
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1483939925769323520) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & 511) != 0):
                            self.state = 550
                            self.expressionList()


                        self.state = 553
                        self.match(ChronoParser.RPAREN)


                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 560
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
            self.state = 587
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 561
                self.match(ChronoParser.NEW)
                self.state = 562
                self.baseType()
                self.state = 563
                self.match(ChronoParser.LPAREN)
                self.state = 565
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1483939925769323520) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & 511) != 0):
                    self.state = 564
                    self.expressionList()


                self.state = 567
                self.match(ChronoParser.RPAREN)
                pass
            elif token in [23, 24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 569
                _la = self._input.LA(1)
                if not(_la==23 or _la==24):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 570
                self.match(ChronoParser.LBRACK)
                self.state = 571
                self.typeSpecifier()
                self.state = 572
                self.match(ChronoParser.RBRACK)
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
            elif token in [26, 68, 69, 70, 71, 72, 73, 75, 76]:
                self.enterOuterAlt(localctx, 3)
                self.state = 579
                self.literal()
                pass
            elif token in [60]:
                self.enterOuterAlt(localctx, 4)
                self.state = 580
                self.initializerList()
                pass
            elif token in [74]:
                self.enterOuterAlt(localctx, 5)
                self.state = 581
                self.match(ChronoParser.IDENTIFIER)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 6)
                self.state = 582
                self.match(ChronoParser.THIS)
                pass
            elif token in [58]:
                self.enterOuterAlt(localctx, 7)
                self.state = 583
                self.match(ChronoParser.LPAREN)
                self.state = 584
                self.expression()
                self.state = 585
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
            self.state = 589
            self.match(ChronoParser.LBRACE)
            self.state = 591
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1483939925769323520) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & 511) != 0):
                self.state = 590
                self.expressionList()


            self.state = 593
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
            self.state = 595
            localctx.funcName = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==25 or _la==74):
                localctx.funcName = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 596
            self.match(ChronoParser.LPAREN)
            self.state = 598
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1483939925769323520) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & 511) != 0):
                self.state = 597
                self.expressionList()


            self.state = 600
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
            self.state = 602
            self.expression()
            self.state = 607
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==67:
                self.state = 603
                self.match(ChronoParser.COMMA)
                self.state = 604
                self.expression()
                self.state = 609
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
            self.state = 610
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





