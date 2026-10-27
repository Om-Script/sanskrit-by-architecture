import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# ==============================================================================
# SANSKRIT BY ARCHITECTURE: MASTER WRAP & FRONT COVER GENERATOR
# Book Trim: 7.0" x 10.0" | Spine: 0.486" (216 pages) | Bleed: 0.125"
# Spread: 14.736" x 10.25" @ 300 DPI = 4421 x 3075 px
# ==============================================================================

base_dir = r"C:\Users\TAG-SB\.gemini\antigravity-ide\brain\76debe45-2007-4e90-8451-5693723b476d\.user_uploaded"
input_path = os.path.join(base_dir, "media_1793072244287.jpg")

im_wrap = Image.open(input_path).convert("RGB")
w, h = im_wrap.size
print(f"Loaded master wrap: {input_path} ({w}x{h})")

def get_font(names, size):
    for n in names:
        for folder in ["final_chapters_md", r"C:\Windows\Fonts", "."]:
            fp = os.path.join(folder, n)
            if os.path.exists(fp):
                return ImageFont.truetype(fp, size)
    return ImageFont.load_default()

out_dir = r"C:\Users\TAG-SB\Desktop\Rama Code"
docs_dir = os.path.join(out_dir, "docs")
os.makedirs(docs_dir, exist_ok=True)

# ==============================================================================
# 1. FRONT COVER: AUTHOR BYLINE AT BOTTOM EDGE
# ==============================================================================
fc = im_wrap.crop((525, 0, 1024, 718))
arr_fc = np.array(fc)

# Inpaint 'by Timothy A. George' from y=286..308, x=150..345 (relative to fc)
# Leaving subtitle 'A Generative, Functional Blueprint for the Human Mind' untouched at y=263..282
y_top = 286
y_bot = 308
for y_cur in range(y_top, y_bot + 1):
    alpha = (y_cur - y_top) / (y_bot - y_top)
    for x_cur in range(150, 345):
        c_top = arr_fc[y_top - 2, x_cur].astype(float)
        c_bot = arr_fc[y_bot + 2, x_cur].astype(float)
        noise = (hash((x_cur, y_cur)) % 5) - 2
        c_blend = np.clip(c_top * (1 - alpha) + c_bot * alpha + noise, 0, 255).astype(np.uint8)
        arr_fc[y_cur, x_cur] = c_blend

fc_cleaned = Image.fromarray(arr_fc)

# Smooth the inpaint patch seamlessly into the sunset clouds
patch = fc_cleaned.crop((148, 285, 347, 310))
patch_smooth = patch.filter(ImageFilter.GaussianBlur(radius=1.2))
fc_cleaned.paste(patch_smooth, (148, 285))

fc_draw = ImageDraw.Draw(fc_cleaned)

# Render 'TIMOTHY A. GEORGE' along the bottom edge of the front cover
f_auth_fc = get_font(["LibertinusSerif-Bold.otf", "georgiab.ttf", "timesbd.ttf"], 13)
auth_str = "TIMOTHY  A.  GEORGE"
auth_w = fc_draw.textlength(auth_str, font=f_auth_fc)
auth_x = (fc_cleaned.width - int(auth_w)) // 2
auth_y = 672

# Rich warm gold bevel with deep shadow for legibility over stone/nebula
fc_draw.text((auth_x + 1, auth_y + 1), auth_str, font=f_auth_fc, fill=(15, 12, 18, 240))
fc_draw.text((auth_x, auth_y), auth_str, font=f_auth_fc, fill=(230, 215, 175, 255))

# Subtle decorative rule accents
line_len = 36
line_y = auth_y + 8
fc_draw.line([(auth_x - line_len - 14, line_y), (auth_x - 14, line_y)], fill=(180, 150, 95, 180), width=1)
fc_draw.point([(auth_x - 14, line_y - 1), (auth_x - 14, line_y + 1)], fill=(210, 180, 110, 220))

fc_draw.line([(auth_x + int(auth_w) + 14, line_y), (auth_x + int(auth_w) + 14 + line_len, line_y)], fill=(180, 150, 95, 180), width=1)
fc_draw.point([(auth_x + int(auth_w) + 14, line_y - 1), (auth_x + int(auth_w) + 14, line_y + 1)], fill=(210, 180, 110, 220))

# Save Standalone Front Cover Deliverables:
# Standard 7x10 aspect ratio portrait cover_final.jpg (718 x 1024 px) for repo & docs
fc_final_7x10 = fc_cleaned.resize((718, 1024), Image.Resampling.LANCZOS)
fc_final_7x10.save(os.path.join(out_dir, "cover_final.jpg"), "JPEG", quality=95)
fc_final_7x10.save(os.path.join(docs_dir, "cover_final.jpg"), "JPEG", quality=95)

# High-Res 300 DPI Standalone Front Cover (2100 x 3000 px) for Amazon KDP print & ebook
fc_final_300dpi = fc_cleaned.resize((2100, 3000), Image.Resampling.LANCZOS)
fc_final_300dpi.save(os.path.join(out_dir, "Ramayana_Front_Cover_300DPI.png"), dpi=(300, 300))

# ==============================================================================
# 2. FULL WRAP COMPOSITE WITH SURGICAL TYPO PATCHES & CLEAN SPINE
# ==============================================================================
master_wrap = im_wrap.copy()
wrap_draw = ImageDraw.Draw(master_wrap)

# A. Back cover: Line 1 'Rämāyana' -> 'Rāmāyaṇa'
bg_p1 = master_wrap.getpixel((201, 85))
wrap_draw.rectangle([203, 85, 209, 88], fill=bg_p1)
gold_p1 = (220, 215, 200)
wrap_draw.line([(204, 86), (209, 86)], fill=gold_p1, width=1)
wrap_draw.point([(247, 97), (248, 97), (247, 98), (248, 98)], fill=gold_p1)

# B. Back cover: Paragraph 3 'esposes' -> 'exposes'
bg_p3 = master_wrap.getpixel((287, 280))
wrap_draw.rectangle([287, 281, 293, 288], fill=bg_p3)
gold_p3 = (220, 215, 200)
gold_mid = (160, 155, 140)
wrap_draw.point([(288, 282), (289, 282), (292, 282), (293, 282)], fill=gold_p3)
wrap_draw.point([(289, 283), (290, 283), (291, 283), (292, 283)], fill=gold_p3)
wrap_draw.point([(290, 284), (291, 284)], fill=gold_p3)
wrap_draw.point([(289, 285), (292, 285)], fill=gold_mid)
wrap_draw.point([(290, 285), (291, 285)], fill=gold_p3)
wrap_draw.point([(290, 286), (291, 286)], fill=gold_p3)
wrap_draw.point([(289, 287), (290, 287), (291, 287), (292, 287)], fill=gold_p3)
wrap_draw.point([(288, 288), (289, 288), (292, 288), (293, 288)], fill=gold_p3)

# C. Back cover: Bullet 3 'arhitrary' -> 'arbitrary'
# Close bowl of 'h' at y=530..531, x=324..328 to form 'b'
gold_b3 = (230, 225, 210)
for x in range(324, 329):
    master_wrap.putpixel((x, 531), gold_b3)
    master_wrap.putpixel((x, 530), gold_b3)
for y in range(526, 531):
    master_wrap.putpixel((328, y), gold_b3)

# D. Paste the clean Front Cover onto the wrap
master_wrap.paste(fc_cleaned, (525, 0))

# E. Spine: Clean Subtitle + Separator Diamond + Author
spine_bg = master_wrap.getpixel((505, 362))
wrap_draw.rectangle([489, 365, 524, 695], fill=spine_bg)

f_sub = get_font(["LibertinusSerif-Semibold.otf", "georgia.ttf", "times.ttf"], 11)
f_auth = get_font(["LibertinusSerif-Bold.otf", "georgiab.ttf", "timesbd.ttf"], 12)

strip_w = 325
strip_h = 34
spine_layer = Image.new("RGBA", (strip_w, strip_h), (0, 0, 0, 0))
s_draw = ImageDraw.Draw(spine_layer)

sub_text = "DECODING THE RĀMĀYAṆA"
sub_w = s_draw.textlength(sub_text, font=f_sub)
sub_x = 10
sub_y = (strip_h - 12) // 2

s_draw.text((sub_x + 1, sub_y + 1), sub_text, font=f_sub, fill=(30, 25, 20, 220))
s_draw.text((sub_x, sub_y), sub_text, font=f_sub, fill=(225, 220, 205, 255))

d_cx = sub_x + int(sub_w) + 16
d_cy = strip_h // 2
s_draw.polygon([(d_cx, d_cy - 3), (d_cx + 3, d_cy), (d_cx, d_cy + 3), (d_cx - 3, d_cy)], fill=(218, 182, 105, 255))

auth_text = "TIMOTHY A. GEORGE"
auth_w = s_draw.textlength(auth_text, font=f_auth)
auth_x = d_cx + 16
auth_y = (strip_h - 13) // 2

s_draw.text((auth_x + 1, auth_y + 1), auth_text, font=f_auth, fill=(30, 25, 20, 220))
s_draw.text((auth_x, auth_y), auth_text, font=f_auth, fill=(218, 182, 105, 255))

spine_vert = spine_layer.rotate(270, expand=True)
master_wrap.paste(spine_vert, (490, 368), spine_vert)

# F. Save All Deliverables
master_wrap.save(os.path.join(out_dir, "Ramayana_Wrap_Cleaned_Native.png"), dpi=(300, 300))

wrap_300dpi = master_wrap.resize((4421, 3075), Image.Resampling.LANCZOS)
wrap_300dpi.save(os.path.join(out_dir, "Ramayana_Full_Wrap_300DPI_KDP.png"), dpi=(300, 300))
wrap_300dpi.save(os.path.join(out_dir, "Ramayana_Full_Wrap_300DPI_KDP.pdf"), "PDF", resolution=300.0)
master_wrap.save(os.path.join(docs_dir, "Ramayana_Full_Wrap.jpg"), "JPEG", quality=95)

print("=== ALL DELIVERABLES GENERATED SUCCESSFULLY ===")
print("Front Cover Final (docs/cover_final.jpg):", os.path.join(docs_dir, "cover_final.jpg"))
print("Front Cover (300 DPI):", os.path.join(out_dir, "Ramayana_Front_Cover_300DPI.png"))
print("Wrap (300 DPI PNG):", os.path.join(out_dir, "Ramayana_Full_Wrap_300DPI_KDP.png"))
print("Wrap (Print PDF):", os.path.join(out_dir, "Ramayana_Full_Wrap_300DPI_KDP.pdf"))
print("Docs Web Wrap:", os.path.join(docs_dir, "Ramayana_Full_Wrap.jpg"))
