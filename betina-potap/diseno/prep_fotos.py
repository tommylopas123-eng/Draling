#!/usr/bin/env python3
"""
Prepara las fotos de producto para el catálogo:
1) guarda una copia liviana del original en  diseno/fotos/_src/  (por si hay que
   re-encuadrar más adelante), y
2) genera el recorte final enfocando el producto en  diseno/fotos/.

Los recortes se definen con (cx, cy, wf, aspect):
  cx, cy  = centro del recorte (fracción 0-1 del ancho/alto del original)
  wf      = ancho del recorte como fracción del ancho del original
  aspect  = relación ancho/alto del recorte (1.0 = cuadrado, >1 = apaisado)

Uso:  cd betina-potap && python3 diseno/prep_fotos.py
Requiere: Pillow
"""
import os
from PIL import Image, ImageOps

SRC_DIR = "/root/.claude/uploads/864f6943-e20c-5d96-8e32-cb9820d6479f"
OUT = "diseno/fotos"
os.makedirs(OUT + "/_src", exist_ok=True)

# key -> (archivo original, cx, cy, wf, aspect)
FOTOS = {
    # --- individuales (cuadradas) ---
    "alfajores":   ("ef0e587e-IMG_1202.jpeg",      0.50, 0.45, 0.74, 1.0),
    "barritas":    ("1787497b-IMG_1230.jpeg",      0.545, 0.55, 0.60, 1.0),
    "muffins":     ("67226268-IMG_1242.jpeg",      0.52, 0.46, 0.86, 1.0),
    "brownies":    ("01c05f21-IMG_1246.jpeg",      0.46, 0.46, 0.74, 1.0),
    "cookies":     ("1c40cdc1-FullSizeRender.jpeg",   0.51, 0.49, 0.52, 1.0),
    "bolitas":     ("305bddcf-FullSizeRender_2.jpeg", 0.50, 0.44, 0.52, 1.0),
    # --- de a varias cosas (apaisadas, llevan flechitas) ---
    "granola_yogurt":   ("44d60a99-IMG_1211.jpeg", 0.51, 0.50, 0.88, 1.85),
    "frutos_garbanzos": ("4298c3a2-IMG_1214.jpeg", 0.52, 0.53, 0.88, 1.85),
    "blends":           ("9a353a4b-IMG_1226.jpeg", 0.50, 0.52, 0.94, 1.9),
    "tostis_crackers":  ("8c1838d7-IMG_1229.jpeg", 0.50, 0.50, 0.90, 1.95),
    "salsas":           ("0710fe91-IMG_1259.jpeg", 0.51, 0.51, 0.92, 1.9),
    # --- foto general (portada de la sección) ---
    "spread":      ("e26f8385-IMG_1264.jpeg",      0.47, 0.50, 0.94, 0.74),
}

def load(name):
    im = Image.open(os.path.join(SRC_DIR, name))
    im = ImageOps.exif_transpose(im).convert("RGB")
    return im

def save_src(key, im):
    s = im.copy(); s.thumbnail((1800, 1800), Image.LANCZOS)
    s.save(f"{OUT}/_src/{key}.jpg", quality=85)

CREAM = (246, 242, 233)  # = #F6F2E9, fondo del catálogo

def round_corners(im, rad_frac=0.045, bg=CREAM):
    """Redondea las esquinas rellenando con el color de fondo del catálogo."""
    r = int(min(im.size) * rad_frac)
    mask = Image.new("L", im.size, 0)
    from PIL import ImageDraw
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, im.size[0] - 1, im.size[1] - 1], radius=r, fill=255)
    base = Image.new("RGB", im.size, bg)
    base.paste(im, (0, 0), mask)
    return base

def crop(im, cx, cy, wf, aspect, long_edge=1500):
    W, H = im.size
    cw = wf * W; ch = cw / aspect
    if ch > H:  # no exceder el alto
        ch = H; cw = ch * aspect
    left = cx * W - cw / 2; top = cy * H - ch / 2
    left = max(0, min(left, W - cw)); top = max(0, min(top, H - ch))
    out = im.crop((round(left), round(top), round(left + cw), round(top + ch)))
    sc = long_edge / max(out.size)
    if sc < 1:
        out = out.resize((round(out.size[0] * sc), round(out.size[1] * sc)), Image.LANCZOS)
    return round_corners(out)

for key, (fn, cx, cy, wf, aspect) in FOTOS.items():
    im = load(fn)
    save_src(key, im)
    out = crop(im, cx, cy, wf, aspect)
    out.save(f"{OUT}/{key}.jpg", quality=86)
    print(f"{key:18s} {out.size[0]}x{out.size[1]}")
print("Listo. Recortes en", OUT)
