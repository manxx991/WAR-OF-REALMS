"""
process_all_assets.py
Script pemrosesan menyeluruh untuk seluruh aset game:
1. Damaged Castles (castle_player_damaged.png, castle_enemy_damaged.png) -> 96x112 px RGBA
2. Sunset & Hills Biome Backgrounds (bg_sky_sunset.png, bg_far_hills.png) -> height 216 px
3. Unit Avatars untuk Deck Cards (avatar_hero_*.png) -> 32x32 px RGBA
4. Action Button Icons (icon_btn_mana_quiz.png, icon_btn_heal_base.png) -> 40x40 px RGBA
5. Quiz Option Buttons (btn_quiz_opt_*.png) -> sliced & RGBA
6. VFX Bubble Pop (vfx_bubble_pop.png) -> 160x32 px RGBA (5 frames)
"""

import os
import shutil
from PIL import Image

ASSETS_DIR = r"C:\GAME\assets"
RAW_BACKUP_DIR = r"C:\GAME\assets_raw"

def chroma_key_magenta(pil_img, corner_color=None, dist_cutoff=45, dist_max=85):
    img = pil_img.convert("RGBA")
    w, h = img.size
    if corner_color is None:
        corner_color = img.getpixel((5, 5))[:3]
        
    cr, cg, cb = corner_color
    pixels = img.load()
    
    for y in range(h):
        for x in range(w):
            r, g, b, a = pixels[x, y]
            dist = ((r - cr)**2 + (g - cg)**2 + (b - cb)**2)**0.5
            if dist <= dist_cutoff:
                pixels[x, y] = (0, 0, 0, 0)
            elif dist <= dist_max:
                alpha = int(((dist - dist_cutoff) / (dist_max - dist_cutoff)) * 255)
                pixels[x, y] = (r, min(255, int(g * 1.25)), b, alpha)
    return img

def chroma_key_black(pil_img, cutoff=35, max_val=80):
    img = pil_img.convert("RGBA")
    w, h = img.size
    pixels = img.load()
    for y in range(h):
        for x in range(w):
            r, g, b, a = pixels[x, y]
            brightness = (r + g + b) / 3.0
            if brightness <= cutoff:
                pixels[x, y] = (0, 0, 0, 0)
            elif brightness <= max_val:
                alpha = int(((brightness - cutoff) / (max_val - cutoff)) * 255)
                pixels[x, y] = (r, g, b, alpha)
    return img

def get_tight_bbox(img_rgba):
    alpha = img_rgba.split()[3]
    return alpha.getbbox()

def process_damaged_castles():
    print("1. Memproses Damaged Castles (Player & Enemy)...")
    castles = [
        ("castle_player_damaged.png", 85, 1285),
        ("castle_enemy_damaged.png", 92, 1279)
    ]
    for filename, y0, y1 in castles:
        src = os.path.join(RAW_BACKUP_DIR, "sprites", "buildings", filename)
        dest = os.path.join(ASSETS_DIR, "sprites", "buildings", filename)
        if not os.path.exists(src):
            print(f"   [SKIP] {src} tidak ditemukan.")
            continue
        
        raw = Image.open(src).convert("RGB")
        corner = raw.getpixel((5, 5))
        cropped = raw.crop((0, y0, raw.size[0], y1))
        rgba = chroma_key_magenta(cropped, corner)
        bbox = get_tight_bbox(rgba)
        if bbox:
            castle_sprite = rgba.crop(bbox)
        else:
            castle_sprite = rgba
            
        sw, sh = castle_sprite.size
        target_w = 96
        target_h = 112
        scale = min(target_w / float(sw), target_h / float(sh))
        final_w = max(1, int(sw * scale))
        final_h = max(1, int(sh * scale))
        
        resized = castle_sprite.resize((final_w, final_h), Image.Resampling.LANCZOS)
        
        castle_canvas = Image.new("RGBA", (target_w, target_h), (0, 0, 0, 0))
        paste_x = (target_w - final_w) // 2
        paste_y = target_h - final_h
        castle_canvas.paste(resized, (paste_x, paste_y), resized)
        castle_canvas.save(dest, "PNG")
        print(f"   [OK] {filename}: {final_w}x{final_h} dipusatkan dalam kanvas 96x112 px")

def process_sunset_biome():
    print("2. Memproses Sunset Biome Backgrounds...")
    # 1. Sky Sunset
    src_sky = os.path.join(RAW_BACKUP_DIR, "background", "bg_sky_sunset.png")
    dest_sky = os.path.join(ASSETS_DIR, "background", "bg_sky_sunset.png")
    if os.path.exists(src_sky):
        img_sky = Image.open(src_sky).convert("RGB")
        sky_w = int(img_sky.size[0] * (216.0 / img_sky.size[1]))
        resized_sky = img_sky.resize((sky_w, 216), Image.Resampling.LANCZOS)
        resized_sky.save(dest_sky, "PNG")
        print(f"   [OK] bg_sky_sunset.png: {sky_w}x216 px")

    # 2. Far Hills (chroma-keyed magenta sky)
    src_hills = os.path.join(RAW_BACKUP_DIR, "background", "bg_far_hills.png")
    dest_hills = os.path.join(ASSETS_DIR, "background", "bg_far_hills.png")
    if os.path.exists(src_hills):
        img_hills = Image.open(src_hills).convert("RGB")
        corner = img_hills.getpixel((5, 5))
        rgba_hills = chroma_key_magenta(img_hills, corner)
        hills_w = int(rgba_hills.size[0] * (216.0 / rgba_hills.size[1]))
        resized_hills = rgba_hills.resize((hills_w, 216), Image.Resampling.LANCZOS)
        resized_hills.save(dest_hills, "PNG")
        print(f"   [OK] bg_far_hills.png: {hills_w}x216 px (RGBA with transparent sky)")

def process_hero_avatars():
    print("3. Memproses Unit Avatars untuk Deck Cards...")
    heroes = [
        ("hero_swordsman", 32),
        ("hero_archer", 32),
        ("hero_mage", 32),
        ("hero_pony", 48),
        ("hero_golem", 64)
    ]
    
    os.makedirs(os.path.join(ASSETS_DIR, "ui"), exist_ok=True)
    
    for name, cell_size in heroes:
        sheet_path = os.path.join(ASSETS_DIR, "sprites", "heroes", f"{name}.png")
        dest_avatar = os.path.join(ASSETS_DIR, "ui", f"avatar_{name}.png")
        if not os.path.exists(sheet_path):
            print(f"   [SKIP] {sheet_path} tidak ditemukan.")
            continue
        
        sheet = Image.open(sheet_path).convert("RGBA")
        # Frame 0 di Baris 0 adalah pose Idle
        frame0 = sheet.crop((0, 0, cell_size, cell_size))
        bbox = get_tight_bbox(frame0)
        if bbox:
            cropped = frame0.crop(bbox)
        else:
            cropped = frame0
            
        target_size = 32
        scale = min(28.0 / cropped.size[0], 28.0 / cropped.size[1])
        aw = max(1, int(cropped.size[0] * scale))
        ah = max(1, int(cropped.size[1] * scale))
        
        # Nearest neighbor agar pixel tetap tajam
        resized = cropped.resize((aw, ah), Image.Resampling.NEAREST)
        
        avatar_img = Image.new("RGBA", (target_size, target_size), (0, 0, 0, 0))
        paste_x = (target_size - aw) // 2
        paste_y = (target_size - ah) // 2
        avatar_img.paste(resized, (paste_x, paste_y), resized)
        avatar_img.save(dest_avatar, "PNG")
        print(f"   [OK] avatar_{name}.png: 32x32 px avatar")

def process_action_button_icons():
    print("4. Memproses Action Button Icons...")
    # Mana Quiz button icon
    src_mana = os.path.join(RAW_BACKUP_DIR, "ui", "btn_mana_quiz.png")
    dest_mana = os.path.join(ASSETS_DIR, "ui", "icon_btn_mana_quiz.png")
    if os.path.exists(src_mana):
        raw = Image.open(src_mana).convert("RGB")
        corner = raw.getpixel((5, 5))
        rgba = chroma_key_magenta(raw, corner)
        bbox = get_tight_bbox(rgba)
        if bbox:
            cropped = rgba.crop(bbox)
        else:
            cropped = rgba
        icon = cropped.resize((40, 40), Image.Resampling.LANCZOS)
        icon.save(dest_mana, "PNG")
        print("   [OK] icon_btn_mana_quiz.png: 40x40 px")

    # Heal Base button icon
    src_heal = os.path.join(RAW_BACKUP_DIR, "ui", "btn_heal_base.png")
    dest_heal = os.path.join(ASSETS_DIR, "ui", "icon_btn_heal_base.png")
    if os.path.exists(src_heal):
        raw = Image.open(src_heal).convert("RGB")
        corner = raw.getpixel((5, 5))
        rgba = chroma_key_magenta(raw, corner)
        bbox = get_tight_bbox(rgba)
        if bbox:
            cropped = rgba.crop(bbox)
        else:
            cropped = rgba
        icon = cropped.resize((40, 40), Image.Resampling.LANCZOS)
        icon.save(dest_heal, "PNG")
        print("   [OK] icon_btn_heal_base.png: 40x40 px")

def process_quiz_option_buttons():
    print("5. Memproses Quiz Option Buttons (A, B, C, D)...")
    src = os.path.join(RAW_BACKUP_DIR, "ui", "btn_quiz_options.png")
    if not os.path.exists(src):
        print(f"   [SKIP] {src} tidak ditemukan.")
        return
    
    raw = Image.open(src).convert("RGB")
    corner = raw.getpixel((5, 5))
    segments = [
        ("btn_quiz_opt_a.png", (52, 310, 443, 571)),
        ("btn_quiz_opt_b.png", (455, 310, 843, 571)),
        ("btn_quiz_opt_c.png", (855, 310, 1244, 571)),
        ("btn_quiz_opt_d.png", (1256, 310, 1647, 571))
    ]
    for filename, (x0, y0, x1, y1) in segments:
        dest = os.path.join(ASSETS_DIR, "ui", filename)
        crop = raw.crop((x0, y0, x1, y1))
        rgba = chroma_key_magenta(crop, corner)
        bbox = get_tight_bbox(rgba)
        if bbox:
            cropped = rgba.crop(bbox)
        else:
            cropped = rgba
        # Target size for quiz option button frame: 190x40
        btn_img = cropped.resize((190, 40), Image.Resampling.LANCZOS)
        btn_img.save(dest, "PNG")
        print(f"   [OK] {filename}: 190x40 px (RGBA)")

def process_vfx_bubble():
    print("6. Memproses VFX Bubble Pop...")
    src = os.path.join(RAW_BACKUP_DIR, "sprites", "vfx", "vfx_bubble_pop.png")
    dest = os.path.join(ASSETS_DIR, "sprites", "vfx", "vfx_bubble_pop.png")
    if not os.path.exists(src):
        print(f"   [SKIP] {src} tidak ditemukan.")
        return
    
    raw = Image.open(src).convert("RGB")
    corner = raw.getpixel((5, 5))
    # 5 frames across width
    w, h = raw.size
    frame_w = w // 5
    sheet = Image.new("RGBA", (5 * 32, 32), (0, 0, 0, 0))
    for i in range(5):
        crop = raw.crop((i * frame_w, 0, (i + 1) * frame_w, h))
        rgba = chroma_key_magenta(crop, corner)
        bbox = get_tight_bbox(rgba)
        if bbox:
            f = rgba.crop(bbox)
            scale = min(30.0 / f.size[0], 30.0 / f.size[1])
            fw = max(1, int(f.size[0] * scale))
            fh = max(1, int(f.size[1] * scale))
            res = f.resize((fw, fh), Image.Resampling.LANCZOS)
            sheet.paste(res, (i * 32 + (32 - fw) // 2, (32 - fh) // 2), res)
    sheet.save(dest, "PNG")
    print("   [OK] vfx_bubble_pop.png: 160x32 px (5 frames x 32x32)")

if __name__ == "__main__":
    process_damaged_castles()
    process_sunset_biome()
    process_hero_avatars()
    process_action_button_icons()
    process_quiz_option_buttons()
    process_vfx_bubble()
    print("\nSeluruh aset baru berhasil diproses dan disesuaikan ke standar retro game!")
