import base64
import sys
import os

try:
    import cairosvg
except ImportError:
    print("错误: 未找到 cairosvg 库。")
    print("请运行: pip install cairosvg")
    print("注意: Windows 用户可能还需要安装 GTK+ 运行时环境。")
    sys.exit(1)


def convert_svg_to_png_base64(input_str, scale=1.0):
    """
    将 SVG 字符串转换为 PNG Base64 字符串
    """
    svg_bytes = b""

    # 1. 预处理输入数据
    input_str = input_str.strip()

    try:
        if input_str.startswith("data:image/svg+xml;base64,"):
            # 情况 A: 完整的 Data URI
            print("检测到: Data URI 格式")
            b64_data = input_str.split("base64,")[1]
            svg_bytes = base64.b64decode(b64_data)

        elif input_str.strip().startswith("<svg") or input_str.strip().startswith("<?xml"):
            # 情况 B: 原始 SVG XML 字符串
            print("检测到: 原始 SVG XML")
            svg_bytes = input_str.encode('utf-8')

        else:
            # 情况 C: 纯 Base64 字符串
            print("检测到: 纯 Base64 字符串")
            # 尝试解码，如果失败则可能不是 Base64
            svg_bytes = base64.b64decode(input_str)

    except Exception as e:
        print(f"解码输入数据失败: {e}")
        return None

    # 2. 使用 CairoSVG 转换为 PNG
    try:
        # parent_width/height 可以控制输出尺寸，scale 控制缩放
        png_bytes = cairosvg.svg2png(bytestring=svg_bytes, scale=scale)
    except Exception as e:
        print(f"SVG 渲染失败: {e}")
        return None

    # 3. 将 PNG 二进制编码为 Base64
    png_b64 = base64.b64encode(png_bytes).decode('ascii')

    # 4. 组装结果
    return f"data:image/png;base64,{png_b64}"


if __name__ == "__main__":
    # 默认使用你提供的测试数据
    default_input = "data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIiB2aWV3Qm94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiA8cGF0aCBkPSJNOCAxNUgxNk0xNSA5SDE1LjAxTTkgOUg5LjAxTTIyIDEyQzIyIDE3LjUyMjggMTcuNTIyOCAyMiAxMiAyMkM2LjQ3NzE1IDIyIDIgMTcuNTIyOCAyIDEyQzIgNi40NzcxNSA2LjQ3NzE1IDIgMTIgMkMxNy41MjI4IDIgMjIgNi40NzcxNSAyMiAxMlpNMTUuNSA5QzE1LjUgOS4yNzYxNCAxNS4yNzYxIDkuNSAxNSA5LjVDMTQuNzIzOSA5LjUgMTQuNSA5LjI3NjE0IDE0LjUgOUMxNC41IDguNzIzODYgMTQuNzIzOSA4LjUgMTUgOC41QzE1LjI3NjEgOC41IDE1LjUgOC43MjM4NiAxNS41IDlaTTkuNSA5QzkuNSA5LjI3NjE0IDkuMjc2MTQgOS41IDkgOS41QzguNzIzODYgOS41IDguNSA5LjI3NjE0IDguNSA5QzguNSA4LjcyMzg2IDguNzIzODYgOC41IDkgOC41QzkuMjc2MTQgOC41IDkuNSA4LjcyMzg2IDkuNSA5WiIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIi8+CiA8L3N2Zz4="

    # 如果命令行有参数，使用参数文件或字符串
    target_input = default_input
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if os.path.exists(arg):
            with open(arg, 'r', encoding='utf-8') as f:
                target_input = f.read()
        else:
            target_input = arg

    print("-" * 60)
    print("开始转换...")

    # 这里设置 scale=2.0 可以生成更高清的图（Retina），默认 1.0
    result = convert_svg_to_png_base64(target_input, scale=1.0)

    if result:
        print("-" * 60)
        print("转换成功！请复制以下内容到 layout.json:")
        print("-" * 60)
        print(result)
        print("-" * 60)

        # 可选：保存到文件查看
        # with open("output.png", "wb") as f:
        #     f.write(base64.b64decode(result.split(",")[1]))
        # print("已保存预览图到 output.png")