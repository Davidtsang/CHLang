import "chui/Application"
import "MyWindow"
import "chui/Geometry"
import "runtime/CH.h"
import "LayoutLoader" // [新增] 引入新的加载器

import <string>

// 退出回调保持在这里
func onExit() {
    @cpp PostQuitMessage(0); @end
}

func CHMain() -> int {
    var app = @make<Application>();
    var window = @make<MyWindow>(app.get(), 600, 400);

    // 设置窗口属性
    window->setBackgroundColor(CGColor(240, 240, 240, 255));


    // --- 1. 创建文件菜单 (子菜单) ---
    var fileMenu = new Menu(true); // true = Popup
    fileMenu->addItem("Open", 101);
    fileMenu->addItem("Save", 102);
    fileMenu->addSeparator();
    fileMenu->addItem("Exit", 103);

    // --- 2. 创建主菜单条 ---
    var menuBar = new Menu(false); // false = Bar
    menuBar->addSubMenu("File", fileMenu);
    menuBar->addItem("Help", 201); // 顶层直接点击项

    // --- 3. 绑定逻辑 ---

    window->bindMenuAction(101, ()=>{
     CH::Log("Menu: Open Clicked");
     });

    window->bindMenuAction(103, onExit); // 绑定退出函数

    window->bindMenuAction(201, ()=>{
    CH::Log("Menu: Help Clicked");
    });

    // --- 4. 挂载到窗口 ---
    window->setMenuBar(menuBar);

    CH::Log("--- Starting Data-Driven Engine ---");

    // [重构核心] 一行代码加载布局
    // 将复杂的解析逻辑委托给 LayoutLoader
    LayoutLoader::load("layout.json", window->m_hWnd, onExit);

    window->show();
    return app->exec();
}
