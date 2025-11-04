#include "ChronoInt.h"
#include "ChronoObject.h"
#include "ChronoString.h"
#include <iostream>

class MemberTest : public ChronoObject {
private:
  int32_t x;
  ChronoString *s;
  ChronoString *name;

  MemberTest(int32_t val, ChronoString *str) {
    this->x = val;
    this->s = str;
    this->s->retain();
  }

  ChronoString *getName() {
    return this->name;
    // --- Method End ---
  }

public:
  virtual ~MemberTest() {
    // --- Chrono Deinit Block ---

    // --- @cpp Block Start ---
    std::cout << "DEINIT" << std::endl;
    // --- @cpp Block End ---

    this->s->release();
    // --- Deinit End ---
  }

  void printAll() {
    Print(this->x);
    Print(this->s);
    // --- Method End ---
  }

  static MemberTest *create(int32_t val, ChronoString *str) {
    return new MemberTest(val, str);
    // --- Method End ---
  }
};

int Chrono_main() {
  ChronoString *s = ChronoString::create("Hello");
  MemberTest *obj = MemberTest::create(100, s);
  obj->printAll();
  obj->release();
  s->release();
  return 0;
}

// C++ 程序的标准入口
int main() { return Chrono_main(); }
