import "Application"
import "Button" // 导入按钮
import "MyWindow"
import <memory>
import <iostream> // 用于打印

// 回调函数
func onBtnClicked() {
    // [重构] 移除 @cpp，使用原生 Chrono 语法 (<< 和 ::)
    std::cout << ">>> Button Clicked! Hello form Chrono!" << std::endl;
}

func CHMain() -> int {
    // [重构] 泛型 [] -> <>
    var app: unique<Application> = @make<Application>();

    // [重构] app 是 unique_ptr 对象，访问其 get() 方法使用 .
    // get() 返回 raw pointer
    var window: unique<MyWindow> = @make<MyWindow>(app.get());

    // 1. 创建按钮
    var btn: unique<Button> = @make<Button>("Click Me!");

    // 2. 设置回调
    // [重构] btn 是指针类型 (unique_ptr 重载了 ->)，使用 -> 访问成员
    btn->setOnClick(onBtnClicked);

    // 3. 添加到窗口 (转移所有权)
    // [重构] window 是指针类型，使用 ->
    window->addChild(@move(btn));

    window->show();

    // [重构] app 也是指针语义，使用 -> 访问 exec
    return app->exec();
}