"""
生成三角眼网站SEO分享图片 (og-image.png)
"""
from PIL import Image, ImageDraw, ImageFont
import os

# 尺寸: 1200x630 (Facebook/Twitter标准)
width, height = 1200, 630

# 颜色配置
bg_color = (10, 14, 23)  # 深蓝黑
accent_color = (255, 107, 53)  # 橙色
text_color = (240, 244, 255)  # 白色
secondary_color = (136, 150, 179)  # 灰蓝

def create_og_image():
    # 创建图片
    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    
    # 尝试加载字体
    try:
        # Windows字体路径
        font_large = ImageFont.truetype("C:/Windows/Fonts/msyh.ttc", 72)  # 微软雅黑
        font_medium = ImageFont.truetype("C:/Windows/Fonts/msyh.ttc", 36)
        font_small = ImageFont.truetype("C:/Windows/Fonts/msyh.ttc", 24)
    except:
        # 使用默认字体
        font_large = ImageFont.load_default()
        font_medium = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    # 绘制背景装饰 - 右上角光晕
    for i in range(100, 0, -5):
        alpha = int(255 * (1 - i/100) * 0.15)
        draw.ellipse([width-300-i*2, -50-i, width+100, 200], 
                     fill=(accent_color[0], accent_color[1], accent_color[2], alpha))
    
    # 绘制网格背景
    for x in range(0, width, 60):
        draw.line([(x, 0), (x, height)], fill=(255, 107, 53, 15), width=1)
    for y in range(0, height, 60):
        draw.line([(0, y), (width, y)], fill=(255, 107, 53, 15), width=1)
    
    # Logo区域 - 左边
    # Logo背景框
    draw.rounded_rectangle([60, 80, 180, 200], radius=20, 
                           fill=(accent_color[0], accent_color[1], accent_color[2]))
    # Logo文字
    draw.text((90, 110), "👁", font=ImageFont.truetype("C:/Windows/Fonts/seguiemj.ttf", 80), 
               fill=(255, 255, 255))
    
    # 主标题
    draw.text((220, 100), "三角眼", font=font_large, fill=text_color)
    draw.text((220, 180), "DELTA FORCE TOOLS", font=font_small, fill=secondary_color)
    
    # 主标题区域
    draw.text((100, 280), "三角洲行动", font=font_large, fill=text_color)
    draw.text((100, 370), "战备工具站", font=font_large, fill=accent_color)
    
    # 副标题
    draw.text((100, 460), "工坊利润计算 · 战备配置推荐 · 改枪配件搭配", 
               font=font_medium, fill=secondary_color)
    
    # 底部信息
    draw.text((100, 550), "df.sanjiaoy.top", font=font_small, fill=secondary_color)
    
    # 右侧功能图标区域
    features = ["⚡", "🛡", "🔫", "📊", "🗺️", "📦"]
    start_x = 750
    for i, feat in enumerate(features):
        x = start_x + (i % 3) * 140
        y = 150 + (i // 3) * 200
        # 图标背景
        draw.rounded_rectangle([x, y, x+100, y+100], radius=15, 
                               fill=(accent_color[0], accent_color[1], accent_color[2], 50))
        # 图标
        draw.text((x+30, y+20), feat, font=ImageFont.truetype("C:/Windows/Fonts/seguiemj.ttf", 50),
                  fill=(255, 255, 255))
    
    # 保存图片
    output_path = os.path.join(os.path.dirname(__file__), '..', 'og-image.png')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path, 'PNG', quality=95)
    print(f"✅ og-image.png 已生成: {output_path}")
    return output_path

if __name__ == "__main__":
    create_og_image()
