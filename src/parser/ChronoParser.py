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
        4,1,82,646,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,1,0,1,0,1,0,1,0,1,0,1,0,1,0,5,0,104,8,0,10,0,12,0,
        107,9,0,1,0,1,0,1,0,1,0,1,0,3,0,114,8,0,1,0,5,0,117,8,0,10,0,12,
        0,120,9,0,1,0,1,0,3,0,124,8,0,1,0,1,0,1,0,1,0,1,0,1,0,3,0,132,8,
        0,1,0,5,0,135,8,0,10,0,12,0,138,9,0,3,0,140,8,0,1,1,1,1,1,1,5,1,
        145,8,1,10,1,12,1,148,9,1,1,1,1,1,1,1,3,1,153,8,1,1,2,1,2,1,2,5,
        2,158,8,2,10,2,12,2,161,9,2,1,3,1,3,1,3,1,3,3,3,167,8,3,1,3,1,3,
        3,3,171,8,3,1,3,1,3,1,4,1,4,3,4,177,8,4,1,5,4,5,180,8,5,11,5,12,
        5,181,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,193,8,6,1,7,1,7,1,
        8,3,8,198,8,8,1,8,1,8,1,8,3,8,203,8,8,1,8,1,8,3,8,207,8,8,3,8,209,
        8,8,1,8,1,8,3,8,213,8,8,1,8,1,8,1,8,1,8,3,8,219,8,8,1,9,1,9,1,9,
        1,9,3,9,225,8,9,1,9,1,9,3,9,229,8,9,1,9,1,9,5,9,233,8,9,10,9,12,
        9,236,9,9,1,9,1,9,1,10,1,10,1,10,1,10,5,10,244,8,10,10,10,12,10,
        247,9,10,1,10,1,10,1,11,3,11,252,8,11,1,11,1,11,3,11,256,8,11,1,
        11,1,11,3,11,260,8,11,1,11,1,11,1,11,3,11,265,8,11,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,3,12,274,8,12,1,12,1,12,5,12,278,8,12,10,12,
        12,12,281,9,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,5,13,291,
        8,13,10,13,12,13,294,9,13,1,13,1,13,1,14,1,14,1,14,5,14,301,8,14,
        10,14,12,14,304,9,14,1,14,1,14,1,15,1,15,1,15,1,15,3,15,312,8,15,
        1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,17,3,17,323,8,17,1,17,
        1,17,1,17,1,17,1,17,1,17,1,17,3,17,332,8,17,1,17,1,17,5,17,336,8,
        17,10,17,12,17,339,9,17,1,17,1,17,1,18,1,18,1,18,5,18,346,8,18,10,
        18,12,18,349,9,18,3,18,351,8,18,1,19,1,19,1,19,1,19,1,20,1,20,5,
        20,359,8,20,10,20,12,20,362,9,20,1,20,1,20,1,21,1,21,1,21,1,21,1,
        22,1,22,1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,1,24,1,
        24,1,24,1,24,5,24,386,8,24,10,24,12,24,389,9,24,1,25,1,25,1,25,1,
        25,1,25,1,25,1,25,1,25,1,25,1,25,3,25,401,8,25,1,26,1,26,1,26,1,
        26,1,26,1,26,1,26,1,26,3,26,411,8,26,3,26,413,8,26,1,27,1,27,5,27,
        417,8,27,10,27,12,27,420,9,27,1,27,1,27,1,28,1,28,5,28,426,8,28,
        10,28,12,28,429,9,28,1,28,1,28,1,29,1,29,1,29,1,29,1,29,1,29,5,29,
        439,8,29,10,29,12,29,442,9,29,1,29,1,29,1,30,1,30,1,30,1,30,1,30,
        1,30,1,30,1,30,1,30,1,30,1,30,1,30,3,30,458,8,30,1,31,1,31,5,31,
        462,8,31,10,31,12,31,465,9,31,1,31,1,31,1,32,1,32,1,32,1,32,1,33,
        1,33,1,33,3,33,476,8,33,1,33,1,33,3,33,480,8,33,1,33,1,33,3,33,484,
        8,33,1,33,1,33,1,33,5,33,489,8,33,10,33,12,33,492,9,33,1,33,1,33,
        1,34,1,34,3,34,498,8,34,1,35,1,35,3,35,502,8,35,1,36,1,36,1,36,1,
        36,1,36,1,36,1,36,3,36,511,8,36,1,36,1,36,1,37,1,37,1,37,1,37,1,
        37,5,37,520,8,37,10,37,12,37,523,9,37,1,37,1,37,1,38,1,38,1,38,1,
        38,3,38,531,8,38,1,38,1,38,3,38,535,8,38,1,39,1,39,1,39,1,39,1,40,
        1,40,1,40,5,40,544,8,40,10,40,12,40,547,9,40,1,41,1,41,1,41,1,41,
        1,41,1,41,1,41,3,41,556,8,41,1,42,1,42,3,42,560,8,42,1,42,1,42,1,
        42,1,42,1,42,1,42,3,42,568,8,42,1,42,1,42,3,42,572,8,42,1,42,3,42,
        575,8,42,1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,42,3,42,585,8,42,1,
        42,3,42,588,8,42,5,42,590,8,42,10,42,12,42,593,9,42,1,43,1,43,1,
        43,1,43,3,43,599,8,43,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,43,3,
        43,609,8,43,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,43,3,
        43,621,8,43,1,44,1,44,3,44,625,8,44,1,44,1,44,1,45,1,45,1,45,3,45,
        632,8,45,1,45,1,45,1,46,1,46,1,46,5,46,639,8,46,10,46,12,46,642,
        9,46,1,47,1,47,1,47,0,0,48,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,
        72,74,76,78,80,82,84,86,88,90,92,94,0,9,2,0,42,42,53,53,1,0,3,4,
        2,0,57,57,76,76,2,0,45,49,66,66,4,0,31,34,36,44,50,51,53,55,3,0,
        40,41,52,52,56,56,1,0,24,25,2,0,26,26,75,75,3,0,27,27,69,74,76,77,
        709,0,139,1,0,0,0,2,152,1,0,0,0,4,154,1,0,0,0,6,162,1,0,0,0,8,176,
        1,0,0,0,10,179,1,0,0,0,12,192,1,0,0,0,14,194,1,0,0,0,16,218,1,0,
        0,0,18,220,1,0,0,0,20,239,1,0,0,0,22,264,1,0,0,0,24,266,1,0,0,0,
        26,284,1,0,0,0,28,297,1,0,0,0,30,307,1,0,0,0,32,315,1,0,0,0,34,322,
        1,0,0,0,36,350,1,0,0,0,38,352,1,0,0,0,40,356,1,0,0,0,42,365,1,0,
        0,0,44,369,1,0,0,0,46,371,1,0,0,0,48,376,1,0,0,0,50,400,1,0,0,0,
        52,402,1,0,0,0,54,414,1,0,0,0,56,423,1,0,0,0,58,432,1,0,0,0,60,457,
        1,0,0,0,62,459,1,0,0,0,64,468,1,0,0,0,66,472,1,0,0,0,68,497,1,0,
        0,0,70,501,1,0,0,0,72,503,1,0,0,0,74,514,1,0,0,0,76,526,1,0,0,0,
        78,536,1,0,0,0,80,540,1,0,0,0,82,555,1,0,0,0,84,559,1,0,0,0,86,620,
        1,0,0,0,88,622,1,0,0,0,90,628,1,0,0,0,92,635,1,0,0,0,94,643,1,0,
        0,0,96,97,5,63,0,0,97,98,3,0,0,0,98,99,5,58,0,0,99,100,3,80,40,0,
        100,101,5,64,0,0,101,105,1,0,0,0,102,104,7,0,0,0,103,102,1,0,0,0,
        104,107,1,0,0,0,105,103,1,0,0,0,105,106,1,0,0,0,106,140,1,0,0,0,
        107,105,1,0,0,0,108,113,3,2,1,0,109,110,5,63,0,0,110,111,3,4,2,0,
        111,112,5,64,0,0,112,114,1,0,0,0,113,109,1,0,0,0,113,114,1,0,0,0,
        114,118,1,0,0,0,115,117,7,0,0,0,116,115,1,0,0,0,117,120,1,0,0,0,
        118,116,1,0,0,0,118,119,1,0,0,0,119,140,1,0,0,0,120,118,1,0,0,0,
        121,131,5,59,0,0,122,124,3,4,2,0,123,122,1,0,0,0,123,124,1,0,0,0,
        124,125,1,0,0,0,125,126,5,60,0,0,126,127,5,35,0,0,127,132,3,0,0,
        0,128,129,3,0,0,0,129,130,5,60,0,0,130,132,1,0,0,0,131,123,1,0,0,
        0,131,128,1,0,0,0,132,136,1,0,0,0,133,135,7,0,0,0,134,133,1,0,0,
        0,135,138,1,0,0,0,136,134,1,0,0,0,136,137,1,0,0,0,137,140,1,0,0,
        0,138,136,1,0,0,0,139,96,1,0,0,0,139,108,1,0,0,0,139,121,1,0,0,0,
        140,1,1,0,0,0,141,146,5,75,0,0,142,143,5,67,0,0,143,145,5,75,0,0,
        144,142,1,0,0,0,145,148,1,0,0,0,146,144,1,0,0,0,146,147,1,0,0,0,
        147,153,1,0,0,0,148,146,1,0,0,0,149,153,5,21,0,0,150,153,5,22,0,
        0,151,153,5,23,0,0,152,141,1,0,0,0,152,149,1,0,0,0,152,150,1,0,0,
        0,152,151,1,0,0,0,153,3,1,0,0,0,154,159,3,8,4,0,155,156,5,68,0,0,
        156,158,3,8,4,0,157,155,1,0,0,0,158,161,1,0,0,0,159,157,1,0,0,0,
        159,160,1,0,0,0,160,5,1,0,0,0,161,159,1,0,0,0,162,163,7,1,0,0,163,
        166,5,75,0,0,164,165,5,65,0,0,165,167,3,0,0,0,166,164,1,0,0,0,166,
        167,1,0,0,0,167,170,1,0,0,0,168,169,5,66,0,0,169,171,3,80,40,0,170,
        168,1,0,0,0,170,171,1,0,0,0,171,172,1,0,0,0,172,173,5,58,0,0,173,
        7,1,0,0,0,174,177,3,0,0,0,175,177,3,94,47,0,176,174,1,0,0,0,176,
        175,1,0,0,0,177,9,1,0,0,0,178,180,3,12,6,0,179,178,1,0,0,0,180,181,
        1,0,0,0,181,179,1,0,0,0,181,182,1,0,0,0,182,183,1,0,0,0,183,184,
        5,0,0,1,184,11,1,0,0,0,185,193,3,30,15,0,186,193,3,40,20,0,187,193,
        3,18,9,0,188,193,3,20,10,0,189,193,3,34,17,0,190,193,3,74,37,0,191,
        193,3,32,16,0,192,185,1,0,0,0,192,186,1,0,0,0,192,187,1,0,0,0,192,
        188,1,0,0,0,192,189,1,0,0,0,192,190,1,0,0,0,192,191,1,0,0,0,193,
        13,1,0,0,0,194,195,5,16,0,0,195,15,1,0,0,0,196,198,3,14,7,0,197,
        196,1,0,0,0,197,198,1,0,0,0,198,199,1,0,0,0,199,219,3,6,3,0,200,
        202,5,11,0,0,201,203,3,14,7,0,202,201,1,0,0,0,202,203,1,0,0,0,203,
        209,1,0,0,0,204,206,3,14,7,0,205,207,5,11,0,0,206,205,1,0,0,0,206,
        207,1,0,0,0,207,209,1,0,0,0,208,200,1,0,0,0,208,204,1,0,0,0,209,
        210,1,0,0,0,210,219,3,24,12,0,211,213,3,14,7,0,212,211,1,0,0,0,212,
        213,1,0,0,0,213,214,1,0,0,0,214,219,3,26,13,0,215,219,3,24,12,0,
        216,219,3,28,14,0,217,219,3,40,20,0,218,197,1,0,0,0,218,208,1,0,
        0,0,218,212,1,0,0,0,218,215,1,0,0,0,218,216,1,0,0,0,218,217,1,0,
        0,0,219,17,1,0,0,0,220,221,5,6,0,0,221,224,5,75,0,0,222,223,5,65,
        0,0,223,225,5,75,0,0,224,222,1,0,0,0,224,225,1,0,0,0,225,228,1,0,
        0,0,226,227,5,18,0,0,227,229,3,4,2,0,228,226,1,0,0,0,228,229,1,0,
        0,0,229,230,1,0,0,0,230,234,5,61,0,0,231,233,3,16,8,0,232,231,1,
        0,0,0,233,236,1,0,0,0,234,232,1,0,0,0,234,235,1,0,0,0,235,237,1,
        0,0,0,236,234,1,0,0,0,237,238,5,62,0,0,238,19,1,0,0,0,239,240,5,
        7,0,0,240,241,5,75,0,0,241,245,5,61,0,0,242,244,3,22,11,0,243,242,
        1,0,0,0,244,247,1,0,0,0,245,243,1,0,0,0,245,246,1,0,0,0,246,248,
        1,0,0,0,247,245,1,0,0,0,248,249,5,62,0,0,249,21,1,0,0,0,250,252,
        3,14,7,0,251,250,1,0,0,0,251,252,1,0,0,0,252,253,1,0,0,0,253,265,
        3,6,3,0,254,256,3,14,7,0,255,254,1,0,0,0,255,256,1,0,0,0,256,257,
        1,0,0,0,257,265,3,24,12,0,258,260,3,14,7,0,259,258,1,0,0,0,259,260,
        1,0,0,0,260,261,1,0,0,0,261,265,3,26,13,0,262,265,3,28,14,0,263,
        265,3,40,20,0,264,251,1,0,0,0,264,255,1,0,0,0,264,259,1,0,0,0,264,
        262,1,0,0,0,264,263,1,0,0,0,265,23,1,0,0,0,266,267,5,2,0,0,267,268,
        5,75,0,0,268,269,5,59,0,0,269,270,3,36,18,0,270,273,5,60,0,0,271,
        272,5,35,0,0,272,274,3,0,0,0,273,271,1,0,0,0,273,274,1,0,0,0,274,
        275,1,0,0,0,275,279,5,61,0,0,276,278,3,60,30,0,277,276,1,0,0,0,278,
        281,1,0,0,0,279,277,1,0,0,0,279,280,1,0,0,0,280,282,1,0,0,0,281,
        279,1,0,0,0,282,283,5,62,0,0,283,25,1,0,0,0,284,285,5,8,0,0,285,
        286,5,59,0,0,286,287,3,36,18,0,287,288,5,60,0,0,288,292,5,61,0,0,
        289,291,3,60,30,0,290,289,1,0,0,0,291,294,1,0,0,0,292,290,1,0,0,
        0,292,293,1,0,0,0,293,295,1,0,0,0,294,292,1,0,0,0,295,296,5,62,0,
        0,296,27,1,0,0,0,297,298,5,9,0,0,298,302,5,61,0,0,299,301,3,60,30,
        0,300,299,1,0,0,0,301,304,1,0,0,0,302,300,1,0,0,0,302,303,1,0,0,
        0,303,305,1,0,0,0,304,302,1,0,0,0,305,306,5,62,0,0,306,29,1,0,0,
        0,307,308,5,1,0,0,308,311,7,2,0,0,309,310,5,19,0,0,310,312,5,75,
        0,0,311,309,1,0,0,0,311,312,1,0,0,0,312,313,1,0,0,0,313,314,5,58,
        0,0,314,31,1,0,0,0,315,316,5,20,0,0,316,317,5,75,0,0,317,318,5,66,
        0,0,318,319,3,0,0,0,319,320,5,58,0,0,320,33,1,0,0,0,321,323,5,11,
        0,0,322,321,1,0,0,0,322,323,1,0,0,0,323,324,1,0,0,0,324,325,5,2,
        0,0,325,326,5,75,0,0,326,327,5,59,0,0,327,328,3,36,18,0,328,331,
        5,60,0,0,329,330,5,35,0,0,330,332,3,0,0,0,331,329,1,0,0,0,331,332,
        1,0,0,0,332,333,1,0,0,0,333,337,5,61,0,0,334,336,3,60,30,0,335,334,
        1,0,0,0,336,339,1,0,0,0,337,335,1,0,0,0,337,338,1,0,0,0,338,340,
        1,0,0,0,339,337,1,0,0,0,340,341,5,62,0,0,341,35,1,0,0,0,342,347,
        3,38,19,0,343,344,5,68,0,0,344,346,3,38,19,0,345,343,1,0,0,0,346,
        349,1,0,0,0,347,345,1,0,0,0,347,348,1,0,0,0,348,351,1,0,0,0,349,
        347,1,0,0,0,350,342,1,0,0,0,350,351,1,0,0,0,351,37,1,0,0,0,352,353,
        5,75,0,0,353,354,5,65,0,0,354,355,3,0,0,0,355,39,1,0,0,0,356,360,
        5,30,0,0,357,359,5,82,0,0,358,357,1,0,0,0,359,362,1,0,0,0,360,358,
        1,0,0,0,360,361,1,0,0,0,361,363,1,0,0,0,362,360,1,0,0,0,363,364,
        5,81,0,0,364,41,1,0,0,0,365,366,5,5,0,0,366,367,3,80,40,0,367,368,
        5,58,0,0,368,43,1,0,0,0,369,370,7,3,0,0,370,45,1,0,0,0,371,372,3,
        48,24,0,372,373,3,44,22,0,373,374,3,80,40,0,374,375,5,58,0,0,375,
        47,1,0,0,0,376,387,3,50,25,0,377,378,5,67,0,0,378,386,5,75,0,0,379,
        380,5,63,0,0,380,381,3,80,40,0,381,382,5,64,0,0,382,386,1,0,0,0,
        383,384,5,35,0,0,384,386,5,75,0,0,385,377,1,0,0,0,385,379,1,0,0,
        0,385,383,1,0,0,0,386,389,1,0,0,0,387,385,1,0,0,0,387,388,1,0,0,
        0,388,49,1,0,0,0,389,387,1,0,0,0,390,401,5,75,0,0,391,401,5,10,0,
        0,392,393,5,42,0,0,393,401,3,50,25,0,394,395,5,53,0,0,395,401,3,
        50,25,0,396,397,5,59,0,0,397,398,3,48,24,0,398,399,5,60,0,0,399,
        401,1,0,0,0,400,390,1,0,0,0,400,391,1,0,0,0,400,392,1,0,0,0,400,
        394,1,0,0,0,400,396,1,0,0,0,401,51,1,0,0,0,402,403,5,12,0,0,403,
        404,5,59,0,0,404,405,3,80,40,0,405,406,5,60,0,0,406,412,3,54,27,
        0,407,410,5,13,0,0,408,411,3,52,26,0,409,411,3,56,28,0,410,408,1,
        0,0,0,410,409,1,0,0,0,411,413,1,0,0,0,412,407,1,0,0,0,412,413,1,
        0,0,0,413,53,1,0,0,0,414,418,5,61,0,0,415,417,3,60,30,0,416,415,
        1,0,0,0,417,420,1,0,0,0,418,416,1,0,0,0,418,419,1,0,0,0,419,421,
        1,0,0,0,420,418,1,0,0,0,421,422,5,62,0,0,422,55,1,0,0,0,423,427,
        5,61,0,0,424,426,3,60,30,0,425,424,1,0,0,0,426,429,1,0,0,0,427,425,
        1,0,0,0,427,428,1,0,0,0,428,430,1,0,0,0,429,427,1,0,0,0,430,431,
        5,62,0,0,431,57,1,0,0,0,432,433,5,14,0,0,433,434,5,59,0,0,434,435,
        3,80,40,0,435,436,5,60,0,0,436,440,5,61,0,0,437,439,3,60,30,0,438,
        437,1,0,0,0,439,442,1,0,0,0,440,438,1,0,0,0,440,441,1,0,0,0,441,
        443,1,0,0,0,442,440,1,0,0,0,443,444,5,62,0,0,444,59,1,0,0,0,445,
        458,3,6,3,0,446,458,3,46,23,0,447,458,3,42,21,0,448,449,3,80,40,
        0,449,450,5,58,0,0,450,458,1,0,0,0,451,458,3,40,20,0,452,458,3,52,
        26,0,453,458,3,58,29,0,454,458,3,64,32,0,455,458,3,66,33,0,456,458,
        3,62,31,0,457,445,1,0,0,0,457,446,1,0,0,0,457,447,1,0,0,0,457,448,
        1,0,0,0,457,451,1,0,0,0,457,452,1,0,0,0,457,453,1,0,0,0,457,454,
        1,0,0,0,457,455,1,0,0,0,457,456,1,0,0,0,458,61,1,0,0,0,459,463,5,
        61,0,0,460,462,3,60,30,0,461,460,1,0,0,0,462,465,1,0,0,0,463,461,
        1,0,0,0,463,464,1,0,0,0,464,466,1,0,0,0,465,463,1,0,0,0,466,467,
        5,62,0,0,467,63,1,0,0,0,468,469,5,29,0,0,469,470,3,80,40,0,470,471,
        5,58,0,0,471,65,1,0,0,0,472,473,5,15,0,0,473,475,5,59,0,0,474,476,
        3,68,34,0,475,474,1,0,0,0,475,476,1,0,0,0,476,477,1,0,0,0,477,479,
        5,58,0,0,478,480,3,80,40,0,479,478,1,0,0,0,479,480,1,0,0,0,480,481,
        1,0,0,0,481,483,5,58,0,0,482,484,3,70,35,0,483,482,1,0,0,0,483,484,
        1,0,0,0,484,485,1,0,0,0,485,486,5,60,0,0,486,490,5,61,0,0,487,489,
        3,60,30,0,488,487,1,0,0,0,489,492,1,0,0,0,490,488,1,0,0,0,490,491,
        1,0,0,0,491,493,1,0,0,0,492,490,1,0,0,0,493,494,5,62,0,0,494,67,
        1,0,0,0,495,498,3,76,38,0,496,498,3,78,39,0,497,495,1,0,0,0,497,
        496,1,0,0,0,498,69,1,0,0,0,499,502,3,78,39,0,500,502,3,80,40,0,501,
        499,1,0,0,0,501,500,1,0,0,0,502,71,1,0,0,0,503,504,5,2,0,0,504,505,
        5,75,0,0,505,506,5,59,0,0,506,507,3,36,18,0,507,510,5,60,0,0,508,
        509,5,35,0,0,509,511,3,0,0,0,510,508,1,0,0,0,510,511,1,0,0,0,511,
        512,1,0,0,0,512,513,5,58,0,0,513,73,1,0,0,0,514,515,5,17,0,0,515,
        516,5,75,0,0,516,521,5,61,0,0,517,520,3,72,36,0,518,520,3,40,20,
        0,519,517,1,0,0,0,519,518,1,0,0,0,520,523,1,0,0,0,521,519,1,0,0,
        0,521,522,1,0,0,0,522,524,1,0,0,0,523,521,1,0,0,0,524,525,5,62,0,
        0,525,75,1,0,0,0,526,527,7,1,0,0,527,530,5,75,0,0,528,529,5,65,0,
        0,529,531,3,0,0,0,530,528,1,0,0,0,530,531,1,0,0,0,531,534,1,0,0,
        0,532,533,5,66,0,0,533,535,3,80,40,0,534,532,1,0,0,0,534,535,1,0,
        0,0,535,77,1,0,0,0,536,537,3,48,24,0,537,538,3,44,22,0,538,539,3,
        80,40,0,539,79,1,0,0,0,540,545,3,82,41,0,541,542,7,4,0,0,542,544,
        3,82,41,0,543,541,1,0,0,0,544,547,1,0,0,0,545,543,1,0,0,0,545,546,
        1,0,0,0,546,81,1,0,0,0,547,545,1,0,0,0,548,549,7,5,0,0,549,556,3,
        82,41,0,550,551,5,53,0,0,551,556,3,82,41,0,552,553,5,42,0,0,553,
        556,3,82,41,0,554,556,3,84,42,0,555,548,1,0,0,0,555,550,1,0,0,0,
        555,552,1,0,0,0,555,554,1,0,0,0,556,83,1,0,0,0,557,560,3,86,43,0,
        558,560,3,90,45,0,559,557,1,0,0,0,559,558,1,0,0,0,560,591,1,0,0,
        0,561,562,5,67,0,0,562,567,5,75,0,0,563,564,5,63,0,0,564,565,3,4,
        2,0,565,566,5,64,0,0,566,568,1,0,0,0,567,563,1,0,0,0,567,568,1,0,
        0,0,568,574,1,0,0,0,569,571,5,59,0,0,570,572,3,92,46,0,571,570,1,
        0,0,0,571,572,1,0,0,0,572,573,1,0,0,0,573,575,5,60,0,0,574,569,1,
        0,0,0,574,575,1,0,0,0,575,590,1,0,0,0,576,577,5,63,0,0,577,578,3,
        80,40,0,578,579,5,64,0,0,579,590,1,0,0,0,580,581,5,35,0,0,581,587,
        5,75,0,0,582,584,5,59,0,0,583,585,3,92,46,0,584,583,1,0,0,0,584,
        585,1,0,0,0,585,586,1,0,0,0,586,588,5,60,0,0,587,582,1,0,0,0,587,
        588,1,0,0,0,588,590,1,0,0,0,589,561,1,0,0,0,589,576,1,0,0,0,589,
        580,1,0,0,0,590,593,1,0,0,0,591,589,1,0,0,0,591,592,1,0,0,0,592,
        85,1,0,0,0,593,591,1,0,0,0,594,595,5,28,0,0,595,596,3,2,1,0,596,
        598,5,59,0,0,597,599,3,92,46,0,598,597,1,0,0,0,598,599,1,0,0,0,599,
        600,1,0,0,0,600,601,5,60,0,0,601,621,1,0,0,0,602,603,7,6,0,0,603,
        604,5,63,0,0,604,605,3,0,0,0,605,606,5,64,0,0,606,608,5,59,0,0,607,
        609,3,92,46,0,608,607,1,0,0,0,608,609,1,0,0,0,609,610,1,0,0,0,610,
        611,5,60,0,0,611,621,1,0,0,0,612,621,3,94,47,0,613,621,3,88,44,0,
        614,621,5,75,0,0,615,621,5,10,0,0,616,617,5,59,0,0,617,618,3,80,
        40,0,618,619,5,60,0,0,619,621,1,0,0,0,620,594,1,0,0,0,620,602,1,
        0,0,0,620,612,1,0,0,0,620,613,1,0,0,0,620,614,1,0,0,0,620,615,1,
        0,0,0,620,616,1,0,0,0,621,87,1,0,0,0,622,624,5,61,0,0,623,625,3,
        92,46,0,624,623,1,0,0,0,624,625,1,0,0,0,625,626,1,0,0,0,626,627,
        5,62,0,0,627,89,1,0,0,0,628,629,7,7,0,0,629,631,5,59,0,0,630,632,
        3,92,46,0,631,630,1,0,0,0,631,632,1,0,0,0,632,633,1,0,0,0,633,634,
        5,60,0,0,634,91,1,0,0,0,635,640,3,80,40,0,636,637,5,68,0,0,637,639,
        3,80,40,0,638,636,1,0,0,0,639,642,1,0,0,0,640,638,1,0,0,0,640,641,
        1,0,0,0,641,93,1,0,0,0,642,640,1,0,0,0,643,644,7,8,0,0,644,95,1,
        0,0,0,77,105,113,118,123,131,136,139,146,152,159,166,170,176,181,
        192,197,202,206,208,212,218,224,228,234,245,251,255,259,264,273,
        279,292,302,311,322,331,337,347,350,360,385,387,400,410,412,418,
        427,440,457,463,475,479,483,490,497,501,510,519,521,530,534,545,
        555,559,567,571,574,584,587,589,591,598,608,620,624,631,640
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
                     "'using'", "'unique'", "'shared'", "'weak'", "'@make'", 
                     "'@make_shared'", "'@move'", "<INVALID>", "'new'", 
                     "'delete'", "'@cpp'", "'=='", "'!='", "'<='", "'>='", 
                     "'->'", "'&&'", "'||'", "'<<'", "'>>'", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'+='", "'-='", "'*='", "'/='", 
                     "'%='", "'<'", "'>'", "'!'", "'&'", "'|'", "'^'", "'~'", 
                     "<INVALID>", "';'", "'('", "')'", "'{'", "'}'", "'['", 
                     "']'", "':'", "'='", "'.'", "','", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'@end'" ]

    symbolicNames = [ "<INVALID>", "IMPORT", "FUNC", "VAR", "CONST", "RETURN", 
                      "CLASS", "STRUCT", "INIT", "DEINIT", "THIS", "STATIC", 
                      "IF", "ELSE", "WHILE", "FOR", "PUBLIC", "INTERFACE", 
                      "IMPL", "AS", "USING", "UNIQUE_KW", "SHARED_KW", "WEAK_KW", 
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
    RULE_usingAlias = 16
    RULE_functionDefinition = 17
    RULE_parameters = 18
    RULE_parameter = 19
    RULE_cppBlock = 20
    RULE_returnStatement = 21
    RULE_assignmentOperator = 22
    RULE_assignment = 23
    RULE_assignableExpression = 24
    RULE_assignablePrimary = 25
    RULE_ifStatement = 26
    RULE_ifBlock = 27
    RULE_elseBlock = 28
    RULE_whileStatement = 29
    RULE_statement = 30
    RULE_blockStatement = 31
    RULE_deleteStatement = 32
    RULE_forStatement = 33
    RULE_forInit = 34
    RULE_forIncrement = 35
    RULE_methodSignature = 36
    RULE_interfaceDefinition = 37
    RULE_variableDeclaration_no_semicolon = 38
    RULE_assignment_no_semicolon = 39
    RULE_expression = 40
    RULE_unaryExpression = 41
    RULE_simpleExpression = 42
    RULE_primary = 43
    RULE_initializerList = 44
    RULE_functionCallExpression = 45
    RULE_expressionList = 46
    RULE_literal = 47

    ruleNames =  [ "typeSpecifier", "baseType", "typeList", "variableDeclaration", 
                   "templateArgument", "program", "topLevelStatement", "accessModifier", 
                   "classBodyStatement", "classDefinition", "structDefinition", 
                   "structBodyStatement", "methodDefinition", "initDefinition", 
                   "deinitBlock", "importDirective", "usingAlias", "functionDefinition", 
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
    USING=20
    UNIQUE_KW=21
    SHARED_KW=22
    WEAK_KW=23
    AT_MAKE_UNIQUE=24
    AT_MAKE_SHARED=25
    AT_MOVE=26
    BOOL_LITERAL=27
    NEW=28
    DELETE=29
    AT_CPP=30
    EQ=31
    NEQ=32
    LTE=33
    GTE=34
    ARROW=35
    AND_OP=36
    OR_OP=37
    LSHIFT=38
    RSHIFT=39
    PLUS=40
    MINUS=41
    STAR=42
    SLASH=43
    MODULO=44
    PLUS_ASSIGN=45
    MINUS_ASSIGN=46
    STAR_ASSIGN=47
    SLASH_ASSIGN=48
    MOD_ASSIGN=49
    LT=50
    GT=51
    NOT_OP=52
    BIT_AND=53
    BIT_OR=54
    BIT_XOR=55
    BIT_NOT=56
    INCLUDE_PATH=57
    SEMIC_TOKEN=58
    LPAREN=59
    RPAREN=60
    LBRACE=61
    RBRACE=62
    LBRACK=63
    RBRACK=64
    COLON=65
    ASSIGN=66
    DOT=67
    COMMA=68
    HEX_LITERAL=69
    BINARY_LITERAL=70
    OCTAL_LITERAL=71
    FLOAT_LITERAL=72
    DECIMAL_LITERAL=73
    BYTE_LITERAL=74
    IDENTIFIER=75
    STRING_LITERAL=76
    CHAR_LITERAL=77
    LINE_COMMENT=78
    WHITESPACE=79
    NEWLINE=80
    AT_END=81
    CPP_BODY=82

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
            self.state = 139
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [63]:
                self.enterOuterAlt(localctx, 1)
                self.state = 96
                self.match(ChronoParser.LBRACK)
                self.state = 97
                self.typeSpecifier()
                self.state = 98
                self.match(ChronoParser.SEMIC_TOKEN)
                self.state = 99
                self.expression()
                self.state = 100
                self.match(ChronoParser.RBRACK)
                self.state = 105
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 102
                        _la = self._input.LA(1)
                        if not(_la==42 or _la==53):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume() 
                    self.state = 107
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

                pass
            elif token in [21, 22, 23, 75]:
                self.enterOuterAlt(localctx, 2)
                self.state = 108
                self.baseType()
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==63:
                    self.state = 109
                    self.match(ChronoParser.LBRACK)
                    self.state = 110
                    self.typeList()
                    self.state = 111
                    self.match(ChronoParser.RBRACK)


                self.state = 118
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 115
                        _la = self._input.LA(1)
                        if not(_la==42 or _la==53):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume() 
                    self.state = 120
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                pass
            elif token in [59]:
                self.enterOuterAlt(localctx, 3)
                self.state = 121
                self.match(ChronoParser.LPAREN)
                self.state = 131
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 123
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if ((((_la - 21)) & ~0x3f) == 0 and ((1 << (_la - 21)) & 143838386023563335) != 0):
                        self.state = 122
                        localctx.params = self.typeList()


                    self.state = 125
                    self.match(ChronoParser.RPAREN)
                    self.state = 126
                    self.match(ChronoParser.ARROW)
                    self.state = 127
                    localctx.returnType = self.typeSpecifier()
                    pass

                elif la_ == 2:
                    self.state = 128
                    localctx.nested = self.typeSpecifier()
                    self.state = 129
                    self.match(ChronoParser.RPAREN)
                    pass


                self.state = 136
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 133
                        _la = self._input.LA(1)
                        if not(_la==42 or _la==53):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume() 
                    self.state = 138
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
            self.state = 152
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [75]:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.match(ChronoParser.IDENTIFIER)
                self.state = 146
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==67:
                    self.state = 142
                    self.match(ChronoParser.DOT)
                    self.state = 143
                    self.match(ChronoParser.IDENTIFIER)
                    self.state = 148
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
                self.match(ChronoParser.UNIQUE_KW)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 3)
                self.state = 150
                self.match(ChronoParser.SHARED_KW)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 4)
                self.state = 151
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
            self.state = 154
            self.templateArgument()
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==68:
                self.state = 155
                self.match(ChronoParser.COMMA)
                self.state = 156
                self.templateArgument()
                self.state = 161
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
            self.state = 162
            _la = self._input.LA(1)
            if not(_la==3 or _la==4):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 163
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==65:
                self.state = 164
                self.match(ChronoParser.COLON)
                self.state = 165
                localctx.typeName = self.typeSpecifier()


            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==66:
                self.state = 168
                self.match(ChronoParser.ASSIGN)
                self.state = 169
                self.expression()


            self.state = 172
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
            self.state = 176
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21, 22, 23, 59, 63, 75]:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.typeSpecifier()
                pass
            elif token in [27, 69, 70, 71, 72, 73, 74, 76, 77]:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
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
            self.state = 179 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 178
                self.topLevelStatement()
                self.state = 181 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1074923718) != 0)):
                    break

            self.state = 183
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
            self.state = 192
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 185
                self.importDirective()
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 2)
                self.state = 186
                self.cppBlock()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 187
                self.classDefinition()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 4)
                self.state = 188
                self.structDefinition()
                pass
            elif token in [2, 11]:
                self.enterOuterAlt(localctx, 5)
                self.state = 189
                self.functionDefinition()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 6)
                self.state = 190
                self.interfaceDefinition()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 7)
                self.state = 191
                self.usingAlias()
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
            self.state = 194
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
            self.state = 218
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 196
                    self.accessModifier()


                self.state = 199
                self.variableDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 208
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [11]:
                    self.state = 200
                    self.match(ChronoParser.STATIC)
                    self.state = 202
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==16:
                        self.state = 201
                        self.accessModifier()


                    pass
                elif token in [16]:
                    self.state = 204
                    self.accessModifier()
                    self.state = 206
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==11:
                        self.state = 205
                        self.match(ChronoParser.STATIC)


                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 210
                self.methodDefinition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 212
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 211
                    self.accessModifier()


                self.state = 214
                self.initDefinition()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 215
                self.methodDefinition()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 216
                self.deinitBlock()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 217
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
            self.state = 220
            self.match(ChronoParser.CLASS)
            self.state = 221
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 224
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==65:
                self.state = 222
                self.match(ChronoParser.COLON)
                self.state = 223
                localctx.base = self.match(ChronoParser.IDENTIFIER)


            self.state = 228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 226
                self.match(ChronoParser.IMPL)
                self.state = 227
                localctx.interfaces = self.typeList()


            self.state = 230
            self.match(ChronoParser.LBRACE)
            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1073810204) != 0):
                self.state = 231
                self.classBodyStatement()
                self.state = 236
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 237
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
            self.state = 239
            self.match(ChronoParser.STRUCT)
            self.state = 240
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 241
            self.match(ChronoParser.LBRACE)
            self.state = 245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1073808156) != 0):
                self.state = 242
                self.structBodyStatement()
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
            self.state = 264
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 251
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 250
                    self.accessModifier()


                self.state = 253
                self.variableDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 255
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 254
                    self.accessModifier()


                self.state = 257
                self.methodDefinition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 259
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 258
                    self.accessModifier()


                self.state = 261
                self.initDefinition()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 262
                self.deinitBlock()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 263
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
            self.state = 266
            self.match(ChronoParser.FUNC)
            self.state = 267
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 268
            self.match(ChronoParser.LPAREN)
            self.state = 269
            self.parameters()
            self.state = 270
            self.match(ChronoParser.RPAREN)
            self.state = 273
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 271
                self.match(ChronoParser.ARROW)
                self.state = 272
                localctx.returnType = self.typeSpecifier()


            self.state = 275
            self.match(ChronoParser.LBRACE)
            self.state = 279
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2967879853149312056) != 0) or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & 511) != 0):
                self.state = 276
                self.statement()
                self.state = 281
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 282
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
            self.state = 284
            self.match(ChronoParser.INIT)
            self.state = 285
            self.match(ChronoParser.LPAREN)
            self.state = 286
            self.parameters()
            self.state = 287
            self.match(ChronoParser.RPAREN)
            self.state = 288
            self.match(ChronoParser.LBRACE)
            self.state = 292
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2967879853149312056) != 0) or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & 511) != 0):
                self.state = 289
                self.statement()
                self.state = 294
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 295
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
            self.state = 297
            self.match(ChronoParser.DEINIT)
            self.state = 298
            self.match(ChronoParser.LBRACE)
            self.state = 302
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2967879853149312056) != 0) or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & 511) != 0):
                self.state = 299
                self.statement()
                self.state = 304
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 305
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
            self.state = 307
            self.match(ChronoParser.IMPORT)
            self.state = 308
            localctx.path = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==57 or _la==76):
                localctx.path = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 311
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 309
                self.match(ChronoParser.AS)
                self.state = 310
                localctx.alias = self.match(ChronoParser.IDENTIFIER)


            self.state = 313
            self.match(ChronoParser.SEMIC_TOKEN)
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
            self.state = 315
            self.match(ChronoParser.USING)
            self.state = 316
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 317
            self.match(ChronoParser.ASSIGN)
            self.state = 318
            localctx.typeName = self.typeSpecifier()
            self.state = 319
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
        self.enterRule(localctx, 34, self.RULE_functionDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 321
                self.match(ChronoParser.STATIC)


            self.state = 324
            self.match(ChronoParser.FUNC)
            self.state = 325
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 326
            self.match(ChronoParser.LPAREN)
            self.state = 327
            self.parameters()
            self.state = 328
            self.match(ChronoParser.RPAREN)
            self.state = 331
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 329
                self.match(ChronoParser.ARROW)
                self.state = 330
                localctx.returnType = self.typeSpecifier()


            self.state = 333
            self.match(ChronoParser.LBRACE)
            self.state = 337
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2967879853149312056) != 0) or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & 511) != 0):
                self.state = 334
                self.statement()
                self.state = 339
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 340
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
        self.enterRule(localctx, 36, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==75:
                self.state = 342
                self.parameter()
                self.state = 347
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==68:
                    self.state = 343
                    self.match(ChronoParser.COMMA)
                    self.state = 344
                    self.parameter()
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
        self.enterRule(localctx, 38, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 353
            self.match(ChronoParser.COLON)
            self.state = 354
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
        self.enterRule(localctx, 40, self.RULE_cppBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            self.match(ChronoParser.AT_CPP)
            self.state = 360
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==82:
                self.state = 357
                self.match(ChronoParser.CPP_BODY)
                self.state = 362
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 363
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
        self.enterRule(localctx, 42, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.match(ChronoParser.RETURN)
            self.state = 366
            self.expression()
            self.state = 367
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
        self.enterRule(localctx, 44, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            _la = self._input.LA(1)
            if not(((((_la - 45)) & ~0x3f) == 0 and ((1 << (_la - 45)) & 2097183) != 0)):
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
        self.enterRule(localctx, 46, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            self.assignableExpression()
            self.state = 372
            self.assignmentOperator()
            self.state = 373
            self.expression()
            self.state = 374
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
        self.enterRule(localctx, 48, self.RULE_assignableExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.assignablePrimary()
            self.state = 387
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 35)) & ~0x3f) == 0 and ((1 << (_la - 35)) & 4563402753) != 0):
                self.state = 385
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [67]:
                    self.state = 377
                    self.match(ChronoParser.DOT)
                    self.state = 378
                    self.match(ChronoParser.IDENTIFIER)
                    pass
                elif token in [63]:
                    self.state = 379
                    self.match(ChronoParser.LBRACK)
                    self.state = 380
                    self.expression()
                    self.state = 381
                    self.match(ChronoParser.RBRACK)
                    pass
                elif token in [35]:
                    self.state = 383
                    self.match(ChronoParser.ARROW)
                    self.state = 384
                    self.match(ChronoParser.IDENTIFIER)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 389
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
        self.enterRule(localctx, 50, self.RULE_assignablePrimary)
        try:
            self.state = 400
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [75]:
                self.enterOuterAlt(localctx, 1)
                self.state = 390
                self.match(ChronoParser.IDENTIFIER)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 391
                self.match(ChronoParser.THIS)
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 3)
                self.state = 392
                self.match(ChronoParser.STAR)
                self.state = 393
                self.assignablePrimary()
                pass
            elif token in [53]:
                self.enterOuterAlt(localctx, 4)
                self.state = 394
                self.match(ChronoParser.BIT_AND)
                self.state = 395
                self.assignablePrimary()
                pass
            elif token in [59]:
                self.enterOuterAlt(localctx, 5)
                self.state = 396
                self.match(ChronoParser.LPAREN)
                self.state = 397
                self.assignableExpression()
                self.state = 398
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
        self.enterRule(localctx, 52, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            self.match(ChronoParser.IF)
            self.state = 403
            self.match(ChronoParser.LPAREN)
            self.state = 404
            self.expression()
            self.state = 405
            self.match(ChronoParser.RPAREN)
            self.state = 406
            localctx.if_block = self.ifBlock()
            self.state = 412
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 407
                self.match(ChronoParser.ELSE)
                self.state = 410
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [12]:
                    self.state = 408
                    localctx.else_if = self.ifStatement()
                    pass
                elif token in [61]:
                    self.state = 409
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
        self.enterRule(localctx, 54, self.RULE_ifBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
            self.match(ChronoParser.LBRACE)
            self.state = 418
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2967879853149312056) != 0) or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & 511) != 0):
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
        self.enterRule(localctx, 56, self.RULE_elseBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 423
            self.match(ChronoParser.LBRACE)
            self.state = 427
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2967879853149312056) != 0) or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & 511) != 0):
                self.state = 424
                self.statement()
                self.state = 429
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 430
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
        self.enterRule(localctx, 58, self.RULE_whileStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            self.match(ChronoParser.WHILE)
            self.state = 433
            self.match(ChronoParser.LPAREN)
            self.state = 434
            self.expression()
            self.state = 435
            self.match(ChronoParser.RPAREN)
            self.state = 436
            self.match(ChronoParser.LBRACE)
            self.state = 440
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2967879853149312056) != 0) or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & 511) != 0):
                self.state = 437
                self.statement()
                self.state = 442
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 443
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
        self.enterRule(localctx, 60, self.RULE_statement)
        try:
            self.state = 457
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 445
                self.variableDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 446
                self.assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 447
                self.returnStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 448
                self.expression()
                self.state = 449
                self.match(ChronoParser.SEMIC_TOKEN)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 451
                self.cppBlock()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 452
                self.ifStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 453
                self.whileStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 454
                self.deleteStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 455
                self.forStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 456
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
        self.enterRule(localctx, 62, self.RULE_blockStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 459
            self.match(ChronoParser.LBRACE)
            self.state = 463
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2967879853149312056) != 0) or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & 511) != 0):
                self.state = 460
                self.statement()
                self.state = 465
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 466
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
        self.enterRule(localctx, 64, self.RULE_deleteStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            self.match(ChronoParser.DELETE)
            self.state = 469
            self.expression()
            self.state = 470
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
        self.enterRule(localctx, 66, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472
            self.match(ChronoParser.FOR)
            self.state = 473
            self.match(ChronoParser.LPAREN)
            self.state = 475
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 585472349604676632) != 0) or _la==75:
                self.state = 474
                localctx.init = self.forInit()


            self.state = 477
            self.match(ChronoParser.SEMIC_TOKEN)
            self.state = 479
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2967879851538646016) != 0) or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & 511) != 0):
                self.state = 478
                localctx.cond = self.expression()


            self.state = 481
            self.match(ChronoParser.SEMIC_TOKEN)
            self.state = 483
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2967879851538646016) != 0) or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & 511) != 0):
                self.state = 482
                localctx.incr = self.forIncrement()


            self.state = 485
            self.match(ChronoParser.RPAREN)
            self.state = 486
            self.match(ChronoParser.LBRACE)
            self.state = 490
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2967879853149312056) != 0) or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & 511) != 0):
                self.state = 487
                self.statement()
                self.state = 492
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 493
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
        self.enterRule(localctx, 68, self.RULE_forInit)
        try:
            self.state = 497
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 495
                self.variableDeclaration_no_semicolon()
                pass
            elif token in [10, 42, 53, 59, 75]:
                self.enterOuterAlt(localctx, 2)
                self.state = 496
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
        self.enterRule(localctx, 70, self.RULE_forIncrement)
        try:
            self.state = 501
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 499
                self.assignment_no_semicolon()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 500
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
        self.enterRule(localctx, 72, self.RULE_methodSignature)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 503
            self.match(ChronoParser.FUNC)
            self.state = 504
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 505
            self.match(ChronoParser.LPAREN)
            self.state = 506
            self.parameters()
            self.state = 507
            self.match(ChronoParser.RPAREN)
            self.state = 510
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 508
                self.match(ChronoParser.ARROW)
                self.state = 509
                localctx.returnType = self.typeSpecifier()


            self.state = 512
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
        self.enterRule(localctx, 74, self.RULE_interfaceDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 514
            self.match(ChronoParser.INTERFACE)
            self.state = 515
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 516
            self.match(ChronoParser.LBRACE)
            self.state = 521
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2 or _la==30:
                self.state = 519
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [2]:
                    self.state = 517
                    self.methodSignature()
                    pass
                elif token in [30]:
                    self.state = 518
                    self.cppBlock()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 523
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 524
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
        self.enterRule(localctx, 76, self.RULE_variableDeclaration_no_semicolon)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 526
            _la = self._input.LA(1)
            if not(_la==3 or _la==4):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 527
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 530
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==65:
                self.state = 528
                self.match(ChronoParser.COLON)
                self.state = 529
                localctx.typeName = self.typeSpecifier()


            self.state = 534
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==66:
                self.state = 532
                self.match(ChronoParser.ASSIGN)
                self.state = 533
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
        self.enterRule(localctx, 78, self.RULE_assignment_no_semicolon)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 536
            self.assignableExpression()
            self.state = 537
            self.assignmentOperator()
            self.state = 538
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
        self.enterRule(localctx, 80, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 540
            self.unaryExpression()
            self.state = 545
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 66463242368581632) != 0):
                self.state = 541
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 66463242368581632) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 542
                self.unaryExpression()
                self.state = 547
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
        self.enterRule(localctx, 82, self.RULE_unaryExpression)
        self._la = 0 # Token type
        try:
            self.state = 555
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [40, 41, 52, 56]:
                self.enterOuterAlt(localctx, 1)
                self.state = 548
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 76564492200181760) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 549
                self.unaryExpression()
                pass
            elif token in [53]:
                self.enterOuterAlt(localctx, 2)
                self.state = 550
                self.match(ChronoParser.BIT_AND)
                self.state = 551
                self.unaryExpression()
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 3)
                self.state = 552
                self.match(ChronoParser.STAR)
                self.state = 553
                self.unaryExpression()
                pass
            elif token in [10, 24, 25, 26, 27, 28, 59, 61, 69, 70, 71, 72, 73, 74, 75, 76, 77]:
                self.enterOuterAlt(localctx, 4)
                self.state = 554
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
        self.enterRule(localctx, 84, self.RULE_simpleExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 559
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
            if la_ == 1:
                self.state = 557
                self.primary()
                pass

            elif la_ == 2:
                self.state = 558
                self.functionCallExpression()
                pass


            self.state = 591
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 35)) & ~0x3f) == 0 and ((1 << (_la - 35)) & 4563402753) != 0):
                self.state = 589
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [67]:
                    self.state = 561
                    self.match(ChronoParser.DOT)
                    self.state = 562
                    self.match(ChronoParser.IDENTIFIER)
                    self.state = 567
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
                    if la_ == 1:
                        self.state = 563
                        self.match(ChronoParser.LBRACK)
                        self.state = 564
                        self.typeList()
                        self.state = 565
                        self.match(ChronoParser.RBRACK)


                    self.state = 574
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==59:
                        self.state = 569
                        self.match(ChronoParser.LPAREN)
                        self.state = 571
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2967879851538646016) != 0) or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & 511) != 0):
                            self.state = 570
                            self.expressionList()


                        self.state = 573
                        self.match(ChronoParser.RPAREN)


                    pass
                elif token in [63]:
                    self.state = 576
                    self.match(ChronoParser.LBRACK)
                    self.state = 577
                    self.expression()
                    self.state = 578
                    self.match(ChronoParser.RBRACK)
                    pass
                elif token in [35]:
                    self.state = 580
                    self.match(ChronoParser.ARROW)
                    self.state = 581
                    self.match(ChronoParser.IDENTIFIER)
                    self.state = 587
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==59:
                        self.state = 582
                        self.match(ChronoParser.LPAREN)
                        self.state = 584
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2967879851538646016) != 0) or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & 511) != 0):
                            self.state = 583
                            self.expressionList()


                        self.state = 586
                        self.match(ChronoParser.RPAREN)


                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 593
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
        self.enterRule(localctx, 86, self.RULE_primary)
        self._la = 0 # Token type
        try:
            self.state = 620
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 594
                self.match(ChronoParser.NEW)
                self.state = 595
                self.baseType()
                self.state = 596
                self.match(ChronoParser.LPAREN)
                self.state = 598
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2967879851538646016) != 0) or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & 511) != 0):
                    self.state = 597
                    self.expressionList()


                self.state = 600
                self.match(ChronoParser.RPAREN)
                pass
            elif token in [24, 25]:
                self.enterOuterAlt(localctx, 2)
                self.state = 602
                _la = self._input.LA(1)
                if not(_la==24 or _la==25):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 603
                self.match(ChronoParser.LBRACK)
                self.state = 604
                self.typeSpecifier()
                self.state = 605
                self.match(ChronoParser.RBRACK)
                self.state = 606
                self.match(ChronoParser.LPAREN)
                self.state = 608
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2967879851538646016) != 0) or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & 511) != 0):
                    self.state = 607
                    self.expressionList()


                self.state = 610
                self.match(ChronoParser.RPAREN)
                pass
            elif token in [27, 69, 70, 71, 72, 73, 74, 76, 77]:
                self.enterOuterAlt(localctx, 3)
                self.state = 612
                self.literal()
                pass
            elif token in [61]:
                self.enterOuterAlt(localctx, 4)
                self.state = 613
                self.initializerList()
                pass
            elif token in [75]:
                self.enterOuterAlt(localctx, 5)
                self.state = 614
                self.match(ChronoParser.IDENTIFIER)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 6)
                self.state = 615
                self.match(ChronoParser.THIS)
                pass
            elif token in [59]:
                self.enterOuterAlt(localctx, 7)
                self.state = 616
                self.match(ChronoParser.LPAREN)
                self.state = 617
                self.expression()
                self.state = 618
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
        self.enterRule(localctx, 88, self.RULE_initializerList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 622
            self.match(ChronoParser.LBRACE)
            self.state = 624
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2967879851538646016) != 0) or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & 511) != 0):
                self.state = 623
                self.expressionList()


            self.state = 626
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
        self.enterRule(localctx, 90, self.RULE_functionCallExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 628
            localctx.funcName = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==26 or _la==75):
                localctx.funcName = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 629
            self.match(ChronoParser.LPAREN)
            self.state = 631
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2967879851538646016) != 0) or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & 511) != 0):
                self.state = 630
                self.expressionList()


            self.state = 633
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
        self.enterRule(localctx, 92, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 635
            self.expression()
            self.state = 640
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==68:
                self.state = 636
                self.match(ChronoParser.COMMA)
                self.state = 637
                self.expression()
                self.state = 642
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
        self.enterRule(localctx, 94, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 643
            _la = self._input.LA(1)
            if not(((((_la - 27)) & ~0x3f) == 0 and ((1 << (_la - 27)) & 1965926790463489) != 0)):
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





