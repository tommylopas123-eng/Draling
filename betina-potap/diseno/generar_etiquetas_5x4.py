#!/usr/bin/env python3
"""
Versión COMPACTA de las etiquetas en 5x4 cm (50x40 mm), 1 por página, sin tarjeta.
Toma los productos de generar_etiquetas.py. Salida: Etiquetas-Betina-Potap-5x4.pdf
Uso: cd betina-potap && python3 diseno/generar_etiquetas_5x4.py
"""
import os
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import simpleSplit
from reportlab.lib.colors import HexColor

FD = "../.claude/skills/canvas-design/canvas-fonts/"
for n, f in [("Display", "Gloock-Regular.ttf"), ("Serif", "YoungSerif-Regular.ttf"),
             ("Sans", "Outfit-Regular.ttf"), ("SansB", "Outfit-Bold.ttf")]:
    pdfmetrics.registerFont(TTFont(n, FD + f))

CREAM = "#F6F2E9"; FOREST = "#22473C"; TEAL = "#2C8A82"; TEALD = "#1C5E57"; SAGE = "#9DBDAE"; GOLD = "#BE9E55"; INK = "#34362F"
def col(h): return HexColor(h)

# Cargar PRODUCTOS y DEFAULT_CLAIMS del generador principal (sin ejecutar el canvas)
src = open(os.path.join(os.path.dirname(__file__), "generar_etiquetas.py")).read()
exec(src.split("c = canvas.Canvas")[0])

c = canvas.Canvas("Etiquetas-Betina-Potap-5x4.pdf")

def leaf(x, y, length, wid, ang, color):
    c.saveState(); c.translate(x, y); c.rotate(ang)
    c.setFillColor(col(color)); c.setStrokeColor(col(color)); c.setLineWidth(0.4)
    p = c.beginPath(); p.moveTo(0, 0)
    p.curveTo(length*0.35, wid, length*0.7, wid, length, 0)
    p.curveTo(length*0.7, -wid, length*0.35, -wid, 0, 0)
    c.drawPath(p, fill=1, stroke=1)
    c.setStrokeColor(col(CREAM)); c.setLineWidth(0.3); c.line(length*0.06, 0, length*0.9, 0)
    c.restoreState()

def wrap(txt, x, y, sz, w, ld, fn, cl):
    c.setFont(fn, sz); c.setFillColor(col(cl))
    for ln in simpleSplit(txt, fn, sz, w):
        c.drawString(x, y, ln); y -= ld
    return y

def etiqueta(p):
    LW, LH = 50*mm, 40*mm
    c.setPageSize((LW, LH))
    c.setFillColor(col(CREAM)); c.rect(0, 0, LW, LH, fill=1, stroke=0)
    c.setStrokeColor(col(SAGE)); c.setLineWidth(0.6); c.rect(2*mm, 2*mm, LW-4*mm, LH-4*mm, fill=0, stroke=1)
    leaf(LW/2, LH-7*mm, 6, 2, 90, TEAL)
    c.setFillColor(col(FOREST)); c.setFont("Display", 10.5); c.drawCentredString(LW/2, LH-10.5*mm, "Betina Potap")
    c.setFillColor(col(TEALD)); c.setFont("Sans", 4.4); c.drawCentredString(LW/2, LH-13*mm, "A L I M E N T O S   N A T U R A L E S")
    # nombre (achica si es largo)
    nsz = 7.5
    while pdfmetrics.stringWidth(p["nombre"], "Serif", nsz) > LW-7*mm and nsz > 5.5:
        nsz -= 0.3
    c.setFillColor(col(FOREST)); c.setFont("Serif", nsz); c.drawCentredString(LW/2, LH-16.2*mm, p["nombre"])
    claims = " · ".join(p.get("claims", DEFAULT_CLAIMS))
    c.setFillColor(col(GOLD)); c.setFont("SansB", 5); c.drawCentredString(LW/2, LH-19*mm, claims)
    c.setStrokeColor(col(SAGE)); c.setLineWidth(0.4); c.line(4*mm, LH-20.3*mm, LW-4*mm, LH-20.3*mm)
    ing = "Ingredientes: " + p["ingredientes"]
    nlines = len(simpleSplit(ing, "Sans", 5, LW-8*mm))
    isz, ild = (5, 5.4) if nlines <= 3 else (4.4, 4.9)
    y = wrap(ing, 4*mm, LH-23*mm, isz, LW-8*mm, ild, "Sans", INK) - 2
    c.setFont("Sans", 4.6); c.setFillColor(col(INK))
    c.drawString(4*mm, y, "Sin conservantes. Conservar en lugar fresco y seco."); y -= 5.2
    c.drawString(4*mm, y, "Elaborado por Betina Potap. Colegiales. CABA."); y -= 5.2
    c.drawString(4*mm, y, "Fecha de elaboración: __ / __ / __"); y -= 7
    c.setFillColor(col(TEALD)); c.setFont("SansB", 4.6)
    c.drawCentredString(LW/2, y, "@betinapotap.naturista · WhatsApp 11 6629 3150")
    c.showPage()

for p in PRODUCTOS:
    etiqueta(p)
c.save()
print(f"Generado: Etiquetas-Betina-Potap-5x4.pdf ({len(PRODUCTOS)} etiquetas, 5x4 cm)")
