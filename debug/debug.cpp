#include "Chrono.h"
#include <iostream>
#include <string>

int main() {
  std::string s = "Hello";
  std::string::reverse_iterator it1;
  s.push_back("s");

  // --- @cpp Block Start ---
  std::cout << s << std::endl;
  // --- @cpp Block End ---

  return 0;
}
