import "Reflection"
import "CHSelector.h" // 引用运行时哈希宏

implement Reflection {
    func getSelector(name: std::string) -> u64 {
        @cpp return static_cast<uint64_t>(_CalcHash(name)); @end
    }
}