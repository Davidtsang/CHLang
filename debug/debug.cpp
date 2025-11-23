#include <iostream>
#include <memory>

struct Box {
public:
  // Line 6
  int id;
};

// Line 13 (func main)
int main() {

  // --- @cpp Block Start ---
  std::cout << "--- CH Borrow Checker Test ---" << std::endl;
  // --- @cpp Block End ---

  // Line 19
  std::unique_ptr<Box> a = std::make_unique<Box>();
  // Line 20
  a->id = 100;

  // --- @cpp Block Start ---
  std::cout << "[1] Created Box A (id=100)" << std::endl;
  // --- @cpp Block End ---

  // Line 24
  auto b = std::move(a);

  // --- @cpp Block Start ---
  std::cout << "[1] Moved A to B. A is now empty." << std::endl;
  // --- @cpp Block End ---

  // Line 29
  a->id = 200;
  // Line 35
  std::unique_ptr<Box> outer_var = std::make_unique<Box>();
  // Line 36
  outer_var->id = 300;
  // Line 38
  int i = 0;
  while (i < 1) {

    // --- @cpp Block Start ---
    std::cout << "[2] Inside Loop..." << std::endl;
    // --- @cpp Block End ---

    // Line 48
    auto forced = std::move(outer_var);

    // --- @cpp Block Start ---
    std::cout << "[2] Unsafe move executed." << std::endl;
    // --- @cpp Block End ---

    // Line 51
    i = i + 1;
  }
  // Line 63
  outer_var = std::make_unique<Box>();
  // Line 64
  outer_var->id = 500;

  // --- @cpp Block Start ---
  std::cout << "[3] Revived outer_var. New ID: " << outer_var->id << std::endl;
  // --- @cpp Block End ---

  // Line 73
  std::unique_ptr<Box> cond_var = std::make_unique<Box>();
  if (true) {
    // Line 81
    std::unique_ptr<Box> inner = std::make_unique<Box>();
    // Line 82
    auto temp3 = std::move(inner);
  }

  // --- @cpp Block Start ---
  std::cout << "--- Test Finished Successfully ---" << std::endl;
  // --- @cpp Block End ---

  // Line 86
  return 0;
  // --- Function End ---
}