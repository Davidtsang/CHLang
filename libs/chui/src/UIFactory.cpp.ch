import "chui/UIFactory"
import "chui/Button"
import "chui/Label"
import "runtime/CH.h"
import "chui/ImageView" // [新增]

implement UIFactory {
    func createWidget(className: std::string) -> dyn {
        if (className == "Button") {return new Button("Default");}
        if (className == "Label")  {return new Label("Default");}
        if (className == "ImageView") { return new ImageView(); }
        CH::Log("UIFactory Error: Unknown class " + className);
        return nullptr;
    }
}