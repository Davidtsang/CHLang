import "Chrono.h";
import "runtime/ChronoObject.h";
import "runtime/ChronoString.h";

func main() -> int {
    let a: i32 = 10;
    let b: i32 = 5;
    let c: i32 = 10;

    Chrono.log("--- Testing Comparisons ---");

    // Test 1: Greater Than (10 > 5 => true)
    if (a > b) { Chrono.log("T1: GT-PASS"); }

    // Test 2: Less Than (10 < 5 => false)
    if (a < b) { Chrono.log("T2: LT-FAIL"); } else { Chrono.log("T2: LT-PASS"); }

    // Test 3: Equals (10 == 10 => true)
    if (a == c) { Chrono.log("T3: EQ-PASS"); }

    // Test 4: Not Equals (10 != 5 => true)
    if (a != b) { Chrono.log("T4: NEQ-PASS"); }

    // Test 5: Greater Than or Equal (10 >= 10 => true)
    if (a >= c) { Chrono.log("T5: GTE-PASS"); }

    // Test 6: Less Than or Equal (10 <= 5 => false)
    if (a <= b) { Chrono.log("T6: LTE-FAIL"); } else { Chrono.log("T6: LTE-PASS"); }

    return 0;
}