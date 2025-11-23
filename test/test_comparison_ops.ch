import "CH.h"
import "runtime/CHObject.h"
import "runtime/CHString.h"

func main() -> int {
    var a: i32 = 10;
    var b: i32 = 5;
    var c: i32 = 10;

    CH::log("--- Testing Comparisons ---");

    // Test 1: Greater Than (10 > 5 => true)
    if (a > b) { CH::log("T1: GT-PASS"); }

    // Test 2: Less Than (10 < 5 => false)
    if (a < b) { CH::log("T2: LT-FAIL"); } else { CH::log("T2: LT-PASS"); }

    // Test 3: Equals (10 == 10 => true)
    if (a == c) { CH::log("T3: EQ-PASS"); }

    // Test 4: Not Equals (10 != 5 => true)
    if (a != b) { CH::log("T4: NEQ-PASS"); }

    // Test 5: Greater Than or Equal (10 >= 10 => true)
    if (a >= c) { CH::log("T5: GTE-PASS"); }

    // Test 6: Less Than or Equal (10 <= 5 => false)
    if (a <= b) { CH::log("T6: LTE-FAIL"); } else { CH::log("T6: LTE-PASS"); }

    return 0;
}