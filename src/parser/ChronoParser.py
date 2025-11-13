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
        4,1,90,667,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,1,0,1,0,1,0,1,0,1,0,1,0,1,0,5,0,106,8,0,
        10,0,12,0,109,9,0,1,0,1,0,1,0,1,0,1,0,3,0,116,8,0,1,0,5,0,119,8,
        0,10,0,12,0,122,9,0,1,0,1,0,3,0,126,8,0,1,0,1,0,1,0,1,0,1,0,1,0,
        3,0,134,8,0,1,0,5,0,137,8,0,10,0,12,0,140,9,0,3,0,142,8,0,1,1,1,
        1,1,1,5,1,147,8,1,10,1,12,1,150,9,1,1,1,1,1,1,1,3,1,155,8,1,1,2,
        1,2,1,2,5,2,160,8,2,10,2,12,2,163,9,2,1,3,1,3,1,3,1,3,3,3,169,8,
        3,1,3,1,3,3,3,173,8,3,1,3,1,3,1,4,1,4,3,4,179,8,4,1,5,4,5,182,8,
        5,11,5,12,5,183,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,196,
        8,6,1,7,1,7,1,8,3,8,201,8,8,1,8,1,8,1,8,3,8,206,8,8,1,8,1,8,3,8,
        210,8,8,3,8,212,8,8,1,8,1,8,3,8,216,8,8,1,8,1,8,1,8,1,8,3,8,222,
        8,8,1,9,1,9,1,9,1,9,3,9,228,8,9,1,9,1,9,3,9,232,8,9,1,9,1,9,5,9,
        236,8,9,10,9,12,9,239,9,9,1,9,1,9,1,10,1,10,1,10,1,10,5,10,247,8,
        10,10,10,12,10,250,9,10,1,10,1,10,1,11,3,11,255,8,11,1,11,1,11,3,
        11,259,8,11,1,11,1,11,3,11,263,8,11,1,11,1,11,1,11,3,11,268,8,11,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,277,8,12,1,12,1,12,5,12,
        281,8,12,10,12,12,12,284,9,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,
        1,13,5,13,294,8,13,10,13,12,13,297,9,13,1,13,1,13,1,14,1,14,1,14,
        5,14,304,8,14,10,14,12,14,307,9,14,1,14,1,14,1,15,1,15,1,15,1,15,
        3,15,315,8,15,1,16,1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,
        3,17,327,8,17,1,17,1,17,1,17,1,17,1,18,3,18,334,8,18,1,18,1,18,1,
        18,1,18,1,18,1,18,1,18,3,18,343,8,18,1,18,1,18,5,18,347,8,18,10,
        18,12,18,350,9,18,1,18,1,18,1,19,1,19,1,19,5,19,357,8,19,10,19,12,
        19,360,9,19,3,19,362,8,19,1,20,1,20,1,20,1,20,1,21,1,21,5,21,370,
        8,21,10,21,12,21,373,9,21,1,21,1,21,1,22,1,22,1,22,1,22,1,23,1,23,
        1,24,1,24,1,24,1,24,1,24,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,
        1,25,5,25,397,8,25,10,25,12,25,400,9,25,1,26,1,26,1,26,1,26,1,26,
        1,26,1,26,1,26,1,26,1,26,3,26,412,8,26,1,27,1,27,1,27,1,27,1,27,
        1,27,1,27,1,27,3,27,422,8,27,3,27,424,8,27,1,28,1,28,5,28,428,8,
        28,10,28,12,28,431,9,28,1,28,1,28,1,29,1,29,5,29,437,8,29,10,29,
        12,29,440,9,29,1,29,1,29,1,30,1,30,1,30,1,30,1,30,1,30,5,30,450,
        8,30,10,30,12,30,453,9,30,1,30,1,30,1,31,1,31,1,31,1,31,1,31,1,31,
        1,31,1,31,1,31,1,31,1,31,1,31,3,31,469,8,31,1,32,1,32,5,32,473,8,
        32,10,32,12,32,476,9,32,1,32,1,32,1,33,1,33,1,33,1,33,1,34,1,34,
        1,34,3,34,487,8,34,1,34,1,34,3,34,491,8,34,1,34,1,34,3,34,495,8,
        34,1,34,1,34,1,34,5,34,500,8,34,10,34,12,34,503,9,34,1,34,1,34,1,
        35,1,35,3,35,509,8,35,1,36,1,36,3,36,513,8,36,1,37,1,37,1,37,1,37,
        1,37,1,37,1,37,3,37,522,8,37,1,37,1,37,1,38,1,38,1,38,1,38,1,38,
        5,38,531,8,38,10,38,12,38,534,9,38,1,38,1,38,1,39,1,39,1,39,1,39,
        3,39,542,8,39,1,39,1,39,3,39,546,8,39,1,40,1,40,1,40,1,40,1,41,1,
        41,1,41,5,41,555,8,41,10,41,12,41,558,9,41,1,42,1,42,1,42,1,42,1,
        42,1,42,1,42,3,42,567,8,42,1,43,1,43,3,43,571,8,43,1,43,1,43,1,43,
        1,43,1,43,1,43,3,43,579,8,43,1,43,1,43,3,43,583,8,43,1,43,3,43,586,
        8,43,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,43,3,43,596,8,43,1,43,
        3,43,599,8,43,5,43,601,8,43,10,43,12,43,604,9,43,1,44,1,44,1,44,
        1,44,3,44,610,8,44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,3,44,
        620,8,44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,3,44,630,8,44,1,
        44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,3,44,642,8,44,1,
        45,1,45,3,45,646,8,45,1,45,1,45,1,46,1,46,1,46,3,46,653,8,46,1,46,
        1,46,1,47,1,47,1,47,5,47,660,8,47,10,47,12,47,663,9,47,1,48,1,48,
        1,48,0,0,49,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,
        38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,
        82,84,86,88,90,92,94,96,0,10,2,0,46,46,57,57,1,0,3,4,2,0,61,61,84,
        84,2,0,49,53,70,70,4,0,35,38,40,48,54,55,57,59,3,0,44,45,56,56,60,
        60,1,0,25,26,2,0,25,26,28,30,2,0,27,27,83,83,3,0,31,31,73,82,84,
        85,733,0,141,1,0,0,0,2,154,1,0,0,0,4,156,1,0,0,0,6,164,1,0,0,0,8,
        178,1,0,0,0,10,181,1,0,0,0,12,195,1,0,0,0,14,197,1,0,0,0,16,221,
        1,0,0,0,18,223,1,0,0,0,20,242,1,0,0,0,22,267,1,0,0,0,24,269,1,0,
        0,0,26,287,1,0,0,0,28,300,1,0,0,0,30,310,1,0,0,0,32,316,1,0,0,0,
        34,322,1,0,0,0,36,333,1,0,0,0,38,361,1,0,0,0,40,363,1,0,0,0,42,367,
        1,0,0,0,44,376,1,0,0,0,46,380,1,0,0,0,48,382,1,0,0,0,50,387,1,0,
        0,0,52,411,1,0,0,0,54,413,1,0,0,0,56,425,1,0,0,0,58,434,1,0,0,0,
        60,443,1,0,0,0,62,468,1,0,0,0,64,470,1,0,0,0,66,479,1,0,0,0,68,483,
        1,0,0,0,70,508,1,0,0,0,72,512,1,0,0,0,74,514,1,0,0,0,76,525,1,0,
        0,0,78,537,1,0,0,0,80,547,1,0,0,0,82,551,1,0,0,0,84,566,1,0,0,0,
        86,570,1,0,0,0,88,641,1,0,0,0,90,643,1,0,0,0,92,649,1,0,0,0,94,656,
        1,0,0,0,96,664,1,0,0,0,98,99,5,67,0,0,99,100,3,0,0,0,100,101,5,62,
        0,0,101,102,3,82,41,0,102,103,5,68,0,0,103,107,1,0,0,0,104,106,7,
        0,0,0,105,104,1,0,0,0,106,109,1,0,0,0,107,105,1,0,0,0,107,108,1,
        0,0,0,108,142,1,0,0,0,109,107,1,0,0,0,110,115,3,2,1,0,111,112,5,
        67,0,0,112,113,3,4,2,0,113,114,5,68,0,0,114,116,1,0,0,0,115,111,
        1,0,0,0,115,116,1,0,0,0,116,120,1,0,0,0,117,119,7,0,0,0,118,117,
        1,0,0,0,119,122,1,0,0,0,120,118,1,0,0,0,120,121,1,0,0,0,121,142,
        1,0,0,0,122,120,1,0,0,0,123,133,5,63,0,0,124,126,3,4,2,0,125,124,
        1,0,0,0,125,126,1,0,0,0,126,127,1,0,0,0,127,128,5,64,0,0,128,129,
        5,39,0,0,129,134,3,0,0,0,130,131,3,0,0,0,131,132,5,64,0,0,132,134,
        1,0,0,0,133,125,1,0,0,0,133,130,1,0,0,0,134,138,1,0,0,0,135,137,
        7,0,0,0,136,135,1,0,0,0,137,140,1,0,0,0,138,136,1,0,0,0,138,139,
        1,0,0,0,139,142,1,0,0,0,140,138,1,0,0,0,141,98,1,0,0,0,141,110,1,
        0,0,0,141,123,1,0,0,0,142,1,1,0,0,0,143,148,5,83,0,0,144,145,5,71,
        0,0,145,147,5,83,0,0,146,144,1,0,0,0,147,150,1,0,0,0,148,146,1,0,
        0,0,148,149,1,0,0,0,149,155,1,0,0,0,150,148,1,0,0,0,151,155,5,22,
        0,0,152,155,5,23,0,0,153,155,5,24,0,0,154,143,1,0,0,0,154,151,1,
        0,0,0,154,152,1,0,0,0,154,153,1,0,0,0,155,3,1,0,0,0,156,161,3,8,
        4,0,157,158,5,72,0,0,158,160,3,8,4,0,159,157,1,0,0,0,160,163,1,0,
        0,0,161,159,1,0,0,0,161,162,1,0,0,0,162,5,1,0,0,0,163,161,1,0,0,
        0,164,165,7,1,0,0,165,168,5,83,0,0,166,167,5,69,0,0,167,169,3,0,
        0,0,168,166,1,0,0,0,168,169,1,0,0,0,169,172,1,0,0,0,170,171,5,70,
        0,0,171,173,3,82,41,0,172,170,1,0,0,0,172,173,1,0,0,0,173,174,1,
        0,0,0,174,175,5,62,0,0,175,7,1,0,0,0,176,179,3,0,0,0,177,179,3,96,
        48,0,178,176,1,0,0,0,178,177,1,0,0,0,179,9,1,0,0,0,180,182,3,12,
        6,0,181,180,1,0,0,0,182,183,1,0,0,0,183,181,1,0,0,0,183,184,1,0,
        0,0,184,185,1,0,0,0,185,186,5,0,0,1,186,11,1,0,0,0,187,196,3,30,
        15,0,188,196,3,42,21,0,189,196,3,18,9,0,190,196,3,20,10,0,191,196,
        3,36,18,0,192,196,3,76,38,0,193,196,3,32,16,0,194,196,3,34,17,0,
        195,187,1,0,0,0,195,188,1,0,0,0,195,189,1,0,0,0,195,190,1,0,0,0,
        195,191,1,0,0,0,195,192,1,0,0,0,195,193,1,0,0,0,195,194,1,0,0,0,
        196,13,1,0,0,0,197,198,5,16,0,0,198,15,1,0,0,0,199,201,3,14,7,0,
        200,199,1,0,0,0,200,201,1,0,0,0,201,202,1,0,0,0,202,222,3,6,3,0,
        203,205,5,11,0,0,204,206,3,14,7,0,205,204,1,0,0,0,205,206,1,0,0,
        0,206,212,1,0,0,0,207,209,3,14,7,0,208,210,5,11,0,0,209,208,1,0,
        0,0,209,210,1,0,0,0,210,212,1,0,0,0,211,203,1,0,0,0,211,207,1,0,
        0,0,212,213,1,0,0,0,213,222,3,24,12,0,214,216,3,14,7,0,215,214,1,
        0,0,0,215,216,1,0,0,0,216,217,1,0,0,0,217,222,3,26,13,0,218,222,
        3,24,12,0,219,222,3,28,14,0,220,222,3,42,21,0,221,200,1,0,0,0,221,
        211,1,0,0,0,221,215,1,0,0,0,221,218,1,0,0,0,221,219,1,0,0,0,221,
        220,1,0,0,0,222,17,1,0,0,0,223,224,5,6,0,0,224,227,5,83,0,0,225,
        226,5,69,0,0,226,228,5,83,0,0,227,225,1,0,0,0,227,228,1,0,0,0,228,
        231,1,0,0,0,229,230,5,18,0,0,230,232,3,4,2,0,231,229,1,0,0,0,231,
        232,1,0,0,0,232,233,1,0,0,0,233,237,5,65,0,0,234,236,3,16,8,0,235,
        234,1,0,0,0,236,239,1,0,0,0,237,235,1,0,0,0,237,238,1,0,0,0,238,
        240,1,0,0,0,239,237,1,0,0,0,240,241,5,66,0,0,241,19,1,0,0,0,242,
        243,5,7,0,0,243,244,5,83,0,0,244,248,5,65,0,0,245,247,3,22,11,0,
        246,245,1,0,0,0,247,250,1,0,0,0,248,246,1,0,0,0,248,249,1,0,0,0,
        249,251,1,0,0,0,250,248,1,0,0,0,251,252,5,66,0,0,252,21,1,0,0,0,
        253,255,3,14,7,0,254,253,1,0,0,0,254,255,1,0,0,0,255,256,1,0,0,0,
        256,268,3,6,3,0,257,259,3,14,7,0,258,257,1,0,0,0,258,259,1,0,0,0,
        259,260,1,0,0,0,260,268,3,24,12,0,261,263,3,14,7,0,262,261,1,0,0,
        0,262,263,1,0,0,0,263,264,1,0,0,0,264,268,3,26,13,0,265,268,3,28,
        14,0,266,268,3,42,21,0,267,254,1,0,0,0,267,258,1,0,0,0,267,262,1,
        0,0,0,267,265,1,0,0,0,267,266,1,0,0,0,268,23,1,0,0,0,269,270,5,2,
        0,0,270,271,5,83,0,0,271,272,5,63,0,0,272,273,3,38,19,0,273,276,
        5,64,0,0,274,275,5,39,0,0,275,277,3,0,0,0,276,274,1,0,0,0,276,277,
        1,0,0,0,277,278,1,0,0,0,278,282,5,65,0,0,279,281,3,62,31,0,280,279,
        1,0,0,0,281,284,1,0,0,0,282,280,1,0,0,0,282,283,1,0,0,0,283,285,
        1,0,0,0,284,282,1,0,0,0,285,286,5,66,0,0,286,25,1,0,0,0,287,288,
        5,8,0,0,288,289,5,63,0,0,289,290,3,38,19,0,290,291,5,64,0,0,291,
        295,5,65,0,0,292,294,3,62,31,0,293,292,1,0,0,0,294,297,1,0,0,0,295,
        293,1,0,0,0,295,296,1,0,0,0,296,298,1,0,0,0,297,295,1,0,0,0,298,
        299,5,66,0,0,299,27,1,0,0,0,300,301,5,9,0,0,301,305,5,65,0,0,302,
        304,3,62,31,0,303,302,1,0,0,0,304,307,1,0,0,0,305,303,1,0,0,0,305,
        306,1,0,0,0,306,308,1,0,0,0,307,305,1,0,0,0,308,309,5,66,0,0,309,
        29,1,0,0,0,310,311,5,1,0,0,311,314,7,2,0,0,312,313,5,19,0,0,313,
        315,5,83,0,0,314,312,1,0,0,0,314,315,1,0,0,0,315,31,1,0,0,0,316,
        317,5,20,0,0,317,318,5,83,0,0,318,319,5,70,0,0,319,320,3,0,0,0,320,
        321,5,62,0,0,321,33,1,0,0,0,322,323,5,21,0,0,323,326,5,83,0,0,324,
        325,5,69,0,0,325,327,3,0,0,0,326,324,1,0,0,0,326,327,1,0,0,0,327,
        328,1,0,0,0,328,329,5,70,0,0,329,330,5,84,0,0,330,331,5,62,0,0,331,
        35,1,0,0,0,332,334,5,11,0,0,333,332,1,0,0,0,333,334,1,0,0,0,334,
        335,1,0,0,0,335,336,5,2,0,0,336,337,5,83,0,0,337,338,5,63,0,0,338,
        339,3,38,19,0,339,342,5,64,0,0,340,341,5,39,0,0,341,343,3,0,0,0,
        342,340,1,0,0,0,342,343,1,0,0,0,343,344,1,0,0,0,344,348,5,65,0,0,
        345,347,3,62,31,0,346,345,1,0,0,0,347,350,1,0,0,0,348,346,1,0,0,
        0,348,349,1,0,0,0,349,351,1,0,0,0,350,348,1,0,0,0,351,352,5,66,0,
        0,352,37,1,0,0,0,353,358,3,40,20,0,354,355,5,72,0,0,355,357,3,40,
        20,0,356,354,1,0,0,0,357,360,1,0,0,0,358,356,1,0,0,0,358,359,1,0,
        0,0,359,362,1,0,0,0,360,358,1,0,0,0,361,353,1,0,0,0,361,362,1,0,
        0,0,362,39,1,0,0,0,363,364,5,83,0,0,364,365,5,69,0,0,365,366,3,0,
        0,0,366,41,1,0,0,0,367,371,5,34,0,0,368,370,5,90,0,0,369,368,1,0,
        0,0,370,373,1,0,0,0,371,369,1,0,0,0,371,372,1,0,0,0,372,374,1,0,
        0,0,373,371,1,0,0,0,374,375,5,89,0,0,375,43,1,0,0,0,376,377,5,5,
        0,0,377,378,3,82,41,0,378,379,5,62,0,0,379,45,1,0,0,0,380,381,7,
        3,0,0,381,47,1,0,0,0,382,383,3,50,25,0,383,384,3,46,23,0,384,385,
        3,82,41,0,385,386,5,62,0,0,386,49,1,0,0,0,387,398,3,52,26,0,388,
        389,5,71,0,0,389,397,5,83,0,0,390,391,5,67,0,0,391,392,3,82,41,0,
        392,393,5,68,0,0,393,397,1,0,0,0,394,395,5,39,0,0,395,397,5,83,0,
        0,396,388,1,0,0,0,396,390,1,0,0,0,396,394,1,0,0,0,397,400,1,0,0,
        0,398,396,1,0,0,0,398,399,1,0,0,0,399,51,1,0,0,0,400,398,1,0,0,0,
        401,412,5,83,0,0,402,412,5,10,0,0,403,404,5,46,0,0,404,412,3,52,
        26,0,405,406,5,57,0,0,406,412,3,52,26,0,407,408,5,63,0,0,408,409,
        3,50,25,0,409,410,5,64,0,0,410,412,1,0,0,0,411,401,1,0,0,0,411,402,
        1,0,0,0,411,403,1,0,0,0,411,405,1,0,0,0,411,407,1,0,0,0,412,53,1,
        0,0,0,413,414,5,12,0,0,414,415,5,63,0,0,415,416,3,82,41,0,416,417,
        5,64,0,0,417,423,3,56,28,0,418,421,5,13,0,0,419,422,3,54,27,0,420,
        422,3,58,29,0,421,419,1,0,0,0,421,420,1,0,0,0,422,424,1,0,0,0,423,
        418,1,0,0,0,423,424,1,0,0,0,424,55,1,0,0,0,425,429,5,65,0,0,426,
        428,3,62,31,0,427,426,1,0,0,0,428,431,1,0,0,0,429,427,1,0,0,0,429,
        430,1,0,0,0,430,432,1,0,0,0,431,429,1,0,0,0,432,433,5,66,0,0,433,
        57,1,0,0,0,434,438,5,65,0,0,435,437,3,62,31,0,436,435,1,0,0,0,437,
        440,1,0,0,0,438,436,1,0,0,0,438,439,1,0,0,0,439,441,1,0,0,0,440,
        438,1,0,0,0,441,442,5,66,0,0,442,59,1,0,0,0,443,444,5,14,0,0,444,
        445,5,63,0,0,445,446,3,82,41,0,446,447,5,64,0,0,447,451,5,65,0,0,
        448,450,3,62,31,0,449,448,1,0,0,0,450,453,1,0,0,0,451,449,1,0,0,
        0,451,452,1,0,0,0,452,454,1,0,0,0,453,451,1,0,0,0,454,455,5,66,0,
        0,455,61,1,0,0,0,456,469,3,6,3,0,457,469,3,48,24,0,458,469,3,44,
        22,0,459,460,3,82,41,0,460,461,5,62,0,0,461,469,1,0,0,0,462,469,
        3,42,21,0,463,469,3,54,27,0,464,469,3,60,30,0,465,469,3,66,33,0,
        466,469,3,68,34,0,467,469,3,64,32,0,468,456,1,0,0,0,468,457,1,0,
        0,0,468,458,1,0,0,0,468,459,1,0,0,0,468,462,1,0,0,0,468,463,1,0,
        0,0,468,464,1,0,0,0,468,465,1,0,0,0,468,466,1,0,0,0,468,467,1,0,
        0,0,469,63,1,0,0,0,470,474,5,65,0,0,471,473,3,62,31,0,472,471,1,
        0,0,0,473,476,1,0,0,0,474,472,1,0,0,0,474,475,1,0,0,0,475,477,1,
        0,0,0,476,474,1,0,0,0,477,478,5,66,0,0,478,65,1,0,0,0,479,480,5,
        33,0,0,480,481,3,82,41,0,481,482,5,62,0,0,482,67,1,0,0,0,483,484,
        5,15,0,0,484,486,5,63,0,0,485,487,3,70,35,0,486,485,1,0,0,0,486,
        487,1,0,0,0,487,488,1,0,0,0,488,490,5,62,0,0,489,491,3,82,41,0,490,
        489,1,0,0,0,490,491,1,0,0,0,491,492,1,0,0,0,492,494,5,62,0,0,493,
        495,3,72,36,0,494,493,1,0,0,0,494,495,1,0,0,0,495,496,1,0,0,0,496,
        497,5,64,0,0,497,501,5,65,0,0,498,500,3,62,31,0,499,498,1,0,0,0,
        500,503,1,0,0,0,501,499,1,0,0,0,501,502,1,0,0,0,502,504,1,0,0,0,
        503,501,1,0,0,0,504,505,5,66,0,0,505,69,1,0,0,0,506,509,3,78,39,
        0,507,509,3,80,40,0,508,506,1,0,0,0,508,507,1,0,0,0,509,71,1,0,0,
        0,510,513,3,80,40,0,511,513,3,82,41,0,512,510,1,0,0,0,512,511,1,
        0,0,0,513,73,1,0,0,0,514,515,5,2,0,0,515,516,5,83,0,0,516,517,5,
        63,0,0,517,518,3,38,19,0,518,521,5,64,0,0,519,520,5,39,0,0,520,522,
        3,0,0,0,521,519,1,0,0,0,521,522,1,0,0,0,522,523,1,0,0,0,523,524,
        5,62,0,0,524,75,1,0,0,0,525,526,5,17,0,0,526,527,5,83,0,0,527,532,
        5,65,0,0,528,531,3,74,37,0,529,531,3,42,21,0,530,528,1,0,0,0,530,
        529,1,0,0,0,531,534,1,0,0,0,532,530,1,0,0,0,532,533,1,0,0,0,533,
        535,1,0,0,0,534,532,1,0,0,0,535,536,5,66,0,0,536,77,1,0,0,0,537,
        538,7,1,0,0,538,541,5,83,0,0,539,540,5,69,0,0,540,542,3,0,0,0,541,
        539,1,0,0,0,541,542,1,0,0,0,542,545,1,0,0,0,543,544,5,70,0,0,544,
        546,3,82,41,0,545,543,1,0,0,0,545,546,1,0,0,0,546,79,1,0,0,0,547,
        548,3,50,25,0,548,549,3,46,23,0,549,550,3,82,41,0,550,81,1,0,0,0,
        551,556,3,84,42,0,552,553,7,4,0,0,553,555,3,84,42,0,554,552,1,0,
        0,0,555,558,1,0,0,0,556,554,1,0,0,0,556,557,1,0,0,0,557,83,1,0,0,
        0,558,556,1,0,0,0,559,560,7,5,0,0,560,567,3,84,42,0,561,562,5,57,
        0,0,562,567,3,84,42,0,563,564,5,46,0,0,564,567,3,84,42,0,565,567,
        3,86,43,0,566,559,1,0,0,0,566,561,1,0,0,0,566,563,1,0,0,0,566,565,
        1,0,0,0,567,85,1,0,0,0,568,571,3,88,44,0,569,571,3,92,46,0,570,568,
        1,0,0,0,570,569,1,0,0,0,571,602,1,0,0,0,572,573,5,71,0,0,573,578,
        5,83,0,0,574,575,5,67,0,0,575,576,3,4,2,0,576,577,5,68,0,0,577,579,
        1,0,0,0,578,574,1,0,0,0,578,579,1,0,0,0,579,585,1,0,0,0,580,582,
        5,63,0,0,581,583,3,94,47,0,582,581,1,0,0,0,582,583,1,0,0,0,583,584,
        1,0,0,0,584,586,5,64,0,0,585,580,1,0,0,0,585,586,1,0,0,0,586,601,
        1,0,0,0,587,588,5,67,0,0,588,589,3,82,41,0,589,590,5,68,0,0,590,
        601,1,0,0,0,591,592,5,39,0,0,592,598,5,83,0,0,593,595,5,63,0,0,594,
        596,3,94,47,0,595,594,1,0,0,0,595,596,1,0,0,0,596,597,1,0,0,0,597,
        599,5,64,0,0,598,593,1,0,0,0,598,599,1,0,0,0,599,601,1,0,0,0,600,
        572,1,0,0,0,600,587,1,0,0,0,600,591,1,0,0,0,601,604,1,0,0,0,602,
        600,1,0,0,0,602,603,1,0,0,0,603,87,1,0,0,0,604,602,1,0,0,0,605,606,
        5,32,0,0,606,607,3,2,1,0,607,609,5,63,0,0,608,610,3,94,47,0,609,
        608,1,0,0,0,609,610,1,0,0,0,610,611,1,0,0,0,611,612,5,64,0,0,612,
        642,1,0,0,0,613,614,7,6,0,0,614,615,5,67,0,0,615,616,3,0,0,0,616,
        617,5,68,0,0,617,619,5,63,0,0,618,620,3,94,47,0,619,618,1,0,0,0,
        619,620,1,0,0,0,620,621,1,0,0,0,621,622,5,64,0,0,622,642,1,0,0,0,
        623,624,7,7,0,0,624,625,5,67,0,0,625,626,3,0,0,0,626,627,5,68,0,
        0,627,629,5,63,0,0,628,630,3,94,47,0,629,628,1,0,0,0,629,630,1,0,
        0,0,630,631,1,0,0,0,631,632,5,64,0,0,632,642,1,0,0,0,633,642,3,96,
        48,0,634,642,3,90,45,0,635,642,5,83,0,0,636,642,5,10,0,0,637,638,
        5,63,0,0,638,639,3,82,41,0,639,640,5,64,0,0,640,642,1,0,0,0,641,
        605,1,0,0,0,641,613,1,0,0,0,641,623,1,0,0,0,641,633,1,0,0,0,641,
        634,1,0,0,0,641,635,1,0,0,0,641,636,1,0,0,0,641,637,1,0,0,0,642,
        89,1,0,0,0,643,645,5,65,0,0,644,646,3,94,47,0,645,644,1,0,0,0,645,
        646,1,0,0,0,646,647,1,0,0,0,647,648,5,66,0,0,648,91,1,0,0,0,649,
        650,7,8,0,0,650,652,5,63,0,0,651,653,3,94,47,0,652,651,1,0,0,0,652,
        653,1,0,0,0,653,654,1,0,0,0,654,655,5,64,0,0,655,93,1,0,0,0,656,
        661,3,82,41,0,657,658,5,72,0,0,658,660,3,82,41,0,659,657,1,0,0,0,
        660,663,1,0,0,0,661,659,1,0,0,0,661,662,1,0,0,0,662,95,1,0,0,0,663,
        661,1,0,0,0,664,665,7,9,0,0,665,97,1,0,0,0,79,107,115,120,125,133,
        138,141,148,154,161,168,172,178,183,195,200,205,209,211,215,221,
        227,231,237,248,254,258,262,267,276,282,295,305,314,326,333,342,
        348,358,361,371,396,398,411,421,423,429,438,451,468,474,486,490,
        494,501,508,512,521,530,532,541,545,556,566,570,578,582,585,595,
        598,600,602,609,619,629,641,645,652,661
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
                     "'using'", "'typemap'", "'unique'", "'shared'", "'weak'", 
                     "'@make'", "'@make_shared'", "'@move'", "'static_cast'", 
                     "'reinterpret_cast'", "'const_cast'", "<INVALID>", 
                     "'new'", "'delete'", "'@cpp'", "'=='", "'!='", "'<='", 
                     "'>='", "'->'", "'&&'", "'||'", "'<<'", "'>>'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'+='", "'-='", "'*='", 
                     "'/='", "'%='", "'<'", "'>'", "'!'", "'&'", "'|'", 
                     "'^'", "'~'", "<INVALID>", "';'", "'('", "')'", "'{'", 
                     "'}'", "'['", "']'", "':'", "'='", "'.'", "','", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'@end'" ]

    symbolicNames = [ "<INVALID>", "IMPORT", "FUNC", "VAR", "CONST", "RETURN", 
                      "CLASS", "STRUCT", "INIT", "DEINIT", "THIS", "STATIC", 
                      "IF", "ELSE", "WHILE", "FOR", "PUBLIC", "INTERFACE", 
                      "IMPL", "AS", "USING", "TYPEMAP", "UNIQUE_KW", "SHARED_KW", 
                      "WEAK_KW", "AT_MAKE_UNIQUE", "AT_MAKE_SHARED", "AT_MOVE", 
                      "STATIC_CAST", "REINTERPRET_CAST", "CONST_CAST", "BOOL_LITERAL", 
                      "NEW", "DELETE", "AT_CPP", "EQ", "NEQ", "LTE", "GTE", 
                      "ARROW", "AND_OP", "OR_OP", "LSHIFT", "RSHIFT", "PLUS", 
                      "MINUS", "STAR", "SLASH", "MODULO", "PLUS_ASSIGN", 
                      "MINUS_ASSIGN", "STAR_ASSIGN", "SLASH_ASSIGN", "MOD_ASSIGN", 
                      "LT", "GT", "NOT_OP", "BIT_AND", "BIT_OR", "BIT_XOR", 
                      "BIT_NOT", "INCLUDE_PATH", "SEMIC_TOKEN", "LPAREN", 
                      "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", 
                      "COLON", "ASSIGN", "DOT", "COMMA", "HEX_LITERAL", 
                      "BINARY_LITERAL", "OCTAL_LITERAL", "FLOAT_LITERAL", 
                      "DECIMAL_LITERAL", "BYTE_LITERAL", "U8_STRING_LITERAL", 
                      "U_STRING_LITERAL", "U_STRING_LITERAL_CAP", "L_STRING_LITERAL_CAP", 
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
    RULE_usingAlias = 16
    RULE_typemapDefinition = 17
    RULE_functionDefinition = 18
    RULE_parameters = 19
    RULE_parameter = 20
    RULE_cppBlock = 21
    RULE_returnStatement = 22
    RULE_assignmentOperator = 23
    RULE_assignment = 24
    RULE_assignableExpression = 25
    RULE_assignablePrimary = 26
    RULE_ifStatement = 27
    RULE_ifBlock = 28
    RULE_elseBlock = 29
    RULE_whileStatement = 30
    RULE_statement = 31
    RULE_blockStatement = 32
    RULE_deleteStatement = 33
    RULE_forStatement = 34
    RULE_forInit = 35
    RULE_forIncrement = 36
    RULE_methodSignature = 37
    RULE_interfaceDefinition = 38
    RULE_variableDeclaration_no_semicolon = 39
    RULE_assignment_no_semicolon = 40
    RULE_expression = 41
    RULE_unaryExpression = 42
    RULE_simpleExpression = 43
    RULE_primary = 44
    RULE_initializerList = 45
    RULE_functionCallExpression = 46
    RULE_expressionList = 47
    RULE_literal = 48

    ruleNames =  [ "typeSpecifier", "baseType", "typeList", "variableDeclaration", 
                   "templateArgument", "program", "topLevelStatement", "accessModifier", 
                   "classBodyStatement", "classDefinition", "structDefinition", 
                   "structBodyStatement", "methodDefinition", "initDefinition", 
                   "deinitBlock", "importDirective", "usingAlias", "typemapDefinition", 
                   "functionDefinition", "parameters", "parameter", "cppBlock", 
                   "returnStatement", "assignmentOperator", "assignment", 
                   "assignableExpression", "assignablePrimary", "ifStatement", 
                   "ifBlock", "elseBlock", "whileStatement", "statement", 
                   "blockStatement", "deleteStatement", "forStatement", 
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
    USING=20
    TYPEMAP=21
    UNIQUE_KW=22
    SHARED_KW=23
    WEAK_KW=24
    AT_MAKE_UNIQUE=25
    AT_MAKE_SHARED=26
    AT_MOVE=27
    STATIC_CAST=28
    REINTERPRET_CAST=29
    CONST_CAST=30
    BOOL_LITERAL=31
    NEW=32
    DELETE=33
    AT_CPP=34
    EQ=35
    NEQ=36
    LTE=37
    GTE=38
    ARROW=39
    AND_OP=40
    OR_OP=41
    LSHIFT=42
    RSHIFT=43
    PLUS=44
    MINUS=45
    STAR=46
    SLASH=47
    MODULO=48
    PLUS_ASSIGN=49
    MINUS_ASSIGN=50
    STAR_ASSIGN=51
    SLASH_ASSIGN=52
    MOD_ASSIGN=53
    LT=54
    GT=55
    NOT_OP=56
    BIT_AND=57
    BIT_OR=58
    BIT_XOR=59
    BIT_NOT=60
    INCLUDE_PATH=61
    SEMIC_TOKEN=62
    LPAREN=63
    RPAREN=64
    LBRACE=65
    RBRACE=66
    LBRACK=67
    RBRACK=68
    COLON=69
    ASSIGN=70
    DOT=71
    COMMA=72
    HEX_LITERAL=73
    BINARY_LITERAL=74
    OCTAL_LITERAL=75
    FLOAT_LITERAL=76
    DECIMAL_LITERAL=77
    BYTE_LITERAL=78
    U8_STRING_LITERAL=79
    U_STRING_LITERAL=80
    U_STRING_LITERAL_CAP=81
    L_STRING_LITERAL_CAP=82
    IDENTIFIER=83
    STRING_LITERAL=84
    CHAR_LITERAL=85
    LINE_COMMENT=86
    WHITESPACE=87
    NEWLINE=88
    AT_END=89
    CPP_BODY=90

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
            self.state = 141
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [67]:
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                self.match(ChronoParser.LBRACK)
                self.state = 99
                self.typeSpecifier()
                self.state = 100
                self.match(ChronoParser.SEMIC_TOKEN)
                self.state = 101
                self.expression()
                self.state = 102
                self.match(ChronoParser.RBRACK)
                self.state = 107
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 104
                        _la = self._input.LA(1)
                        if not(_la==46 or _la==57):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume() 
                    self.state = 109
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

                pass
            elif token in [22, 23, 24, 83]:
                self.enterOuterAlt(localctx, 2)
                self.state = 110
                self.baseType()
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==67:
                    self.state = 111
                    self.match(ChronoParser.LBRACK)
                    self.state = 112
                    self.typeList()
                    self.state = 113
                    self.match(ChronoParser.RBRACK)


                self.state = 120
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 117
                        _la = self._input.LA(1)
                        if not(_la==46 or _la==57):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume() 
                    self.state = 122
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                pass
            elif token in [63]:
                self.enterOuterAlt(localctx, 3)
                self.state = 123
                self.match(ChronoParser.LPAREN)
                self.state = 133
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 125
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if ((((_la - 22)) & ~0x3f) == 0 and ((1 << (_la - 22)) & -2214416418340345) != 0):
                        self.state = 124
                        localctx.params = self.typeList()


                    self.state = 127
                    self.match(ChronoParser.RPAREN)
                    self.state = 128
                    self.match(ChronoParser.ARROW)
                    self.state = 129
                    localctx.returnType = self.typeSpecifier()
                    pass

                elif la_ == 2:
                    self.state = 130
                    localctx.nested = self.typeSpecifier()
                    self.state = 131
                    self.match(ChronoParser.RPAREN)
                    pass


                self.state = 138
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 135
                        _la = self._input.LA(1)
                        if not(_la==46 or _la==57):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume() 
                    self.state = 140
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
            self.state = 154
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [83]:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self.match(ChronoParser.IDENTIFIER)
                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==71:
                    self.state = 144
                    self.match(ChronoParser.DOT)
                    self.state = 145
                    self.match(ChronoParser.IDENTIFIER)
                    self.state = 150
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 151
                self.match(ChronoParser.UNIQUE_KW)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 3)
                self.state = 152
                self.match(ChronoParser.SHARED_KW)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 4)
                self.state = 153
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
            self.state = 156
            self.templateArgument()
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==72:
                self.state = 157
                self.match(ChronoParser.COMMA)
                self.state = 158
                self.templateArgument()
                self.state = 163
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
            self.state = 164
            _la = self._input.LA(1)
            if not(_la==3 or _la==4):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 165
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 168
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==69:
                self.state = 166
                self.match(ChronoParser.COLON)
                self.state = 167
                localctx.typeName = self.typeSpecifier()


            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==70:
                self.state = 170
                self.match(ChronoParser.ASSIGN)
                self.state = 171
                self.expression()


            self.state = 174
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
            self.state = 178
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22, 23, 24, 63, 67, 83]:
                self.enterOuterAlt(localctx, 1)
                self.state = 176
                self.typeSpecifier()
                pass
            elif token in [31, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 84, 85]:
                self.enterOuterAlt(localctx, 2)
                self.state = 177
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
            self.state = 181 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 180
                self.topLevelStatement()
                self.state = 183 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 17183148230) != 0)):
                    break

            self.state = 185
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


        def usingAlias(self):
            return self.getTypedRuleContext(ChronoParser.UsingAliasContext,0)


        def typemapDefinition(self):
            return self.getTypedRuleContext(ChronoParser.TypemapDefinitionContext,0)


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
            self.state = 195
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self.importDirective()
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 188
                self.cppBlock()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 189
                self.classDefinition()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 4)
                self.state = 190
                self.structDefinition()
                pass
            elif token in [2, 11]:
                self.enterOuterAlt(localctx, 5)
                self.state = 191
                self.functionDefinition()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 6)
                self.state = 192
                self.interfaceDefinition()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 7)
                self.state = 193
                self.usingAlias()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 8)
                self.state = 194
                self.typemapDefinition()
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
            self.state = 197
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
            self.state = 221
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 199
                    self.accessModifier()


                self.state = 202
                self.variableDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 211
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [11]:
                    self.state = 203
                    self.match(ChronoParser.STATIC)
                    self.state = 205
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==16:
                        self.state = 204
                        self.accessModifier()


                    pass
                elif token in [16]:
                    self.state = 207
                    self.accessModifier()
                    self.state = 209
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==11:
                        self.state = 208
                        self.match(ChronoParser.STATIC)


                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 213
                self.methodDefinition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 215
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 214
                    self.accessModifier()


                self.state = 217
                self.initDefinition()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 218
                self.methodDefinition()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 219
                self.deinitBlock()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 220
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
            self.state = 223
            self.match(ChronoParser.CLASS)
            self.state = 224
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 227
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==69:
                self.state = 225
                self.match(ChronoParser.COLON)
                self.state = 226
                localctx.base = self.match(ChronoParser.IDENTIFIER)


            self.state = 231
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 229
                self.match(ChronoParser.IMPL)
                self.state = 230
                localctx.interfaces = self.typeList()


            self.state = 233
            self.match(ChronoParser.LBRACE)
            self.state = 237
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 17179937564) != 0):
                self.state = 234
                self.classBodyStatement()
                self.state = 239
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 240
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
            self.state = 242
            self.match(ChronoParser.STRUCT)
            self.state = 243
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 244
            self.match(ChronoParser.LBRACE)
            self.state = 248
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 17179935516) != 0):
                self.state = 245
                self.structBodyStatement()
                self.state = 250
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 251
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
            self.state = 267
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 254
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 253
                    self.accessModifier()


                self.state = 256
                self.variableDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 258
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 257
                    self.accessModifier()


                self.state = 260
                self.methodDefinition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 262
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 261
                    self.accessModifier()


                self.state = 264
                self.initDefinition()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 265
                self.deinitBlock()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 266
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
            self.state = 269
            self.match(ChronoParser.FUNC)
            self.state = 270
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 271
            self.match(ChronoParser.LPAREN)
            self.state = 272
            self.parameters()
            self.state = 273
            self.match(ChronoParser.RPAREN)
            self.state = 276
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 274
                self.match(ChronoParser.ARROW)
                self.state = 275
                localctx.returnType = self.typeSpecifier()


            self.state = 278
            self.match(ChronoParser.LBRACE)
            self.state = 282
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -7854154570505595848) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & 2096897) != 0):
                self.state = 279
                self.statement()
                self.state = 284
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 285
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
            self.state = 287
            self.match(ChronoParser.INIT)
            self.state = 288
            self.match(ChronoParser.LPAREN)
            self.state = 289
            self.parameters()
            self.state = 290
            self.match(ChronoParser.RPAREN)
            self.state = 291
            self.match(ChronoParser.LBRACE)
            self.state = 295
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -7854154570505595848) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & 2096897) != 0):
                self.state = 292
                self.statement()
                self.state = 297
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 298
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
            self.state = 300
            self.match(ChronoParser.DEINIT)
            self.state = 301
            self.match(ChronoParser.LBRACE)
            self.state = 305
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -7854154570505595848) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & 2096897) != 0):
                self.state = 302
                self.statement()
                self.state = 307
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 308
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
            self.state = 310
            self.match(ChronoParser.IMPORT)
            self.state = 311
            localctx.path = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==61 or _la==84):
                localctx.path = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 314
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 312
                self.match(ChronoParser.AS)
                self.state = 313
                localctx.alias = self.match(ChronoParser.IDENTIFIER)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UsingAliasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token
            self.typeName = None # TypeSpecifierContext

        def USING(self):
            return self.getToken(ChronoParser.USING, 0)

        def ASSIGN(self):
            return self.getToken(ChronoParser.ASSIGN, 0)

        def SEMIC_TOKEN(self):
            return self.getToken(ChronoParser.SEMIC_TOKEN, 0)

        def IDENTIFIER(self):
            return self.getToken(ChronoParser.IDENTIFIER, 0)

        def typeSpecifier(self):
            return self.getTypedRuleContext(ChronoParser.TypeSpecifierContext,0)


        def getRuleIndex(self):
            return ChronoParser.RULE_usingAlias

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUsingAlias" ):
                listener.enterUsingAlias(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUsingAlias" ):
                listener.exitUsingAlias(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUsingAlias" ):
                return visitor.visitUsingAlias(self)
            else:
                return visitor.visitChildren(self)




    def usingAlias(self):

        localctx = ChronoParser.UsingAliasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_usingAlias)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.match(ChronoParser.USING)
            self.state = 317
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 318
            self.match(ChronoParser.ASSIGN)
            self.state = 319
            localctx.typeName = self.typeSpecifier()
            self.state = 320
            self.match(ChronoParser.SEMIC_TOKEN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypemapDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token
            self.hint = None # TypeSpecifierContext
            self.value = None # Token

        def TYPEMAP(self):
            return self.getToken(ChronoParser.TYPEMAP, 0)

        def ASSIGN(self):
            return self.getToken(ChronoParser.ASSIGN, 0)

        def SEMIC_TOKEN(self):
            return self.getToken(ChronoParser.SEMIC_TOKEN, 0)

        def IDENTIFIER(self):
            return self.getToken(ChronoParser.IDENTIFIER, 0)

        def STRING_LITERAL(self):
            return self.getToken(ChronoParser.STRING_LITERAL, 0)

        def COLON(self):
            return self.getToken(ChronoParser.COLON, 0)

        def typeSpecifier(self):
            return self.getTypedRuleContext(ChronoParser.TypeSpecifierContext,0)


        def getRuleIndex(self):
            return ChronoParser.RULE_typemapDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypemapDefinition" ):
                listener.enterTypemapDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypemapDefinition" ):
                listener.exitTypemapDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypemapDefinition" ):
                return visitor.visitTypemapDefinition(self)
            else:
                return visitor.visitChildren(self)




    def typemapDefinition(self):

        localctx = ChronoParser.TypemapDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_typemapDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            self.match(ChronoParser.TYPEMAP)
            self.state = 323
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 326
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==69:
                self.state = 324
                self.match(ChronoParser.COLON)
                self.state = 325
                localctx.hint = self.typeSpecifier()


            self.state = 328
            self.match(ChronoParser.ASSIGN)
            self.state = 329
            localctx.value = self.match(ChronoParser.STRING_LITERAL)
            self.state = 330
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
        self.enterRule(localctx, 36, self.RULE_functionDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 332
                self.match(ChronoParser.STATIC)


            self.state = 335
            self.match(ChronoParser.FUNC)
            self.state = 336
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 337
            self.match(ChronoParser.LPAREN)
            self.state = 338
            self.parameters()
            self.state = 339
            self.match(ChronoParser.RPAREN)
            self.state = 342
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 340
                self.match(ChronoParser.ARROW)
                self.state = 341
                localctx.returnType = self.typeSpecifier()


            self.state = 344
            self.match(ChronoParser.LBRACE)
            self.state = 348
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -7854154570505595848) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & 2096897) != 0):
                self.state = 345
                self.statement()
                self.state = 350
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 351
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
        self.enterRule(localctx, 38, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==83:
                self.state = 353
                self.parameter()
                self.state = 358
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==72:
                    self.state = 354
                    self.match(ChronoParser.COMMA)
                    self.state = 355
                    self.parameter()
                    self.state = 360
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
        self.enterRule(localctx, 40, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 364
            self.match(ChronoParser.COLON)
            self.state = 365
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
        self.enterRule(localctx, 42, self.RULE_cppBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.match(ChronoParser.AT_CPP)
            self.state = 371
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==90:
                self.state = 368
                self.match(ChronoParser.CPP_BODY)
                self.state = 373
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 374
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
        self.enterRule(localctx, 44, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.match(ChronoParser.RETURN)
            self.state = 377
            self.expression()
            self.state = 378
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
        self.enterRule(localctx, 46, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            _la = self._input.LA(1)
            if not(((((_la - 49)) & ~0x3f) == 0 and ((1 << (_la - 49)) & 2097183) != 0)):
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
        self.enterRule(localctx, 48, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self.assignableExpression()
            self.state = 383
            self.assignmentOperator()
            self.state = 384
            self.expression()
            self.state = 385
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
        self.enterRule(localctx, 50, self.RULE_assignableExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.assignablePrimary()
            self.state = 398
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 39)) & ~0x3f) == 0 and ((1 << (_la - 39)) & 4563402753) != 0):
                self.state = 396
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [71]:
                    self.state = 388
                    self.match(ChronoParser.DOT)
                    self.state = 389
                    self.match(ChronoParser.IDENTIFIER)
                    pass
                elif token in [67]:
                    self.state = 390
                    self.match(ChronoParser.LBRACK)
                    self.state = 391
                    self.expression()
                    self.state = 392
                    self.match(ChronoParser.RBRACK)
                    pass
                elif token in [39]:
                    self.state = 394
                    self.match(ChronoParser.ARROW)
                    self.state = 395
                    self.match(ChronoParser.IDENTIFIER)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 400
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
        self.enterRule(localctx, 52, self.RULE_assignablePrimary)
        try:
            self.state = 411
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [83]:
                self.enterOuterAlt(localctx, 1)
                self.state = 401
                self.match(ChronoParser.IDENTIFIER)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 402
                self.match(ChronoParser.THIS)
                pass
            elif token in [46]:
                self.enterOuterAlt(localctx, 3)
                self.state = 403
                self.match(ChronoParser.STAR)
                self.state = 404
                self.assignablePrimary()
                pass
            elif token in [57]:
                self.enterOuterAlt(localctx, 4)
                self.state = 405
                self.match(ChronoParser.BIT_AND)
                self.state = 406
                self.assignablePrimary()
                pass
            elif token in [63]:
                self.enterOuterAlt(localctx, 5)
                self.state = 407
                self.match(ChronoParser.LPAREN)
                self.state = 408
                self.assignableExpression()
                self.state = 409
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
        self.enterRule(localctx, 54, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
            self.match(ChronoParser.IF)
            self.state = 414
            self.match(ChronoParser.LPAREN)
            self.state = 415
            self.expression()
            self.state = 416
            self.match(ChronoParser.RPAREN)
            self.state = 417
            localctx.if_block = self.ifBlock()
            self.state = 423
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 418
                self.match(ChronoParser.ELSE)
                self.state = 421
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [12]:
                    self.state = 419
                    localctx.else_if = self.ifStatement()
                    pass
                elif token in [65]:
                    self.state = 420
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
        self.enterRule(localctx, 56, self.RULE_ifBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 425
            self.match(ChronoParser.LBRACE)
            self.state = 429
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -7854154570505595848) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & 2096897) != 0):
                self.state = 426
                self.statement()
                self.state = 431
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 432
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
        self.enterRule(localctx, 58, self.RULE_elseBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 434
            self.match(ChronoParser.LBRACE)
            self.state = 438
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -7854154570505595848) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & 2096897) != 0):
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
        self.enterRule(localctx, 60, self.RULE_whileStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 443
            self.match(ChronoParser.WHILE)
            self.state = 444
            self.match(ChronoParser.LPAREN)
            self.state = 445
            self.expression()
            self.state = 446
            self.match(ChronoParser.RPAREN)
            self.state = 447
            self.match(ChronoParser.LBRACE)
            self.state = 451
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -7854154570505595848) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & 2096897) != 0):
                self.state = 448
                self.statement()
                self.state = 453
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 454
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
        self.enterRule(localctx, 62, self.RULE_statement)
        try:
            self.state = 468
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 456
                self.variableDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 457
                self.assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 458
                self.returnStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 459
                self.expression()
                self.state = 460
                self.match(ChronoParser.SEMIC_TOKEN)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 462
                self.cppBlock()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 463
                self.ifStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 464
                self.whileStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 465
                self.deleteStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 466
                self.forStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 467
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
        self.enterRule(localctx, 64, self.RULE_blockStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 470
            self.match(ChronoParser.LBRACE)
            self.state = 474
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -7854154570505595848) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & 2096897) != 0):
                self.state = 471
                self.statement()
                self.state = 476
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 477
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
        self.enterRule(localctx, 66, self.RULE_deleteStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 479
            self.match(ChronoParser.DELETE)
            self.state = 480
            self.expression()
            self.state = 481
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
        self.enterRule(localctx, 68, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 483
            self.match(ChronoParser.FOR)
            self.state = 484
            self.match(ChronoParser.LPAREN)
            self.state = 486
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -9079186480034741224) != 0) or _la==83:
                self.state = 485
                localctx.init = self.forInit()


            self.state = 488
            self.match(ChronoParser.SEMIC_TOKEN)
            self.state = 490
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -7854154596275452928) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & 2096897) != 0):
                self.state = 489
                localctx.cond = self.expression()


            self.state = 492
            self.match(ChronoParser.SEMIC_TOKEN)
            self.state = 494
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -7854154596275452928) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & 2096897) != 0):
                self.state = 493
                localctx.incr = self.forIncrement()


            self.state = 496
            self.match(ChronoParser.RPAREN)
            self.state = 497
            self.match(ChronoParser.LBRACE)
            self.state = 501
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -7854154570505595848) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & 2096897) != 0):
                self.state = 498
                self.statement()
                self.state = 503
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 504
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
        self.enterRule(localctx, 70, self.RULE_forInit)
        try:
            self.state = 508
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 506
                self.variableDeclaration_no_semicolon()
                pass
            elif token in [10, 46, 57, 63, 83]:
                self.enterOuterAlt(localctx, 2)
                self.state = 507
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
        self.enterRule(localctx, 72, self.RULE_forIncrement)
        try:
            self.state = 512
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 510
                self.assignment_no_semicolon()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 511
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
        self.enterRule(localctx, 74, self.RULE_methodSignature)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 514
            self.match(ChronoParser.FUNC)
            self.state = 515
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 516
            self.match(ChronoParser.LPAREN)
            self.state = 517
            self.parameters()
            self.state = 518
            self.match(ChronoParser.RPAREN)
            self.state = 521
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 519
                self.match(ChronoParser.ARROW)
                self.state = 520
                localctx.returnType = self.typeSpecifier()


            self.state = 523
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
        self.enterRule(localctx, 76, self.RULE_interfaceDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 525
            self.match(ChronoParser.INTERFACE)
            self.state = 526
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 527
            self.match(ChronoParser.LBRACE)
            self.state = 532
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2 or _la==34:
                self.state = 530
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [2]:
                    self.state = 528
                    self.methodSignature()
                    pass
                elif token in [34]:
                    self.state = 529
                    self.cppBlock()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 534
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 535
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
        self.enterRule(localctx, 78, self.RULE_variableDeclaration_no_semicolon)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 537
            _la = self._input.LA(1)
            if not(_la==3 or _la==4):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 538
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 541
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==69:
                self.state = 539
                self.match(ChronoParser.COLON)
                self.state = 540
                localctx.typeName = self.typeSpecifier()


            self.state = 545
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==70:
                self.state = 543
                self.match(ChronoParser.ASSIGN)
                self.state = 544
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
        self.enterRule(localctx, 80, self.RULE_assignment_no_semicolon)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 547
            self.assignableExpression()
            self.state = 548
            self.assignmentOperator()
            self.state = 549
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
        self.enterRule(localctx, 82, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 551
            self.unaryExpression()
            self.state = 556
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1063411877897306112) != 0):
                self.state = 552
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1063411877897306112) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 553
                self.unaryExpression()
                self.state = 558
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
        self.enterRule(localctx, 84, self.RULE_unaryExpression)
        self._la = 0 # Token type
        try:
            self.state = 566
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [44, 45, 56, 60]:
                self.enterOuterAlt(localctx, 1)
                self.state = 559
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1225031875202908160) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 560
                self.unaryExpression()
                pass
            elif token in [57]:
                self.enterOuterAlt(localctx, 2)
                self.state = 561
                self.match(ChronoParser.BIT_AND)
                self.state = 562
                self.unaryExpression()
                pass
            elif token in [46]:
                self.enterOuterAlt(localctx, 3)
                self.state = 563
                self.match(ChronoParser.STAR)
                self.state = 564
                self.unaryExpression()
                pass
            elif token in [10, 25, 26, 27, 28, 29, 30, 31, 32, 63, 65, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85]:
                self.enterOuterAlt(localctx, 4)
                self.state = 565
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
        self.enterRule(localctx, 86, self.RULE_simpleExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 570
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
            if la_ == 1:
                self.state = 568
                self.primary()
                pass

            elif la_ == 2:
                self.state = 569
                self.functionCallExpression()
                pass


            self.state = 602
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 39)) & ~0x3f) == 0 and ((1 << (_la - 39)) & 4563402753) != 0):
                self.state = 600
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [71]:
                    self.state = 572
                    self.match(ChronoParser.DOT)
                    self.state = 573
                    self.match(ChronoParser.IDENTIFIER)
                    self.state = 578
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
                    if la_ == 1:
                        self.state = 574
                        self.match(ChronoParser.LBRACK)
                        self.state = 575
                        self.typeList()
                        self.state = 576
                        self.match(ChronoParser.RBRACK)


                    self.state = 585
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==63:
                        self.state = 580
                        self.match(ChronoParser.LPAREN)
                        self.state = 582
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & -7854154596275452928) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & 2096897) != 0):
                            self.state = 581
                            self.expressionList()


                        self.state = 584
                        self.match(ChronoParser.RPAREN)


                    pass
                elif token in [67]:
                    self.state = 587
                    self.match(ChronoParser.LBRACK)
                    self.state = 588
                    self.expression()
                    self.state = 589
                    self.match(ChronoParser.RBRACK)
                    pass
                elif token in [39]:
                    self.state = 591
                    self.match(ChronoParser.ARROW)
                    self.state = 592
                    self.match(ChronoParser.IDENTIFIER)
                    self.state = 598
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==63:
                        self.state = 593
                        self.match(ChronoParser.LPAREN)
                        self.state = 595
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & -7854154596275452928) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & 2096897) != 0):
                            self.state = 594
                            self.expressionList()


                        self.state = 597
                        self.match(ChronoParser.RPAREN)


                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 604
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

        def STATIC_CAST(self):
            return self.getToken(ChronoParser.STATIC_CAST, 0)

        def REINTERPRET_CAST(self):
            return self.getToken(ChronoParser.REINTERPRET_CAST, 0)

        def CONST_CAST(self):
            return self.getToken(ChronoParser.CONST_CAST, 0)

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
        self.enterRule(localctx, 88, self.RULE_primary)
        self._la = 0 # Token type
        try:
            self.state = 641
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,75,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 605
                self.match(ChronoParser.NEW)
                self.state = 606
                self.baseType()
                self.state = 607
                self.match(ChronoParser.LPAREN)
                self.state = 609
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & -7854154596275452928) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & 2096897) != 0):
                    self.state = 608
                    self.expressionList()


                self.state = 611
                self.match(ChronoParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 613
                _la = self._input.LA(1)
                if not(_la==25 or _la==26):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 614
                self.match(ChronoParser.LBRACK)
                self.state = 615
                self.typeSpecifier()
                self.state = 616
                self.match(ChronoParser.RBRACK)
                self.state = 617
                self.match(ChronoParser.LPAREN)
                self.state = 619
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & -7854154596275452928) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & 2096897) != 0):
                    self.state = 618
                    self.expressionList()


                self.state = 621
                self.match(ChronoParser.RPAREN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 623
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1979711488) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 624
                self.match(ChronoParser.LBRACK)
                self.state = 625
                self.typeSpecifier()
                self.state = 626
                self.match(ChronoParser.RBRACK)
                self.state = 627
                self.match(ChronoParser.LPAREN)
                self.state = 629
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & -7854154596275452928) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & 2096897) != 0):
                    self.state = 628
                    self.expressionList()


                self.state = 631
                self.match(ChronoParser.RPAREN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 633
                self.literal()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 634
                self.initializerList()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 635
                self.match(ChronoParser.IDENTIFIER)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 636
                self.match(ChronoParser.THIS)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 637
                self.match(ChronoParser.LPAREN)
                self.state = 638
                self.expression()
                self.state = 639
                self.match(ChronoParser.RPAREN)
                pass


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
        self.enterRule(localctx, 90, self.RULE_initializerList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 643
            self.match(ChronoParser.LBRACE)
            self.state = 645
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -7854154596275452928) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & 2096897) != 0):
                self.state = 644
                self.expressionList()


            self.state = 647
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
        self.enterRule(localctx, 92, self.RULE_functionCallExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 649
            localctx.funcName = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==27 or _la==83):
                localctx.funcName = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 650
            self.match(ChronoParser.LPAREN)
            self.state = 652
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -7854154596275452928) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & 2096897) != 0):
                self.state = 651
                self.expressionList()


            self.state = 654
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
        self.enterRule(localctx, 94, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 656
            self.expression()
            self.state = 661
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==72:
                self.state = 657
                self.match(ChronoParser.COMMA)
                self.state = 658
                self.expression()
                self.state = 663
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

        def U8_STRING_LITERAL(self):
            return self.getToken(ChronoParser.U8_STRING_LITERAL, 0)

        def U_STRING_LITERAL(self):
            return self.getToken(ChronoParser.U_STRING_LITERAL, 0)

        def U_STRING_LITERAL_CAP(self):
            return self.getToken(ChronoParser.U_STRING_LITERAL_CAP, 0)

        def L_STRING_LITERAL_CAP(self):
            return self.getToken(ChronoParser.L_STRING_LITERAL_CAP, 0)

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
        self.enterRule(localctx, 96, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 664
            _la = self._input.LA(1)
            if not(((((_la - 31)) & ~0x3f) == 0 and ((1 << (_la - 31)) & 31520799345082369) != 0)):
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





