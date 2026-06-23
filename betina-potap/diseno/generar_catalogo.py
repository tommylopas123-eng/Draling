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
"""
import math
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import simpleSplit
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

# ---------- PÁGINA 1 — PORTADA ----------
bg(CREAM); c.setStrokeColor(col(SAGE)); c.setLineWidth(0.8); c.rect(34, 34, W - 68, H - 68, fill=0, stroke=1)
sprig(60, H - 120, 1.5, -20, SAGE, 0.9); sprig(W - 60, 120, 1.5, 160, SAGE, 0.9)
center_label("ALIMENTOS NATURALES   ·   CABA", H - 150, 10.5, "Sans", TEALD, 3)
c.setFillColor(col(FOREST)); c.setFont("Display", 58); c.drawCentredString(W / 2, H / 2 + 70, "Betina Potap")
c.setFillColor(col(GOLD)); c.setFont("Script", 30); c.drawCentredString(W / 2, H / 2 + 30, "hecho a mano, con tiempo y cuidado")
c.setStrokeColor(col(SAGE)); c.setLineWidth(1); c.line(W / 2 - 90, H / 2 - 2, W / 2 - 18, H / 2 - 2); c.line(W / 2 + 18, H / 2 - 2, W / 2 + 90, H / 2 - 2)
leaf(W / 2, H / 2 - 11, 18, 6, 90, SAGE)  # hoja centrada (horizontal y vertical) en el divisor
textc("Catálogo para empresas", H / 2 - 52, 20, "Serif", FOREST)
parac("Snacks · Coffee breaks · Regalos corporativos · Catering", H / 2 - 80, 11.5, W * 0.8, 16, "Sans", INK)
center_label("@BETINAPOTAP.NATURISTA   ·   WHATSAPP 11 6629 3150", 70, 9, "Sans", TEALD, 2.5)
c.showPage()

# ---------- PÁGINA 2 — PROPUESTA DE VALOR ----------
bg(CREAM); sprig(W - 70, H - 95, 1.2, 150, SAGE, 0.8)
c.setFillColor(col(FOREST)); c.setFont("Display", 30); c.drawString(56, H - 150, "Comida real e inclusiva"); c.drawString(56, H - 186, "para todo tu equipo.")
y = para("Llevamos comida saludable y artesanal a tu oficina. Una sola compra que incluye a todos "
         "—intolerantes al gluten, veganos, diabéticos y a quienes entrenan. Nada industrial, nada en serie: "
         "hecho a mano, fresco y a medida.", 56, H - 224, 12.5, W - 200, 18, "Sans", INK) - 24
pills = [("Sin", "gluten"), ("Sin", "lácteos"), ("Sin", "azúcar")]; bw = (W - 112 - 40) / 3
for i, (a, b) in enumerate(pills):
    x = 56 + i * (bw + 20); rrect(x, y - 110, bw, 100, 10, CARD); leaf(x + bw / 2, y - 34, 18, 6, 90, TEAL)  # hojita centrada en la tarjeta
    c.setFillColor(col(TEALD)); c.setFont("Serif", 17); c.drawCentredString(x + bw / 2, y - 66, a)
    c.setFont("Serif", 20); c.drawCentredString(x + bw / 2, y - 90, b)
y -= 150; center_label("ARTESANAL   ·   FRESCO   ·   INCLUSIVO", y, 12, "Sans", GOLD, 4); y -= 40
c.setStrokeColor(col(SAGE)); c.setLineWidth(0.8); c.line(56, y, W - 56, y)
c.setFillColor(col(INK)); c.setFont("SerifI", 13); c.drawCentredString(W / 2, y - 30, "“Que nadie del equipo quede afuera de la mesa.”")
sprig(70, 90, 1.1, -15, SAGE, 0.8); c.showPage()

# ---------- helper: tarjeta de propuesta ----------
def box_card(num, title, desc, incl, price, y_top, accent=TEAL, h=300, tsize=21, dsize=11.5, dlead=16):
    x = 56; w = W - 112; rrect(x, y_top - h, w, h, 14, CARD); rrect(x, y_top - h, w, h, 14, CARD, accent, 1.2)
    c.setFillColor(col(accent)); c.setFont("Display", 40); c.drawString(x + 26, y_top - 58, num); leaf(x + w - 44, y_top - 40, 20, 7, 40, accent)
    c.setFillColor(col(FOREST)); c.setFont("Serif", tsize); c.drawString(x + 92, y_top - 50, title)
    yy = para(desc, x + 92, y_top - 78, dsize, w - 130, dlead, "Sans", INK) - 6
    c.setFillColor(col(TEALD)); c.setFont("SansB", 10.5); c.drawString(x + 92, yy, "Incluye"); yy = para(incl, x + 92, yy - 16, 10.5, w - 130, 15, "Sans", INK)
    c.setFillColor(col(accent)); c.roundRect(x + 92, y_top - h + 22, w - 184, 40, 8, fill=1, stroke=0)
    c.setFillColor(col(CREAM)); c.setFont("SansB", 14); c.drawCentredString(x + w / 2, y_top - h + 36, price)

# ---------- PÁGINA 3 — PROPUESTA ESTRELLA: CATERING PARA EMPRESAS (página entera, sin número) ----------
bg(CREAM); c.setStrokeColor(col(SAGE)); c.setLineWidth(0.8); c.rect(34, 34, W - 68, H - 68, fill=0, stroke=1)
sprig(W - 60, H - 105, 1.2, 150, SAGE, 0.6); sprig(60, 110, 1.2, -25, SAGE, 0.6)
leaf(W / 2, H - 165, 80, 27, 90, GOLD)  # hoja entera grande = protagonista de la propuesta estrella
center_label("NUESTRA PROPUESTA ESTRELLA PARA EMPRESAS", H - 205, 10.5, "Sans", TEALD, 3)
c.setFillColor(col(FOREST)); c.setFont("Display", 33); c.drawCentredString(W / 2, H - 250, "Catering para empresas"); c.drawCentredString(W / 2, H - 289, "y oficinas")
parac("Llevamos la comida de nuestro menú —proteico y naturista— a tus eventos, capacitaciones, "
      "desayunos de equipo y “días saludables”. Todo fresco, artesanal y apto para todas las dietas: "
      "sin gluten, sin lácteos y sin azúcar. Una sola compra donde come todo el equipo, sin que nadie "
      "quede afuera de la mesa.", H - 328, 12.5, W * 0.74, 19, "Sans", INK)
fmts = [("Coffee breaks", "Para reuniones y desayunos de equipo."),
        ("Días saludables", "Un día sano para todo el equipo."),
        ("Eventos corporativos", "Catering a medida para tu evento.")]
fy = H - 430; bw = (W - 112 - 40) / 3
for i, (t, d) in enumerate(fmts):
    x = 56 + i * (bw + 20); rrect(x, fy - 98, bw, 98, 12, CARD); leaf(x + bw / 2, fy - 30, 16, 5.5, 90, TEAL)
    c.setFillColor(col(TEALD)); c.setFont("SansB", 12); c.drawCentredString(x + bw / 2, fy - 52, t)
    para(d, x + 12, fy - 70, 9.5, bw - 24, 12, "Sans", INK, "center")
iy = fy - 132
c.setFillColor(col(TEALD)); c.setFont("SansB", 10.5); c.drawCentredString(W / 2, iy, "INCLUYE")
parac("Bowls, wraps, pollo, pescado y opciones veggie, más colaciones dulces y saladas, a elección.", iy - 18, 11.5, W * 0.78, 16, "Sans", INK)
pb_y = 152; rrect(W / 2 - 188, pb_y, 376, 64, 12, FOREST)
c.setFillColor(col(GOLD)); c.setFont("SansB", 9); c.drawCentredString(W / 2, pb_y + 43, "DESDE")
c.setFillColor(col(CREAM)); c.setFont("SansB", 17); c.drawCentredString(W / 2, pb_y + 21, "$15.000 por persona  ·  mínimo 10")
center_label("PEDÍ TU PROPUESTA A MEDIDA  ·  MUESTRA GRATIS", 74, 9, "Sans", TEALD, 2.5); c.showPage()

# ---------- PÁGINA 4 — Las otras propuestas (más chicas) ----------
bg(CREAM); c.setFillColor(col(FOREST)); c.setFont("Display", 25); c.drawString(56, H - 82, "Nuestras otras propuestas")
box_card("01", "Box Snacking Semanal",
         "Picoteo sano de la semana, listo en la cocina de tu oficina. Por suscripción; se puede pausar.",
         "barritas, granola, crackers, dátiles y bomboncitos.",
         "Desde $8.000 por persona / semana", H - 108, TEAL, h=215, tsize=18, dsize=11, dlead=14)
box_card("02", "Box Coffee Break",
         "Para reuniones o desayunos de equipo. Llega listo para servir, fresco del día.",
         "budín, granola, pancakes y dátiles rellenos.",
         "Desde $58.000  ·  10 a 12 personas", H - 108 - 233, TEALD, h=215, tsize=18, dsize=11, dlead=14)
box_card("03", "Welcome Kit · Regalo Corporativo",
         "Para bienvenida, fin de año o regalar a clientes. Podés sumar tu branding.",
         "barritas, granola, crackers y brownie, en caja con tarjeta.",
         "Desde $22.000 por kit  ·  premium $32.000", H - 108 - 466, GOLD, h=215, tsize=16, dsize=11, dlead=14)
c.showPage()

# ---------- PÁGINA 5 — Por qué + Cómo funciona ----------
bg(CREAM); c.setFillColor(col(FOREST)); c.setFont("Display", 26); c.drawString(56, H - 110, "¿Por qué Betina Potap?")
diffs = [("100% inclusivo", "Sin gluten + sin lácteos + sin azúcar, todo junto. Comen todos."),
         ("Artesanal y fresco", "Nada industrial ni envasado en serie. Hecho a mano."),
         ("A medida", "Armamos el box para tu equipo y tu frecuencia de entrega."),
         ("Sin riesgo", "Probás con muestra gratis y elegís sin compromiso.")]
y = H - 150
for t, d in diffs:
    leaf(64, y + 3, 18, 6, 20, TEAL); c.setFillColor(col(TEALD)); c.setFont("SansB", 13); c.drawString(92, y, t)
    para(d, 92, y - 17, 11, W - 220, 15, "Sans", INK); y -= 58
y -= 6; c.setStrokeColor(col(SAGE)); c.setLineWidth(0.8); c.line(56, y, W - 56, y); y -= 40
c.setFillColor(col(FOREST)); c.setFont("Display", 26); c.drawString(56, y, "Cómo funciona"); y -= 30
steps = [("1", "Probás", "Te mandamos una muestra gratis para que el equipo la pruebe."),
         ("2", "Elegís", "El box y la frecuencia. Sin compromiso, se puede pausar."),
         ("3", "Recibís", "Entregamos en tu oficina, de lunes a viernes.")]
bw = (W - 112 - 40) / 3
for i, (n, t, d) in enumerate(steps):
    x = 56 + i * (bw + 20); rrect(x, y - 140, bw, 128, 12, FOREST)
    c.setFillColor(col(GOLD)); c.setFont("Display", 34); c.drawCentredString(x + bw / 2, y - 52, n)
    c.setFillColor(col(CREAM)); c.setFont("SansB", 13); c.drawCentredString(x + bw / 2, y - 76, t)
    para(d, x + 12, y - 96, 9.5, bw - 24, 12.5, "Sans", CREAM, "center")
sprig(W - 70, 90, 1.1, 150, SAGE, 0.7); c.showPage()

# ---------- PÁGINA 6 — Cierre / contacto ----------
bg(FOREST); c.setStrokeColor(col(SAGE)); c.setLineWidth(0.8); c.setStrokeAlpha(0.5); c.rect(34, 34, W - 68, H - 68, fill=0, stroke=1); c.setStrokeAlpha(1)
sprig(62, H - 76, 1.15, -22, SAGE, 0.55); sprig(W - 70, 150, 1.6, 160, SAGE, 0.5)
c.setFillColor(col(CREAM)); c.setFont("Display", 30); c.drawCentredString(W / 2, H - 150, "¿Lista tu oficina"); c.drawCentredString(W / 2, H - 188, "para comer mejor?")
c.setFillColor(col(GOLD)); c.setFont("Script", 26); c.drawCentredString(W / 2, H - 232, "pedí tu muestra gratis")
parac("Escribinos y coordinamos una muestra gratis para tu equipo.", H - 274, 12, W * 0.72, 16, "Sans", SAGE)
# Tres recuadros de contacto: WhatsApp, Instagram y TikTok
contacts = [("WhatsApp", "11 6629 3150"), ("Instagram", "@betinapotap.naturista"), ("TikTok", "@betinapotap.naturista")]
cw = (W - 112 - 40) / 3; ch = 100; cy = H - 430
for i, (lab, val) in enumerate(contacts):
    x = 56 + i * (cw + 20); rrect(x, cy, cw, ch, 12, "#2C5A4E")
    leaf(x + cw / 2, cy + ch - 24, 14, 5, 90, SAGE)
    c.setFillColor(col(SAGE)); c.setFont("SansB", 11); c.drawCentredString(x + cw / 2, cy + ch - 48, lab)
    c.setFillColor(col(CREAM)); c.setFont("SansB", 11.5); c.drawCentredString(x + cw / 2, cy + 34, val)
center_label("BETINA POTAP · ALIMENTOS NATURALES · CABA", 110, 9, "Sans", SAGE, 2.5); c.showPage()

c.save()
print("Catálogo generado: Catalogo-Comercial-Betina-Potap.pdf")
