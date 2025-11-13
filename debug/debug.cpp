#include "ChronoObject.h"
#include <cstdint>
#include <iostream>
#include <type_traits>
#include <windows.h>

int main() {

  // --- @cpp Block Start ---
  std::cout << "--- C++ Casts Test ---" << std::endl;
  // --- @cpp Block End ---

  auto f = static_cast<float>(10);

  // --- @cpp Block Start ---
  std::cout << "Test 1 (static_cast[f32]): " << f << std::endl;
  static_assert(std::is_same_v<decltype(f), float>, "static_cast[f32] failed");
  // --- @cpp Block End ---

  auto h = static_cast<HBRUSH>(C_COLOR_WINDOW + 1);

  // --- @cpp Block Start ---
  std::cout << "Test 2 (static_cast[C_HBRUSH]): (Compiled)" << std::endl;
  // [ [ [ 修复 2 ] ] ]
  // 在 @cpp 块内部, 我们 *必须* 使用 C++ 的真实类型
  static_assert(std::is_same_v<decltype(h), HBRUSH>,
                "static_cast<C_HBRUSH> failed");
  // --- @cpp Block End ---

  int32_t i = 12345;
  auto p = reinterpret_cast<intptr_t>(&i);

  // --- @cpp Block Start ---
  std::cout << "Test 3 (reinterpret_cast): (Compiled)" << std::endl;
  // [ [ [ 修复 3 ] ] ]
  // 必须使用 C++ 的 intptr_t, 而不是 Chrono 的 C_INT_PTR
  static_assert(std::is_same_v<decltype(p), intptr_t>,
                "reinterpret_cast failed");
  // --- @cpp Block End ---

  const int32_t x = 50;
  auto y = const_cast<int32_t *>(&x);
  (*y) = 100;

  // --- @cpp Block Start ---
  std::cout << "Test 4 (const_cast): New value at *y = " << *y << std::endl;
  static_assert(std::is_same_v<decltype(y), int32_t *>, "const_cast failed");
  // --- @cpp Block End ---

  // --- @cpp Block Start ---
  std::cout << "--- Test Passed ---" << std::endl;
  // --- @cpp Block End ---

  return 0;
}
