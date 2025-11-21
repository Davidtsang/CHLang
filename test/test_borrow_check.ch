// file: test/test_borrow_check.ch
import <iostream>
import <memory>

struct Box {
    public var id: int;
}

implement Box {
    // 默认构造函数
}

func main() -> int {
    @cpp std::cout << "--- Chrono Borrow Checker Test ---" << std::endl; @end

    // ==========================================
    // 场景 1: 线性移动检查 (Linear Check)
    // ==========================================
    var a: unique<Box> = @make<Box>();
    a->id = 100;
    @cpp std::cout << "[1] Created Box A (id=100)" << std::endl; @end

    // 移动 a -> b
    var b = @move(a);
    @cpp std::cout << "[1] Moved A to B. A is now empty." << std::endl; @end

    // [验证 A]: 访问已移动变量
    // 取消下面这行的注释，应该报错: "Use of moved variable 'a'"
    //a->id = 200;


    // ==========================================
    // 场景 2: 循环安全墙 (Loop Safety Wall)
    // ==========================================
    var outer_var: unique<Box> = @make<Box>();
    outer_var->id = 300;

    var i: int = 0;
    while (i < 1) {
        @cpp std::cout << "[2] Inside Loop..." << std::endl; @end

        // [验证 B]: 在循环内使用普通 @move 移动外部变量
        // 取消下面这行的注释，应该报错: "Cannot safely @move('outer_var') inside a loop"
        //var temp = @move(outer_var);

        // [验证 C]: 使用 @unsafe_move 强制移动
        // 编译器应该放行，但 outer_var 状态变为 Moved
        var forced = @unsafe_move(outer_var);
        @cpp std::cout << "[2] Unsafe move executed." << std::endl; @end

        i = i + 1;
    }

    // [验证 D]: 循环出来后，outer_var 应该是 Moved 状态
    // 取消下面这行的注释，应该报错: "Use of moved variable 'outer_var'"
    // outer_var->id = 400;


    // ==========================================
    // 场景 3: 变量复活 (Revival via Reassignment)
    // ==========================================
    // outer_var 目前是尸体 (Moved)。我们给它注入新生命。
    //outer_var = @make<Box>();
    //outer_var->id = 500;

    // [验证 E]: 复活后应该可以正常访问
    //@cpp std::cout << "[3] Revived outer_var. New ID: " << outer_var->id << std::endl; @end


    // ==========================================
    // 场景 4: 条件分支安全墙 (If Safety Wall)
    // ==========================================
    var cond_var: unique<Box> = @make<Box>();

    if (true) {
        // [验证 F]: 在 If 内使用普通 @move 移动外部变量
        // 取消下面这行的注释，应该报错: "Cannot safely @move('cond_var') inside a loop or conditional block"
        // var temp2 = @move(cond_var);

        // 内部定义的变量可以随意 move
        var inner: unique<Box> = @make<Box>();
        var temp3 = @move(inner); // 这是安全的，因为 inner 定义在当前层级
    }

    @cpp std::cout << "--- Test Finished Successfully ---" << std::endl; @end
    return 0;
}