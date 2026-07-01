#!/usr/bin/env python3
"""
Generador del catálogo comercial PDF de Betina Potap.
Estética "Jardín Sereno" (ver FILOSOFIA-Jardin-Sereno.md).
Hecho con la skill canvas-design (fuentes en .claude/skills/canvas-design/canvas-fonts).

Uso:
    cd betina-potap && python3 diseno/generar_catalogo.py
Genera: betina-potap/Catalogo-Comercial-Betina-Potap.pdf

Requiere: reportlab  (pip install reportlab)
Para previsualizar páginas como PNG: pip install pymupdf y usar fitz.

NOTA: si se mueven las fuentes, ajustar la variable FD.
Para editar precios/textos: buscar las llamadas box_card(...) y los textos de cada página.

Las fotos de producto se intercalan con la presentación (no van todas juntas al final):
mesa servida (temprano), dulces/snacks tras el Box Snacking, y frescos/salsas tras el
Coffee Break.
"""
import math
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import simpleSplit, ImageReader
from reportlab.lib.colors import HexColor

# Ruta a las fuentes de la skill canvas-design (relativa a la raíz del repo)
FD = "../.claude/skills/canvas-design/canvas-fonts/"

def reg(n, f):
    pdfmetrics.registerFont(TTFont(n, FD + f))

for n, f in [("Display", "Gloock-Regular.ttf"), ("Serif", "YoungSerif-Regular.ttf"),
             ("SerifI", "Lora-Italic.ttf"), ("Sans", "Outfit-Regular.ttf"),
             ("SansB", "Outfit-Bold.ttf"), ("Script", "NothingYouCouldDo-Regular.ttf"),
             ("Mono", "DMMono-Regular.ttf")]:
    reg(n, f)

W, H = A4
CREAM = "#F6F2E9"; FOREST = "#22473C"; TEAL = "#2C8A82"; TEALD = "#1C5E57"
SAGE = "#9DBDAE"; GOLD = "#BE9E55"; INK = "#34362F"; CARD = "#EFE9DA"
def col(h): return HexColor(h)

c = canvas.Canvas("Catalogo-Comercial-Betina-Potap.pdf", pagesize=A4)

def bg(color):
    c.setFillColor(col(color)); c.rect(0, 0, W, H, fill=1, stroke=0)

def center_label(txt, y, size, font="Sans", color=INK, track=2.2):
    c.setFont(font, size); c.setFillColor(col(color))
    total = sum(pdfmetrics.stringWidth(ch, font, size) + track for ch in txt) - track
    x = (W - total) / 2
    for ch in txt:
        c.drawString(x, y, ch); x += pdfmetrics.stringWidth(ch, font, size) + track

def textc(txt, y, size, font="Sans", color=INK):
    c.setFont(font, size); c.setFillColor(col(color)); c.drawCentredString(W / 2, y, txt)

def para(txt, xleft, y, size, width, leading, font="Sans", color=INK, align="left"):
    c.setFont(font, size); c.setFillColor(col(color))
    for line in simpleSplit(txt, font, size, width):
        if align == "center": c.drawCentredString(xleft + width / 2, y, line)
        else: c.drawString(xleft, y, line)
        y -= leading
    return y

def parac(txt, y, size, width, leading, font="Sans", color=INK):
    return para(txt, (W - width) / 2, y, size, width, leading, font, color, "center")

def leaf(x, y, length, wid, ang, color=SAGE, alpha=1):
    c.saveState(); c.translate(x, y); c.rotate(ang)
    c.setFillColor(col(color)); c.setStrokeColor(col(color)); c.setLineWidth(0.6)
    if alpha < 1: c.setFillAlpha(alpha); c.setStrokeAlpha(alpha)
    p = c.beginPath(); p.moveTo(0, 0)
    p.curveTo(length * 0.35, wid, length * 0.7, wid, length, 0)
    p.curveTo(length * 0.7, -wid, length * 0.35, -wid, 0, 0)
    c.drawPath(p, fill=1, stroke=1)
    c.setStrokeColor(col(CREAM)); c.setLineWidth(0.5); c.line(length * 0.05, 0, length * 0.92, 0)
    c.restoreState()

def sprig(x, y, scale, ang, color=SAGE, alpha=1, n=5):
    c.saveState(); c.translate(x, y); c.rotate(ang)
    c.setStrokeColor(col(color)); c.setLineWidth(1.1)
    if alpha < 1: c.setStrokeAlpha(alpha)
    L = 60 * scale
    p = c.beginPath(); p.moveTo(0, 0); p.curveTo(L * 0.3, L * 0.15, L * 0.7, L * 0.25, L, L * 0.18)
    c.drawPath(p, fill=0, stroke=1)
    for i in range(n):
        t = (i + 1) / (n + 1); lx = L * t
        leaf(lx * 0.96, L * 0.16 * t, 16 * scale, 5.5 * scale, 35, color, alpha)
        leaf(lx * 0.96, L * 0.16 * t, 16 * scale, 5.5 * scale, -35, color, alpha)
    leaf(L, L * 0.18, 18 * scale, 6 * scale, 12, color, alpha)
    c.restoreState()

def rrect(x, y, w, h, r, fill, stroke=None, sw=1):
    c.setFillColor(col(fill))
    if stroke: c.setStrokeColor(col(stroke)); c.setLineWidth(sw)
    c.roundRect(x, y, w, h, r, fill=1, stroke=1 if stroke else 0)

# ========================= HELPERS DE CONTENIDO =========================
# ---------- tarjeta de propuesta (box_card) ----------
# El alto se calcula a partir del contenido para que el botón de precio quede
# pegado al texto (sin huecos). Devuelve el borde inferior de la tarjeta.
def box_card(num, title, desc, incl, price, y_top, accent=TEAL, tsize=21, dsize=11.5, dlead=16, nota=None):
    x = 56; w = W - 112; btn_h = 46
    n_desc = len(simpleSplit(desc, "Sans", dsize, w - 130))
    n_incl = len(simpleSplit(incl, "Sans", 10.5, w - 130))
    incl_label_y = (y_top - 78) - n_desc * dlead - 6
    incl_end = incl_label_y - 16 - n_incl * 15
    nota_h = 20 if nota else 0
    btn_top = incl_end + 2 - nota_h
    card_bottom = btn_top - btn_h - 22
    h = y_top - card_bottom
    rrect(x, card_bottom, w, h, 14, CARD); rrect(x, card_bottom, w, h, 14, CARD, accent, 1.2)
    c.setFillColor(col(accent)); c.setFont("Display", 40); c.drawString(x + 26, y_top - 58, num); leaf(x + w - 44, y_top - 40, 20, 7, 40, accent)
    c.setFillColor(col(FOREST)); c.setFont("Serif", tsize); c.drawString(x + 92, y_top - 50, title)
    para(desc, x + 92, y_top - 78, dsize, w - 130, dlead, "Sans", INK)
    c.setFillColor(col(TEALD)); c.setFont("SansB", 10.5); c.drawString(x + 92, incl_label_y, "Incluye")
    para(incl, x + 92, incl_label_y - 16, 10.5, w - 130, 15, "Sans", INK)
    if nota:
        c.setFillColor(col(accent)); c.setFont("Sans", 9.2); c.drawString(x + 92, incl_end - 13, nota)
    bx = x + 92; bbw = w - 184
    c.setFillColor(col(accent)); c.roundRect(bx, btn_top - btn_h, bbw, btn_h, 8, fill=1, stroke=0)
    c.setFillColor(col(CREAM))
    parts = price.split("\n")
    if len(parts) == 3:
        # Precio por unidades: dos filas apiladas a la izquierda + "por persona" a la derecha
        a, b, side = parts
        lx = bx + 26
        c.setFont("SansB", 13)
        c.drawString(lx, btn_top - 18, a)
        c.drawString(lx, btn_top - 35, b)
        c.setStrokeColor(col(CREAM)); c.setStrokeAlpha(0.4); c.setLineWidth(0.8)
        sepx = bx + bbw - 116
        c.line(sepx, btn_top - 34, sepx, btn_top - 13); c.setStrokeAlpha(1)
        c.setFillColor(col(CREAM)); c.setFont("Sans", 11)
        c.drawRightString(bx + bbw - 24, btn_top - 28, side)
    else:
        c.setFont("SansB", 14); c.drawCentredString(x + w / 2, btn_top - 29, price)
    return card_bottom

# ---------- encabezado hero de una box ----------
def box_hero(eyebrow, title, subtitle, tsize=44):
    bg(CREAM)
    center_label(eyebrow, H - 92, 10.5, "Sans", TEALD, 2.6)
    c.setFillColor(col(FOREST)); c.setFont("Display", tsize); c.drawCentredString(W / 2, H - 142, title)
    c.setStrokeColor(col(SAGE)); c.setLineWidth(1)
    c.line(W / 2 - 92, H - 162, W / 2 - 18, H - 162); c.line(W / 2 + 18, H - 162, W / 2 + 92, H - 162)
    leaf(W / 2, H - 171, 18, 6, 90, GOLD)
    textc(subtitle, H - 196, 13, "SerifI", TEALD)

# ---------- fotos de producto (frame completo). Ver diseno/prep_fotos.py ----------
FOTODIR = "diseno/fotos/%s.jpg"
_ASP = {}
def aspect(key):
    if key not in _ASP:
        iw, ih = ImageReader(FOTODIR % key).getSize(); _ASP[key] = iw / ih
    return _ASP[key]

def draw_photo(key, x, y, w, h, frame=SAGE):
    c.drawImage(FOTODIR % key, x, y, width=w, height=h)
    if frame:
        r = 0.04 * min(w, h)
        c.setStrokeColor(col(frame)); c.setLineWidth(0.8); c.roundRect(x, y, w, h, r, stroke=1, fill=0)

def up_arrow(ax, ty, color=GOLD):
    p = c.beginPath(); p.moveTo(ax, ty); p.lineTo(ax - 3.6, ty - 6.2); p.lineTo(ax + 3.6, ty - 6.2); p.close()
    c.setFillColor(col(color)); c.drawPath(p, fill=1, stroke=0)

def photo_multi(key, x, y_top, w, items, fs=8):
    # foto vertical (frame completo) + flechitas hacia el nombre de cada cosa
    h = w / aspect(key); draw_photo(key, x, y_top - h, w, h)
    base = y_top - h; slot = w / len(items)
    for name, afx in items:
        ax = x + afx * w
        up_arrow(ax, base - 4)
        para(name, ax - slot / 2, base - 17, fs, slot - 3, fs + 1.3, "Sans", TEALD, "center")
    return base

# ============================== PÁGINAS ==============================

# ---------- PÁGINA 1 — PORTADA ----------
bg(CREAM); c.setStrokeColor(col(SAGE)); c.setLineWidth(0.8); c.rect(34, 34, W - 68, H - 68, fill=0, stroke=1)
sprig(60, H - 120, 1.5, -20, SAGE, 0.9); sprig(W - 60, 120, 1.5, 160, SAGE, 0.9)
center_label("ALIMENTOS NATURALES   ·   CABA", H - 150, 10.5, "Sans", TEALD, 3)
c.setFillColor(col(FOREST)); c.setFont("Display", 58); c.drawCentredString(W / 2, H / 2 + 70, "Betina Potap")
c.setFillColor(col(GOLD)); c.setFont("Script", 26); c.drawCentredString(W / 2, H / 2 + 30, "hecho a mano con amor y consciencia")
c.setStrokeColor(col(SAGE)); c.setLineWidth(1); c.line(W / 2 - 90, H / 2 - 2, W / 2 - 18, H / 2 - 2); c.line(W / 2 + 18, H / 2 - 2, W / 2 + 90, H / 2 - 2)
leaf(W / 2, H / 2 - 11, 18, 6, 90, SAGE)  # hoja centrada (horizontal y vertical) en el divisor
textc("Catálogo para empresas", H / 2 - 52, 20, "Serif", FOREST)
parac("Snacks · Coffee breaks · Regalos corporativos · Catering", H / 2 - 80, 11.5, W * 0.8, 16, "Sans", INK)
center_label("@BETINAPOTAP.NATURISTA   ·   WHATSAPP 11 6629 3150", 70, 9, "Sans", TEALD, 2.5)
c.showPage()

# ---------- PÁGINA 2 — PROPUESTA DE VALOR ----------
bg(CREAM); sprig(W - 70, H - 95, 1.2, 150, SAGE, 0.8)
c.setFillColor(col(FOREST)); c.setFont("Display", 30); c.drawString(56, H - 150, "Comida real"); c.drawString(56, H - 186, "para todo tu equipo.")
y = para("Llevamos comida saludable y artesanal a tu oficina. Una sola compra que incluye a todos "
         "—intolerantes al gluten, veganos, diabéticos y a quienes entrenan. Nada industrial, nada en serie: "
         "hecho a mano, fresco y a medida.", 56, H - 224, 12.5, W - 200, 18, "Sans", INK) - 58
pills = [("Sin", "gluten"), ("Sin", "lácteos"), ("Sin", "azúcar")]; bw = (W - 112 - 40) / 3
for i, (a, b) in enumerate(pills):
    x = 56 + i * (bw + 20); rrect(x, y - 110, bw, 100, 10, CARD); leaf(x + bw / 2, y - 34, 18, 6, 90, TEAL)  # hojita centrada en la tarjeta
    c.setFillColor(col(TEALD)); c.setFont("Serif", 17); c.drawCentredString(x + bw / 2, y - 66, a)
    c.setFont("Serif", 20); c.drawCentredString(x + bw / 2, y - 90, b)
y -= 184; center_label("ARTESANAL   ·   FRESCO   ·   SALUDABLE", y, 12, "Sans", GOLD, 4); y -= 48
c.setStrokeColor(col(SAGE)); c.setLineWidth(0.8); c.line(150, y, W - 150, y)
c.setFillColor(col(INK)); c.setFont("SerifI", 14); c.drawCentredString(W / 2, y - 34, "“Que nadie del equipo quede afuera de la mesa.”")
sprig(70, 96, 1.1, -15, SAGE, 0.8); sprig(W - 70, 96, 1.1, 195, SAGE, 0.8); c.showPage()

# ---------- PÁGINA 3 — "Mesa servida": la foto general (temprano, como gancho) ----------
bg(CREAM); c.setStrokeColor(col(SAGE)); c.setLineWidth(0.8); c.rect(34, 34, W - 68, H - 68, fill=0, stroke=1)
sprig(66, 96, 1.1, -20, SAGE, 0.5); sprig(W - 66, 96, 1.1, 200, SAGE, 0.5)
center_label("TODO HECHO A MANO, PARA TODO EL EQUIPO", H - 92, 10.5, "Sans", TEALD, 2.4)
c.setFillColor(col(FOREST)); c.setFont("Display", 31); c.drawCentredString(W / 2, H - 132, "Una mesa que")
c.drawCentredString(W / 2, H - 168, "nos incluye a todos")
sw = 232; sh = sw / aspect("spread"); sx = (W - sw) / 2; sy = 196
draw_photo("spread", sx, sy, sw, sh, frame=SAGE)
parac("Sin gluten · sin lácteos · sin azúcar — comen todos, sin que nadie quede afuera de la mesa.",
      158, 11, W * 0.74, 15, "SerifI", TEALD); c.showPage()

# ---------- PÁGINA 4 — PROPUESTA ESTRELLA: CATERING PARA EMPRESAS ----------
bg(CREAM); c.setStrokeColor(col(SAGE)); c.setLineWidth(0.8); c.rect(34, 34, W - 68, H - 68, fill=0, stroke=1)
sprig(W - 60, H - 105, 1.2, 150, SAGE, 0.6); sprig(60, 110, 1.2, -25, SAGE, 0.6)
leaf(W / 2, H - 165, 80, 27, 90, GOLD)  # hoja entera grande = protagonista de la propuesta estrella
center_label("NUESTRA PROPUESTA ESTRELLA PARA EMPRESAS", H - 205, 10.5, "Sans", TEALD, 3)
c.setFillColor(col(FOREST)); c.setFont("Display", 33); c.drawCentredString(W / 2, H - 250, "Catering para empresas"); c.drawCentredString(W / 2, H - 289, "y oficinas")
parac("Llevamos la comida de nuestro menú —proteico y naturista— a tus eventos, capacitaciones, "
      "desayunos de equipo y “días saludables”. Todo fresco, artesanal y apto para todas las dietas: "
      "sin gluten, sin lácteos y sin azúcar. Una sola compra donde come todo el equipo, sin que nadie "
      "quede afuera de la mesa.", H - 328, 12.5, W * 0.74, 19, "Sans", INK)
fmts = [("Almuerzos de negocios", "Para reuniones de trabajo, al mediodía."),
        ("Días saludables", "Un día sano para todo el equipo."),
        ("Eventos corporativos", "Catering a medida para tu evento.")]
fy = H - 430; bw = (W - 112 - 40) / 3
for i, (t, d) in enumerate(fmts):
    x = 56 + i * (bw + 20); rrect(x, fy - 98, bw, 98, 12, CARD); leaf(x + bw / 2, fy - 30, 16, 5.5, 90, TEAL)
    c.setFillColor(col(TEALD)); c.setFont("SansB", 12); c.drawCentredString(x + bw / 2, fy - 52, t)
    para(d, x + 12, fy - 70, 9.5, bw - 24, 12, "Sans", INK, "center")
pb_y = 158; rrect(W / 2 - 212, pb_y, 424, 74, 12, FOREST)
c.setFillColor(col(GOLD)); c.setFont("SansB", 9); c.drawCentredString(W / 2, pb_y + 52, "PRESUPUESTO")
c.setFillColor(col(CREAM)); c.setFont("SansB", 15); c.drawCentredString(W / 2, pb_y + 30, "Armamos el presupuesto")
c.setFont("SansB", 15); c.drawCentredString(W / 2, pb_y + 11, "a la medida de tu necesidad")
center_label("PEDÍ TU PROPUESTA A MEDIDA", 74, 9, "Sans", TEALD, 2.5); c.showPage()

# ---------- PÁGINA 5 — Box Snacking (hero) + dos versiones (Seca / Plus) ----------
bg(CREAM)
center_label("DESCUBRÍ NUESTRAS PROPUESTAS", H - 92, 10.5, "Sans", TEALD, 3)
c.setFillColor(col(FOREST)); c.setFont("Display", 46); c.drawCentredString(W / 2, H - 142, "Box Snacking")
c.setStrokeColor(col(SAGE)); c.setLineWidth(1)
c.line(W / 2 - 92, H - 162, W / 2 - 18, H - 162); c.line(W / 2 + 18, H - 162, W / 2 + 92, H - 162)
leaf(W / 2, H - 171, 18, 6, 90, GOLD)
textc("Picoteo sano de la semana, en dos versiones a elección.", H - 196, 13, "SerifI", TEALD)
GAP = 28
yb = box_card("01", "Versión Seca · base",
         "Todo seco y de larga duración. Listo para la cocina de tu oficina.",
         "frutos secos, bolitas de dátiles, cookies de avena, muffins de choco con dátiles, "
         "alfajor de cacao con dátiles y maní, crackers de zanahoria, garbanzos crocantes, "
         "brownies, barritas de semillas y blends de mate y de té.",
         "5 unidades $9.000\n10 unidades $17.000\npor persona", H - 208, TEAL, tsize=19, dsize=11, dlead=14,
         nota="5 un = 1 picoteo al día      ·      10 un = 2 colaciones al día")
yb2 = box_card("02", "Versión Plus · fresca",
         "Agrandá tu box con opciones frescas.",
         "todo lo de la Seca + yogurt griego, granola, hummus, mayonesa de zanahoria y cúrcuma, "
         "fruta fresca de estación y tostis de sarraceno y almendras.",
         "5 unidades $11.000\n10 unidades $20.000\npor persona", yb - GAP, GOLD, tsize=19, dsize=11, dlead=14,
         nota="5 un = 2 frescas + 3 secas      ·      10 un = 4 frescas + 6 secas")
c.setFillColor(col(TEALD)); c.setFont("SerifI", 11.5)
c.drawCentredString(W / 2, yb2 - 24, "Compra mínima: 10 cubiertos · por suscripción, se puede pausar.")
sprig(72, 64, 0.95, -18, SAGE, 0.5); sprig(W - 72, 64, 0.95, 198, SAGE, 0.5)
c.showPage()

# ---------- PÁGINA 6 — Fotos: dulces y snacks del Box Snacking ----------
bg(CREAM); c.setFillColor(col(FOREST)); c.setFont("Display", 26); c.drawString(56, H - 80, "Dulces y snacks")
c.setFillColor(col(TEALD)); c.setFont("SerifI", 13); c.drawString(56, H - 104, "Algunos de los que entran en tu Box Snacking, hechos a mano.")
singles = [("alfajores", "Alfajores de cacao y dátiles"), ("cookies", "Cookies de avena"),
           ("brownies", "Brownies"), ("muffins", "Muffins de choco y dátiles"),
           ("barritas", "Barritas de semillas"), ("bolitas", "Bolitas de dátiles")]
gap = 26; cell = (W - 112 - 2 * gap) / 3; ph = cell / aspect("alfajores"); pitch = ph + 50
for i, (key, name) in enumerate(singles):
    cx = 56 + (i % 3) * (cell + gap); ytop = H - 138 - (i // 3) * pitch
    draw_photo(key, cx, ytop - ph, cell, ph)
    para(name, cx - 6, ytop - ph - 16, 10, cell + 12, 12.5, "Serif", FOREST, "center")
c.showPage()

# ---------- PÁGINA 7 — Box Coffee Break (hero + menú) ----------
box_hero("PARA REUNIONES Y DESAYUNOS DE EQUIPO", "Box Coffee Break",
         "Un desayuno completo, recién hecho y listo para servir.")
incl_cb = ("Tostadas de sarraceno · Huevos revueltos y palta · Crackers con hummus · "
           "Dip de zanahoria · Yogur griego con granola y frutos rojos · Fruta fresca de "
           "estación · Budín de choco · Pancakes de banana y cacao con miel · "
           "Crocante dulce · Blend de mate y té · Limonada")
cx0 = 56; cw0 = W - 112; ctop = H - 332
lns = simpleSplit(incl_cb, "Sans", 11.5, cw0 - 96)
chh = 32 + len(lns) * 17 + 26 + 46 + 26; cbot = ctop - chh
rrect(cx0, cbot, cw0, chh, 14, CARD); rrect(cx0, cbot, cw0, chh, 14, CARD, TEALD, 1.2)
c.setFillColor(col(TEALD)); c.setFont("SansB", 10.5); c.drawCentredString(W / 2, ctop - 32, "I N C L U Y E")
yy = ctop - 56
for ln in lns:
    c.setFillColor(col(INK)); c.setFont("Sans", 11.5); c.drawCentredString(W / 2, yy, ln); yy -= 17
bwc = 330; byc = cbot + 26
c.setFillColor(col(TEALD)); c.roundRect(W / 2 - bwc / 2, byc, bwc, 46, 8, fill=1, stroke=0)
c.setFillColor(col(GOLD)); c.setFont("SansB", 9); c.drawCentredString(W / 2, byc + 31, "PRECIO")
c.setFillColor(col(CREAM)); c.setFont("SansB", 15); c.drawCentredString(W / 2, byc + 12, "$15.000 por persona")
c.setFillColor(col(TEALD)); c.setFont("SerifI", 12.5); c.drawCentredString(W / 2, cbot - 28, "Incluye 7 unidades por persona.")
sprig(72, 92, 1.0, -18, SAGE, 0.5); sprig(W - 72, 92, 1.0, 198, SAGE, 0.5)
parac("Recién hecho · entregamos listo para servir.",
      120, 11, W * 0.72, 15, "SerifI", TEALD); c.showPage()

# ---------- PÁGINA 8 — Fotos: frescos, salsas y blends (con flechitas) ----------
bg(CREAM); c.setFillColor(col(FOREST)); c.setFont("Display", 26); c.drawString(56, H - 80, "Frescos y salsas")
c.setFillColor(col(TEALD)); c.setFont("SerifI", 13); c.drawString(56, H - 104, "Los frescos del Coffee Break y de la Versión Plus.")
gap = 26; cell = (W - 112 - 2 * gap) / 3; ph = cell / aspect("blends"); pitch = ph + 56
r1 = H - 138
photo_multi("granola_yogurt", 56, r1, cell, [("Granola", 0.29), ("Yogurt griego", 0.72)])
photo_multi("frutos_garbanzos", 56 + cell + gap, r1, cell, [("Frutos secos", 0.27), ("Garbanzos crocantes", 0.71)])
photo_multi("blends", 56 + 2 * (cell + gap), r1, cell, [("Blend de té", 0.27), ("Blend de mate", 0.74)])
r2 = r1 - pitch; sx2 = 56 + (W - 112 - (2 * cell + gap)) / 2
photo_multi("salsas", sx2, r2, cell, [("Mayonesa de zanahoria", 0.28), ("Hummus", 0.72)])
photo_multi("tostis_crackers", sx2 + cell + gap, r2, cell,
            [("Tostis almendras", 0.17), ("Tostis sarraceno", 0.5), ("Crackers zanahoria", 0.83)], fs=7.5)
c.showPage()

# ---------- PÁGINA 9 — Box Welcome Kit (hero + dos versiones) ----------
box_hero("PARA REGALAR A TU EQUIPO Y A TUS CLIENTES", "Box Welcome Kit",
         "Para bienvenidas, fin de año o clientes. Podés sumar tu branding.")
GAP = 30
yb = box_card("01", "Clásico",
         "Para bienvenidas, fin de año o regalar a clientes.",
         "barritas, crackers, hummus, 1 pan de sarraceno, granola, budín de choco y "
         "blend de mate y té.",
         "$35.000 · por kit", H - 214, TEAL, tsize=19, dsize=11, dlead=14)
box_card("02", "Premium",
         "Todo lo del Clásico, con un plus para destacarte.",
         "todo lo del Clásico + dátiles con maní y choco y wrap proteico.",
         "$55.000 · por kit", yb - GAP, GOLD, tsize=19, dsize=11, dlead=14)
sprig(72, 96, 1.0, -18, SAGE, 0.5); sprig(W - 72, 96, 1.0, 198, SAGE, 0.5)
parac("Sumá tu logo y una tarjeta personalizada — armamos el kit a tu medida.",
      120, 11, W * 0.72, 15, "SerifI", TEALD); c.showPage()

# ---------- PÁGINA 10 — Por qué + Cómo funciona ----------
bg(CREAM); c.setFillColor(col(FOREST)); c.setFont("Display", 26); c.drawString(56, H - 130, "¿Por qué Betina Potap?")
diffs = [("100% alimentación consciente", "Sin gluten + sin lácteos + sin azúcar, todo junto. Comen todos."),
         ("Artesanal y fresco", "Nada industrial ni envasado en serie. Hecho a mano."),
         ("A medida", "Armamos el box para tu equipo y tu frecuencia de entrega."),
         ("Sin riesgo", "Probás con muestra gratis y elegís sin compromiso.")]
y = H - 172
for t, d in diffs:
    leaf(64, y + 3, 18, 6, 20, TEAL); c.setFillColor(col(TEALD)); c.setFont("SansB", 13); c.drawString(92, y, t)
    para(d, 92, y - 17, 11, W - 220, 15, "Sans", INK); y -= 66
y -= 8; c.setStrokeColor(col(SAGE)); c.setLineWidth(0.8); c.line(56, y, W - 56, y); y -= 52
c.setFillColor(col(FOREST)); c.setFont("Display", 26); c.drawString(56, y, "Cómo funciona"); y -= 38
steps = [("1", "Probás", "Te mandamos una muestra gratis para que el equipo la pruebe."),
         ("2", "Elegís", "El box y la frecuencia. Sin compromiso, se puede pausar."),
         ("3", "Recibís", "Entregamos en tu oficina, de lunes a viernes.")]
bw = (W - 112 - 40) / 3
for i, (n, t, d) in enumerate(steps):
    x = 56 + i * (bw + 20); rrect(x, y - 140, bw, 128, 12, FOREST)
    c.setFillColor(col(GOLD)); c.setFont("Display", 34); c.drawCentredString(x + bw / 2, y - 52, n)
    c.setFillColor(col(CREAM)); c.setFont("SansB", 13); c.drawCentredString(x + bw / 2, y - 76, t)
    para(d, x + 12, y - 96, 9.5, bw - 24, 12.5, "Sans", CREAM, "center")
sprig(70, 86, 1.0, -20, SAGE, 0.55); sprig(W - 70, 86, 1.1, 200, SAGE, 0.6); c.showPage()

# ---------- Íconos de redes ----------
def ig_icon(cx, cy, s, color=SAGE):
    c.setStrokeColor(col(color)); c.setLineWidth(s * 0.10); c.setLineJoin(1)
    c.roundRect(cx - s / 2, cy - s / 2, s, s, s * 0.30, stroke=1, fill=0)
    c.circle(cx, cy, s * 0.27, stroke=1, fill=0)
    c.setFillColor(col(color)); c.circle(cx + s * 0.30, cy + s * 0.30, s * 0.075, stroke=0, fill=1)

def wa_icon(cx, cy, s, color=SAGE, bg="#2C5A4E"):
    R = s * 0.5
    c.setFillColor(col(color)); c.circle(cx, cy, R, stroke=0, fill=1)
    p = c.beginPath(); p.moveTo(cx - R * 0.62, cy - R * 0.42); p.lineTo(cx - R * 1.02, cy - R * 0.98)
    p.lineTo(cx - R * 0.16, cy - R * 0.80); p.close(); c.drawPath(p, fill=1, stroke=0)
    c.saveState(); c.translate(cx, cy); c.rotate(45)
    c.setStrokeColor(col(bg)); c.setLineWidth(s * 0.15); c.setLineCap(1); c.setLineJoin(1)
    p = c.beginPath(); p.moveTo(-s * 0.20, s * 0.06)
    p.curveTo(-s * 0.07, -s * 0.12, s * 0.07, -s * 0.12, s * 0.20, s * 0.06)
    c.drawPath(p, stroke=1, fill=0)
    c.setFillColor(col(bg)); c.circle(-s * 0.205, s * 0.075, s * 0.078, fill=1, stroke=0)
    c.circle(s * 0.205, s * 0.075, s * 0.078, fill=1, stroke=0); c.restoreState()

def tt_icon(cx, cy, s, color=SAGE):
    c.setStrokeColor(col(color)); c.setLineWidth(s * 0.13); c.setLineCap(1); c.setLineJoin(1)
    stemx = cx - s * 0.02
    c.line(stemx, cy - s * 0.18, stemx, cy + s * 0.44)
    p = c.beginPath(); p.moveTo(stemx, cy + s * 0.44)
    p.curveTo(stemx + s * 0.34, cy + s * 0.42, stemx + s * 0.44, cy + s * 0.16, stemx + s * 0.26, cy + s * 0.04)
    c.drawPath(p, stroke=1, fill=0)
    c.setFillColor(col(color)); c.saveState(); c.translate(stemx - s * 0.20, cy - s * 0.22); c.rotate(-18)
    c.ellipse(-s * 0.19, -s * 0.13, s * 0.19, s * 0.13, fill=1, stroke=0); c.restoreState()

def social_icon(name, cx, cy, s):  # fallback dibujado a mano
    if name == "WhatsApp": wa_icon(cx, cy, s)
    elif name == "Instagram": ig_icon(cx, cy, s)
    else: tt_icon(cx, cy, s)

# Logos oficiales (paquete simpleicons + svglib) renderizados como vectores nítidos.
# Si las librerías no están, queda el fallback dibujado de arriba.
ICON_COLOR = GOLD
try:
    import tempfile
    from simpleicons.icons import si_whatsapp, si_instagram, si_tiktok
    from svglib.svglib import svg2rlg
    from reportlab.graphics import renderPDF
    _SI = {"WhatsApp": si_whatsapp, "Instagram": si_instagram, "TikTok": si_tiktok}
    _SVGF = {}
    def _icon_svg(name, color):
        key = (name, color)
        if key not in _SVGF:
            d = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="{_SI[name].path}" fill="{color}"/></svg>'
            f = tempfile.NamedTemporaryFile("w", suffix=".svg", delete=False); f.write(d); f.close()
            _SVGF[key] = f.name
        return _SVGF[key]
    def social_icon(name, cx, cy, s, color=ICON_COLOR):
        dr = svg2rlg(_icon_svg(name, color)); k = s / dr.width
        dr.scale(k, k); renderPDF.draw(dr, c, cx - s / 2, cy - s / 2)
except Exception as _e:
    print("Aviso: uso íconos dibujados (instalá simpleicons y svglib para los logos oficiales):", _e)

# ---------- PÁGINA 11 — Cierre / contacto ----------
bg(FOREST); c.setStrokeColor(col(SAGE)); c.setLineWidth(0.8); c.setStrokeAlpha(0.5); c.rect(34, 34, W - 68, H - 68, fill=0, stroke=1); c.setStrokeAlpha(1)
sprig(62, H - 76, 1.15, -22, SAGE, 0.55); sprig(W - 66, 84, 1.15, 160, SAGE, 0.45)
c.setFillColor(col(CREAM)); c.setFont("Display", 30); c.drawCentredString(W / 2, H - 196, "¿Lista tu oficina"); c.drawCentredString(W / 2, H - 234, "para comer mejor?")
c.setFillColor(col(GOLD)); c.setFont("Script", 26); c.drawCentredString(W / 2, H - 278, "pedí tu muestra gratis")
parac("Escribinos y coordinamos una muestra gratis para tu equipo.", H - 320, 12, W * 0.72, 16, "Sans", SAGE)
# Tres recuadros de contacto: WhatsApp, Instagram y TikTok
contacts = [("WhatsApp", "11 6629 3150"), ("Instagram", "@betinapotap.naturista"), ("TikTok", "@betinapotap.naturista")]
cw = (W - 112 - 40) / 3; ch = 116; cy = H - 548
for i, (lab, val) in enumerate(contacts):
    x = 56 + i * (cw + 20); rrect(x, cy, cw, ch, 12, "#2C5A4E")
    social_icon(lab, x + cw / 2, cy + ch - 33, 23)
    c.setFillColor(col(SAGE)); c.setFont("SansB", 11); c.drawCentredString(x + cw / 2, cy + ch - 60, lab)
    c.setFillColor(col(CREAM)); c.setFont("SansB", 12); c.drawCentredString(x + cw / 2, cy + 40, val)
# Cierre: divisor con hoja + frase de marca para anclar el pie
dy = 210
c.setStrokeColor(col(SAGE)); c.setLineWidth(0.9); c.setStrokeAlpha(0.5)
c.line(W / 2 - 86, dy, W / 2 - 20, dy); c.line(W / 2 + 20, dy, W / 2 + 86, dy); c.setStrokeAlpha(1)
leaf(W / 2, dy - 9, 17, 5.8, 90, GOLD)
c.setFillColor(col(SAGE)); c.setFont("SerifI", 13.5); c.drawCentredString(W / 2, dy - 44, "“Que nadie del equipo quede afuera de la mesa.”")
center_label("BETINA POTAP · ALIMENTOS NATURALES · CABA", 104, 9, "Sans", SAGE, 2.5); c.showPage()

c.save()
print("Catálogo generado: Catalogo-Comercial-Betina-Potap.pdf")
