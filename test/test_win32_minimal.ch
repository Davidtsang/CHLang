// file: test/test_win32_minimal.ch
// 目的:
// 1. 验证 'typemap' (字面量代换)
// 2. 验证 'using' (类型别名)
// 3. [已修复] 添加缺失的 import (functional, vector)
// 4. [已修复] 重命名冲突的 WinMain 函数

// --- 1. 导入 (修复: 添加 functional 和 vector) ---
import <windows.h>
import <iostream>
import <functional> // [ [ [ 修复 1 ] ] ] (解决 'std::function' 错误)
import <vector>     // [ [ [ 修复 2 ] ] ] (解决 'std::vector' 错误)
import "runtime/ChronoObject.h" // (用于 main)

// --- 2. 链接 Win32 库 (如果需要调用 API) ---

#pragma comment(lib, "Kernel32.lib")


// --- 3. 使用 'typemap' (字面量代换) ---
// (用于 C++ 互操作性)
#define  C_LRESULT_CALLBACK LRESULT CALLBACK
#define C_IN_HINSTANCE _In_ HINSTANCE
#define C_INT_WINAPI int WINAPI
#define C_HWND HWND
#define C_UINT UINT
#define C_INT int


// --- 4. 使用 'using' (Chrono 类型别名) ---
// (只用于纯 Chrono 类型)
// (这些行是导致 C2039 错误的原因)
using MyInt = i32;

using AddFunc = (i32) -> i32;
using IntVector = std.vector<i32>;

// --- 5. 编写 Chrono 函数 (100% 干净) ---

func WindowProc(
    hwnd: C_HWND
) -> C_LRESULT_CALLBACK
{
    return 0;
}

// [ [ [ 修复 3 ] ] ]
// (解决 C2731 'WinMain' 重载错误)
// 必须重命名此函数，以避免与 <windows.h> 中的 WinMain 冲突
func MyChronoWinMainTest(
    hInstance: C_IN_HINSTANCE,
    nCmdShow: C_INT,
    myCount: MyInt
) -> C_INT_WINAPI
{
    @cpp
        std::cout << "MyChronoWinMainTest function compiled." << std::endl;
    @end
    return 0;
}

// --- 6. Chrono 入口点 ---
func main() -> int {
    @cpp
        std::cout << "--- Win32 Minimal Test ---" << std::endl;
    @end

    // 调用我们修复后的函数
    MyChronoWinMainTest(0, 0, 10);

    @cpp
        std::cout << "Test passed (Compilation)." << std::endl;
    @end
    return 0;
}