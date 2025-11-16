// file: project/app.ch

// --- 1. 导入框架和您自己的窗口 ---
import "Application.h"
import "MyWindow.h"
import <memory>
// --- 2. 实现 Chrono 入口点 ---
func CHMain() -> int {

    // --- 3. 创建核心对象 ---
    var app: unique[Application] = @make[Application]();
    var window: unique[MyWindow] = @make[MyWindow](app->get()); // [ [ 修正: 传递 app 指针 ] ]

    // --- 4. 运行应用 ---
    window.show();
    var exit_code: int = app.exec();

    // --- 5. 返回退出码 ---
    return exit_code;
}