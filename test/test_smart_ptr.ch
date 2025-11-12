// file: test/test_cpp_smart_pointers.ch
// 目的: 验证 Chrono 语法对 C++ 原生智能指针的调用
//
// 验证:
// - 泛型调用: std.make_shared[T]()
// - 泛型类型: var p: std::shared_ptr[T];
// - Chrono 原生 . 访问: p.use_count()
// - Chrono 原生 -> 访问: p->member

import <iostream>; // 用于 @cpp std::cout
import <memory>;   // 用于 std::make_unique, std::make_shared
import <string>;   // 用于 std::string
import <utility>;  // 用于 std::move

// --- 1. 独占指针 (std::unique_ptr) ---

// 用于测试的 "哑巴" struct (非侵入式)
struct Resource {
    var id: i32;
    init(i: i32) {
        this.id = i;
     }
    deinit {
     }
}

func demo_unique_ptr() {

    { // 创建内部作用域
        // 1a. 创建 (C++: auto ptr1 = std::make_unique<Resource>(1);)
        var ptr1 = std.make_unique[Resource](1);

        // 1b. [验证 -> 访问]
        // 使用 Chrono 的 -> 语法从智能指针读取值
        var id_val: i32 = ptr1->id;
        @cpp
            std::cout << "  ptr1 points to Resource " << id_val << std::endl;
        @end

        // 1c. 转移所有权 (C++: auto ptr2 = std::move(ptr1);)
        var ptr2 = std.move(ptr1);

        // 1d. 验证 ptr1 已失效
        @cpp
            if (ptr1 == nullptr) {
                std::cout << "  ptr1 is now null after move." << std::endl;
            }
        @end

        @cpp std::cout << "  Inner scope ending (ptr2 dies)..." << std::endl; @end
    } // <-- ptr2 在此离开作用域. Resource 1 应该被销毁.
}


// --- 2. 共享指针 (std::shared_ptr) ---
func demo_shared_ptr() {
    @cpp std::cout << "\n--- 2. std::shared_ptr Demo ---\n" << std::endl; @end

    // 声明一个 shared_ptr (在 main 作用域)
    var p_main: std.shared_ptr[Resource];

    { // 创建内部作用域
        // 2a. 创建 (C++: auto p_inner = std::make_shared<Resource>(2);)
        var p_inner = std.make_shared[Resource](2);

        // 2b. 共享所有权 (C++: p_main = p_inner; RC=2)
        p_main = p_inner;

        // 2c. [验证 . 访问]
        // 我们可以使用 Chrono 的 . 语法访问智能指针自身的方法
        var count: i64 = p_main.use_count();

        @cpp std::cout << "  p_main and p_inner share Resource 2 (RC=" << count << ")." << std::endl; @end
        @cpp std::cout << "  Inner scope ending (p_inner dies)..." << std::endl; @end
    } // <-- p_inner 在此离开作用域. RC 降为 1.
      // [关键] Resource 2 *不*应该被销毁.

    @cpp std::cout << "  Resource 2 is still alive (RC=1)." << std::endl; @end
    @cpp std::cout << "  demo_shared_ptr() scope ending (p_main dies)..." << std::endl; @end
    // <-- p_main 在此离开作用域. RC 降为 0. Resource 2 应该被销毁.
}


// --- 3. 弱指针 (std::weak_ptr) ---
// [前置声明] C++ 需要
@cpp struct Parent; struct Child; @end

struct Parent {
    var child: std.shared_ptr[Child]; // Parent 强引用 Child
    init() { @cpp std::cout << "  Parent created." << std::endl; @end }
    deinit { @cpp std::cout << "  Parent destroyed." << std::endl; @end }
}

struct Child {
    // [关键] Child *弱*引用 Parent
    var parent: std.weak_ptr[Parent];
    init() { @cpp std::cout << "  Child created." << std::endl; @end }
    deinit { @cpp std::cout << "  Child destroyed." << std::endl; @end }
}

func demo_weak_ptr() {
    @cpp std::cout << "\n--- 3. std::weak_ptr Demo ---\n" << std::endl; @end

    { // 创建内部作用域
        // 3a. 创建 (C++: auto p = std::make_shared<Parent>();)
        var p = std.make_shared[Parent](); // p (RC=1)
        var c = std.make_shared[Child]();   // c (RC=1)

        // 3b. [验证 -> 赋值]
        // 我们现在可以使用 Chrono 的 -> 语法进行赋值，无需 @cpp
        p->child = c;  // c (RC=2) (p 强引用 c)
        c->parent = p; // p (RC=1) (c *弱*引用 p, RC 不增加!)

        @cpp std::cout << "  Cycle created. Scopes ending..." << std::endl; @end
    } // <-- p (RC=0) 销毁 -> Parent 销毁 -> p->child 销毁 -> c (RC=1)
      //     c (RC=0) 销毁 -> Child 销毁

    @cpp std::cout << "  Both Parent and Child were destroyed (no leak)." << std::endl; @end
}

// --- Main ---
func main() -> int {
    demo_unique_ptr();
    demo_shared_ptr();
    demo_weak_ptr();

    @cpp std::cout << "\n--- C++ Smart Pointers Test End ---\n" << std::endl; @end
    return 0;
}