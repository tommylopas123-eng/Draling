#!/usr/bin/env python3
"""
3 ESTILOS de posteo de Instagram (1080x1080) con ESPACIO PARA FOTO, para elegir.
Mismo contenido de ejemplo en los 3 para comparar el diseño.
Salida: post-opcion-A.pdf / B / C  (se renderizan a PNG para ver).
Estética base "Jardín Sereno". Fuentes de canvas-design.
"""
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import simpleSplit
from reportlab.lib.colors import HexColor

FD = "../.claude/skills/canvas-design/canvas-fonts/"
for n, f in [("Display", "Gloock-Regular.ttf"), ("Serif", "YoungSerif-Regular.ttf"),
             ("Sans", "Outfit-Regular.ttf"), ("SansB", "Outfit-Bold.ttf"),
             ("Script", "NothingYouCouldDo-Regular.ttf")]:
    pdfmetrics.registerFont(TTFont(n, FD + f))

CREAM = "#F6F2E9"; FOREST = "#22473C"; TEAL = "#2C8A82"; TEALD = "#1C5E57"
SAGE = "#9DBDAE"; GOLD = "#BE9E55"; INK = "#34362F"; CARD = "#E7DEC9"
def col(h): return HexColor(h)
S = 1080

def leaf(c, x, y, length, wid, ang, color, alpha=1):
    c.saveState(); c.translate(x, y); c.rotate(ang)
    c.setFillColor(col(color)); c.setStrokeColor(col(color)); c.setLineWidth(1)
    if alpha < 1: c.setFillAlpha(alpha)
    p = c.beginPath(); p.moveTo(0, 0)
    p.curveTo(length*0.35, wid, length*0.7, wid, length, 0)
    p.curveTo(length*0.7, -wid, length*0.35, -wid, 0, 0)
    c.drawPath(p, fill=1, stroke=1); c.restoreState()

def photo_ph(c, x, y, w, h, r=28, label="ESPACIO PARA FOTO", dark=False):
    base = "#2E544A" if dark else CARD
    c.setFillColor(col(base)); c.roundRect(x, y, w, h, r, fill=1, stroke=0)
    c.setStrokeColor(col(SAGE if not dark else "#6E9385")); c.setLineWidth(2); c.setDash(8, 8)
    c.roundRect(x+14, y+14, w-28, h-28, r-6, fill=0, stroke=1); c.setDash()
    cx, cy = x+w/2, y+h/2
    # iconito camara simple
    c.setFillColor(col(SAGE)); c.roundRect(cx-34, cy+6, 68, 44, 8, fill=1, stroke=0)
    c.setFillColor(col(base)); c.circle(cx, cy+28, 15, fill=1, stroke=0)
    c.setFillColor(col(SAGE)); c.setFont("SansB", 22)
    c.drawCentredString(cx, cy-44, label)

def wrap(c, txt, x, y, size, width, lead, font, color, align="left"):
    c.setFont(font, size); c.setFillColor(col(color))
    for ln in simpleSplit(txt, font, size, width):
        if align == "center": c.drawCentredString(x+width/2, y, ln)
        else: c.drawString(x, y, ln)
        y -= lead
    return y

HEAD = "Llevá Betina a tu oficina"
SUB = "Snacks artesanales sin TACC, sin lácteos y sin azúcar. Comen todos, sin excepción."
TAG = "@betinapotap.naturista"

# ---------- OPCIÓN A — Jardín Sereno (crema, elegante) ----------
def opcion_A():
    c = canvas.Canvas("post-opcion-A.pdf", pagesize=(S, S))
    c.setFillColor(col(CREAM)); c.rect(0, 0, S, S, fill=1, stroke=0)
    c.setStrokeColor(col(SAGE)); c.setLineWidth(2); c.rect(36, 36, S-72, S-72, fill=0, stroke=1)
    leaf(c, S/2-9, S-118, 30, 10, 90, TEAL)
    c.setFillColor(col(TEALD)); c.setFont("Sans", 20)
    c.drawCentredString(S/2, S-150, "B E T I N A   P O T A P")
    photo_ph(c, 90, 360, S-180, 470)
    c.setFillColor(col(FOREST)); c.setFont("Display", 54)
    c.drawCentredString(S/2, 280, HEAD)
    wrap(c, SUB, 130, 225, 24, S-260, 32, "Sans", INK, "center")
    c.setFillColor(col(GOLD)); c.setFont("SansB", 22)
    c.drawCentredString(S/2, 95, TAG)
    c.showPage(); c.save()

# ---------- OPCIÓN B — Bold (foto grande arriba, banda verde abajo) ----------
def opcion_B():
    c = canvas.Canvas("post-opcion-B.pdf", pagesize=(S, S))
    c.setFillColor(col(FOREST)); c.rect(0, 0, S, S, fill=1, stroke=0)
    photo_ph(c, 0, 430, S, S-430, r=0, label="ESPACIO PARA FOTO", dark=True)
    # banda inferior
    c.setFillColor(col(FOREST)); c.rect(0, 0, S, 430, fill=1, stroke=0)
    leaf(c, 70, 350, 34, 11, 25, GOLD)
    c.setFillColor(col(GOLD)); c.setFont("Display", 62)
    wrap(c, HEAD, 70, 320, 62, S-140, 64, "Display", GOLD, "left")
    wrap(c, SUB, 70, 170, 26, S-300, 34, "Sans", CREAM, "left")
    c.setFillColor(col(SAGE)); c.setFont("SansB", 24)
    c.drawString(70, 70, TAG)
    c.showPage(); c.save()

# ---------- OPCIÓN C — Editorial (split: foto izquierda, texto derecha) ----------
def opcion_C():
    c = canvas.Canvas("post-opcion-C.pdf", pagesize=(S, S))
    c.setFillColor(col(CREAM)); c.rect(0, 0, S, S, fill=1, stroke=0)
    photo_ph(c, 0, 0, 540, S, r=0)
    # panel derecho
    c.setFillColor(col(CREAM)); c.rect(540, 0, 540, S, fill=1, stroke=0)
    leaf(c, 590, S-150, 30, 10, 30, TEAL)
    c.setFillColor(col(TEALD)); c.setFont("Sans", 18)
    c.drawString(590, S-200, "S N A C K I N G   S A L U D A B L E")
    wrap(c, HEAD, 590, S-300, 46, 440, 54, "Display", FOREST, "left")
    wrap(c, SUB, 590, S-560, 23, 430, 31, "Sans", INK, "left")
    c.setStrokeColor(col(GOLD)); c.setLineWidth(3); c.line(590, 250, 700, 250)
    c.setFillColor(col(GOLD)); c.setFont("SansB", 21)
    c.drawString(590, 180, TAG)
    c.showPage(); c.save()

opcion_A(); opcion_B(); opcion_C()
print("Generados: post-opcion-A/B/C.pdf")
