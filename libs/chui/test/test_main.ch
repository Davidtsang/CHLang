import "chui/Chui"
import "runtime/CH.h"

func main() -> int {
    CH::Log("--- Testing Library chui ---");
    var obj: Chui* = new Chui("Chrono");
    obj->greet();
    obj->release();
    return 0;
}
