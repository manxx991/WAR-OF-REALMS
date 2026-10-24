"""
process_hud_icons.py
Script pemrosesan otomatis untuk aset Master HUD Icons:
1. Membaca gambar raw dari assets_raw/ui/hud_top_icons_raw.png (atau path kustom)
2. Menghapus latar belakang solid magenta (#FF00FF) menjadi transparan murni (RGBA)
3. Melakukan slicing grid 4x2 secara otomatis
4. Menyimpan 8 ikon individual 32x32 px ke assets/ui/:
   - icon_btn_pause.png
   - icon_btn_sound_on.png
   - icon_btn_speed_1x.png
   - icon_btn_fullscreen_enter.png
   - icon_btn_resume.png
   - icon_btn_sound_off.png
   - icon_btn_speed_2x.png
   - icon_btn_fullscreen_exit.png
"""

import os
import sys
from PIL import Image

ASSETS_DIR = r"C:\GAME\assets\ui"
RAW_DIR = r"C:\GAME\assets_raw\ui"
DEFAULT_RAW_FILE = os.path.join(RAW_DIR, "hud_top_icons_raw.png")

ICON_NAMES = [
    # Baris 0 (State Normal)
    ["icon_btn_pause.png", "icon_btn_sound_on.png", "icon_btn_speed_1x.png", "icon_btn_fullscreen_enter.png"],
    # Baris 1 (State Aktif / Toggle)
    ["icon_btn_resume.png", "icon_btn_sound_off.png", "icon_btn_speed_2x.png", "icon_btn_fullscreen_exit.png"]
]

def chroma_key_magenta(pil_img, corner_color=None, dist_cutoff=45, dist_max=85):
    """Mengubah warna latar belakang magenta menjadi transparan murni dengan soft anti-aliased edge."""
    img = pil_img.convert("RGBA")
    w, h = img.size
    if corner_color is None:
        corner_color = img.getpixel((2, 2))[:3]
        
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
                # Defringe magenta
                pixels[x, y] = (r, min(255, int(g * 1.25)), b, alpha)
    return img

def get_tight_bbox(img_rgba):
    alpha = img_rgba.split()[3]
    return alpha.getbbox()

def process_hud_icons(raw_path=DEFAULT_RAW_FILE):
    if not os.path.exists(raw_path):
        print(f"[ERROR] File raw tidak ditemukan di: {raw_path}")
        print("Silakan letakkan hasil generate DALL-E / ChatGPT di path tersebut.")
        return False

    print(f"Membuka raw image: {raw_path}")
    raw_img = Image.open(raw_path).convert("RGB")
    w, h = raw_img.size
    print(f"Ukuran raw image: {w}x{h} px")

    # Chroma key latar magenta
    transparent_sheet = chroma_key_magenta(raw_img)

    # Menghitung perkiraan pembagian 4 kolom x 2 baris
    grid_cols = 4
    grid_rows = 2
    step_x = w / grid_cols
    step_y = h / grid_rows

    os.makedirs(ASSETS_DIR, exist_ok=True)

    print("\nMelakukan slicing dan optimasi 8 ikon ke standard 32x32 px RGBA:")
    for r in range(grid_rows):
        for c in range(grid_cols):
            name = ICON_NAMES[r][c]
            # Potong cell
            x0 = int(c * step_x)
            y0 = int(r * step_y)
            x1 = int((c + 1) * step_x)
            y1 = int((r + 1) * step_y)

            cell = transparent_sheet.crop((x0, y0, x1, y1))
            bbox = get_tight_bbox(cell)
            if bbox:
                cropped = cell.crop(bbox)
            else:
                cropped = cell

            # Resize proporsional ke kanvas 32x32 px
            cw, ch = cropped.size
            target_size = 32
            padding = 2
            max_inner = target_size - (padding * 2)

            scale = min(max_inner / float(cw), max_inner / float(ch))
            final_w = max(1, int(cw * scale))
            final_h = max(1, int(ch * scale))

            resized = cropped.resize((final_w, final_h), Image.Resampling.LANCZOS)

            canvas = Image.new("RGBA", (target_size, target_size), (0, 0, 0, 0))
            px = (target_size - final_w) // 2
            py = (target_size - final_h) // 2
            canvas.paste(resized, (px, py), resized)

            out_dest = os.path.join(ASSETS_DIR, name)
            canvas.save(out_dest, "PNG")
            print(f"   [OK] {name}: {final_w}x{final_h} dipusatkan dalam 32x32 px RGBA -> {out_dest}")

    print("\nSeluruh 8 ikon HUD berhasil diproses dan disimpan!")
    return True

if __name__ == "__main__":
    target_raw = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_RAW_FILE
    process_hud_icons(target_raw)
