//project/app.ch
import "framework/Application.ch"

func main() -> int {

    var app: unique[Application] = @make[Application]();
    var window: unique[MyWindow] = @make[MyWindow]();

    // [ [ [ 关键的 API 调用 ] ] ]
    // 这将被翻译为 C++ 的 '->' (箭头) 操作符
    window.show();
    var exit_code: int = app.exec(); // 阻塞消息循环

    return exit_code;

}