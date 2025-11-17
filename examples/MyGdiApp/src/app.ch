import "Application"
import "Button" // 导入按钮
import "MyWindow"
import <memory>
import <iostream> // 用于打印

// 回调函数
func onBtnClicked() {
    @cpp std::cout << ">>> Button Clicked! Hello form Chrono!" << std::endl; @end
}

func CHMain() -> int {
    var app: unique[Application] = @make[Application]();
    var window: unique[MyWindow] = @make[MyWindow](app->get());

    // 1. 创建按钮
    var btn: unique[Button] = @make[Button]("Click Me!");

    // 2. 设置回调
    btn.setOnClick(onBtnClicked);

    // 3. 添加到窗口 (转移所有权)
    window.addChild(@move(btn));

    window.show();

    return app.exec();
}