#include "Chrono.h"
#include "ChronoInt.h"
#include "ChronoObject.h"
#include "ChronoString.h"

class AccessTest : public ChronoObject {
private:
  int32_t val;
  String *_name;

  AccessTest(int32_t v, String *_n) {
    Chrono::log("Init (Private)");
    this->val = v;
    this->name = _n;
    this->name->retain();
  }

  int32_t doInternalCalc() {
    Chrono::log("Private Method: doInternalCalc()");
    return this->val * 2;
    // --- Method End ---
  }

public:
  virtual ~AccessTest() {
    // --- Chrono Deinit Block ---
    Chrono::log("Deinit (Public)");
    this->name->release();
    // --- Deinit End ---
  }

  Int *getCalculatedValue() {
    Chrono::log("Public Method: getCalculatedValue()");
    int32_t result = this->doInternalCalc();
    return Int::create(result);
    // --- Method End ---
  }

  static AccessTest *create(int32_t v, String *_n) {
    Chrono::log("Public Static: create()");
    return new AccessTest(v, _n);
    // --- Method End ---
  }
};

int main() {
  Chrono::log("--- Test Start ---");
  String *_s = String::create("Test");
  AccessTest *_obj = AccessTest::create(10, _s);
  Int *_val_obj = _obj->getCalculatedValue();
  Chrono::log("Final Value:");
  Chrono::log(_val_obj);
  _s->release();
  _obj->release();
  _val_obj->release();
  Chrono::log("--- Test End ---");
  return 0;
}
