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
        4,1,93,711,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,5,0,112,8,0,10,0,12,0,115,9,0,1,0,1,0,1,0,1,0,
        1,0,3,0,122,8,0,1,0,5,0,125,8,0,10,0,12,0,128,9,0,1,0,1,0,3,0,132,
        8,0,1,0,1,0,1,0,1,0,1,0,1,0,3,0,140,8,0,1,0,5,0,143,8,0,10,0,12,
        0,146,9,0,3,0,148,8,0,1,1,1,1,1,1,5,1,153,8,1,10,1,12,1,156,9,1,
        1,1,1,1,1,1,3,1,161,8,1,1,2,1,2,1,2,5,2,166,8,2,10,2,12,2,169,9,
        2,1,3,1,3,1,3,1,3,3,3,175,8,3,1,3,1,3,3,3,179,8,3,1,3,1,3,1,4,1,
        4,3,4,185,8,4,1,5,4,5,188,8,5,11,5,12,5,189,1,5,1,5,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,3,6,202,8,6,1,7,1,7,1,8,3,8,207,8,8,1,8,1,8,
        1,8,3,8,212,8,8,1,8,1,8,3,8,216,8,8,3,8,218,8,8,1,8,1,8,3,8,222,
        8,8,1,8,1,8,1,8,1,8,3,8,228,8,8,1,9,1,9,1,9,1,9,3,9,234,8,9,1,9,
        1,9,3,9,238,8,9,1,9,1,9,5,9,242,8,9,10,9,12,9,245,9,9,1,9,1,9,1,
        10,1,10,1,10,1,10,5,10,253,8,10,10,10,12,10,256,9,10,1,10,1,10,1,
        11,3,11,261,8,11,1,11,1,11,3,11,265,8,11,1,11,1,11,3,11,269,8,11,
        1,11,1,11,1,11,3,11,274,8,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        3,12,283,8,12,1,12,1,12,5,12,287,8,12,10,12,12,12,290,9,12,1,12,
        1,12,1,13,1,13,1,13,1,13,1,13,1,13,5,13,300,8,13,10,13,12,13,303,
        9,13,1,13,1,13,1,14,1,14,1,14,5,14,310,8,14,10,14,12,14,313,9,14,
        1,14,1,14,1,15,1,15,1,15,1,15,3,15,321,8,15,1,16,1,16,1,16,1,16,
        1,16,1,16,1,17,1,17,1,17,1,17,3,17,333,8,17,1,17,1,17,1,17,1,17,
        1,18,3,18,340,8,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,349,8,
        18,1,18,1,18,5,18,353,8,18,10,18,12,18,356,9,18,1,18,1,18,1,19,1,
        19,1,19,5,19,363,8,19,10,19,12,19,366,9,19,3,19,368,8,19,1,20,1,
        20,1,20,1,20,1,21,1,21,5,21,376,8,21,10,21,12,21,379,9,21,1,21,1,
        21,1,22,1,22,1,22,1,22,1,23,1,23,1,24,1,24,1,24,1,24,1,24,1,25,1,
        25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,5,25,403,8,25,10,25,12,25,
        406,9,25,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,3,26,
        418,8,26,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,3,27,428,8,27,3,
        27,430,8,27,1,28,1,28,5,28,434,8,28,10,28,12,28,437,9,28,1,28,1,
        28,1,29,1,29,5,29,443,8,29,10,29,12,29,446,9,29,1,29,1,29,1,30,1,
        30,1,30,1,30,1,30,1,30,5,30,456,8,30,10,30,12,30,459,9,30,1,30,1,
        30,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,
        31,3,31,476,8,31,1,32,1,32,5,32,480,8,32,10,32,12,32,483,9,32,1,
        32,1,32,1,33,1,33,1,33,1,33,5,33,491,8,33,10,33,12,33,494,9,33,1,
        33,1,33,1,34,1,34,1,34,5,34,501,8,34,10,34,12,34,504,9,34,1,34,1,
        34,1,35,1,35,1,35,1,35,1,35,1,35,5,35,514,8,35,10,35,12,35,517,9,
        35,1,35,3,35,520,8,35,1,35,1,35,1,36,1,36,1,36,1,36,1,37,1,37,1,
        37,3,37,531,8,37,1,37,1,37,3,37,535,8,37,1,37,1,37,3,37,539,8,37,
        1,37,1,37,1,37,5,37,544,8,37,10,37,12,37,547,9,37,1,37,1,37,1,38,
        1,38,3,38,553,8,38,1,39,1,39,3,39,557,8,39,1,40,1,40,1,40,1,40,1,
        40,1,40,1,40,3,40,566,8,40,1,40,1,40,1,41,1,41,1,41,1,41,1,41,5,
        41,575,8,41,10,41,12,41,578,9,41,1,41,1,41,1,42,1,42,1,42,1,42,3,
        42,586,8,42,1,42,1,42,3,42,590,8,42,1,43,1,43,1,43,1,43,1,44,1,44,
        1,44,5,44,599,8,44,10,44,12,44,602,9,44,1,45,1,45,1,45,1,45,1,45,
        1,45,1,45,3,45,611,8,45,1,46,1,46,3,46,615,8,46,1,46,1,46,1,46,1,
        46,1,46,1,46,3,46,623,8,46,1,46,1,46,3,46,627,8,46,1,46,3,46,630,
        8,46,1,46,1,46,1,46,1,46,1,46,1,46,1,46,1,46,3,46,640,8,46,1,46,
        3,46,643,8,46,5,46,645,8,46,10,46,12,46,648,9,46,1,47,1,47,1,47,
        1,47,3,47,654,8,47,1,47,1,47,1,47,1,47,1,47,1,47,1,47,1,47,3,47,
        664,8,47,1,47,1,47,1,47,1,47,1,47,1,47,1,47,1,47,3,47,674,8,47,1,
        47,1,47,1,47,1,47,1,47,1,47,1,47,1,47,1,47,1,47,3,47,686,8,47,1,
        48,1,48,3,48,690,8,48,1,48,1,48,1,49,1,49,1,49,3,49,697,8,49,1,49,
        1,49,1,50,1,50,1,50,5,50,704,8,50,10,50,12,50,707,9,50,1,51,1,51,
        1,51,0,0,52,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,
        38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,
        82,84,86,88,90,92,94,96,98,100,102,0,10,2,0,49,49,60,60,1,0,3,4,
        2,0,64,64,87,87,2,0,52,56,73,73,4,0,38,41,43,51,57,58,60,62,3,0,
        47,48,59,59,63,63,1,0,28,29,2,0,28,29,31,33,2,0,30,30,86,86,3,0,
        34,34,76,85,87,88,779,0,147,1,0,0,0,2,160,1,0,0,0,4,162,1,0,0,0,
        6,170,1,0,0,0,8,184,1,0,0,0,10,187,1,0,0,0,12,201,1,0,0,0,14,203,
        1,0,0,0,16,227,1,0,0,0,18,229,1,0,0,0,20,248,1,0,0,0,22,273,1,0,
        0,0,24,275,1,0,0,0,26,293,1,0,0,0,28,306,1,0,0,0,30,316,1,0,0,0,
        32,322,1,0,0,0,34,328,1,0,0,0,36,339,1,0,0,0,38,367,1,0,0,0,40,369,
        1,0,0,0,42,373,1,0,0,0,44,382,1,0,0,0,46,386,1,0,0,0,48,388,1,0,
        0,0,50,393,1,0,0,0,52,417,1,0,0,0,54,419,1,0,0,0,56,431,1,0,0,0,
        58,440,1,0,0,0,60,449,1,0,0,0,62,475,1,0,0,0,64,477,1,0,0,0,66,486,
        1,0,0,0,68,497,1,0,0,0,70,507,1,0,0,0,72,523,1,0,0,0,74,527,1,0,
        0,0,76,552,1,0,0,0,78,556,1,0,0,0,80,558,1,0,0,0,82,569,1,0,0,0,
        84,581,1,0,0,0,86,591,1,0,0,0,88,595,1,0,0,0,90,610,1,0,0,0,92,614,
        1,0,0,0,94,685,1,0,0,0,96,687,1,0,0,0,98,693,1,0,0,0,100,700,1,0,
        0,0,102,708,1,0,0,0,104,105,5,70,0,0,105,106,3,0,0,0,106,107,5,65,
        0,0,107,108,3,88,44,0,108,109,5,71,0,0,109,113,1,0,0,0,110,112,7,
        0,0,0,111,110,1,0,0,0,112,115,1,0,0,0,113,111,1,0,0,0,113,114,1,
        0,0,0,114,148,1,0,0,0,115,113,1,0,0,0,116,121,3,2,1,0,117,118,5,
        70,0,0,118,119,3,4,2,0,119,120,5,71,0,0,120,122,1,0,0,0,121,117,
        1,0,0,0,121,122,1,0,0,0,122,126,1,0,0,0,123,125,7,0,0,0,124,123,
        1,0,0,0,125,128,1,0,0,0,126,124,1,0,0,0,126,127,1,0,0,0,127,148,
        1,0,0,0,128,126,1,0,0,0,129,139,5,66,0,0,130,132,3,4,2,0,131,130,
        1,0,0,0,131,132,1,0,0,0,132,133,1,0,0,0,133,134,5,67,0,0,134,135,
        5,42,0,0,135,140,3,0,0,0,136,137,3,0,0,0,137,138,5,67,0,0,138,140,
        1,0,0,0,139,131,1,0,0,0,139,136,1,0,0,0,140,144,1,0,0,0,141,143,
        7,0,0,0,142,141,1,0,0,0,143,146,1,0,0,0,144,142,1,0,0,0,144,145,
        1,0,0,0,145,148,1,0,0,0,146,144,1,0,0,0,147,104,1,0,0,0,147,116,
        1,0,0,0,147,129,1,0,0,0,148,1,1,0,0,0,149,154,5,86,0,0,150,151,5,
        74,0,0,151,153,5,86,0,0,152,150,1,0,0,0,153,156,1,0,0,0,154,152,
        1,0,0,0,154,155,1,0,0,0,155,161,1,0,0,0,156,154,1,0,0,0,157,161,
        5,25,0,0,158,161,5,26,0,0,159,161,5,27,0,0,160,149,1,0,0,0,160,157,
        1,0,0,0,160,158,1,0,0,0,160,159,1,0,0,0,161,3,1,0,0,0,162,167,3,
        8,4,0,163,164,5,75,0,0,164,166,3,8,4,0,165,163,1,0,0,0,166,169,1,
        0,0,0,167,165,1,0,0,0,167,168,1,0,0,0,168,5,1,0,0,0,169,167,1,0,
        0,0,170,171,7,1,0,0,171,174,5,86,0,0,172,173,5,72,0,0,173,175,3,
        0,0,0,174,172,1,0,0,0,174,175,1,0,0,0,175,178,1,0,0,0,176,177,5,
        73,0,0,177,179,3,88,44,0,178,176,1,0,0,0,178,179,1,0,0,0,179,180,
        1,0,0,0,180,181,5,65,0,0,181,7,1,0,0,0,182,185,3,0,0,0,183,185,3,
        102,51,0,184,182,1,0,0,0,184,183,1,0,0,0,185,9,1,0,0,0,186,188,3,
        12,6,0,187,186,1,0,0,0,188,189,1,0,0,0,189,187,1,0,0,0,189,190,1,
        0,0,0,190,191,1,0,0,0,191,192,5,0,0,1,192,11,1,0,0,0,193,202,3,30,
        15,0,194,202,3,42,21,0,195,202,3,18,9,0,196,202,3,20,10,0,197,202,
        3,36,18,0,198,202,3,82,41,0,199,202,3,32,16,0,200,202,3,34,17,0,
        201,193,1,0,0,0,201,194,1,0,0,0,201,195,1,0,0,0,201,196,1,0,0,0,
        201,197,1,0,0,0,201,198,1,0,0,0,201,199,1,0,0,0,201,200,1,0,0,0,
        202,13,1,0,0,0,203,204,5,16,0,0,204,15,1,0,0,0,205,207,3,14,7,0,
        206,205,1,0,0,0,206,207,1,0,0,0,207,208,1,0,0,0,208,228,3,6,3,0,
        209,211,5,11,0,0,210,212,3,14,7,0,211,210,1,0,0,0,211,212,1,0,0,
        0,212,218,1,0,0,0,213,215,3,14,7,0,214,216,5,11,0,0,215,214,1,0,
        0,0,215,216,1,0,0,0,216,218,1,0,0,0,217,209,1,0,0,0,217,213,1,0,
        0,0,218,219,1,0,0,0,219,228,3,24,12,0,220,222,3,14,7,0,221,220,1,
        0,0,0,221,222,1,0,0,0,222,223,1,0,0,0,223,228,3,26,13,0,224,228,
        3,24,12,0,225,228,3,28,14,0,226,228,3,42,21,0,227,206,1,0,0,0,227,
        217,1,0,0,0,227,221,1,0,0,0,227,224,1,0,0,0,227,225,1,0,0,0,227,
        226,1,0,0,0,228,17,1,0,0,0,229,230,5,6,0,0,230,233,5,86,0,0,231,
        232,5,72,0,0,232,234,5,86,0,0,233,231,1,0,0,0,233,234,1,0,0,0,234,
        237,1,0,0,0,235,236,5,18,0,0,236,238,3,4,2,0,237,235,1,0,0,0,237,
        238,1,0,0,0,238,239,1,0,0,0,239,243,5,68,0,0,240,242,3,16,8,0,241,
        240,1,0,0,0,242,245,1,0,0,0,243,241,1,0,0,0,243,244,1,0,0,0,244,
        246,1,0,0,0,245,243,1,0,0,0,246,247,5,69,0,0,247,19,1,0,0,0,248,
        249,5,7,0,0,249,250,5,86,0,0,250,254,5,68,0,0,251,253,3,22,11,0,
        252,251,1,0,0,0,253,256,1,0,0,0,254,252,1,0,0,0,254,255,1,0,0,0,
        255,257,1,0,0,0,256,254,1,0,0,0,257,258,5,69,0,0,258,21,1,0,0,0,
        259,261,3,14,7,0,260,259,1,0,0,0,260,261,1,0,0,0,261,262,1,0,0,0,
        262,274,3,6,3,0,263,265,3,14,7,0,264,263,1,0,0,0,264,265,1,0,0,0,
        265,266,1,0,0,0,266,274,3,24,12,0,267,269,3,14,7,0,268,267,1,0,0,
        0,268,269,1,0,0,0,269,270,1,0,0,0,270,274,3,26,13,0,271,274,3,28,
        14,0,272,274,3,42,21,0,273,260,1,0,0,0,273,264,1,0,0,0,273,268,1,
        0,0,0,273,271,1,0,0,0,273,272,1,0,0,0,274,23,1,0,0,0,275,276,5,2,
        0,0,276,277,5,86,0,0,277,278,5,66,0,0,278,279,3,38,19,0,279,282,
        5,67,0,0,280,281,5,42,0,0,281,283,3,0,0,0,282,280,1,0,0,0,282,283,
        1,0,0,0,283,284,1,0,0,0,284,288,5,68,0,0,285,287,3,62,31,0,286,285,
        1,0,0,0,287,290,1,0,0,0,288,286,1,0,0,0,288,289,1,0,0,0,289,291,
        1,0,0,0,290,288,1,0,0,0,291,292,5,69,0,0,292,25,1,0,0,0,293,294,
        5,8,0,0,294,295,5,66,0,0,295,296,3,38,19,0,296,297,5,67,0,0,297,
        301,5,68,0,0,298,300,3,62,31,0,299,298,1,0,0,0,300,303,1,0,0,0,301,
        299,1,0,0,0,301,302,1,0,0,0,302,304,1,0,0,0,303,301,1,0,0,0,304,
        305,5,69,0,0,305,27,1,0,0,0,306,307,5,9,0,0,307,311,5,68,0,0,308,
        310,3,62,31,0,309,308,1,0,0,0,310,313,1,0,0,0,311,309,1,0,0,0,311,
        312,1,0,0,0,312,314,1,0,0,0,313,311,1,0,0,0,314,315,5,69,0,0,315,
        29,1,0,0,0,316,317,5,1,0,0,317,320,7,2,0,0,318,319,5,19,0,0,319,
        321,5,86,0,0,320,318,1,0,0,0,320,321,1,0,0,0,321,31,1,0,0,0,322,
        323,5,20,0,0,323,324,5,86,0,0,324,325,5,73,0,0,325,326,3,0,0,0,326,
        327,5,65,0,0,327,33,1,0,0,0,328,329,5,21,0,0,329,332,5,86,0,0,330,
        331,5,72,0,0,331,333,3,0,0,0,332,330,1,0,0,0,332,333,1,0,0,0,333,
        334,1,0,0,0,334,335,5,73,0,0,335,336,5,87,0,0,336,337,5,65,0,0,337,
        35,1,0,0,0,338,340,5,11,0,0,339,338,1,0,0,0,339,340,1,0,0,0,340,
        341,1,0,0,0,341,342,5,2,0,0,342,343,5,86,0,0,343,344,5,66,0,0,344,
        345,3,38,19,0,345,348,5,67,0,0,346,347,5,42,0,0,347,349,3,0,0,0,
        348,346,1,0,0,0,348,349,1,0,0,0,349,350,1,0,0,0,350,354,5,68,0,0,
        351,353,3,62,31,0,352,351,1,0,0,0,353,356,1,0,0,0,354,352,1,0,0,
        0,354,355,1,0,0,0,355,357,1,0,0,0,356,354,1,0,0,0,357,358,5,69,0,
        0,358,37,1,0,0,0,359,364,3,40,20,0,360,361,5,75,0,0,361,363,3,40,
        20,0,362,360,1,0,0,0,363,366,1,0,0,0,364,362,1,0,0,0,364,365,1,0,
        0,0,365,368,1,0,0,0,366,364,1,0,0,0,367,359,1,0,0,0,367,368,1,0,
        0,0,368,39,1,0,0,0,369,370,5,86,0,0,370,371,5,72,0,0,371,372,3,0,
        0,0,372,41,1,0,0,0,373,377,5,37,0,0,374,376,5,93,0,0,375,374,1,0,
        0,0,376,379,1,0,0,0,377,375,1,0,0,0,377,378,1,0,0,0,378,380,1,0,
        0,0,379,377,1,0,0,0,380,381,5,92,0,0,381,43,1,0,0,0,382,383,5,5,
        0,0,383,384,3,88,44,0,384,385,5,65,0,0,385,45,1,0,0,0,386,387,7,
        3,0,0,387,47,1,0,0,0,388,389,3,50,25,0,389,390,3,46,23,0,390,391,
        3,88,44,0,391,392,5,65,0,0,392,49,1,0,0,0,393,404,3,52,26,0,394,
        395,5,74,0,0,395,403,5,86,0,0,396,397,5,70,0,0,397,398,3,88,44,0,
        398,399,5,71,0,0,399,403,1,0,0,0,400,401,5,42,0,0,401,403,5,86,0,
        0,402,394,1,0,0,0,402,396,1,0,0,0,402,400,1,0,0,0,403,406,1,0,0,
        0,404,402,1,0,0,0,404,405,1,0,0,0,405,51,1,0,0,0,406,404,1,0,0,0,
        407,418,5,86,0,0,408,418,5,10,0,0,409,410,5,49,0,0,410,418,3,52,
        26,0,411,412,5,60,0,0,412,418,3,52,26,0,413,414,5,66,0,0,414,415,
        3,50,25,0,415,416,5,67,0,0,416,418,1,0,0,0,417,407,1,0,0,0,417,408,
        1,0,0,0,417,409,1,0,0,0,417,411,1,0,0,0,417,413,1,0,0,0,418,53,1,
        0,0,0,419,420,5,12,0,0,420,421,5,66,0,0,421,422,3,88,44,0,422,423,
        5,67,0,0,423,429,3,56,28,0,424,427,5,13,0,0,425,428,3,54,27,0,426,
        428,3,58,29,0,427,425,1,0,0,0,427,426,1,0,0,0,428,430,1,0,0,0,429,
        424,1,0,0,0,429,430,1,0,0,0,430,55,1,0,0,0,431,435,5,68,0,0,432,
        434,3,62,31,0,433,432,1,0,0,0,434,437,1,0,0,0,435,433,1,0,0,0,435,
        436,1,0,0,0,436,438,1,0,0,0,437,435,1,0,0,0,438,439,5,69,0,0,439,
        57,1,0,0,0,440,444,5,68,0,0,441,443,3,62,31,0,442,441,1,0,0,0,443,
        446,1,0,0,0,444,442,1,0,0,0,444,445,1,0,0,0,445,447,1,0,0,0,446,
        444,1,0,0,0,447,448,5,69,0,0,448,59,1,0,0,0,449,450,5,14,0,0,450,
        451,5,66,0,0,451,452,3,88,44,0,452,453,5,67,0,0,453,457,5,68,0,0,
        454,456,3,62,31,0,455,454,1,0,0,0,456,459,1,0,0,0,457,455,1,0,0,
        0,457,458,1,0,0,0,458,460,1,0,0,0,459,457,1,0,0,0,460,461,5,69,0,
        0,461,61,1,0,0,0,462,476,3,6,3,0,463,476,3,48,24,0,464,476,3,44,
        22,0,465,466,3,88,44,0,466,467,5,65,0,0,467,476,1,0,0,0,468,476,
        3,42,21,0,469,476,3,54,27,0,470,476,3,60,30,0,471,476,3,72,36,0,
        472,476,3,74,37,0,473,476,3,64,32,0,474,476,3,70,35,0,475,462,1,
        0,0,0,475,463,1,0,0,0,475,464,1,0,0,0,475,465,1,0,0,0,475,468,1,
        0,0,0,475,469,1,0,0,0,475,470,1,0,0,0,475,471,1,0,0,0,475,472,1,
        0,0,0,475,473,1,0,0,0,475,474,1,0,0,0,476,63,1,0,0,0,477,481,5,68,
        0,0,478,480,3,62,31,0,479,478,1,0,0,0,480,483,1,0,0,0,481,479,1,
        0,0,0,481,482,1,0,0,0,482,484,1,0,0,0,483,481,1,0,0,0,484,485,5,
        69,0,0,485,65,1,0,0,0,486,487,5,23,0,0,487,488,3,88,44,0,488,492,
        5,68,0,0,489,491,3,62,31,0,490,489,1,0,0,0,491,494,1,0,0,0,492,490,
        1,0,0,0,492,493,1,0,0,0,493,495,1,0,0,0,494,492,1,0,0,0,495,496,
        5,69,0,0,496,67,1,0,0,0,497,498,5,24,0,0,498,502,5,68,0,0,499,501,
        3,62,31,0,500,499,1,0,0,0,501,504,1,0,0,0,502,500,1,0,0,0,502,503,
        1,0,0,0,503,505,1,0,0,0,504,502,1,0,0,0,505,506,5,69,0,0,506,69,
        1,0,0,0,507,508,5,22,0,0,508,509,5,66,0,0,509,510,3,88,44,0,510,
        511,5,67,0,0,511,515,5,68,0,0,512,514,3,66,33,0,513,512,1,0,0,0,
        514,517,1,0,0,0,515,513,1,0,0,0,515,516,1,0,0,0,516,519,1,0,0,0,
        517,515,1,0,0,0,518,520,3,68,34,0,519,518,1,0,0,0,519,520,1,0,0,
        0,520,521,1,0,0,0,521,522,5,69,0,0,522,71,1,0,0,0,523,524,5,36,0,
        0,524,525,3,88,44,0,525,526,5,65,0,0,526,73,1,0,0,0,527,528,5,15,
        0,0,528,530,5,66,0,0,529,531,3,76,38,0,530,529,1,0,0,0,530,531,1,
        0,0,0,531,532,1,0,0,0,532,534,5,65,0,0,533,535,3,88,44,0,534,533,
        1,0,0,0,534,535,1,0,0,0,535,536,1,0,0,0,536,538,5,65,0,0,537,539,
        3,78,39,0,538,537,1,0,0,0,538,539,1,0,0,0,539,540,1,0,0,0,540,541,
        5,67,0,0,541,545,5,68,0,0,542,544,3,62,31,0,543,542,1,0,0,0,544,
        547,1,0,0,0,545,543,1,0,0,0,545,546,1,0,0,0,546,548,1,0,0,0,547,
        545,1,0,0,0,548,549,5,69,0,0,549,75,1,0,0,0,550,553,3,84,42,0,551,
        553,3,86,43,0,552,550,1,0,0,0,552,551,1,0,0,0,553,77,1,0,0,0,554,
        557,3,86,43,0,555,557,3,88,44,0,556,554,1,0,0,0,556,555,1,0,0,0,
        557,79,1,0,0,0,558,559,5,2,0,0,559,560,5,86,0,0,560,561,5,66,0,0,
        561,562,3,38,19,0,562,565,5,67,0,0,563,564,5,42,0,0,564,566,3,0,
        0,0,565,563,1,0,0,0,565,566,1,0,0,0,566,567,1,0,0,0,567,568,5,65,
        0,0,568,81,1,0,0,0,569,570,5,17,0,0,570,571,5,86,0,0,571,576,5,68,
        0,0,572,575,3,80,40,0,573,575,3,42,21,0,574,572,1,0,0,0,574,573,
        1,0,0,0,575,578,1,0,0,0,576,574,1,0,0,0,576,577,1,0,0,0,577,579,
        1,0,0,0,578,576,1,0,0,0,579,580,5,69,0,0,580,83,1,0,0,0,581,582,
        7,1,0,0,582,585,5,86,0,0,583,584,5,72,0,0,584,586,3,0,0,0,585,583,
        1,0,0,0,585,586,1,0,0,0,586,589,1,0,0,0,587,588,5,73,0,0,588,590,
        3,88,44,0,589,587,1,0,0,0,589,590,1,0,0,0,590,85,1,0,0,0,591,592,
        3,50,25,0,592,593,3,46,23,0,593,594,3,88,44,0,594,87,1,0,0,0,595,
        600,3,90,45,0,596,597,7,4,0,0,597,599,3,90,45,0,598,596,1,0,0,0,
        599,602,1,0,0,0,600,598,1,0,0,0,600,601,1,0,0,0,601,89,1,0,0,0,602,
        600,1,0,0,0,603,604,7,5,0,0,604,611,3,90,45,0,605,606,5,60,0,0,606,
        611,3,90,45,0,607,608,5,49,0,0,608,611,3,90,45,0,609,611,3,92,46,
        0,610,603,1,0,0,0,610,605,1,0,0,0,610,607,1,0,0,0,610,609,1,0,0,
        0,611,91,1,0,0,0,612,615,3,94,47,0,613,615,3,98,49,0,614,612,1,0,
        0,0,614,613,1,0,0,0,615,646,1,0,0,0,616,617,5,74,0,0,617,622,5,86,
        0,0,618,619,5,70,0,0,619,620,3,4,2,0,620,621,5,71,0,0,621,623,1,
        0,0,0,622,618,1,0,0,0,622,623,1,0,0,0,623,629,1,0,0,0,624,626,5,
        66,0,0,625,627,3,100,50,0,626,625,1,0,0,0,626,627,1,0,0,0,627,628,
        1,0,0,0,628,630,5,67,0,0,629,624,1,0,0,0,629,630,1,0,0,0,630,645,
        1,0,0,0,631,632,5,70,0,0,632,633,3,88,44,0,633,634,5,71,0,0,634,
        645,1,0,0,0,635,636,5,42,0,0,636,642,5,86,0,0,637,639,5,66,0,0,638,
        640,3,100,50,0,639,638,1,0,0,0,639,640,1,0,0,0,640,641,1,0,0,0,641,
        643,5,67,0,0,642,637,1,0,0,0,642,643,1,0,0,0,643,645,1,0,0,0,644,
        616,1,0,0,0,644,631,1,0,0,0,644,635,1,0,0,0,645,648,1,0,0,0,646,
        644,1,0,0,0,646,647,1,0,0,0,647,93,1,0,0,0,648,646,1,0,0,0,649,650,
        5,35,0,0,650,651,3,2,1,0,651,653,5,66,0,0,652,654,3,100,50,0,653,
        652,1,0,0,0,653,654,1,0,0,0,654,655,1,0,0,0,655,656,5,67,0,0,656,
        686,1,0,0,0,657,658,7,6,0,0,658,659,5,70,0,0,659,660,3,0,0,0,660,
        661,5,71,0,0,661,663,5,66,0,0,662,664,3,100,50,0,663,662,1,0,0,0,
        663,664,1,0,0,0,664,665,1,0,0,0,665,666,5,67,0,0,666,686,1,0,0,0,
        667,668,7,7,0,0,668,669,5,70,0,0,669,670,3,0,0,0,670,671,5,71,0,
        0,671,673,5,66,0,0,672,674,3,100,50,0,673,672,1,0,0,0,673,674,1,
        0,0,0,674,675,1,0,0,0,675,676,5,67,0,0,676,686,1,0,0,0,677,686,3,
        102,51,0,678,686,3,96,48,0,679,686,5,86,0,0,680,686,5,10,0,0,681,
        682,5,66,0,0,682,683,3,88,44,0,683,684,5,67,0,0,684,686,1,0,0,0,
        685,649,1,0,0,0,685,657,1,0,0,0,685,667,1,0,0,0,685,677,1,0,0,0,
        685,678,1,0,0,0,685,679,1,0,0,0,685,680,1,0,0,0,685,681,1,0,0,0,
        686,95,1,0,0,0,687,689,5,68,0,0,688,690,3,100,50,0,689,688,1,0,0,
        0,689,690,1,0,0,0,690,691,1,0,0,0,691,692,5,69,0,0,692,97,1,0,0,
        0,693,694,7,8,0,0,694,696,5,66,0,0,695,697,3,100,50,0,696,695,1,
        0,0,0,696,697,1,0,0,0,697,698,1,0,0,0,698,699,5,67,0,0,699,99,1,
        0,0,0,700,705,3,88,44,0,701,702,5,75,0,0,702,704,3,88,44,0,703,701,
        1,0,0,0,704,707,1,0,0,0,705,703,1,0,0,0,705,706,1,0,0,0,706,101,
        1,0,0,0,707,705,1,0,0,0,708,709,7,9,0,0,709,103,1,0,0,0,83,113,121,
        126,131,139,144,147,154,160,167,174,178,184,189,201,206,211,215,
        217,221,227,233,237,243,254,260,264,268,273,282,288,301,311,320,
        332,339,348,354,364,367,377,402,404,417,427,429,435,444,457,475,
        481,492,502,515,519,530,534,538,545,552,556,565,574,576,585,589,
        600,610,614,622,626,629,639,642,644,646,653,663,673,685,689,696,
        705
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
                     "'using'", "'typemap'", "'switch'", "'case'", "'default'", 
                     "'unique'", "'shared'", "'weak'", "'@make'", "'@make_shared'", 
                     "'@move'", "'static_cast'", "'reinterpret_cast'", "'const_cast'", 
                     "<INVALID>", "'new'", "'delete'", "'@cpp'", "'=='", 
                     "'!='", "'<='", "'>='", "'->'", "'&&'", "'||'", "'<<'", 
                     "'>>'", "'+'", "'-'", "'*'", "'/'", "'%'", "'+='", 
                     "'-='", "'*='", "'/='", "'%='", "'<'", "'>'", "'!'", 
                     "'&'", "'|'", "'^'", "'~'", "<INVALID>", "';'", "'('", 
                     "')'", "'{'", "'}'", "'['", "']'", "':'", "'='", "'.'", 
                     "','", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'@end'" ]

    symbolicNames = [ "<INVALID>", "IMPORT", "FUNC", "VAR", "CONST", "RETURN", 
                      "CLASS", "STRUCT", "INIT", "DEINIT", "THIS", "STATIC", 
                      "IF", "ELSE", "WHILE", "FOR", "PUBLIC", "INTERFACE", 
                      "IMPL", "AS", "USING", "TYPEMAP", "SWITCH", "CASE", 
                      "DEFAULT", "UNIQUE_KW", "SHARED_KW", "WEAK_KW", "AT_MAKE_UNIQUE", 
                      "AT_MAKE_SHARED", "AT_MOVE", "STATIC_CAST", "REINTERPRET_CAST", 
                      "CONST_CAST", "BOOL_LITERAL", "NEW", "DELETE", "AT_CPP", 
                      "EQ", "NEQ", "LTE", "GTE", "ARROW", "AND_OP", "OR_OP", 
                      "LSHIFT", "RSHIFT", "PLUS", "MINUS", "STAR", "SLASH", 
                      "MODULO", "PLUS_ASSIGN", "MINUS_ASSIGN", "STAR_ASSIGN", 
                      "SLASH_ASSIGN", "MOD_ASSIGN", "LT", "GT", "NOT_OP", 
                      "BIT_AND", "BIT_OR", "BIT_XOR", "BIT_NOT", "INCLUDE_PATH", 
                      "SEMIC_TOKEN", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                      "LBRACK", "RBRACK", "COLON", "ASSIGN", "DOT", "COMMA", 
                      "HEX_LITERAL", "BINARY_LITERAL", "OCTAL_LITERAL", 
                      "FLOAT_LITERAL", "DECIMAL_LITERAL", "BYTE_LITERAL", 
                      "U8_STRING_LITERAL", "U_STRING_LITERAL", "U_STRING_LITERAL_CAP", 
                      "L_STRING_LITERAL_CAP", "IDENTIFIER", "STRING_LITERAL", 
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
    RULE_caseBlock = 33
    RULE_defaultBlock = 34
    RULE_switchStatement = 35
    RULE_deleteStatement = 36
    RULE_forStatement = 37
    RULE_forInit = 38
    RULE_forIncrement = 39
    RULE_methodSignature = 40
    RULE_interfaceDefinition = 41
    RULE_variableDeclaration_no_semicolon = 42
    RULE_assignment_no_semicolon = 43
    RULE_expression = 44
    RULE_unaryExpression = 45
    RULE_simpleExpression = 46
    RULE_primary = 47
    RULE_initializerList = 48
    RULE_functionCallExpression = 49
    RULE_expressionList = 50
    RULE_literal = 51

    ruleNames =  [ "typeSpecifier", "baseType", "typeList", "variableDeclaration", 
                   "templateArgument", "program", "topLevelStatement", "accessModifier", 
                   "classBodyStatement", "classDefinition", "structDefinition", 
                   "structBodyStatement", "methodDefinition", "initDefinition", 
                   "deinitBlock", "importDirective", "usingAlias", "typemapDefinition", 
                   "functionDefinition", "parameters", "parameter", "cppBlock", 
                   "returnStatement", "assignmentOperator", "assignment", 
                   "assignableExpression", "assignablePrimary", "ifStatement", 
                   "ifBlock", "elseBlock", "whileStatement", "statement", 
                   "blockStatement", "caseBlock", "defaultBlock", "switchStatement", 
                   "deleteStatement", "forStatement", "forInit", "forIncrement", 
                   "methodSignature", "interfaceDefinition", "variableDeclaration_no_semicolon", 
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
    USING=20
    TYPEMAP=21
    SWITCH=22
    CASE=23
    DEFAULT=24
    UNIQUE_KW=25
    SHARED_KW=26
    WEAK_KW=27
    AT_MAKE_UNIQUE=28
    AT_MAKE_SHARED=29
    AT_MOVE=30
    STATIC_CAST=31
    REINTERPRET_CAST=32
    CONST_CAST=33
    BOOL_LITERAL=34
    NEW=35
    DELETE=36
    AT_CPP=37
    EQ=38
    NEQ=39
    LTE=40
    GTE=41
    ARROW=42
    AND_OP=43
    OR_OP=44
    LSHIFT=45
    RSHIFT=46
    PLUS=47
    MINUS=48
    STAR=49
    SLASH=50
    MODULO=51
    PLUS_ASSIGN=52
    MINUS_ASSIGN=53
    STAR_ASSIGN=54
    SLASH_ASSIGN=55
    MOD_ASSIGN=56
    LT=57
    GT=58
    NOT_OP=59
    BIT_AND=60
    BIT_OR=61
    BIT_XOR=62
    BIT_NOT=63
    INCLUDE_PATH=64
    SEMIC_TOKEN=65
    LPAREN=66
    RPAREN=67
    LBRACE=68
    RBRACE=69
    LBRACK=70
    RBRACK=71
    COLON=72
    ASSIGN=73
    DOT=74
    COMMA=75
    HEX_LITERAL=76
    BINARY_LITERAL=77
    OCTAL_LITERAL=78
    FLOAT_LITERAL=79
    DECIMAL_LITERAL=80
    BYTE_LITERAL=81
    U8_STRING_LITERAL=82
    U_STRING_LITERAL=83
    U_STRING_LITERAL_CAP=84
    L_STRING_LITERAL_CAP=85
    IDENTIFIER=86
    STRING_LITERAL=87
    CHAR_LITERAL=88
    LINE_COMMENT=89
    WHITESPACE=90
    NEWLINE=91
    AT_END=92
    CPP_BODY=93

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
            self.state = 147
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [70]:
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                self.match(ChronoParser.LBRACK)
                self.state = 105
                self.typeSpecifier()
                self.state = 106
                self.match(ChronoParser.SEMIC_TOKEN)
                self.state = 107
                self.expression()
                self.state = 108
                self.match(ChronoParser.RBRACK)
                self.state = 113
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 110
                        _la = self._input.LA(1)
                        if not(_la==49 or _la==60):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume() 
                    self.state = 115
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

                pass
            elif token in [25, 26, 27, 86]:
                self.enterOuterAlt(localctx, 2)
                self.state = 116
                self.baseType()
                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==70:
                    self.state = 117
                    self.match(ChronoParser.LBRACK)
                    self.state = 118
                    self.typeList()
                    self.state = 119
                    self.match(ChronoParser.RBRACK)


                self.state = 126
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 123
                        _la = self._input.LA(1)
                        if not(_la==49 or _la==60):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume() 
                    self.state = 128
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                pass
            elif token in [66]:
                self.enterOuterAlt(localctx, 3)
                self.state = 129
                self.match(ChronoParser.LPAREN)
                self.state = 139
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 131
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if ((((_la - 25)) & ~0x3f) == 0 and ((1 << (_la - 25)) & -2214416418340345) != 0):
                        self.state = 130
                        localctx.params = self.typeList()


                    self.state = 133
                    self.match(ChronoParser.RPAREN)
                    self.state = 134
                    self.match(ChronoParser.ARROW)
                    self.state = 135
                    localctx.returnType = self.typeSpecifier()
                    pass

                elif la_ == 2:
                    self.state = 136
                    localctx.nested = self.typeSpecifier()
                    self.state = 137
                    self.match(ChronoParser.RPAREN)
                    pass


                self.state = 144
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 141
                        _la = self._input.LA(1)
                        if not(_la==49 or _la==60):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume() 
                    self.state = 146
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
            self.state = 160
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [86]:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self.match(ChronoParser.IDENTIFIER)
                self.state = 154
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==74:
                    self.state = 150
                    self.match(ChronoParser.DOT)
                    self.state = 151
                    self.match(ChronoParser.IDENTIFIER)
                    self.state = 156
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
                self.match(ChronoParser.UNIQUE_KW)
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 3)
                self.state = 158
                self.match(ChronoParser.SHARED_KW)
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 4)
                self.state = 159
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
            self.state = 162
            self.templateArgument()
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==75:
                self.state = 163
                self.match(ChronoParser.COMMA)
                self.state = 164
                self.templateArgument()
                self.state = 169
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
            self.state = 170
            _la = self._input.LA(1)
            if not(_la==3 or _la==4):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 171
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==72:
                self.state = 172
                self.match(ChronoParser.COLON)
                self.state = 173
                localctx.typeName = self.typeSpecifier()


            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==73:
                self.state = 176
                self.match(ChronoParser.ASSIGN)
                self.state = 177
                self.expression()


            self.state = 180
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
            self.state = 184
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25, 26, 27, 66, 70, 86]:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.typeSpecifier()
                pass
            elif token in [34, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 87, 88]:
                self.enterOuterAlt(localctx, 2)
                self.state = 183
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
            self.state = 187 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 186
                self.topLevelStatement()
                self.state = 189 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 137442232518) != 0)):
                    break

            self.state = 191
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
            self.state = 201
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.importDirective()
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
                self.cppBlock()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 195
                self.classDefinition()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 4)
                self.state = 196
                self.structDefinition()
                pass
            elif token in [2, 11]:
                self.enterOuterAlt(localctx, 5)
                self.state = 197
                self.functionDefinition()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 6)
                self.state = 198
                self.interfaceDefinition()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 7)
                self.state = 199
                self.usingAlias()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 8)
                self.state = 200
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
            self.state = 203
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
            self.state = 227
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 205
                    self.accessModifier()


                self.state = 208
                self.variableDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 217
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [11]:
                    self.state = 209
                    self.match(ChronoParser.STATIC)
                    self.state = 211
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==16:
                        self.state = 210
                        self.accessModifier()


                    pass
                elif token in [16]:
                    self.state = 213
                    self.accessModifier()
                    self.state = 215
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==11:
                        self.state = 214
                        self.match(ChronoParser.STATIC)


                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 219
                self.methodDefinition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 221
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 220
                    self.accessModifier()


                self.state = 223
                self.initDefinition()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 224
                self.methodDefinition()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 225
                self.deinitBlock()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 226
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
            self.state = 229
            self.match(ChronoParser.CLASS)
            self.state = 230
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 233
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==72:
                self.state = 231
                self.match(ChronoParser.COLON)
                self.state = 232
                localctx.base = self.match(ChronoParser.IDENTIFIER)


            self.state = 237
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 235
                self.match(ChronoParser.IMPL)
                self.state = 236
                localctx.interfaces = self.typeList()


            self.state = 239
            self.match(ChronoParser.LBRACE)
            self.state = 243
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 137439021852) != 0):
                self.state = 240
                self.classBodyStatement()
                self.state = 245
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 246
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
            self.state = 248
            self.match(ChronoParser.STRUCT)
            self.state = 249
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 250
            self.match(ChronoParser.LBRACE)
            self.state = 254
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 137439019804) != 0):
                self.state = 251
                self.structBodyStatement()
                self.state = 256
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 257
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
            self.state = 273
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 260
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 259
                    self.accessModifier()


                self.state = 262
                self.variableDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 264
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 263
                    self.accessModifier()


                self.state = 266
                self.methodDefinition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 268
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 267
                    self.accessModifier()


                self.state = 270
                self.initDefinition()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 271
                self.deinitBlock()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 272
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
            self.state = 275
            self.match(ChronoParser.FUNC)
            self.state = 276
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 277
            self.match(ChronoParser.LPAREN)
            self.state = 278
            self.parameters()
            self.state = 279
            self.match(ChronoParser.RPAREN)
            self.state = 282
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==42:
                self.state = 280
                self.match(ChronoParser.ARROW)
                self.state = 281
                localctx.returnType = self.typeSpecifier()


            self.state = 284
            self.match(ChronoParser.LBRACE)
            self.state = 288
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -7493004342912297928) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & 8387589) != 0):
                self.state = 285
                self.statement()
                self.state = 290
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 291
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
            self.state = 293
            self.match(ChronoParser.INIT)
            self.state = 294
            self.match(ChronoParser.LPAREN)
            self.state = 295
            self.parameters()
            self.state = 296
            self.match(ChronoParser.RPAREN)
            self.state = 297
            self.match(ChronoParser.LBRACE)
            self.state = 301
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -7493004342912297928) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & 8387589) != 0):
                self.state = 298
                self.statement()
                self.state = 303
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 304
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
            self.state = 306
            self.match(ChronoParser.DEINIT)
            self.state = 307
            self.match(ChronoParser.LBRACE)
            self.state = 311
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -7493004342912297928) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & 8387589) != 0):
                self.state = 308
                self.statement()
                self.state = 313
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 314
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
            self.state = 316
            self.match(ChronoParser.IMPORT)
            self.state = 317
            localctx.path = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==64 or _la==87):
                localctx.path = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 320
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 318
                self.match(ChronoParser.AS)
                self.state = 319
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
            self.state = 322
            self.match(ChronoParser.USING)
            self.state = 323
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 324
            self.match(ChronoParser.ASSIGN)
            self.state = 325
            localctx.typeName = self.typeSpecifier()
            self.state = 326
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
            self.state = 328
            self.match(ChronoParser.TYPEMAP)
            self.state = 329
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 332
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==72:
                self.state = 330
                self.match(ChronoParser.COLON)
                self.state = 331
                localctx.hint = self.typeSpecifier()


            self.state = 334
            self.match(ChronoParser.ASSIGN)
            self.state = 335
            localctx.value = self.match(ChronoParser.STRING_LITERAL)
            self.state = 336
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
            self.state = 339
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 338
                self.match(ChronoParser.STATIC)


            self.state = 341
            self.match(ChronoParser.FUNC)
            self.state = 342
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 343
            self.match(ChronoParser.LPAREN)
            self.state = 344
            self.parameters()
            self.state = 345
            self.match(ChronoParser.RPAREN)
            self.state = 348
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==42:
                self.state = 346
                self.match(ChronoParser.ARROW)
                self.state = 347
                localctx.returnType = self.typeSpecifier()


            self.state = 350
            self.match(ChronoParser.LBRACE)
            self.state = 354
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -7493004342912297928) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & 8387589) != 0):
                self.state = 351
                self.statement()
                self.state = 356
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 357
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
            self.state = 367
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==86:
                self.state = 359
                self.parameter()
                self.state = 364
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==75:
                    self.state = 360
                    self.match(ChronoParser.COMMA)
                    self.state = 361
                    self.parameter()
                    self.state = 366
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
            self.state = 369
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 370
            self.match(ChronoParser.COLON)
            self.state = 371
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
            self.state = 373
            self.match(ChronoParser.AT_CPP)
            self.state = 377
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==93:
                self.state = 374
                self.match(ChronoParser.CPP_BODY)
                self.state = 379
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 380
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
            self.state = 382
            self.match(ChronoParser.RETURN)
            self.state = 383
            self.expression()
            self.state = 384
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
            self.state = 386
            _la = self._input.LA(1)
            if not(((((_la - 52)) & ~0x3f) == 0 and ((1 << (_la - 52)) & 2097183) != 0)):
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
            self.state = 388
            self.assignableExpression()
            self.state = 389
            self.assignmentOperator()
            self.state = 390
            self.expression()
            self.state = 391
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
            self.state = 393
            self.assignablePrimary()
            self.state = 404
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 42)) & ~0x3f) == 0 and ((1 << (_la - 42)) & 4563402753) != 0):
                self.state = 402
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [74]:
                    self.state = 394
                    self.match(ChronoParser.DOT)
                    self.state = 395
                    self.match(ChronoParser.IDENTIFIER)
                    pass
                elif token in [70]:
                    self.state = 396
                    self.match(ChronoParser.LBRACK)
                    self.state = 397
                    self.expression()
                    self.state = 398
                    self.match(ChronoParser.RBRACK)
                    pass
                elif token in [42]:
                    self.state = 400
                    self.match(ChronoParser.ARROW)
                    self.state = 401
                    self.match(ChronoParser.IDENTIFIER)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 406
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
            self.state = 417
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [86]:
                self.enterOuterAlt(localctx, 1)
                self.state = 407
                self.match(ChronoParser.IDENTIFIER)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 408
                self.match(ChronoParser.THIS)
                pass
            elif token in [49]:
                self.enterOuterAlt(localctx, 3)
                self.state = 409
                self.match(ChronoParser.STAR)
                self.state = 410
                self.assignablePrimary()
                pass
            elif token in [60]:
                self.enterOuterAlt(localctx, 4)
                self.state = 411
                self.match(ChronoParser.BIT_AND)
                self.state = 412
                self.assignablePrimary()
                pass
            elif token in [66]:
                self.enterOuterAlt(localctx, 5)
                self.state = 413
                self.match(ChronoParser.LPAREN)
                self.state = 414
                self.assignableExpression()
                self.state = 415
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
            self.state = 419
            self.match(ChronoParser.IF)
            self.state = 420
            self.match(ChronoParser.LPAREN)
            self.state = 421
            self.expression()
            self.state = 422
            self.match(ChronoParser.RPAREN)
            self.state = 423
            localctx.if_block = self.ifBlock()
            self.state = 429
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 424
                self.match(ChronoParser.ELSE)
                self.state = 427
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [12]:
                    self.state = 425
                    localctx.else_if = self.ifStatement()
                    pass
                elif token in [68]:
                    self.state = 426
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
            self.state = 431
            self.match(ChronoParser.LBRACE)
            self.state = 435
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -7493004342912297928) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & 8387589) != 0):
                self.state = 432
                self.statement()
                self.state = 437
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 438
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
            self.state = 440
            self.match(ChronoParser.LBRACE)
            self.state = 444
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -7493004342912297928) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & 8387589) != 0):
                self.state = 441
                self.statement()
                self.state = 446
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 447
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
            self.state = 449
            self.match(ChronoParser.WHILE)
            self.state = 450
            self.match(ChronoParser.LPAREN)
            self.state = 451
            self.expression()
            self.state = 452
            self.match(ChronoParser.RPAREN)
            self.state = 453
            self.match(ChronoParser.LBRACE)
            self.state = 457
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -7493004342912297928) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & 8387589) != 0):
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


        def switchStatement(self):
            return self.getTypedRuleContext(ChronoParser.SwitchStatementContext,0)


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
            self.state = 475
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 462
                self.variableDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 463
                self.assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 464
                self.returnStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 465
                self.expression()
                self.state = 466
                self.match(ChronoParser.SEMIC_TOKEN)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 468
                self.cppBlock()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 469
                self.ifStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 470
                self.whileStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 471
                self.deleteStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 472
                self.forStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 473
                self.blockStatement()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 474
                self.switchStatement()
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
            self.state = 477
            self.match(ChronoParser.LBRACE)
            self.state = 481
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -7493004342912297928) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & 8387589) != 0):
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


    class CaseBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASE(self):
            return self.getToken(ChronoParser.CASE, 0)

        def expression(self):
            return self.getTypedRuleContext(ChronoParser.ExpressionContext,0)


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
            return ChronoParser.RULE_caseBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCaseBlock" ):
                listener.enterCaseBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCaseBlock" ):
                listener.exitCaseBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCaseBlock" ):
                return visitor.visitCaseBlock(self)
            else:
                return visitor.visitChildren(self)




    def caseBlock(self):

        localctx = ChronoParser.CaseBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_caseBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 486
            self.match(ChronoParser.CASE)
            self.state = 487
            self.expression()
            self.state = 488
            self.match(ChronoParser.LBRACE)
            self.state = 492
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -7493004342912297928) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & 8387589) != 0):
                self.state = 489
                self.statement()
                self.state = 494
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 495
            self.match(ChronoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefaultBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFAULT(self):
            return self.getToken(ChronoParser.DEFAULT, 0)

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
            return ChronoParser.RULE_defaultBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefaultBlock" ):
                listener.enterDefaultBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefaultBlock" ):
                listener.exitDefaultBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefaultBlock" ):
                return visitor.visitDefaultBlock(self)
            else:
                return visitor.visitChildren(self)




    def defaultBlock(self):

        localctx = ChronoParser.DefaultBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_defaultBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 497
            self.match(ChronoParser.DEFAULT)
            self.state = 498
            self.match(ChronoParser.LBRACE)
            self.state = 502
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -7493004342912297928) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & 8387589) != 0):
                self.state = 499
                self.statement()
                self.state = 504
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 505
            self.match(ChronoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SWITCH(self):
            return self.getToken(ChronoParser.SWITCH, 0)

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

        def caseBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChronoParser.CaseBlockContext)
            else:
                return self.getTypedRuleContext(ChronoParser.CaseBlockContext,i)


        def defaultBlock(self):
            return self.getTypedRuleContext(ChronoParser.DefaultBlockContext,0)


        def getRuleIndex(self):
            return ChronoParser.RULE_switchStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchStatement" ):
                listener.enterSwitchStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchStatement" ):
                listener.exitSwitchStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitchStatement" ):
                return visitor.visitSwitchStatement(self)
            else:
                return visitor.visitChildren(self)




    def switchStatement(self):

        localctx = ChronoParser.SwitchStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_switchStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 507
            self.match(ChronoParser.SWITCH)
            self.state = 508
            self.match(ChronoParser.LPAREN)
            self.state = 509
            self.expression()
            self.state = 510
            self.match(ChronoParser.RPAREN)
            self.state = 511
            self.match(ChronoParser.LBRACE)
            self.state = 515
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23:
                self.state = 512
                self.caseBlock()
                self.state = 517
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 519
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 518
                self.defaultBlock()


            self.state = 521
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
        self.enterRule(localctx, 72, self.RULE_deleteStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 523
            self.match(ChronoParser.DELETE)
            self.state = 524
            self.expression()
            self.state = 525
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
        self.enterRule(localctx, 74, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 527
            self.match(ChronoParser.FOR)
            self.state = 528
            self.match(ChronoParser.LPAREN)
            self.state = 530
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1153484454560269336) != 0) or _la==66 or _la==86:
                self.state = 529
                localctx.init = self.forInit()


            self.state = 532
            self.match(ChronoParser.SEMIC_TOKEN)
            self.state = 534
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -7493004549074975744) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & 8387589) != 0):
                self.state = 533
                localctx.cond = self.expression()


            self.state = 536
            self.match(ChronoParser.SEMIC_TOKEN)
            self.state = 538
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -7493004549074975744) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & 8387589) != 0):
                self.state = 537
                localctx.incr = self.forIncrement()


            self.state = 540
            self.match(ChronoParser.RPAREN)
            self.state = 541
            self.match(ChronoParser.LBRACE)
            self.state = 545
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -7493004342912297928) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & 8387589) != 0):
                self.state = 542
                self.statement()
                self.state = 547
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 548
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
        self.enterRule(localctx, 76, self.RULE_forInit)
        try:
            self.state = 552
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 550
                self.variableDeclaration_no_semicolon()
                pass
            elif token in [10, 49, 60, 66, 86]:
                self.enterOuterAlt(localctx, 2)
                self.state = 551
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
        self.enterRule(localctx, 78, self.RULE_forIncrement)
        try:
            self.state = 556
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 554
                self.assignment_no_semicolon()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 555
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
        self.enterRule(localctx, 80, self.RULE_methodSignature)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 558
            self.match(ChronoParser.FUNC)
            self.state = 559
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 560
            self.match(ChronoParser.LPAREN)
            self.state = 561
            self.parameters()
            self.state = 562
            self.match(ChronoParser.RPAREN)
            self.state = 565
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==42:
                self.state = 563
                self.match(ChronoParser.ARROW)
                self.state = 564
                localctx.returnType = self.typeSpecifier()


            self.state = 567
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
        self.enterRule(localctx, 82, self.RULE_interfaceDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 569
            self.match(ChronoParser.INTERFACE)
            self.state = 570
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 571
            self.match(ChronoParser.LBRACE)
            self.state = 576
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2 or _la==37:
                self.state = 574
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [2]:
                    self.state = 572
                    self.methodSignature()
                    pass
                elif token in [37]:
                    self.state = 573
                    self.cppBlock()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 578
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 579
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
        self.enterRule(localctx, 84, self.RULE_variableDeclaration_no_semicolon)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 581
            _la = self._input.LA(1)
            if not(_la==3 or _la==4):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 582
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 585
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==72:
                self.state = 583
                self.match(ChronoParser.COLON)
                self.state = 584
                localctx.typeName = self.typeSpecifier()


            self.state = 589
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==73:
                self.state = 587
                self.match(ChronoParser.ASSIGN)
                self.state = 588
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
        self.enterRule(localctx, 86, self.RULE_assignment_no_semicolon)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 591
            self.assignableExpression()
            self.state = 592
            self.assignmentOperator()
            self.state = 593
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
        self.enterRule(localctx, 88, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 595
            self.unaryExpression()
            self.state = 600
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8507295023178448896) != 0):
                self.state = 596
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8507295023178448896) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 597
                self.unaryExpression()
                self.state = 602
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
        self.enterRule(localctx, 90, self.RULE_unaryExpression)
        self._la = 0 # Token type
        try:
            self.state = 610
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [47, 48, 59, 63]:
                self.enterOuterAlt(localctx, 1)
                self.state = 603
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & -8646489072086286336) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 604
                self.unaryExpression()
                pass
            elif token in [60]:
                self.enterOuterAlt(localctx, 2)
                self.state = 605
                self.match(ChronoParser.BIT_AND)
                self.state = 606
                self.unaryExpression()
                pass
            elif token in [49]:
                self.enterOuterAlt(localctx, 3)
                self.state = 607
                self.match(ChronoParser.STAR)
                self.state = 608
                self.unaryExpression()
                pass
            elif token in [10, 28, 29, 30, 31, 32, 33, 34, 35, 66, 68, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88]:
                self.enterOuterAlt(localctx, 4)
                self.state = 609
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
        self.enterRule(localctx, 92, self.RULE_simpleExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 614
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,68,self._ctx)
            if la_ == 1:
                self.state = 612
                self.primary()
                pass

            elif la_ == 2:
                self.state = 613
                self.functionCallExpression()
                pass


            self.state = 646
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 42)) & ~0x3f) == 0 and ((1 << (_la - 42)) & 4563402753) != 0):
                self.state = 644
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [74]:
                    self.state = 616
                    self.match(ChronoParser.DOT)
                    self.state = 617
                    self.match(ChronoParser.IDENTIFIER)
                    self.state = 622
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,69,self._ctx)
                    if la_ == 1:
                        self.state = 618
                        self.match(ChronoParser.LBRACK)
                        self.state = 619
                        self.typeList()
                        self.state = 620
                        self.match(ChronoParser.RBRACK)


                    self.state = 629
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==66:
                        self.state = 624
                        self.match(ChronoParser.LPAREN)
                        self.state = 626
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & -7493004549074975744) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & 8387589) != 0):
                            self.state = 625
                            self.expressionList()


                        self.state = 628
                        self.match(ChronoParser.RPAREN)


                    pass
                elif token in [70]:
                    self.state = 631
                    self.match(ChronoParser.LBRACK)
                    self.state = 632
                    self.expression()
                    self.state = 633
                    self.match(ChronoParser.RBRACK)
                    pass
                elif token in [42]:
                    self.state = 635
                    self.match(ChronoParser.ARROW)
                    self.state = 636
                    self.match(ChronoParser.IDENTIFIER)
                    self.state = 642
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==66:
                        self.state = 637
                        self.match(ChronoParser.LPAREN)
                        self.state = 639
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & -7493004549074975744) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & 8387589) != 0):
                            self.state = 638
                            self.expressionList()


                        self.state = 641
                        self.match(ChronoParser.RPAREN)


                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 648
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
        self.enterRule(localctx, 94, self.RULE_primary)
        self._la = 0 # Token type
        try:
            self.state = 685
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,79,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 649
                self.match(ChronoParser.NEW)
                self.state = 650
                self.baseType()
                self.state = 651
                self.match(ChronoParser.LPAREN)
                self.state = 653
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & -7493004549074975744) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & 8387589) != 0):
                    self.state = 652
                    self.expressionList()


                self.state = 655
                self.match(ChronoParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 657
                _la = self._input.LA(1)
                if not(_la==28 or _la==29):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 658
                self.match(ChronoParser.LBRACK)
                self.state = 659
                self.typeSpecifier()
                self.state = 660
                self.match(ChronoParser.RBRACK)
                self.state = 661
                self.match(ChronoParser.LPAREN)
                self.state = 663
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & -7493004549074975744) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & 8387589) != 0):
                    self.state = 662
                    self.expressionList()


                self.state = 665
                self.match(ChronoParser.RPAREN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 667
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15837691904) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 668
                self.match(ChronoParser.LBRACK)
                self.state = 669
                self.typeSpecifier()
                self.state = 670
                self.match(ChronoParser.RBRACK)
                self.state = 671
                self.match(ChronoParser.LPAREN)
                self.state = 673
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & -7493004549074975744) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & 8387589) != 0):
                    self.state = 672
                    self.expressionList()


                self.state = 675
                self.match(ChronoParser.RPAREN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 677
                self.literal()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 678
                self.initializerList()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 679
                self.match(ChronoParser.IDENTIFIER)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 680
                self.match(ChronoParser.THIS)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 681
                self.match(ChronoParser.LPAREN)
                self.state = 682
                self.expression()
                self.state = 683
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
        self.enterRule(localctx, 96, self.RULE_initializerList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 687
            self.match(ChronoParser.LBRACE)
            self.state = 689
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -7493004549074975744) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & 8387589) != 0):
                self.state = 688
                self.expressionList()


            self.state = 691
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
        self.enterRule(localctx, 98, self.RULE_functionCallExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 693
            localctx.funcName = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==30 or _la==86):
                localctx.funcName = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 694
            self.match(ChronoParser.LPAREN)
            self.state = 696
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -7493004549074975744) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & 8387589) != 0):
                self.state = 695
                self.expressionList()


            self.state = 698
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
        self.enterRule(localctx, 100, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 700
            self.expression()
            self.state = 705
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==75:
                self.state = 701
                self.match(ChronoParser.COMMA)
                self.state = 702
                self.expression()
                self.state = 707
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
        self.enterRule(localctx, 102, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 708
            _la = self._input.LA(1)
            if not(((((_la - 34)) & ~0x3f) == 0 and ((1 << (_la - 34)) & 31520799345082369) != 0)):
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





