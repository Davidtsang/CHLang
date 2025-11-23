// test/test_multi_arrays.ch
import <iostream>
import <cstdint>
import "runtime/CHObject.h"

func main() -> int {
    std::cout << "--- Multi-Array Test Start ---" << std::endl; 

    // 1. 声明
    // CH: [[i32; 3]; 2]
    // C++: int32_t matrix[2][3]
    var matrix: [[i32; 3]; 2] = {{10, 11, 12}, {20, 21, 22}};

    std::cout << "Test 1: Declared matrix[2][3]" << std::endl; 

    // 2. 访问
    std::cout << "Test 2: Accessing matrix[0][1]" << std::endl;
    std::cout << matrix[0][1] << std::endl; // 预期: 11
    

    // 3. 写入
    matrix[1][2] = 99;

    std::cout << "Test 3: Writing matrix[1][2] = 99" << std::endl;
    std::cout << matrix[1][2] << std::endl; // 预期: 99

    std::cout << "--- Multi-Array Test End ---" << std::endl;
    return 0;
}