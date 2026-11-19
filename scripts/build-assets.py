#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""素材处理脚本：把桌面素材文件夹里的原始图片转换为网站用资源（webp / 透明底 png）。
用法：python3 scripts/build-assets.py
"""
import os
from PIL import Image

SRC = os.path.expanduser("~/Desktop/浙江品汇阀门有限公司/素材")
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "public", "images")
os.makedirs(OUT, exist_ok=True)

P62 = os.path.join(SRC, "品汇1-62", "品汇1-62")
P82 = os.path.join(SRC, "品汇63-82")
WX = os.path.join(SRC, "联系方式")
SLURRY = os.path.join(SRC, "浆液阀系列 ")   # 目录名末尾带空格，勿删
HOME = os.path.join(SRC, "首页")


def save_webp(img, name, max_w=None, quality=82):
    img = img.convert("RGB")
    if max_w and img.width > max_w:
        h = int(img.height * max_w / img.width)
        img = img.resize((max_w, h), Image.LANCZOS)
    path = os.path.join(OUT, name)
    img.save(path, "WEBP", quality=quality, method=6)
    print(f"  {name}  {img.width}x{img.height}  {os.path.getsize(path)//1024}KB")


def cutout(src_path, name, height=1100, bg_level=238):
    """白底产品图 -> 透明底 webp。
    做法：先按亮度阈值得到"背景候选"，再从四角洪水填充，只去掉与画面边缘连通的背景，
    这样产品内部的不锈钢高光（同样接近白色）不会被误删。边缘做 0.6px 羽化避免硬锯齿。
    """
    from PIL import ImageDraw, ImageFilter

    im = Image.open(src_path).convert("RGB")
    if im.height > height:
        w = int(im.width * height / im.height)
        im = im.resize((w, height), Image.LANCZOS)

    g = im.convert("L")
    mask = g.point(lambda v: 255 if v >= bg_level else 0)
    w, h = im.size
    d = ImageDraw.Draw(mask)
    for xy in ((0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1)):
        if mask.getpixel(xy) == 255:
            ImageDraw.floodfill(mask, xy, 128, thresh=12)

    alpha = mask.point(lambda v: 0 if v == 128 else 255)
    alpha = alpha.filter(ImageFilter.GaussianBlur(0.6))

    # 边缘反白（un-premultiply）：羽化后的半透明像素原本混了白底，减掉白色成分避免深色背景上出现白边
    import numpy as np

    rgb = np.asarray(im, dtype=np.float32)
    a = np.asarray(alpha, dtype=np.float32) / 255.0
    a3 = a[..., None]
    fixed = np.where(a3 > 0.02, (rgb - (1.0 - a3) * 255.0) / np.maximum(a3, 0.02), rgb)
    rgb = np.clip(fixed, 0, 255).astype(np.uint8)

    out = Image.fromarray(rgb, "RGB").convert("RGBA")
    out.putalpha(alpha)
    bbox = alpha.getbbox()
    if bbox:
        out = out.crop(bbox)

    path = os.path.join(OUT, name)
    out.save(path, "WEBP", quality=88, method=6)
    print(f"  {name}  {out.width}x{out.height}  {os.path.getsize(path)//1024}KB")


def logo():
    """企业 logo：白底 -> 透明，并生成深色底用的白色版本"""
    src = os.path.join(P62, "01.JPG")
    im = Image.open(src).convert("RGB")
    px = im.load()
    out = Image.new("RGBA", im.size, (255, 255, 255, 0))
    op = out.load()
    for y in range(im.height):
        for x in range(im.width):
            r, g, b = px[x, y]
            m = min(r, g, b)
            a = 0 if m >= 246 else (255 if m < 232 else int(255 * (246 - m) / 14))
            op[x, y] = (r, g, b, a)
    bbox = out.split()[3].getbbox()
    out = out.crop(bbox)
    if out.width > 900:
        out = out.resize((900, int(out.height * 900 / out.width)), Image.LANCZOS)
    out.save(os.path.join(OUT, "logo.png"))
    print(f"  logo.png {out.width}x{out.height}")

    # 白色版本（页脚 / 深色背景）
    white = Image.new("RGBA", out.size, (255, 255, 255, 0))
    wp, sp = white.load(), out.load()
    for y in range(out.height):
        for x in range(out.width):
            a = sp[x, y][3]
            if a:
                wp[x, y] = (255, 255, 255, a)
    white.save(os.path.join(OUT, "logo-white.png"))
    print(f"  logo-white.png {white.width}x{white.height}")


FACTORY = {
    "hero.jpg": "13.JPG",        # 成品区：蓝色阀门阵列（首屏背景）
    "about.jpg": "07.JPG",       # 车间全景
    "strength-cnc.jpg": "05.JPG",    # 机加工中心
    "strength-line.jpg": "06.JPG",   # 装配线
    "strength-stock.jpg": "09.JPG",  # 成品库存
    "strength-qc.jpg": "08.JPG",     # 加工 / 检验现场
    "gallery-1.jpg": "11.JPG",
    "gallery-2.jpg": "16.JPG",
    "gallery-3.jpg": "10.JPG",
}

PRODUCTS = {
    # 文件名 -> (源图, 说明)
    "p-pz73.png": ("@62", "PZ73/PZ43 系列刀闸阀"),
    "p-pz73-alt.png": ("@61", "PZ73 伞齿轮刀闸阀"),
    "p-daigai.png": ("65.JPG", "带盖刀闸阀"),
    "p-dmz73.png": ("63.JPG", "DMZ73 手动暗板刀闸阀"),
    "p-slurry.png": ("66.JPG", "气动浆液阀"),
    "p-slurry-manual.png": ("68.JPG", "手动浆液阀"),
    "p-scz673.png": ("70.JPG", "气动穿透式插板阀"),
    "p-scz673-alt.png": ("72.JPG", "穿透式插板阀"),
    "p-ceramic-knife.png": ("73.JPG", "陶瓷刀闸阀"),
    "p-ceramic-double.png": ("75.JPG", "气动陶瓷双闸板阀"),
    "p-ceramic-slag.png": ("76.JPG", "电动陶瓷排渣阀"),
    "p-square.png": ("77.JPG", "方形闸阀"),
    "p-lmd.png": ("79.JPG", "LMD 手动方型插板阀"),
    "p-gate-sq.png": ("81.JPG", "镶铜铸铁方形闸门"),
    "p-gate-circle.png": ("82.JPG", "镶铜铸铁圆形闸门"),
    "p-group-daigai.png": ("64.JPG", "带盖系列"),
    "p-group-slurry.png": ("67.JPG", "浆液阀系列"),
    "p-group-scz.png": ("71.JPG", "穿透式系列"),
    "p-group-ceramic.png": ("74.JPG", "陶瓷系列"),
    "p-group-square.png": ("78.JPG", "方形系列"),
    # 浆液阀系列（素材/浆液阀系列 ）与首页主图（素材/首页）
    "p-hero-valve.png": ("@HOME/微信图片_20261118190807_280_84.jpg", "首页主图：PZ73 不锈钢刀闸阀（手轮）"),
    "p-slurry-a.png": ("@SLURRY/微信图片_20261117151756_716_225.jpg", "浆液阀 手动 正面"),
    "p-slurry-b.png": ("@SLURRY/微信图片_20261117151756_714_225.jpg", "浆液阀 手动 大规格"),
    "p-slurry-c.png": ("@SLURRY/微信图片_20261117151756_717_225.jpg", "浆液阀 手动 中型"),
    "p-slurry-d.png": ("@SLURRY/微信图片_20261117151756_715_225.jpg", "浆液阀 手动 小规格"),
}

print("[1/3] logo")
logo()
print("[2/3] 工厂 / 场景图")
for name, f in FACTORY.items():
    save_webp(Image.open(os.path.join(P62, f)), name, max_w=1920, quality=80)
print("[3/3] 产品图（透明底）")
for name, (f, desc) in PRODUCTS.items():
    if f.startswith("@HOME/"):
        src = os.path.join(HOME, f[6:])
    elif f.startswith("@SLURRY/"):
        src = os.path.join(SLURRY, f[8:])
    elif f.startswith("@"):
        src = os.path.join(P62, f[1:] + ".JPG")
    else:
        src = os.path.join(P82, f)
    cutout(src, name)

# 微信名片：统一画布尺寸（两张图原始长宽比不同，统一到 360x480 后再等比缩放居中）
def qr_card(src_path, name, canvas=(360, 480), pad=12):
    from PIL import ImageChops

    im = Image.open(src_path).convert("RGB")
    # 去掉四周白边 / 空白
    diff = ImageChops.difference(im, Image.new("RGB", im.size, (255, 255, 255))).convert("L")
    bbox = diff.point(lambda v: 255 if v > 14 else 0).getbbox()
    if bbox:
        # 内缩 4px，去掉源图自带的边缘细线
        x0, y0, x1, y1 = bbox
        im = im.crop((x0 + 4, y0 + 4, max(x0 + 5, x1 - 4), max(y0 + 5, y1 - 4)))

    max_w, max_h = canvas[0] - 2 * pad, canvas[1] - 2 * pad
    ratio = min(max_w / im.width, max_h / im.height)
    im = im.resize((max(1, int(im.width * ratio)), max(1, int(im.height * ratio))), Image.LANCZOS)

    out = Image.new("RGB", canvas, (255, 255, 255))
    out.paste(im, ((canvas[0] - im.width) // 2, (canvas[1] - im.height) // 2))
    out.save(os.path.join(OUT, name), optimize=True)
    print(f"  {name} {out.width}x{out.height}")


for src, name in (("微信1.png", "wechat-1.png"), ("微信2.png", "wechat-2.png")):
    qr_card(os.path.join(WX, src), name)

print("完成 ->", OUT)
