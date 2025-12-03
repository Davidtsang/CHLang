import "chui/Application"
import "MyWindow"
import "chui/Geometry"
import "runtime/CH.h"
import "LayoutLoader" // [新增] 引入新的加载器

import <string>

// --- [新增] 定义常量枚举 ---
enum MenuID {
    Open = 101,
    Save,       // 102
    Exit,       // 103
    Help = 201
}

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

    // [重构] 使用枚举，意图清晰
    fileMenu->addItem("Open", MenuID::Open);
    fileMenu->addItem("Save", MenuID::Save);
    fileMenu->addSeparator();
    fileMenu->addItem("Exit", MenuID::Exit);

    // --- 2. 创建主菜单条 ---
    var menuBar = new Menu(false); // false = Bar
    menuBar->addSubMenu("File", fileMenu);

    // [重构]
    menuBar->addItem("Help", MenuID::Help);

    // --- 3. 绑定逻辑 ---

    // [重构] 这里的 ID 和上面添加时的 ID 永远保持一致，不会写错
    window->bindMenuAction(MenuID::Open, () => {
        CH::Log("Menu: Open Clicked");
    });

    // Save 也可以绑一下
    window->bindMenuAction(MenuID::Save, () => {
        CH::Log("Menu: Save Clicked");
    });

    window->bindMenuAction(MenuID::Exit, onExit);

    window->bindMenuAction(MenuID::Help, () => {
        CH::Log("Menu: Help Clicked");
    });

    // --- 4. 挂载到窗口 ---
    window->setMenuBar(menuBar);

    CH::Log("--- Starting Data-Driven Engine ---");

    LayoutLoader::load("layout.json", window->m_hWnd, onExit);

    window->show();
    return app->exec();
}