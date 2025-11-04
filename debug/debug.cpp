#include "ChronoInt.h"
#include "ChronoObject.h"
#include "ChronoString.h"

class AccessTest : public ChronoObject {
private:
  int32_t val;
  ChronoString *name;

  AccessTest(int32_t v, ChronoString *n) {
    Print(ChronoString::create("Init (Private)"));
    this->val = v;
    this->name = n;
    this->name->retain();
    // --- Method End ---
  }

  int32_t doInternalCalc() {
    Print(ChronoString::create("Private Method: doInternalCalc()"));
    return this->val * 2;
    // --- Method End ---
  }

public:
  virtual ~AccessTest() {
    // --- Chrono Deinit Block ---
    Print(ChronoString::create("Deinit (Public)"));
    this->name->release();
    // --- Deinit End ---
  }

  ChronoInt *getCalculatedValue() {
    Print(ChronoString::create("Public Method: getCalculatedValue()"));
    int32_t result = this->doInternalCalc();
    return ChronoInt::create(result);
    // --- Method End ---
  }

  static AccessTest *create(int32_t v, ChronoString *n) {
    Print(ChronoString::create("Public Static: create()"));
    return new AccessTest(v, n);
    // --- Method End ---
  }
};

int Chrono_main() {
  Print(ChronoString::create("--- Test Start ---"));
  ChronoString *s = ChronoString::create("Test");
  AccessTest *obj = AccessTest::create(10, s);
  ChronoInt *val_obj = obj->getCalculatedValue();
  Print(ChronoString::create("Final Value:"));
  Print(val_obj);
  s->release();
  obj->release();
  val_obj->release();
  Print(ChronoString::create("--- Test End ---"));
  return 0;
}

// C++ 程序的标准入口
int main() { return Chrono_main(); }
