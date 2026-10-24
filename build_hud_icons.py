"""
build_hud_icons.py
Generator aset ikon pixel-art 16-bit untuk 4 tombol HUD atas:
1. icon_btn_pause.png (Jeda - 32x32 RGBA)
2. icon_btn_resume.png (Lanjut - 32x32 RGBA)
3. icon_btn_sound_on.png (Suara Nyala - 32x32 RGBA)
4. icon_btn_sound_off.png (Bungkam / Mute - 32x32 RGBA)
5. icon_btn_speed_1x.png (Kecepatan 1X Normal - 32x32 RGBA)
6. icon_btn_speed_2x.png (Kecepatan 2X Turbo - 32x32 RGBA)
7. icon_btn_fullscreen_enter.png (Masuk Layar Penuh - 32x32 RGBA)
8. icon_btn_fullscreen_exit.png (Keluar Layar Penuh - 32x32 RGBA)

Juga membuat master sheet berlatar magenta (#FF00FF) di assets_raw/ui/hud_top_icons_raw.png
sebagai referensi DALL-E / backup raw asset.
"""

import os
from PIL import Image, ImageDraw

UI_DIR = r"C:\GAME\assets\ui"
RAW_UI_DIR = r"C:\GAME\assets_raw\ui"

os.makedirs(UI_DIR, exist_ok=True)
os.makedirs(RAW_UI_DIR, exist_ok=True)

def create_base_frame(accent_rgb, border_rgb=(30, 41, 59)):
    """Membuat bingkai beveled titanium dengan aksen sudut neon cybernetic."""
    img = Image.new("RGBA", (32, 32), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Isi latar belakang gelap bergradasi sedikit
    for y in range(2, 30):
        shade = int(12 + (y - 2) * 0.4)
        draw.line([(2, y), (29, y)], fill=(shade, shade + 4, shade + 12, 235))

    # Border frame luar
    draw.rectangle([2, 2, 29, 29], outline=border_rgb)

    # Cyber corner brackets (4 sudut aksen neon)
    ar, ag, ab = accent_rgb
    glow_col = (ar, ag, ab, 120)
    solid_col = (ar, ag, ab, 255)

    # Top-Left Bracket
    draw.point([(2, 2), (3, 2), (4, 2), (5, 2), (2, 3), (2, 4), (2, 5)], fill=solid_col)
    draw.point([(3, 3), (4, 3), (3, 4)], fill=glow_col)

    # Top-Right Bracket
    draw.point([(29, 2), (28, 2), (27, 2), (26, 2), (29, 3), (29, 4), (29, 5)], fill=solid_col)
    draw.point([(28, 3), (27, 3), (28, 4)], fill=glow_col)

    # Bottom-Left Bracket
    draw.point([(2, 29), (3, 29), (4, 29), (5, 29), (2, 28), (2, 27), (2, 26)], fill=solid_col)
    draw.point([(3, 28), (4, 28), (3, 27)], fill=glow_col)

    # Bottom-Right Bracket
    draw.point([(29, 29), (28, 29), (27, 29), (26, 29), (29, 28), (29, 27), (29, 26)], fill=solid_col)
    draw.point([(28, 28), (27, 28), (28, 27)], fill=glow_col)

    return img

# ==========================================
# 1. ICON PAUSE (JEDA)
# ==========================================
def draw_icon_pause():
    accent = (0, 242, 254)  # Cyan
    img = create_base_frame(accent, (20, 60, 80))
    draw = ImageDraw.Draw(img)

    # Dua baris energi holografik vertikal
    bars = [(9, 12), (18, 21)]  # (x_start, x_end)
    y_start, y_end = 8, 23

    # Outer aura glow
    for x0, x1 in bars:
        draw.rectangle([x0 - 1, y_start - 1, x1 + 1, y_end + 1], fill=(0, 242, 254, 70))

    # Bar body
    for x0, x1 in bars:
        draw.rectangle([x0, y_start, x1, y_end], fill=(0, 220, 250, 240))
        # Highlight inti putih
        draw.line([(x0 + 1, y_start + 1), (x0 + 1, y_end - 1)], fill=(240, 255, 255, 255))
        draw.line([(x0 + 2, y_start + 1), (x0 + 2, y_end - 1)], fill=(200, 245, 255, 255))

    return img

# ==========================================
# 2. ICON RESUME (LANJUT / PLAY)
# ==========================================
def draw_icon_resume():
    accent = (255, 210, 0)  # Gold
    img = create_base_frame(accent, (70, 55, 20))
    draw = ImageDraw.Draw(img)

    # Segitiga arah kanan
    poly = [(11, 8), (23, 16), (11, 24)]

    # Glow aura
    draw.polygon([(10, 7), (25, 16), (10, 25)], fill=(255, 210, 0, 75))
    draw.polygon([(10, 8), (24, 16), (10, 24)], fill=(245, 158, 11, 200))
    # Body
    draw.polygon(poly, fill=(255, 220, 40, 255))

    # Core highlight
    draw.polygon([(12, 11), (20, 16), (12, 21)], fill=(255, 250, 210, 255))
    draw.line([(13, 13), (17, 16)], fill=(255, 255, 255, 255))

    return img

# ==========================================
# 3. ICON SOUND ON (SUARA AKTIF)
# ==========================================
def draw_icon_sound_on():
    accent = (56, 189, 248)  # Sky blue
    img = create_base_frame(accent, (25, 55, 75))
    draw = ImageDraw.Draw(img)

    # Speaker base (kotak)
    draw.rectangle([6, 12, 9, 19], fill=(70, 95, 120, 255))
    draw.rectangle([7, 13, 8, 18], fill=(180, 215, 240, 255))

    # Speaker cone (trapezoid melebar ke kanan)
    cone_pts = [(9, 12), (14, 8), (14, 23), (9, 19)]
    draw.polygon(cone_pts, fill=(56, 189, 248, 230))
    draw.line([(14, 9), (14, 22)], fill=(224, 242, 254, 255))

    # Gelombang suara 1 (dekat)
    arc1 = [(17, 13), (18, 14), (18, 17), (17, 18)]
    for pt in arc1:
        draw.point(pt, fill=(56, 189, 248, 255))
        draw.point((pt[0]-1, pt[1]), fill=(56, 189, 248, 90))

    # Gelombang suara 2 (jauh)
    arc2 = [(21, 10), (22, 11), (23, 13), (23, 18), (22, 20), (21, 21)]
    for pt in arc2:
        draw.point(pt, fill=(0, 242, 254, 255))
        draw.point((pt[0]+1, pt[1]), fill=(0, 242, 254, 100))

    return img

# ==========================================
# 4. ICON SOUND OFF (BUNGKAM / MUTE)
# ==========================================
def draw_icon_sound_off():
    accent = (239, 68, 68)  # Crimson Red
    img = create_base_frame(accent, (65, 30, 35))
    draw = ImageDraw.Draw(img)

    # Speaker redup / desaturasi
    draw.rectangle([6, 12, 9, 19], fill=(60, 65, 75, 230))
    cone_pts = [(9, 12), (14, 8), (14, 23), (9, 19)]
    draw.polygon(cone_pts, fill=(80, 88, 100, 230))

    # Laser Slash Mute Merah Menyilang (Diagonal Slash Bar)
    # Garis dari (7, 7) ke (24, 24)
    for offset in [-1, 0, 1]:
        draw.line([(7 + offset, 7), (24 + offset, 24)], fill=(239, 68, 68, 180 if offset != 0 else 255))
    # Core highlight putih-merah di tengah garis
    draw.line([(8, 8), (23, 23)], fill=(254, 202, 202, 255))

    # Mini "X" di kanan (area gelombang suara)
    draw.line([(18, 13), (23, 18)], fill=(239, 68, 68, 255))
    draw.line([(23, 13), (18, 18)], fill=(239, 68, 68, 255))

    return img

# ==========================================
# 5. ICON SPEED 1X (KECEPATAN NORMAL)
# ==========================================
def draw_icon_speed_1x():
    accent = (255, 210, 0)  # Gold
    img = create_base_frame(accent, (70, 60, 25))
    draw = ImageDraw.Draw(img)

    # Single vertical cyber lightning bolt
    # Aura luar
    pts_aura = [
        (16, 6), (11, 15), (15, 15), (12, 25), (20, 14), (16, 14)
    ]
    draw.polygon(pts_aura, fill=(255, 210, 0, 80))

    # Petir inti tajam
    pts_bolt = [
        (16, 7), (12, 15), (16, 15), (13, 24), (20, 14), (16, 14)
    ]
    draw.polygon(pts_bolt, fill=(255, 230, 60, 255))

    # Highlight putih
    draw.line([(15, 8), (13, 14)], fill=(255, 255, 240, 255))
    draw.line([(16, 16), (14, 22)], fill=(255, 255, 240, 255))

    # Indikator teks mini pixel "1" di sudut kanan bawah
    # 1 baris
    draw.point([(23, 20), (24, 19), (24, 20), (24, 21), (24, 22), (24, 23), (23, 23), (25, 23)], fill=(255, 210, 0, 220))

    return img

# ==========================================
# 6. ICON SPEED 2X (KECEPATAN TURBO)
# ==========================================
def draw_icon_speed_2x():
    accent = (255, 119, 0)  # Fire Orange / Red
    img = create_base_frame(accent, (80, 40, 15))
    draw = ImageDraw.Draw(img)

    # Petir ganda + akselerasi supersonik
    # Petir 1 (kiri)
    pts_bolt1 = [(12, 8), (8, 16), (12, 16), (9, 24), (16, 15), (12, 15)]
    draw.polygon(pts_bolt1, fill=(245, 158, 11, 240))

    # Petir 2 (kanan)
    pts_bolt2 = [(18, 7), (14, 15), (18, 15), (15, 23), (22, 14), (18, 14)]
    draw.polygon(pts_bolt2, fill=(255, 80, 0, 255))

    # Highlight core putih di petir kanan
    draw.line([(17, 8), (15, 14)], fill=(255, 240, 200, 255))
    draw.line([(18, 16), (16, 21)], fill=(255, 240, 200, 255))

    # Supersonic chevron ">>" di kanan atas
    # Chevron 1
    draw.line([(22, 8), (24, 10)], fill=(255, 210, 0, 240))
    draw.line([(24, 10), (22, 12)], fill=(255, 210, 0, 240))
    # Chevron 2
    draw.line([(25, 8), (27, 10)], fill=(255, 119, 0, 240))
    draw.line([(27, 10), (25, 12)], fill=(255, 119, 0, 240))

    return img

# ==========================================
# 7. ICON FULLSCREEN ENTER (MASUK LAYAR PENUH)
# ==========================================
def draw_icon_fullscreen_enter():
    accent = (0, 242, 254)  # Cyan
    img = create_base_frame(accent, (20, 60, 80))
    draw = ImageDraw.Draw(img)

    # 4 kurung siku reticle mengarah KELUAR ke sudut-sudut
    col = (0, 242, 254, 255)
    col_white = (220, 250, 255, 255)

    # Top-Left outward bracket
    draw.rectangle([8, 8, 13, 9], fill=col)
    draw.rectangle([8, 8, 9, 13], fill=col)
    draw.point((8, 8), fill=col_white)

    # Top-Right outward bracket
    draw.rectangle([18, 8, 23, 9], fill=col)
    draw.rectangle([22, 8, 23, 13], fill=col)
    draw.point((23, 8), fill=col_white)

    # Bottom-Left outward bracket
    draw.rectangle([8, 22, 13, 23], fill=col)
    draw.rectangle([8, 18, 9, 23], fill=col)
    draw.point((8, 23), fill=col_white)

    # Bottom-Right outward bracket
    draw.rectangle([18, 22, 23, 23], fill=col)
    draw.rectangle([22, 18, 23, 23], fill=col)
    draw.point((23, 23), fill=col_white)

    # Titik radar sensor di tengah
    draw.rectangle([15, 15, 16, 16], fill=(0, 242, 254, 180))

    return img

# ==========================================
# 8. ICON FULLSCREEN EXIT (KELUAR LAYAR PENUH)
# ==========================================
def draw_icon_fullscreen_exit():
    accent = (52, 211, 153)  # Emerald Mint
    img = create_base_frame(accent, (20, 65, 50))
    draw = ImageDraw.Draw(img)

    # 4 kurung siku reticle mengarah KE DALAM (mengecil)
    col = (52, 211, 153, 255)
    col_white = (230, 255, 240, 255)

    # Top-Left inward bracket (menghadap pusat)
    draw.rectangle([10, 13, 14, 14], fill=col)
    draw.rectangle([13, 10, 14, 14], fill=col)
    draw.point((14, 14), fill=col_white)

    # Top-Right inward bracket
    draw.rectangle([17, 13, 21, 14], fill=col)
    draw.rectangle([17, 10, 18, 14], fill=col)
    draw.point((17, 14), fill=col_white)

    # Bottom-Left inward bracket
    draw.rectangle([10, 17, 14, 18], fill=col)
    draw.rectangle([13, 17, 14, 21], fill=col)
    draw.point((14, 17), fill=col_white)

    # Bottom-Right inward bracket
    draw.rectangle([17, 17, 21, 18], fill=col)
    draw.rectangle([17, 17, 18, 21], fill=col)
    draw.point((17, 17), fill=col_white)

    return img

# ==========================================
# EKSEKUSI PENYIMPANAN
# ==========================================
def main():
    icons = {
        "icon_btn_pause.png": draw_icon_pause(),
        "icon_btn_resume.png": draw_icon_resume(),
        "icon_btn_sound_on.png": draw_icon_sound_on(),
        "icon_btn_sound_off.png": draw_icon_sound_off(),
        "icon_btn_speed_1x.png": draw_icon_speed_1x(),
        "icon_btn_speed_2x.png": draw_icon_speed_2x(),
        "icon_btn_fullscreen_enter.png": draw_icon_fullscreen_enter(),
        "icon_btn_fullscreen_exit.png": draw_icon_fullscreen_exit(),
    }

    print("1. Menyimpan 8 ikon pixel art individual ke assets/ui/ ...")
    for filename, img in icons.items():
        out_path = os.path.join(UI_DIR, filename)
        img.save(out_path, "PNG")
        print(f"   [OK] {filename} (32x32 RGBA)")

    # Buat Master Raw Sheet (Grid 4x2 di atas latar #FF00FF Magenta)
    print("\n2. Membuat Master Spritesheet Raw (Grid 4x2) di assets_raw/ui/hud_top_icons_raw.png ...")
    # Kanvas: 4 kolom x 2 baris, padding 8px antar ikon
    cell_w, cell_h = 32, 32
    pad = 8
    grid_cols, grid_rows = 4, 2
    sheet_w = grid_cols * cell_w + (grid_cols + 1) * pad
    sheet_h = grid_rows * cell_h + (grid_rows + 1) * pad

    magenta_bg = (255, 0, 255)
    sheet = Image.new("RGB", (sheet_w, sheet_h), magenta_bg)

    icon_order = [
        # Baris 1: State Normal
        "icon_btn_pause.png",
        "icon_btn_sound_on.png",
        "icon_btn_speed_1x.png",
        "icon_btn_fullscreen_enter.png",
        # Baris 2: State Toggle / Aktif
        "icon_btn_resume.png",
        "icon_btn_sound_off.png",
        "icon_btn_speed_2x.png",
        "icon_btn_fullscreen_exit.png",
    ]

    for idx, name in enumerate(icon_order):
        row = idx // grid_cols
        col = idx % grid_cols
        x = pad + col * (cell_w + pad)
        y = pad + row * (cell_h + pad)
        img = icons[name]
        # Paste dengan mask alpha di atas latar magenta
        sheet.paste(img, (x, y), img)

    raw_path = os.path.join(RAW_UI_DIR, "hud_top_icons_raw.png")
    sheet.save(raw_path, "PNG")
    print(f"   [OK] Master Raw Sheet tersimpan ({sheet_w}x{sheet_h} px RGB #FF00FF)")

if __name__ == "__main__":
    main()
