// file: framework/Events.cpp.ch
import "Events" // 引入自己的头文件

implement MouseEvent {
    init(x: int, y: int, btn: int) {
        this->x = x;
        this->y = y;
        this->button = btn;
    }
}