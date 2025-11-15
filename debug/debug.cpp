#include "Chrono.h"
#include "ChronoObject.h"
#include "ChronoString.h"
#include "ChronoInt.h"

class AccessTest : public ChronoObject {
private:
  int32_t val;
  String *name = nullptr;
  AccessTest(int32_t v, String *n);
  virtual int32_t doInternalCalc();

public:
  virtual ~AccessTest();
  virtual Int *getCalculatedValue();
  virtual AccessTest *create(int32_t v, String *n);
};

AccessTest::AccessTest(int32_t v, String *n) {
  Chrono::log("Init (Private)");
  this.val = v;
  this.name = n;
  this.name.retain();
}

AccessTest::~AccessTest() {
  // --- Chrono Deinit Block ---
  Chrono::log("Deinit (Public)");
  this.name.release();
  // --- Deinit End ---
}

int32_t AccessTest::doInternalCalc() {
  Chrono::log("Private Method: doInternalCalc()");
  return this.val * 2;
  // --- Method End ---
}

Int *AccessTest::getCalculatedValue() {
  Chrono::log("Public Method: getCalculatedValue()");
  int32_t result = this.doInternalCalc();
  return Int::create(result);
  // --- Method End ---
}

AccessTest *AccessTest::create(int32_t v, String *n) {
  Chrono::log("Public Static: create()");
  return new AccessTest(v, n);
  // --- Method End ---
}
