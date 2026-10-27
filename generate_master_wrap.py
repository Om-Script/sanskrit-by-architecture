import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# ==============================================================================
# SANSKRIT BY ARCHITECTURE: MASTER WRAP COVER GENERATOR
# Book Trim: 7.0" x 10.0" | Spine: 0.486" (216 pages) | Bleed: 0.125"
# Spread: 14.736" x 10.25" @ 300 DPI = 4421 x 3075 px
# ==============================================================================

base_dir = r"C:\Users\TAG-SB\.gemini\antigravity-ide\brain\76debe45-2007-4e90-8451-5693723b476d\.user_uploaded"
input_path = os.path.join(base_dir, "media_1793069995951.jpg")

im = Image.open(input_path).convert("RGB")
w, h = im.size
print(f"Loaded master wrap: {input_path} ({w}x{h})")

draw = ImageDraw.Draw(im)

def get_font(names, size):
    for n in names:
        for folder in ["final_chapters_md", r"C:\Windows\Fonts", "."]:
            fp = os.path.join(folder, n)
            if os.path.exists(fp):
                return ImageFont.truetype(fp, size)
    return ImageFont.load_default()

# ------------------------------------------------------------------------------
# 1. SPINE PATCH
# ------------------------------------------------------------------------------
# Clear AI garbled lower spine zone from y=365 to 695 (x=489..524)
spine_bg = im.getpixel((505, 362))
draw.rectangle([489, 365, 524, 695], fill=spine_bg)

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

# Subtle drop shadow + warm elegant cream gold
s_draw.text((sub_x + 1, sub_y + 1), sub_text, font=f_sub, fill=(30, 25, 20, 220))
s_draw.text((sub_x, sub_y), sub_text, font=f_sub, fill=(225, 220, 205, 255))

# Elegant gold separator diamond
d_cx = sub_x + int(sub_w) + 16
d_cy = strip_h // 2
s_draw.polygon([(d_cx, d_cy - 3), (d_cx + 3, d_cy), (d_cx, d_cy + 3), (d_cx - 3, d_cy)], fill=(218, 182, 105, 255))

# Author: TIMOTHY A. GEORGE
auth_text = "TIMOTHY A. GEORGE"
auth_w = s_draw.textlength(auth_text, font=f_auth)
auth_x = d_cx + 16
auth_y = (strip_h - 13) // 2

s_draw.text((auth_x + 1, auth_y + 1), auth_text, font=f_auth, fill=(30, 25, 20, 220))
s_draw.text((auth_x, auth_y), auth_text, font=f_auth, fill=(218, 182, 105, 255))

spine_vert = spine_layer.rotate(270, expand=True)
im.paste(spine_vert, (490, 368), spine_vert)

# ------------------------------------------------------------------------------
# 2. BACK COVER - PARAGRAPH 1: "Rämāyana" -> "Rāmāyaṇa"
# ------------------------------------------------------------------------------
# Clear umlaut above first 'a' (x=203..209, y=85..88)
bg_p1 = im.getpixel((201, 85))
draw.rectangle([203, 85, 209, 88], fill=bg_p1)

gold_p1 = (220, 215, 200)

# Draw horizontal macron bar across first 'a' (x=204..209, y=86)
draw.line([(204, 86), (209, 86)], fill=gold_p1, width=1)

# Crisp retroflex underdot on 'ṇ' (x=247..248, y=97..98)
draw.point([(247, 97), (248, 97), (247, 98), (248, 98)], fill=gold_p1)

# ------------------------------------------------------------------------------
# 3. BACK COVER - PARAGRAPH 3: "esposes" -> "exposes"
# ------------------------------------------------------------------------------
# Clear erroneous 's' at x=287..293, y=281..288
bg_p3 = im.getpixel((287, 280))
draw.rectangle([287, 281, 293, 288], fill=bg_p3)

gold_p3 = (220, 215, 200)
gold_mid = (160, 155, 140)

# Symmetrical Roman serif 'x':
draw.point([(288, 282), (289, 282), (292, 282), (293, 282)], fill=gold_p3)
draw.point([(289, 283), (290, 283), (291, 283), (292, 283)], fill=gold_p3)
draw.point([(290, 284), (291, 284)], fill=gold_p3)
draw.point([(289, 285), (292, 285)], fill=gold_mid)
draw.point([(290, 285), (291, 285)], fill=gold_p3)
draw.point([(290, 286), (291, 286)], fill=gold_p3)
draw.point([(289, 287), (290, 287), (291, 287), (292, 287)], fill=gold_p3)
draw.point([(288, 288), (289, 288), (292, 288), (293, 288)], fill=gold_p3)

# ------------------------------------------------------------------------------
# 4. BACK COVER - BULLET 3: "arhitrary" -> "arbitrary"
# ------------------------------------------------------------------------------
# Clear spurious descender and 'h' glitch zone from x=271 to 284, y=520 to 535
bg_b3 = im.getpixel((275, 519))
draw.rectangle([271, 520, 284, 535], fill=bg_b3)

gold_b3 = (215, 210, 195)
gold_b3_mid = (150, 145, 135)

# Roman lowercase 'b':
# Ascender stem (x=276..277, y=521..524)
for y_asc in range(521, 525):
    draw.point([(276, y_asc), (277, y_asc)], fill=gold_b3)

# Left stem down to baseline (x=276..277, y=525..531)
for y_stem in range(525, 532):
    draw.point([(276, y_stem), (277, y_stem)], fill=gold_b3)

# Closed bowl:
# Top curve at y=525: x=277..281
draw.point([(277, 525), (278, 525), (279, 525), (280, 525)], fill=gold_b3)
draw.point([(281, 525)], fill=gold_b3_mid)

# Right wall at y=526..530:
draw.point([(280, 526), (281, 526)], fill=gold_b3)
draw.point([(281, 527), (282, 527)], fill=gold_b3)
draw.point([(281, 528), (282, 528)], fill=gold_b3)
draw.point([(281, 529), (282, 529)], fill=gold_b3)
draw.point([(280, 530), (281, 530)], fill=gold_b3)

# Bottom curve at y=531: x=277..281
draw.point([(277, 531), (278, 531), (279, 531), (280, 531)], fill=gold_b3)
draw.point([(281, 531)], fill=gold_b3_mid)

# ==============================================================================
# EXPORT ALL KDP & WEB DELIVERABLES
# ==============================================================================
out_dir = r"C:\Users\TAG-SB\Desktop\Rama Code"
os.makedirs(out_dir, exist_ok=True)
os.makedirs(os.path.join(out_dir, "docs"), exist_ok=True)

# 1. Native Resolution Cleaned Wrap PNG (1024 x 718 px)
master_native_path = os.path.join(out_dir, "Ramayana_Wrap_Cleaned_Native.png")
im.save(master_native_path, dpi=(300, 300))

# 2. 300 DPI High-Resolution Master PNG (4421 x 3075 px)
master_300dpi = im.resize((4421, 3075), Image.Resampling.LANCZOS)
master_300dpi_path = os.path.join(out_dir, "Ramayana_Full_Wrap_300DPI_KDP.png")
master_300dpi.save(master_300dpi_path, dpi=(300, 300))

# 3. Print-Ready PDF (Amazon KDP 7" x 10" specification)
master_pdf_path = os.path.join(out_dir, "Ramayana_Full_Wrap_300DPI_KDP.pdf")
master_300dpi.save(master_pdf_path, "PDF", resolution=300.0)

# 4. Web showcase asset in docs/
docs_cover_path = os.path.join(out_dir, "docs", "Ramayana_Full_Wrap.jpg")
im.save(docs_cover_path, "JPEG", quality=95)

print("=== ALL DELIVERABLES GENERATED SUCCESSFULLY ===")
print("Native PNG:", master_native_path)
print("300 DPI PNG:", master_300dpi_path)
print("Print PDF:", master_pdf_path)
print("Docs Web:", docs_cover_path)
