import "Application"
import "Button"
import "Label"
import "MyWindow"
import "Geometry" // 导入 CG 类型
import <memory>
import <iostream>

// [修正] 定义一个具名的回调函数
func onShutdownCallback() {
    @cpp std::cout << "Shutdown confirmed via Callback!" << std::endl; @end
}

func CHMain() -> int {
    var app = @make<Application>();
    var window = @make<MyWindow>(app.get(), 600, 400);

    // 使用 CGColor
    window->setBackgroundColor(CGColor(240, 240, 240, 255));

    // --- 1. Label ---
    var label = @make<Label>("System Alert");

    // 使用 CGRect 和 CGColor
    label->setFrame(CGRect(50.0, 20.0, 500.0, 30.0));
    label->setTextColor(CGColor::red());
    label->setFont("Tahoma", 16.0);

    // --- 2. Modular Button ---
    var btn = @make<Button>("Confirm Shutdown");

    // 设置位置
    btn->setFrame(CGRect(200.0, 100.0, 200.0, 50.0));

    // 设置样式
    btn->setStyle(
        CGColor::white(),      // 背景
        CGColor::black(),      // 边框
        2.0                    // 边框宽
    );
    btn->setFont("Segoe UI", 12.0);

    // [修正] 传入函数名，而不是匿名函数
    btn->setOnClick(onShutdownCallback);

    // --- 3. 添加 ---
    window->addChild(@move(label));
    window->addChild(@move(btn));

    window->show();
    return app->exec();
}