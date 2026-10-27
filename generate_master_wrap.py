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
# 2. FULL WRAP COMPOSITE WITH SURGICAL TYPO PATCHES & BRAND NEW SPINE
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
# Close bowl of 'h' at x=315..318, y=530..531 to form crisp Roman 'b'
gold_b3 = (220, 215, 200)
master_wrap.putpixel((315, 530), (200, 195, 180))
master_wrap.putpixel((316, 530), gold_b3)
master_wrap.putpixel((317, 530), gold_b3)
master_wrap.putpixel((318, 530), gold_b3)

master_wrap.putpixel((315, 531), (170, 165, 150))
master_wrap.putpixel((316, 531), gold_b3)
master_wrap.putpixel((317, 531), gold_b3)
master_wrap.putpixel((318, 531), (200, 195, 180))

# D. Paste the clean Front Cover onto the wrap
master_wrap.paste(fc_cleaned, (525, 0))

# E. BRAND NEW SPINE REGENERATION (x = 488..525, y = 0..718)
# Create a pristine horizontal spine strip (718 x 37 px) and rotate 270 deg
strip_w = 718
strip_h = 37

spine_img = Image.new("RGBA", (strip_w, strip_h), (24, 22, 28, 255))
s_draw = ImageDraw.Draw(spine_img)

# Outer gold borders along spine hinges
s_draw.line([(0, 1), (strip_w, 1)], fill=(150, 120, 70), width=1)
s_draw.line([(0, strip_h - 2), (strip_w, strip_h - 2)], fill=(150, 120, 70), width=1)
# Inner subtle hairline
s_draw.line([(0, 3), (strip_w, 3)], fill=(70, 55, 35), width=1)
s_draw.line([(0, strip_h - 4), (strip_w, strip_h - 4)], fill=(70, 55, 35), width=1)

f_om = get_font(["Nirmala.ttf", "Shobhika-Bold.otf", "arial.ttf"], 15)
f_title = get_font(["LibertinusSerif-Bold.otf", "georgiab.ttf", "timesbd.ttf"], 13)
f_sub = get_font(["LibertinusSerif-Semibold.otf", "georgia.ttf", "times.ttf"], 10)
f_auth = get_font(["LibertinusSerif-Bold.otf", "georgiab.ttf", "timesbd.ttf"], 11)

gold_bright = (235, 218, 175, 255)
gold_warm = (218, 185, 115, 255)
gold_dark = (160, 130, 75, 255)
shadow_col = (10, 8, 12, 230)

# 1. Sacred Om ॐ at top
om_text = "ॐ"
om_x = 26
om_y = (strip_h - 18) // 2
s_draw.text((om_x + 1, om_y + 1), om_text, font=f_om, fill=shadow_col)
s_draw.text((om_x, om_y), om_text, font=f_om, fill=gold_warm)

# Top divider
d1_x = 52
s_draw.line([(d1_x, 8), (d1_x, strip_h - 8)], fill=gold_dark, width=1)
s_draw.polygon([(d1_x, strip_h//2 - 2), (d1_x + 2, strip_h//2), (d1_x, strip_h//2 + 2), (d1_x - 2, strip_h//2)], fill=gold_warm)

# 2. Main Title: "SANSKRIT BY ARCHITECTURE" (completely intact, zero cutoff)
title_text = "SANSKRIT BY ARCHITECTURE"
title_w = s_draw.textlength(title_text, font=f_title)
title_x = 68
title_y = (strip_h - 14) // 2
s_draw.text((title_x + 1, title_y + 1), title_text, font=f_title, fill=shadow_col)
s_draw.text((title_x, title_y), title_text, font=f_title, fill=gold_bright)

# Middle separator diamond
d2_x = title_x + int(title_w) + 20
d2_y = strip_h // 2
s_draw.polygon([(d2_x, d2_y - 3), (d2_x + 3, d2_y), (d2_x, d2_y + 3), (d2_x - 3, d2_y)], fill=gold_warm)

# 3. Subtitle: "DECODING THE RĀMĀYAṆA"
sub_text = "DECODING THE RĀMĀYAṆA"
sub_w = s_draw.textlength(sub_text, font=f_sub)
sub_x = d2_x + 20
sub_y = (strip_h - 11) // 2
s_draw.text((sub_x + 1, sub_y + 1), sub_text, font=f_sub, fill=shadow_col)
s_draw.text((sub_x, sub_y), sub_text, font=f_sub, fill=(225, 220, 205, 255))

# Third separator diamond
d3_x = sub_x + int(sub_w) + 20
d3_y = strip_h // 2
s_draw.polygon([(d3_x, d3_y - 3), (d3_x + 3, d3_y), (d3_x, d3_y + 3), (d3_x - 3, d3_y)], fill=gold_warm)

# 4. Author: "TIMOTHY A. GEORGE"
auth_text = "TIMOTHY A. GEORGE"
auth_w = s_draw.textlength(auth_text, font=f_auth)
auth_x = d3_x + 20
auth_y = (strip_h - 12) // 2
s_draw.text((auth_x + 1, auth_y + 1), auth_text, font=f_auth, fill=shadow_col)
s_draw.text((auth_x, auth_y), auth_text, font=f_auth, fill=gold_warm)

# Bottom divider
d4_x = auth_x + int(auth_w) + 16
if d4_x < strip_w - 12:
    s_draw.line([(d4_x, 8), (d4_x, strip_h - 8)], fill=gold_dark, width=1)
    s_draw.polygon([(d4_x, strip_h//2 - 2), (d4_x + 2, strip_h//2), (d4_x, strip_h//2 + 2), (d4_x - 2, strip_h//2)], fill=gold_warm)

# Rotate 270 deg and paste onto the wrap covering x=488..525, y=0..718
spine_vert = spine_img.rotate(270, expand=True)
master_wrap.paste(spine_vert, (488, 0), spine_vert)

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
