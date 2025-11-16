#pragma once
#include <windows.h>

// [ [ [ 关键 ] ] ]
// 将 WinMain.cpp 中定义的全局变量声明为 'extern'，
// 以便 Application.cpp 可以在链接时找到它们。

@cpp
extern HINSTANCE g_hInstance;
extern int g_nCmdShow;
@end