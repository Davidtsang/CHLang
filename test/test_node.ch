// file: test/test_manual_memory.ch
// 目的: 验证 "方案 B" - struct的原始指针和手动内存管理(new/delete)
//
// 1. struct Node (值类型)
// 2. $next: Node (翻译为原始指针 Node* _next)
// 3. class LinkedList (引用类型)
// 4. deinit 中手动的 'delete' 循环

import <iostream>;
import "runtime/ChronoObject.h";

// --- 1. 节点 Struct (值类型) ---
// 它将被翻译为 C++ struct
struct Node {
    // 默认 public
    let data: i32;
    let $next: Node; // 翻译为 C++ 原始指针: Node* _next;

    // init (构造函数)
    init(val: i32) {
        // 翻译为: this->data = val;
        this.data = val;
        // 翻译为: this->_next = nullptr;
        this.$next = nullptr;
    }
}

// --- 2. 链表 Class (引用类型) ---
// 它继承 ChronoObject (RC=1)，但它*管理*的是原始指针
class LinkedList : ChronoObject {

    // $head 是一个原始指针 (Node* _head;)
    let $head: Node;

    // public init
    public init() {
        this.$head = nullptr;
        @cpp std::cout << "LinkedList: Init" << std::endl; @end
    }

    // [关键] deinit 必须手动清理所有原始指针
    deinit {
        @cpp std::cout << "LinkedList: Deinit Start (Manual Delete Loop)" << std::endl; @end

        let $current: Node = this.$head;
        while ($current != nullptr) {
            let $temp: Node = $current;
            $current = $current.$next; // 移动到下一个 ( _current = _current->_next; )

            // [测试] 我们可以在 @cpp 中访问翻译后的 C++ 成员
            @cpp std::cout << "  Deleting node with data: " << _temp->data << std::endl; @end

            // [关键] 使用 'delete' 关键字释放原始指针 struct
            delete $temp;
        }

        @cpp std::cout << "LinkedList: Deinit Finish" << std::endl; @end
    }

    // --- 方法 ---

    // public func push (在头部添加)
    public func push(val: i32) {
        // [关键] 使用 'new' 创建一个 struct 实例在堆上
        let $newNode: Node = new Node(val);

        $newNode.$next = this.$head; // _newNode->_next = this->_head;
        this.$head = $newNode;       // this->_head = _newNode;
    }

    // public func printList
    public func printList() {
        @cpp std::cout << "List contents: ["; @end
        let $current: Node = this.$head;
        while ($current != nullptr) {
            @cpp std::cout << " " <<  _current->data; @end
            $current = $current.$next;
        }
        @cpp std::cout << " ]" << std::endl; @end
    }
}


// --- 3. Main ---
func main() -> int {
    @cpp std::cout << "--- Manual Memory Test (Struct Node*) ---" << std::endl; @end

    // 1. 创建 List (RC=1)
    let $list: LinkedList = new LinkedList();

    // 2. 添加数据
    $list.push(10);
    $list.push(20);
    $list.push(30);

    // 3. 打印 (预期: 30, 20, 10, 因为是头部插入)
    $list.printList();

    // 4. 释放 List (RC=0)
    // 这将触发 LinkedList::deinit，进而测试 'delete' 循环
    @cpp std::cout << "Releasing list..." << std::endl; @end
    $list.release();

    @cpp std::cout << "--- Test End ---" << std::endl; @end
    return 0;
}