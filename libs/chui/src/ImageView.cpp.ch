import "chui/ImageView"
import "chui/Base64"  // 用于 Base64 解码
import "runtime/CH.h"
import <algorithm>    // 用于 std::min, std::max
import <vector>

@cpp
#include <windows.h>
#include <gdiplus.h>
#include <shlwapi.h> // 用于 IStream
#include <string>

using namespace Gdiplus;
@end

@dynamic
implement ImageView {

    init() {
        this->m_gdiImage = nullptr;
        this->m_pStream = nullptr; // 仅 Base64 模式使用

        // 默认样式
        this->m_scaleMode = ImageScaleMode::ScaleToFill;
        this->m_borderWidth = 0.0;
        this->m_borderColor = CGColor::black();
        this->m_padding = 0.0;
    }

    // --- 统一资源清理 ---
    // 这是一个私有辅助逻辑，但在 Chrono 中我们通常直接写在 deinit 或方法里
    // 为了复用，我们定义一个清理逻辑的 helper (或者直接在 setter 里写)

    deinit {
        @cpp
        // 1. 释放 Image
        if (this->m_gdiImage) {
            delete static_cast<Image*>(this->m_gdiImage);
            this->m_gdiImage = nullptr;
        }
        // 2. 释放 Stream (如果是 Base64 创建的)
        if (this->m_pStream) {
            static_cast<IStream*>(this->m_pStream)->Release();
            this->m_pStream = nullptr;
        }
        @end
    }

    // 在 Label 和 ImageView 中
    func hitTest(x: int, y: int) -> int {
        // 返回 HTTRANSPARENT (-1) 或 0 (取决于你的 WindowProc 封装)
        // 告诉 Windows：“我不处理鼠标，去问我爸爸”
        return -1;
    }

    // --- 模式 A: 从文件路径加载 ---
    func setImagePath(path: std::string) {
        if (this->m_imagePath == path) { return; }
        this->m_imagePath = path;

        // 1. 清理旧资源
        @cpp
        if (this->m_gdiImage) { delete static_cast<Image*>(this->m_gdiImage); this->m_gdiImage = nullptr; }
        if (this->m_pStream) { static_cast<IStream*>(this->m_pStream)->Release(); this->m_pStream = nullptr; }

        // 2. 加载新图片
        std::wstring widestr = std::wstring(path.begin(), path.end());
        Image* img = Image::FromFile(widestr.c_str());

        if (img && img->GetLastStatus() == Ok) {
             this->m_gdiImage = img;
        } else {
             if (img) delete img;
             this->m_gdiImage = nullptr;
             // CH::Log 不在 @cpp 内部调用，我们在外面打印
        }
        @end

        if (this->m_gdiImage == nullptr) {
             CH::Log("ImageView Error: Failed to load image from " + path);
        }

        // 3. 触发重绘
        if (this->m_hWnd != NULL) { InvalidateRect(this->m_hWnd, NULL, true); }
    }

    // --- 模式 B: 从 Base64 字符串加载 ---
    func setImageBase64(data: std::string) {
        // 1. 清理旧资源
        @cpp
        if (this->m_gdiImage) { delete static_cast<Image*>(this->m_gdiImage); this->m_gdiImage = nullptr; }
        if (this->m_pStream) { static_cast<IStream*>(this->m_pStream)->Release(); this->m_pStream = nullptr; }
        @end

        // 2. 解码 Base64 -> 二进制
        // 调用我们在 Base64.h.ch 中定义的纯 Chrono 函数
        var binary: std::vector<u8> = CH::Utils::Base64Decode(data);
        if (binary.empty()) {
            CH::Log("ImageView Error: Base64 decode failed or empty.");
            return;
        }

        // 3. 创建内存流并加载 (需要 Win32 API)
        @cpp
        // 分配全局内存
        HGLOBAL hMem = GlobalAlloc(GMEM_MOVEABLE, binary.size());
        if (hMem) {
            void* pMem = GlobalLock(hMem);
            memcpy(pMem, binary.data(), binary.size());
            GlobalUnlock(hMem);

            // 创建 IStream
            IStream* pStream = NULL;
            if (CreateStreamOnHGlobal(hMem, TRUE, &pStream) == S_OK) {
                this->m_pStream = pStream; // 持有 Stream

                // 从流创建 Image
                Image* img = Image::FromStream(pStream);
                if (img && img->GetLastStatus() == Ok) {
                    this->m_gdiImage = img;
                } else {
                    if(img) delete img;
                }
            } else {
                GlobalFree(hMem);
            }
        }
        @end

        // 4. 触发重绘
        if (this->m_hWnd != NULL) { InvalidateRect(this->m_hWnd, NULL, true); }
    }

    // --- 属性 Setters ---

    func setScaleMode(mode: ImageScaleMode) {
        this->m_scaleMode = mode;
        if (this->m_hWnd != NULL) { InvalidateRect(this->m_hWnd, NULL, true); }
    }

    func setBorder(width: f32, color: CGColor) {
        this->m_borderWidth = width;
        this->m_borderColor = color;
        if (this->m_hWnd != NULL) { InvalidateRect(this->m_hWnd, NULL, true); }
    }

    func setPadding(p: f32) {
        this->m_padding = p;
        if (this->m_hWnd != NULL) { InvalidateRect(this->m_hWnd, NULL, true); }
    }

    // --- 核心绘制逻辑 ---
    func onPaint(g: Graphics*) {
        @cpp
        // 1. 获取控件区域
        RECT clientRect;
        GetClientRect(this->m_hWnd, &clientRect);
        float w = (float)(clientRect.right - clientRect.left);
        float h = (float)(clientRect.bottom - clientRect.top);

        // 2. 绘制边框 (如果有)
        if (this->m_borderWidth > 0) {
            auto bc = this->m_borderColor;
            Color penColor(bc.a, bc.r, bc.g, bc.b);
            Pen pen(penColor, this->m_borderWidth);
            // 边框向内画，避免被裁剪
            pen.SetAlignment(PenAlignmentInset);
            g->DrawRectangle(&pen, 0.0f, 0.0f, w, h);
        }

        // 3. 绘制图片
        Image* img = static_cast<Image*>(this->m_gdiImage);
        if (img) {
            // 计算内容区域 (减去边框和 Padding)
            float offset = this->m_borderWidth + this->m_padding;
            float contentX = offset;
            float contentY = offset;
            float contentW = std::max(0.0f, w - offset * 2.0f);
            float contentH = std::max(0.0f, h - offset * 2.0f);

            // 如果内容区域太小，不绘制
            if (contentW <= 0 || contentH <= 0) return;

            // 目标绘制区域 (Dest Rect)
            float destX = contentX;
            float destY = contentY;
            float destW = contentW;
            float destH = contentH;

            float imgW = (float)img->GetWidth();
            float imgH = (float)img->GetHeight();

            // 根据缩放模式调整 Dest Rect
            // 注意：这里需要把 ImageScaleMode 枚举强转为 int 才能在 switch/if 中比较
            // 或者 Chrono 已经生成了对应的 C++ enum

            auto mode = this->m_scaleMode;

            if (mode == ImageScaleMode::ScaleToFill) {
                // 默认：拉伸填满 content 区域 (destW/H 保持不变)
            }
            else if (mode == ImageScaleMode::Center) {
                // 居中：保持原始大小
                destW = imgW;
                destH = imgH;
                destX = contentX + (contentW - imgW) / 2.0f;
                destY = contentY + (contentH - imgH) / 2.0f;
                // GDI+ DrawImage 默认不会自动裁剪超出 Rect 的部分，但会受 Graphics Clip 限制
                // 为了严谨，可以设置 Clip，但这里为了简单先略过
            }
            else if (mode == ImageScaleMode::AspectFit) {
                // 保持比例适应 (Letterbox) - 显示全图，留黑边
                if (imgW > 0 && imgH > 0) {
                    float scaleX = contentW / imgW;
                    float scaleY = contentH / imgH;
                    float scale = std::min(scaleX, scaleY); // 取较小缩放比

                    destW = imgW * scale;
                    destH = imgH * scale;
                    // 居中放置
                    destX = contentX + (contentW - destW) / 2.0f;
                    destY = contentY + (contentH - destH) / 2.0f;
                }
            }
            else if (mode == ImageScaleMode::AspectFill) {
                 // 保持比例填满 (Zoom / Crop) - 填满区域，裁剪多余
                 if (imgW > 0 && imgH > 0) {
                    float scaleX = contentW / imgW;
                    float scaleY = contentH / imgH;
                    float scale = std::max(scaleX, scaleY); // 取较大缩放比

                    destW = imgW * scale;
                    destH = imgH * scale;
                    destX = contentX + (contentW - destW) / 2.0f;
                    destY = contentY + (contentH - destH) / 2.0f;
                 }
            }

            // 设置高质量插值模式，防止缩放锯齿
            g->SetInterpolationMode(InterpolationModeHighQualityBicubic);

            // 绘制
            RectF destRect(destX, destY, destW, destH);

            // 如果是 AspectFill，可能需要裁剪超出部分
            // 这里简单使用 DrawImage，它会绘制到指定 Rect
            g->DrawImage(img, destRect);
        }
        @end
    }
}