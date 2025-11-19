#pragma once
import <windows.h>

// 声明用户必须提供的 "CHMain"
func CHMain() -> int;

// 声明全局变量
extern var g_hInstance: HINSTANCE;
extern var g_nCmdShow: int;