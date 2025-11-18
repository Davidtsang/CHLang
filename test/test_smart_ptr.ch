// file: test/test_smart_ptr.ch
// 目的: 验证 Chrono 的新内置智能指针语法
//
// 验证:
// - 内置泛型调用: @make[T](), @make_shared[T]()
// - 内置泛型类型: var p: unique[T];
// - 翻转 . 访问 (访问对象): p.member (原 p->member)
// - 翻转 -> 访问 (访问指针): p->use_count() (原 p.use_count())

import <iostream> // 用于 std::cout
import <memory>   // 依赖项，保持不变
import <string>   // 依赖项，保持不变
import <utility>  // 依赖项，保持不变

// --- 1. 独占指针 (std::unique_ptr) ---

struct Resource {
    var id: i32;
    init(i: i32) ;
    deinit ;
}

implement Resource{
    init(i: i32) {
        this->id = i;
     }
    deinit {
     }
}

func demo_unique_ptr() {

    { // 创建内部作用域
        // [修改] 1a. 创建 (使用 @make)
        var ptr1 = @make<Resource>(1);

        // [修改] 1b. [验证 . 访问] (访问被管理的对象)
        var id_val: i32 = ptr1->id;

        std::cout << "  ptr1 points to Resource " << id_val << std::endl;
   
        // [修改] 1c. 转移所有权 (使用 @move)
        var ptr2 = @move(ptr1);

        // 1d. 验证 ptr1 已失效
        
        if (ptr1 == nullptr) {
           std::cout << "  ptr1 is now null after move." << std::endl;
        }        

        std::cout << "  Inner scope ending (ptr2 dies)..." << std::endl;
    } // <-- ptr2 在此离开作用域. Resource 1 应该被销毁.
}


// --- 2. 共享指针 (std::shared_ptr) ---
func demo_shared_ptr() {
    std::cout << "\n--- 2. std::shared_ptr Demo ---\n" << std::endl;
    
    // [修改] 声明一个 shared_ptr (使用内置类型)
    var p_main: shared<Resource>;

    { // 创建内部作用域
        // [修改] 2a. 创建 (使用 @make_shared)
        var p_inner = @make_shared<Resource>(2);

        // 2b. 共享所有权
        p_main = p_inner;

        // [修改] 2c. [验证 -> 访问] (访问智能指针对象本身)
        var count: i64 = p_main.use_count();

        std::cout << "  p_main and p_inner share Resource 2 (RC=" << count << ")." << std::endl; 
        std::cout << "  Inner scope ending (p_inner dies)..." << std::endl; 
    } // <-- p_inner 在此离开作用域. RC 降为 1.

    std::cout << "  Resource 2 is still alive (RC=1)." << std::endl; 
    std::cout << "  demo_shared_ptr() scope ending (p_main dies)..." << std::endl; 
}


// --- 3. 弱指针 (std::weak_ptr) ---
type Parent : struct;
type Child : struct;

struct Parent {
    // [修改] 使用内置类型
    var child: shared<Child>;
    init();
    deinit;
}

implement Parent{
    init() { std::cout << "  Parent created." << std::endl;  }
    deinit { std::cout << "  Parent destroyed." << std::endl;  }
}


struct Child {
    // [修改] 使用内置类型
    var parent: weak<Parent>;
    init();
    deinit;
}

implement Child{
    init() { std::cout << "  Child created." << std::endl;  }
    deinit { std::cout << "  Child destroyed." << std::endl;  }
}

func demo_weak_ptr() {
    std::cout << "\n--- 3. std::weak_ptr Demo ---\n" << std::endl; 

    { // 创建内部作用域
        // [修改] 3a. 创建
        var p = @make_shared<Parent>();
        var c = @make_shared<Child>();

        // [修改] 3b. [验证 . 赋值] (访问被管理的对象)
        p->child = c;
        c->parent = p;

        std::cout << "  Cycle created. Scopes ending..." << std::endl; 
    }

    std::cout << "  Both Parent and Child were destroyed (no leak)." << std::endl; 
}

// --- Main ---
func main() -> int {
    demo_unique_ptr();
    demo_shared_ptr();
    demo_weak_ptr();

    std::cout << "\n--- C++ Smart Pointers Test End ---\n" << std::endl;
    return 0;
}