#pragma once
import "Widget"
import "Geometry"
import <string>

// 图片缩放模式
enum ImageScaleMode {
    ScaleToFill,    // 拉伸填满 (默认)
    AspectFit,      // 保持比例适应 (留黑边)
    Center,         // 居中显示原始大小 (可能裁剪)
    AspectFill      // 保持比例填满 (裁剪多余部分)
}

@dynamic
class ImageView : Widget {
    // 数据
    var m_imagePath: std::string;
    var m_gdiImage: void*; // 存储 Gdiplus::Image*

    // 样式属性
    var m_scaleMode: ImageScaleMode;
    var m_borderColor: CGColor;
    var m_borderWidth: f32;
    var m_padding: f32;       // 内边距
    var m_cornerRadius: f32;  // (预留) 圆角
    var m_pStream: void*;  // 用于持有 Base64 的 IStream*

    public init();
    public deinit;

    // --- API ---
    public func setImagePath(path: std::string);   // 模式 A: 文件
    public func setImageBase64(data: std::string); // 模式 B: 内存

    // 设置缩放模式
    public func setScaleMode(mode: ImageScaleMode);

    // 设置样式
    public func setBorder(width: f32, color: CGColor);
    public func setPadding(p: f32);

    // --- 重写绘制 ---
    public override func onPaint(g: Graphics*);

    // [新增] 必须声明 hitTest
    public override func hitTest(x: int, y: int) -> int;
}