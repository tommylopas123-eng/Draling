#!/usr/bin/env python3
"""
Genera la ETIQUETA de producto y la TARJETA del box para Betina Potap.
Estética "Jardín Sereno". Salida: Etiquetas-y-Tarjeta-Betina-Potap.pdf
Uso: cd betina-potap && python3 diseno/generar_etiquetas.py
Requiere: reportlab. Fuentes en .claude/skills/canvas-design/canvas-fonts.

NOTA: La etiqueta usa "Crackers" como EJEMPLO. Para cada producto hay que cambiar
el nombre, los ingredientes y el peso. Vencimiento y lote se completan por tanda
(se imprimen en blanco para escribir a mano, o se ajustan acá).
"""
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
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
SAGE = "#9DBDAE"; GOLD = "#BE9E55"; INK = "#34362F"
def col(h): return HexColor(h)

c = canvas.Canvas("Etiquetas-y-Tarjeta-Betina-Potap.pdf")

def leaf(x, y, length, wid, ang, color, alpha=1):
    c.saveState(); c.translate(x, y); c.rotate(ang)
    c.setFillColor(col(color)); c.setStrokeColor(col(color)); c.setLineWidth(0.5)
    if alpha < 1: c.setFillAlpha(alpha)
    p = c.beginPath(); p.moveTo(0, 0)
    p.curveTo(length*0.35, wid, length*0.7, wid, length, 0)
    p.curveTo(length*0.7, -wid, length*0.35, -wid, 0, 0)
    c.drawPath(p, fill=1, stroke=1)
    c.setStrokeColor(col(CREAM)); c.setLineWidth(0.4); c.line(length*0.06, 0, length*0.9, 0)
    c.restoreState()

def para(txt, x, y, size, width, leading, font, color, align="left"):
    c.setFont(font, size); c.setFillColor(col(color))
    for line in simpleSplit(txt, font, size, width):
        if align == "center": c.drawCentredString(x + width/2, y, line)
        else: c.drawString(x, y, line)
        y -= leading
    return y

# ---------- ETIQUETA DE PRODUCTO (90 x 65 mm) ----------
LW, LH = 90*mm, 65*mm
c.setPageSize((LW, LH))
c.setFillColor(col(CREAM)); c.rect(0, 0, LW, LH, fill=1, stroke=0)
c.setStrokeColor(col(SAGE)); c.setLineWidth(0.8); c.rect(3*mm, 3*mm, LW-6*mm, LH-6*mm, fill=0, stroke=1)
# cabecera marca
leaf(LW/2 - 4, LH-12*mm, 8, 2.6, 90, TEAL)
c.setFillColor(col(FOREST)); c.setFont("Display", 19); c.drawCentredString(LW/2, LH-21*mm, "Betina Potap")
c.setFillColor(col(TEALD)); c.setFont("Sans", 6.5)
c.drawCentredString(LW/2, LH-25*mm, "A L I M E N T O S   N A T U R A L E S")
# producto (EJEMPLO)
c.setFillColor(col(FOREST)); c.setFont("Serif", 12); c.drawCentredString(LW/2, LH-33*mm, "Crackers de semillas y orégano")
# claims
c.setFillColor(col(GOLD)); c.setFont("SansB", 7.5)
c.drawCentredString(LW/2, LH-38*mm, "SIN GLUTEN  ·  SIN LÁCTEOS  ·  SIN AZÚCAR")
c.setStrokeColor(col(SAGE)); c.setLineWidth(0.5); c.line(8*mm, LH-41*mm, LW-8*mm, LH-41*mm)
# info obligatoria
y = LH - 45*mm
y = para("Ingredientes: harina de garbanzos, semillas de lino, sésamo y girasol, "
         "aceite de oliva, orégano y sal marina.", 8*mm, y, 6.5, LW-16*mm, 8, "Sans", INK) - 1
c.setFont("SansB", 6.5); c.setFillColor(col(INK)); c.drawString(8*mm, y, "Peso neto: 250 g")
c.setFont("Sans", 6.5); c.drawRightString(LW-8*mm, y, "Sin conservantes · conservar en lugar fresco y seco")
y -= 8
c.setFont("Sans", 6.5); c.drawString(8*mm, y, "Elaborado por Betina Potap — Colegiales, CABA. Factura C (monotributo).")
y -= 8
c.setFont("Sans", 6.5); c.drawString(8*mm, y, "Vto: ___ / ___ / ___        Lote: __________")
# pie contacto
c.setFillColor(col(TEALD)); c.setFont("SansB", 6.5)
c.drawCentredString(LW/2, 6*mm, "@betinapotap.naturista   ·   WhatsApp 11 6629 3150")
c.showPage()

# ---------- TARJETA DEL BOX (90 x 55 mm) ----------
TW, TH = 90*mm, 55*mm
c.setPageSize((TW, TH))
c.setFillColor(col(FOREST)); c.rect(0, 0, TW, TH, fill=1, stroke=0)
c.setStrokeColor(col(SAGE)); c.setLineWidth(0.7); c.setStrokeAlpha(0.5)
c.rect(3*mm, 3*mm, TW-6*mm, TH-6*mm, fill=0, stroke=1); c.setStrokeAlpha(1)
leaf(TW/2 - 5, TH-12*mm, 10, 3.2, 90, GOLD)
c.setFillColor(col(CREAM)); c.setFont("Script", 22); c.drawCentredString(TW/2, TH-23*mm, "¡Gracias!")
c.setFillColor(col(CREAM)); c.setFont("Serif", 11); c.drawCentredString(TW/2, TH-31*mm, "Hecho a mano para tu equipo")
para("Comida natural, sin gluten, sin lácteos y sin azúcar. "
     "Para que coman todos, sin que nadie quede afuera.", 10*mm, TH-37*mm, 7.5, TW-20*mm, 9.5, "Sans", SAGE, "center")
c.setFillColor(col(GOLD)); c.setFont("SansB", 7)
c.drawCentredString(TW/2, 7*mm, "@betinapotap.naturista   ·   11 6629 3150")
c.showPage()

c.save()
print("Generado: Etiquetas-y-Tarjeta-Betina-Potap.pdf")
