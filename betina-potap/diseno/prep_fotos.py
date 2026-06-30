#!/usr/bin/env python3
"""
Prepara las fotos de producto para el catálogo.

IMPORTANTE: se usan las fotos TAL CUAL fueron tomadas (frame completo, sin recorte
ni zoom), sólo se corrige la orientación, se redondean las esquinas (en color crema
para integrarse al fondo) y se exporta a máxima calidad razonable para impresión.

Uso:  cd betina-potap && python3 diseno/prep_fotos.py
Requiere: Pillow
"""
import os
from PIL import Image, ImageOps, ImageDraw

SRC_DIR = "/root/.claude/uploads/864f6943-e20c-5d96-8e32-cb9820d6479f"
OUT = "diseno/fotos"
os.makedirs(OUT, exist_ok=True)
CREAM = (246, 242, 233)  # = #F6F2E9, fondo del catálogo

# key -> archivo original (sin recorte: frame completo)
FOTOS = {
    "alfajores":        "ef0e587e-IMG_1202.jpeg",
    "barritas":         "1787497b-IMG_1230.jpeg",
    "muffins":          "67226268-IMG_1242.jpeg",
    "brownies":         "01c05f21-IMG_1246.jpeg",
    "cookies":          "1c40cdc1-FullSizeRender.jpeg",
    "bolitas":          "305bddcf-FullSizeRender_2.jpeg",
    "granola_yogurt":   "44d60a99-IMG_1211.jpeg",
    "frutos_garbanzos": "4298c3a2-IMG_1214.jpeg",
    "blends":           "9a353a4b-IMG_1226.jpeg",
    "tostis_crackers":  "8c1838d7-IMG_1229.jpeg",
    "salsas":           "0710fe91-IMG_1259.jpeg",
    "spread":           "e26f8385-IMG_1264.jpeg",
}

def round_corners(im, rad_frac=0.04, bg=CREAM):
    r = int(min(im.size) * rad_frac)
    mask = Image.new("L", im.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, im.size[0] - 1, im.size[1] - 1], radius=r, fill=255)
    base = Image.new("RGB", im.size, bg)
    base.paste(im, (0, 0), mask)
    return base

for key, fn in FOTOS.items():
    im = Image.open(os.path.join(SRC_DIR, fn))
    im = ImageOps.exif_transpose(im).convert("RGB")   # orientación correcta, SIN recorte
    sc = 2000 / max(im.size)                            # máxima calidad razonable para impresión
    if sc < 1:
        im = im.resize((round(im.size[0] * sc), round(im.size[1] * sc)), Image.LANCZOS)
    out = round_corners(im)
    out.save(f"{OUT}/{key}.jpg", quality=92)
    print(f"{key:18s} {out.size[0]}x{out.size[1]}")
print("Listo (frame completo). Recortes en", OUT)
