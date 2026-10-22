"""
process_assets.py
Script otomatis untuk:
1. Backup asset mentah resolusi tinggi ke C:/GAME/assets_raw/
2. Menghapus latar magenta/hitam menjadi transparan (RGBA)
3. Crop & resize karakter, benteng, background, VFX, dan UI ke standar native pixel-art
"""

import os
import shutil
from PIL import Image

ASSETS_DIR = r"C:\GAME\assets"
RAW_BACKUP_DIR = r"C:\GAME\assets_raw"

def make_dirs():
    os.makedirs(RAW_BACKUP_DIR, exist_ok=True)
    for root, dirs, files in os.walk(ASSETS_DIR):
        rel = os.path.relpath(root, ASSETS_DIR)
        dest = os.path.join(RAW_BACKUP_DIR, rel)
        os.makedirs(dest, exist_ok=True)

def backup_raw_assets():
    print("1. Membuat backup aset mentah ke assets_raw/ ...")
    for root, dirs, files in os.walk(ASSETS_DIR):
        for f in files:
            if f.lower().endswith(".png"):
                src = os.path.join(root, f)
                rel = os.path.relpath(src, ASSETS_DIR)
                dest = os.path.join(RAW_BACKUP_DIR, rel)
                if not os.path.exists(dest):
                    shutil.copy2(src, dest)
    print("   Backup selesai!")

def chroma_key_magenta(pil_img, corner_color=None, dist_cutoff=40, dist_max=75):
    """
    Mengubah warna latar belakang magenta menjadi transparan murni dengan soft anti-aliased edge.
    """
    img = pil_img.convert("RGBA")
    w, h = img.size
    if corner_color is None:
        corner_color = img.getpixel((5, 5))[:3]
        
    cr, cg, cb = corner_color
    pixels = img.load()
    
    for y in range(h):
        for x in range(w):
            r, g, b, a = pixels[x, y]
            # Euclidean distance to corner color in RGB
            dist = ((r - cr)**2 + (g - cg)**2 + (b - cb)**2)**0.5
            if dist <= dist_cutoff:
                pixels[x, y] = (0, 0, 0, 0)
            elif dist <= dist_max:
                alpha = int(((dist - dist_cutoff) / (dist_max - dist_cutoff)) * 255)
                # Defringe: reduce magenta contamination
                pixels[x, y] = (r, min(255, int(g * 1.2)), b, alpha)
    return img

def chroma_key_black(pil_img, cutoff=35, max_val=80):
    """
    Untuk efek visual (VFX Sparks) berlatar belakang hitam murni.
    """
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
    """Menemukan bounding box dari pixel non-transparan"""
    alpha = img_rgba.split()[3]
    return alpha.getbbox()

def process_characters():
    print("2. Memproses Spritesheet Karakter Pasukan & Monster...")
    characters = [
        # (folder, name, target_cell_size)
        ("heroes", "hero_swordsman", 32),
        ("heroes", "hero_archer", 32),
        ("heroes", "hero_mage", 32),
        ("heroes", "hero_pony", 48),
        ("heroes", "hero_golem", 64),
        ("enemies", "enemy_slime", 32),
        ("enemies", "enemy_bunny", 32),
        ("enemies", "enemy_pebble", 32),
        ("enemies", "boss_croc", 64),
        ("enemies", "boss_dragon", 96),
    ]
    
    for folder, name, cell_size in characters:
        src_path = os.path.join(RAW_BACKUP_DIR, "sprites", folder, f"{name}.png")
        dest_path = os.path.join(ASSETS_DIR, "sprites", folder, f"{name}.png")
        
        raw_img = Image.open(src_path).convert("RGB")
        w, h = raw_img.size
        corner = raw_img.getpixel((5, 5))
        
        # 1. Deteksi 5 baris animasi utama
        row_counts = [sum(1 for x in range(0, w, 4) if abs(raw_img.getpixel((x, y))[0]-corner[0]) + abs(raw_img.getpixel((x, y))[1]-corner[1]) + abs(raw_img.getpixel((x, y))[2]-corner[2]) > 60) for y in range(h)]
        blocks = []
        in_b = False
        start = 0
        for y, cnt in enumerate(row_counts):
            if cnt > 15 and not in_b: in_b = True; start = y
            elif cnt <= 15 and in_b: in_b = False; blocks.append((start, y))
        if in_b: blocks.append((start, h))
        sprite_rows = [b for b in blocks if (b[1]-b[0]) >= 60][:5]
        
        # Buat spritesheet target: 6 kolom x 5 baris
        sheet_w = 6 * cell_size
        sheet_h = 5 * cell_size
        new_sheet = Image.new("RGBA", (sheet_w, sheet_h), (0, 0, 0, 0))
        
        for r_idx, (y0, y1) in enumerate(sprite_rows):
            # Deteksi frame dalam baris
            col_counts = [sum(1 for y in range(y0, y1, 2) if abs(raw_img.getpixel((x, y))[0]-corner[0]) + abs(raw_img.getpixel((x, y))[1]-corner[1]) + abs(raw_img.getpixel((x, y))[2]-corner[2]) > 60) for x in range(w)]
            thresh = max(12, int(0.08 * (y1 - y0)))
            frames = []
            in_f = False
            f_start = 0
            for x, cnt in enumerate(col_counts):
                if cnt >= thresh and not in_f: in_f = True; f_start = x
                elif cnt < thresh and in_f:
                    in_f = False
                    if x - f_start > 30: frames.append((f_start, x))
            if in_f and w - f_start > 30: frames.append((f_start, w))
            
            # Ambil maksimal 6 frame
            for col_idx, (fx0, fx1) in enumerate(frames[:6]):
                frame_crop = raw_img.crop((fx0, y0, fx1, y1))
                frame_rgba = chroma_key_magenta(frame_crop, corner)
                bbox = get_tight_bbox(frame_rgba)
                if not bbox: continue
                
                sprite_crop = frame_rgba.crop(bbox)
                sw, sh = sprite_crop.size
                
                # Skala proporsional ke dalam target cell (dengan margin 2px agar proporsional)
                max_dim = cell_size - 2
                scale = min(max_dim / float(sw), max_dim / float(sh))
                new_sw = max(1, int(sw * scale))
                new_sh = max(1, int(sh * scale))
                
                resized_sprite = sprite_crop.resize((new_sw, new_sh), Image.Resampling.LANCZOS)
                
                # Posisi di dalam sel: tengah horizontal, kaki nempel bawah (grounded)
                paste_x = col_idx * cell_size + (cell_size - new_sw) // 2
                paste_y = r_idx * cell_size + (cell_size - new_sh)
                
                new_sheet.paste(resized_sprite, (paste_x, paste_y), resized_sprite)
                
        new_sheet.save(dest_path, "PNG")
        print(f"   [OK] {name}: {sheet_w}x{sheet_h} px (6 cols x 5 rows, cell {cell_size}x{cell_size})")

def process_castles():
    print("3. Memproses Bangunan Benteng...")
    castles = [
        ("castle_player.png", (108, 1278)),
        ("castle_enemy.png", (79, 1299))
    ]
    for filename, (y0, y1) in castles:
        src = os.path.join(RAW_BACKUP_DIR, "sprites", "buildings", filename)
        dest = os.path.join(ASSETS_DIR, "sprites", "buildings", filename)
        
        raw = Image.open(src).convert("RGB")
        corner = raw.getpixel((5, 5))
        
        # Crop bagian benteng tanpa label atas
        cropped = raw.crop((0, y0, raw.size[0], y1))
        rgba = chroma_key_magenta(cropped, corner)
        bbox = get_tight_bbox(rgba)
        if bbox:
            castle_sprite = rgba.crop(bbox)
        else:
            castle_sprite = rgba
            
        sw, sh = castle_sprite.size
        # Target size: width <= 96, height <= 112
        target_w = 96
        target_h = 112
        scale = min(target_w / float(sw), target_h / float(sh))
        final_w = max(1, int(sw * scale))
        final_h = max(1, int(sh * scale))
        
        resized = castle_sprite.resize((final_w, final_h), Image.Resampling.LANCZOS)
        
        # Buat canvas tepat 96 x 112 dengan benteng ditaruh di dasar
        castle_canvas = Image.new("RGBA", (target_w, target_h), (0, 0, 0, 0))
        paste_x = (target_w - final_w) // 2
        paste_y = target_h - final_h
        castle_canvas.paste(resized, (paste_x, paste_y), resized)
        castle_canvas.save(dest, "PNG")
        print(f"   [OK] {filename}: {final_w}x{final_h} dipusatkan dalam kanvas 96x112 px")

def process_backgrounds():
    print("4. Memproses Background & Lintasan...")
    # 1. Skybox
    src_sky = os.path.join(RAW_BACKUP_DIR, "background", "bg_sky_cyber.png")
    dest_sky = os.path.join(ASSETS_DIR, "background", "bg_sky_cyber.png")
    img_sky = Image.open(src_sky).convert("RGB")
    # scale height to 216 px
    sky_w = int(img_sky.size[0] * (216.0 / img_sky.size[1]))
    resized_sky = img_sky.resize((sky_w, 216), Image.Resampling.LANCZOS)
    resized_sky.save(dest_sky, "PNG")
    print(f"   [OK] bg_sky_cyber.png: {sky_w}x216 px")

    # 2. Far City
    src_far = os.path.join(RAW_BACKUP_DIR, "background", "bg_far_cyber_city.png")
    dest_far = os.path.join(ASSETS_DIR, "background", "bg_far_cyber_city.png")
    img_far = Image.open(src_far).convert("RGBA")
    far_w = int(img_far.size[0] * (216.0 / img_far.size[1]))
    resized_far = img_far.resize((far_w, 216), Image.Resampling.LANCZOS)
    resized_far.save(dest_far, "PNG")
    print(f"   [OK] bg_far_cyber_city.png: {far_w}x216 px (RGBA)")

    # 3. Mid Pylons
    src_mid = os.path.join(RAW_BACKUP_DIR, "background", "bg_mid_pylons.png")
    dest_mid = os.path.join(ASSETS_DIR, "background", "bg_mid_pylons.png")
    img_mid = Image.open(src_mid).convert("RGBA")
    mid_w = int(img_mid.size[0] * (216.0 / img_mid.size[1]))
    resized_mid = img_mid.resize((mid_w, 216), Image.Resampling.LANCZOS)
    resized_mid.save(dest_mid, "PNG")
    print(f"   [OK] bg_mid_pylons.png: {mid_w}x216 px (RGBA)")

    # 4. Tile Cyber Lane (Ground Strip)
    src_lane = os.path.join(RAW_BACKUP_DIR, "background", "tilesets", "tile_cyber_lane.png")
    dest_lane = os.path.join(ASSETS_DIR, "background", "tilesets", "tile_cyber_lane.png")
    img_lane = Image.open(src_lane).convert("RGB")
    corner = img_lane.getpixel((5, 5))
    # Crop central road strip (y=316..563)
    lane_strip = img_lane.crop((0, 316, img_lane.size[0], 563))
    lane_rgba = chroma_key_magenta(lane_strip, corner)
    bbox = get_tight_bbox(lane_rgba)
    if bbox:
        lane_cropped = lane_rgba.crop((0, bbox[1], lane_rgba.size[0], bbox[3]))
    else:
        lane_cropped = lane_rgba
    # Resize height to 72 px (covering ground y=144 to 216)
    lane_w = int(lane_cropped.size[0] * (72.0 / lane_cropped.size[1]))
    resized_lane = lane_cropped.resize((lane_w, 72), Image.Resampling.LANCZOS)
    resized_lane.save(dest_lane, "PNG")
    print(f"   [OK] tile_cyber_lane.png: {lane_w}x72 px (RGBA, height 72px for ground line y=144)")

def process_vfx():
    print("5. Memproses Visual Effects (VFX)...")
    # 1. Poof Cloud
    src_poof = os.path.join(RAW_BACKUP_DIR, "sprites", "vfx", "vfx_poof_cloud.png")
    dest_poof = os.path.join(ASSETS_DIR, "sprites", "vfx", "vfx_poof_cloud.png")
    img_poof = Image.open(src_poof).convert("RGB")
    corner_poof = img_poof.getpixel((5, 5))
    
    # 5 frames detected in range y=294..611
    col_ranges = [(73, 257), (352, 647), (711, 1054), (1112, 1408), (1486, 1701)]
    poof_sheet = Image.new("RGBA", (5 * 32, 32), (0, 0, 0, 0))
    for i, (cx0, cx1) in enumerate(col_ranges):
        crop = img_poof.crop((cx0, 294, cx1, 611))
        rgba = chroma_key_magenta(crop, corner_poof)
        bbox = get_tight_bbox(rgba)
        if bbox:
            f = rgba.crop(bbox)
            scale = min(30.0 / f.size[0], 30.0 / f.size[1])
            fw = max(1, int(f.size[0] * scale))
            fh = max(1, int(f.size[1] * scale))
            res = f.resize((fw, fh), Image.Resampling.LANCZOS)
            poof_sheet.paste(res, (i * 32 + (32 - fw) // 2, (32 - fh) // 2), res)
    poof_sheet.save(dest_poof, "PNG")
    print("   [OK] vfx_poof_cloud.png: 160x32 px (5 frames x 32x32)")

    # 2. Sparks
    src_sparks = os.path.join(RAW_BACKUP_DIR, "sprites", "vfx", "vfx_sparks.png")
    dest_sparks = os.path.join(ASSETS_DIR, "sprites", "vfx", "vfx_sparks.png")
    img_sparks = Image.open(src_sparks).convert("RGB")
    col_ranges_sp = [(52, 266), (344, 624), (707, 1077), (1148, 1427), (1534, 1789), (1897, 1953), (2020, 2111)]
    sparks_sheet = Image.new("RGBA", (len(col_ranges_sp) * 16, 16), (0, 0, 0, 0))
    for i, (cx0, cx1) in enumerate(col_ranges_sp):
        crop = img_sparks.crop((cx0, 180, cx1, 542))
        rgba = chroma_key_black(crop)
        bbox = get_tight_bbox(rgba)
        if bbox:
            f = rgba.crop(bbox)
            scale = min(14.0 / f.size[0], 14.0 / f.size[1])
            fw = max(1, int(f.size[0] * scale))
            fh = max(1, int(f.size[1] * scale))
            res = f.resize((fw, fh), Image.Resampling.LANCZOS)
            sparks_sheet.paste(res, (i * 16 + (16 - fw) // 2, (16 - fh) // 2), res)
    sparks_sheet.save(dest_sparks, "PNG")
    print(f"   [OK] vfx_sparks.png: {len(col_ranges_sp)*16}x16 px ({len(col_ranges_sp)} frames x 16x16)")

def process_ui():
    print("6. Memproses Antarmuka UI...")
    import colorsys
    from PIL import ImageDraw

    # 1. Pisahkan hud_mana_tube + hud_hp_bar
    src_combo = os.path.join(RAW_BACKUP_DIR, "ui", "hud_mana_tube + hud_hp_bar.png")
    if os.path.exists(src_combo):
        img_combo = Image.open(src_combo).convert("RGB")
        c = img_combo.getpixel((5, 5))
        # Tube: col (153, 433), row (155, 745)
        tube_crop = img_combo.crop((153, 155, 433, 745))
        tube_rgba = chroma_key_magenta(tube_crop, c)
        tube_bbox = get_tight_bbox(tube_rgba)
        if tube_bbox:
            tube_final = tube_rgba.crop(tube_bbox).resize((24, 48), Image.Resampling.LANCZOS)
        else:
            tube_final = tube_rgba.resize((24, 48), Image.Resampling.LANCZOS)
        tube_final.save(os.path.join(ASSETS_DIR, "ui", "hud_mana_tube.png"), "PNG")
        print("   [OK] hud_mana_tube.png: 24x48 px")

        # HP Bar: col (589, 1671), row (290, 565) - Bounding Box Tepat!
        hp_crop = img_combo.crop((589, 290, 1671, 565))
        hp_rgba = chroma_key_magenta(hp_crop, c)
        hp_bbox = get_tight_bbox(hp_rgba)
        if hp_bbox:
            hp_clean = hp_rgba.crop(hp_bbox)
        else:
            hp_clean = hp_rgba
        
        # Player HP Bar (96x22 px)
        player_bar = hp_clean.resize((96, 22), Image.Resampling.LANCZOS)
        player_bar.save(os.path.join(ASSETS_DIR, "ui", "hud_hp_bar_player.png"), "PNG")
        player_bar.save(os.path.join(ASSETS_DIR, "ui", "hud_hp_bar.png"), "PNG")

        # Enemy HP Bar (Varian Merah/Crimson)
        def make_red_variant(img):
            img_copy = img.copy()
            pixels = img_copy.load()
            w, h = img_copy.size
            for y in range(h):
                for x in range(w):
                    r, g, b, a = pixels[x, y]
                    if a == 0: continue
                    h_val, s_val, v_val = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
                    if 0.15 <= h_val <= 0.65:
                        new_h = (h_val - 0.33) % 1.0
                        new_r, new_g, new_b = colorsys.hsv_to_rgb(new_h, min(1.0, s_val * 1.2), v_val)
                        pixels[x, y] = (int(new_r * 255), int(new_g * 255), int(new_b * 255), a)
            return img_copy

        enemy_bar = make_red_variant(player_bar)
        enemy_bar.save(os.path.join(ASSETS_DIR, "ui", "hud_hp_bar_enemy.png"), "PNG")

        # Shield Icons (18x18 px)
        shield_crop = hp_clean.crop((0, 0, int(hp_clean.width * 0.24), hp_clean.height))
        sh_bbox = get_tight_bbox(shield_crop)
        if sh_bbox:
            shield_icon = shield_crop.crop(sh_bbox).resize((18, 18), Image.Resampling.LANCZOS)
        else:
            shield_icon = shield_crop.resize((18, 18), Image.Resampling.LANCZOS)
        shield_icon.save(os.path.join(ASSETS_DIR, "ui", "icon_shield_player.png"), "PNG")
        enemy_shield = make_red_variant(shield_icon)
        enemy_shield.save(os.path.join(ASSETS_DIR, "ui", "icon_shield_enemy.png"), "PNG")

        # Frame dengan slot transparan gelap untuk live dynamic fill
        def create_frame(src_img, out_path):
            f_img = src_img.copy()
            pixels = f_img.load()
            for y in range(7, 15):
                for x in range(25, 91):
                    pixels[x, y] = (10, 16, 28, 220)
            f_img.save(out_path)

        create_frame(player_bar, os.path.join(ASSETS_DIR, "ui", "hud_hp_bar_frame_player.png"))
        create_frame(enemy_bar, os.path.join(ASSETS_DIR, "ui", "hud_hp_bar_frame_enemy.png"))
        print("   [OK] hud_hp_bar_player.png, hud_hp_bar_enemy.png, frames & icons: 96x22 px")

    # 2. Card Unit Frame
    src_card = os.path.join(RAW_BACKUP_DIR, "ui", "card_unit_frame.png")
    if os.path.exists(src_card):
        img_card = Image.open(src_card).convert("RGB")
        c = img_card.getpixel((5, 5))
        # Frame Normal
        card_crop = img_card.crop((179, 87, 773, 746))
        card_rgba = chroma_key_magenta(card_crop, c)
        card_bbox = get_tight_bbox(card_rgba)
        if card_bbox:
            card_final = card_rgba.crop(card_bbox).resize((62, 68), Image.Resampling.LANCZOS)
        else:
            card_final = card_rgba.resize((62, 68), Image.Resampling.LANCZOS)
        card_final.save(os.path.join(ASSETS_DIR, "ui", "card_unit_frame.png"), "PNG")

        # Frame Active / Cooldown
        card_crop_act = img_card.crop((973, 87, 1564, 746))
        card_rgba_act = chroma_key_magenta(card_crop_act, c)
        act_bbox = get_tight_bbox(card_rgba_act)
        if act_bbox:
            act_final = card_rgba_act.crop(act_bbox).resize((62, 68), Image.Resampling.LANCZOS)
        else:
            act_final = card_rgba_act.resize((62, 68), Image.Resampling.LANCZOS)
        act_final.save(os.path.join(ASSETS_DIR, "ui", "card_unit_frame_active.png"), "PNG")
        print("   [OK] card_unit_frame.png & card_unit_frame_active.png: 62x68 px")

    # 3. Popup Quiz Dialog
    src_dlg = os.path.join(RAW_BACKUP_DIR, "ui", "popup_quiz_dialog.png")
    if os.path.exists(src_dlg):
        img_dlg = Image.open(src_dlg).convert("RGB")
        c = img_dlg.getpixel((5, 5))
        dlg_crop = img_dlg.crop((81, 79, 1942, 710))
        dlg_rgba = chroma_key_magenta(dlg_crop, c)
        dlg_bbox = get_tight_bbox(dlg_rgba)
        if dlg_bbox:
            dlg_final = dlg_rgba.crop(dlg_bbox).resize((420, 150), Image.Resampling.LANCZOS)
        else:
            dlg_final = dlg_rgba.resize((420, 150), Image.Resampling.LANCZOS)
        dlg_final.save(os.path.join(ASSETS_DIR, "ui", "popup_quiz_dialog.png"), "PNG")
        print("   [OK] popup_quiz_dialog.png: 420x150 px")

    # 4. Radar Frame Asset
    rf = Image.new('RGBA', (160, 16), (0, 0, 0, 0))
    d = ImageDraw.Draw(rf)
    d.rectangle([1, 1, 158, 14], fill=(6, 12, 24, 230), outline=(0, 242, 254, 80))
    for y in range(3, 14, 3):
        d.line([(2, y), (157, y)], fill=(0, 242, 254, 25))
    corner_len = 5
    cyan = (0, 242, 254, 255)
    d.line([(0, 0), (corner_len, 0)], fill=cyan)
    d.line([(0, 0), (0, corner_len)], fill=cyan)
    d.line([(159 - corner_len, 0), (159, 0)], fill=cyan)
    d.line([(159, 0), (159, corner_len)], fill=cyan)
    d.line([(0, 15), (corner_len, 15)], fill=cyan)
    d.line([(0, 15 - corner_len), (0, 15)], fill=cyan)
    d.line([(159 - corner_len, 15), (159, 15)], fill=cyan)
    d.line([(159, 15 - corner_len), (159, 15)], fill=cyan)
    rf.save(os.path.join(ASSETS_DIR, "ui", "hud_radar_frame.png"), "PNG")
    print("   [OK] hud_radar_frame.png: 160x16 px")

if __name__ == "__main__":
    make_dirs()
    backup_raw_assets()
    process_characters()
    process_castles()
    process_backgrounds()
    process_vfx()
    process_ui()
    print("\nSELURUH 21 ASET BERHASIL DIKONVERSI & TERHUBUNG KE STANDAR RETRO GAME!")
