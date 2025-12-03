// libs/chui/include/chui/Base64.h.ch
#pragma once

import <string>
import <vector>
import <cctype> // 用于 isalnum

namespace CH.Utils;

// [C++17] inline 变量：保证在头文件中定义全局常量不会冲突
inline const base64_chars: std::string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";

// [C++17] inline 函数：允许函数体直接写在头文件里
inline func is_base64(c: u8) -> bool {
    // Chrono 直接透传调用 C 标准库
    return (isalnum(c) || (c == '+') || (c == '/'));
}

inline func Base64Decode(encoded_string: std::string) -> std::vector<u8> {
    var in_len: i32 = static_cast<i32>(encoded_string.length());
    var i: i32 = 0;
    var j: i32 = 0;
    var in_: i32 = 0;
    
    // C 风格数组
    var char_array_4: [u8; 4];
    var char_array_3: [u8; 3];
    
    var ret: std::vector<u8>;

    // 逻辑与 C++ 版本完全一致
    while (in_len > 0 && encoded_string[in_] != '=' && is_base64(encoded_string[in_])) {
        in_len = in_len - 1;
        
        char_array_4[i] = encoded_string[in_];
        i = i + 1;
        in_ = in_ + 1;

        if (i == 4) {
            for (j = 0; j < 4; j = j + 1) {
                char_array_4[j] = static_cast<u8>(base64_chars.find(char_array_4[j]));
            }

            char_array_3[0] = (char_array_4[0] << 2) + ((char_array_4[1] & 0x30) >> 4);
            char_array_3[1] = ((char_array_4[1] & 0xf) << 4) + ((char_array_4[2] & 0x3c) >> 2);
            char_array_3[2] = ((char_array_4[2] & 0x3) << 6) + char_array_4[3];

            for (j = 0; j < 3; j = j + 1) {
                ret.push_back(char_array_3[j]); // 注意这里其实是 char_array_3[j]，原C++代码里可能是j
            }
            i = 0;
        }
    }

    if (i > 0) {
        for (j = i; j < 4; j = j + 1) {
            char_array_4[j] = 0;
        }

        for (j = 0; j < 4; j = j + 1) {
            char_array_4[j] = static_cast<u8>(base64_chars.find(char_array_4[j]));
        }

        char_array_3[0] = (char_array_4[0] << 2) + ((char_array_4[1] & 0x30) >> 4);
        char_array_3[1] = ((char_array_4[1] & 0xf) << 4) + ((char_array_4[2] & 0x3c) >> 2);
        char_array_3[2] = ((char_array_4[2] & 0x3) << 6) + char_array_4[3];

        for (j = 0; j < (i - 1); j = j + 1) {
            ret.push_back(char_array_3[j]);
        }
    }

    return ret;
}

endnamespace;