#include "ChronoObject.h"
#include "ChronoString.h"

class MRCClass : public ChronoObject {
private:
  MRCClass() { Print("MRC Init"); }

public:
  virtual ~MRCClass() {
    // --- Chrono Deinit Block ---
    Print("MRC Deinit");
    // --- Deinit End ---
  }

  static MRCClass *create() {
    return new MRCClass();
    // --- Method End ---
  }
};

class NativeClass {
private:
  NativeClass() { Print("Native Init"); }

public:
  static NativeClass *create() {
    return new NativeClass();
    // --- Method End ---
  }
};

int main() {
  Print("--- Test Start ---");
  MRCClass *objA = MRCClass::create();
  Print("A: MRC object created (Factory).");
  objA->release();
  NativeClass *objB = NativeClass::create();
  Print("B: Native object created (Factory).");
  delete objB;
  Print("B: Native object deleted (explicit DELETE).");
  Print("--- Test End ---");
  return 0;
}
