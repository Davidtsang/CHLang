import "chui/PropertyInjector"
import "chui/Geometry"
import "runtime/CH.h"
import "runtime/TypeConverters.h"
import "chui/Button"
import "chui/Menu"
import "chui/HBox"
import "runtime/Reflection.h"

implement PropertyInjector {
    func inject(obj: dyn, key: std::string, value: std::string) {
        if (key == "visible") {
            if (value == "false") { obj~>setVisible(false); return; }
            if (value == "true")  { obj~>setVisible(true);  return; }
        }

        var hbox = obj as HBox;
        if (hbox) {
            var color = CH::Converter<CGColor>::fromString(value);
            // [修复] 调用细粒度 API
            if (key == "borderTopColor")    { hbox->setBorderTopColor(color); return; }
            if (key == "borderBottomColor") { hbox->setBorderBottomColor(color); return; }
            if (key == "borderLeftColor")   { hbox->setBorderLeftColor(color); return; }
            if (key == "borderRightColor")  { hbox->setBorderRightColor(color); return; }
        }

        @codegen("PropertyInjector");
        CH::Log("Warning: Unknown property: " + key);
    }

    func injectInt(obj: dyn, key: std::string, value: i32) {
         if (key == "x") { obj~>setX(value); return; }
         if (key == "y") { obj~>setY(value); return; }
         if (key == "width") { obj~>setWidth(value); return; }
         if (key == "height") { obj~>setHeight(value); return; }

         var hbox = obj as HBox;
         if (hbox) {
             var fv = static_cast<f32>(value);
             // [修复] 调用细粒度 API
             if (key == "borderTopWidth")    { hbox->setBorderTopWidth(fv); return; }
             if (key == "borderBottomWidth") { hbox->setBorderBottomWidth(fv); return; }
             if (key == "borderLeftWidth")   { hbox->setBorderLeftWidth(fv); return; }
             if (key == "borderRightWidth")  { hbox->setBorderRightWidth(fv); return; }
         }
    }

    // ... injectBool 保持不变 ...
    func injectBool(obj: dyn, key: std::string, value: bool) {
        if (key == "visible") {
            obj~>setVisible(value);
            return;
        }
    }
}