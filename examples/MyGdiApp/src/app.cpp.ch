import "Application"
import "Button"
import "Label"
import "MyWindow"
import <memory>
import <iostream>
import <gdiplus.h>

@cpp using namespace Gdiplus; @end

func onBtnClicked() {
    std::cout << ">>> Bye Bye!" << std::endl;
}

func CHMain() -> int {
    var app = @make<Application>();
    var window = @make<MyWindow>(app.get(), 600, 400);

    window->setBackgroundColor(192, 192, 192);

    // --- 1. Label ---
    var label = @make<Label>("Warning: System will shutdown.");
    label->setFont("Tahoma", 9.0);
    label->setTextColor(Color(255, 0, 0, 0));
    label->setBackgroundColor(Color(0, 0, 0, 0));
    label->setAlignment(1, 1); // 居中

    // [关键修复] 在 move 之前设置位置
    // x=50, y=50, w=500, h=40
    label->setGeometry(50, 50, 500, 40);

    // --- 2. Button ---
    var btn = @make<Button>("Shut Down");
    btn->setStyle(
        Color(255, 210, 210, 210),
        Color(255, 0, 0, 0),
        Color(255, 0, 0, 0),
        1.0, 9.0
    );
    btn->setOnClick(onBtnClicked);

    // [关键修复] 在 move 之前设置位置
    // x=200, y=150, w=200, h=50
    btn->setGeometry(200, 150, 200, 50);

    // --- 3. 添加并转移所有权 ---
    // 注意：这行代码执行后，本地变量 'label' 和 'btn' 变为空指针
    // 绝对不能再访问它们了
    window->addChild(@move(label));
    window->addChild(@move(btn));

    // [安全] 移除了那个导致崩溃的 @cpp SetWindowPos 块

    window->show();
    return app->exec();
}