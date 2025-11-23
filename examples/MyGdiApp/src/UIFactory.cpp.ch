import "UIFactory"
import "Button"
import "Label"
import "runtime/CH.h"

implement UIFactory {
    func createWidget(className: std::string) -> dyn {
        if (className == "Button") {return new Button("Default");}
        if (className == "Label")  {return new Label("Default");}

        CH::Log("UIFactory Error: Unknown class " + className);
        return nullptr;
    }
}