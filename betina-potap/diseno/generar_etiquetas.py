#!/usr/bin/env python3
"""
Genera las ETIQUETAS de producto (una por página) + la TARJETA del box.
Estética "Jardín Sereno". Salida: Etiquetas-Betina-Potap.pdf
Uso: cd betina-potap && python3 diseno/generar_etiquetas.py

Para editar: cambiá la lista PRODUCTOS (nombre, ingredientes, y "claims" si hace falta).
Fecha de elaboración se completa a mano por tanda.
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
DEFAULT_CLAIMS = ["SIN GLUTEN", "SIN LÁCTEOS", "SIN AZÚCAR"]

# ====== PRODUCTOS (nombre · ingredientes · claims opcional) ======
PRODUCTOS = [
    {"nombre": "Frutos secos activados", "ingredientes": "almendras, nueces, castañas, semillas de calabaza, girasol y sal marina."},
    {"nombre": "Bolitas de dátiles", "ingredientes": "dátiles, almendras, cacao amargo y coco rallado."},
    {"nombre": "Cookies de avena", "ingredientes": "avena sin TACC, dátiles, huevo, aceite y naranja."},
    {"nombre": "Muffins de chocolate", "ingredientes": "harina de almendras, cacao amargo, dátiles, pasta de maní y huevo."},
    {"nombre": "Alfajor de cacao y dátiles", "ingredientes": "harina de arroz, cacao amargo, polvo de hornear, aceite, esencia, leche de almendras, dátiles, pasta de maní, sal marina y coco rallado."},
    {"nombre": "Crackers de zanahoria", "ingredientes": "harina de almendras, zanahoria, chía, sal y aceite."},
    {"nombre": "Garbanzos crocantes", "ingredientes": "garbanzos, sal marina, especias y aceite."},
    {"nombre": "Brownies", "ingredientes": "harina de almendras, dátiles, pasta de maní, esencia de vainilla y chía."},
    {"nombre": "Blend de hierbas para mate", "ingredientes": "cedrón, cola de caballo, melisa, marcela, burrito, té verde, manzanilla, diente de león, boldo y coco rallado."},
    {"nombre": "Blend de té", "ingredientes": "té rojo, hibiscus y pétalos de rosa."},
    {"nombre": "Barrita de semillas", "ingredientes": "sésamo, girasol, clara de huevo y dátil."},
    {"nombre": "Barrita de dátiles", "ingredientes": "dátiles, maní, cacao amargo y arroz inflado."},
    {"nombre": "Yogur griego", "ingredientes": "leche entera, leche en polvo, esencia de vainilla y yogur griego.", "claims": ["SIN GLUTEN", "SIN AZÚCAR"]},
    {"nombre": "Granola", "ingredientes": "frutos secos, banana, clara de huevo y cacao amargo."},
    {"nombre": "Dip de hummus", "ingredientes": "garbanzos, aceite de oliva, sal marina, comino, limón y ajo."},
    {"nombre": "Dip de zanahoria", "ingredientes": "zanahoria, aceite de oliva, sal marina, cúrcuma y pimienta."},
    {"nombre": "Fruta fresca de estación", "ingredientes": "fruta fresca de estación, seleccionada, lavada y lista para consumo."},
    {"nombre": "Tostadas de sarraceno", "ingredientes": "trigo sarraceno, mandioca, levadura, sal marina, aceite y psyllium."},
    {"nombre": "Tostadas de almendras", "ingredientes": "harina de almendras, mandioca, levadura, sal marina, aceite y psyllium."},
]

c = canvas.Canvas("Etiquetas-Betina-Potap.pdf")

def leaf(x, y, length, wid, ang, color):
    c.saveState(); c.translate(x, y); c.rotate(ang)
    c.setFillColor(col(color)); c.setStrokeColor(col(color)); c.setLineWidth(0.5)
    p = c.beginPath(); p.moveTo(0, 0)
    p.curveTo(length*0.35, wid, length*0.7, wid, length, 0)
    p.curveTo(length*0.7, -wid, length*0.35, -wid, 0, 0)
    c.drawPath(p, fill=1, stroke=1)
    c.setStrokeColor(col(CREAM)); c.setLineWidth(0.4); c.line(length*0.06, 0, length*0.9, 0)
    c.restoreState()

def wrap(txt, x, y, size, width, lead, font, color, align="left"):
    c.setFont(font, size); c.setFillColor(col(color))
    for ln in simpleSplit(txt, font, size, width):
        if align == "center": c.drawCentredString(x + width/2, y, ln)
        else: c.drawString(x, y, ln)
        y -= lead
    return y

def etiqueta(p):
    LW, LH = 90*mm, 65*mm
    c.setPageSize((LW, LH))
    c.setFillColor(col(CREAM)); c.rect(0, 0, LW, LH, fill=1, stroke=0)
    c.setStrokeColor(col(SAGE)); c.setLineWidth(0.8); c.rect(3*mm, 3*mm, LW-6*mm, LH-6*mm, fill=0, stroke=1)
    leaf(LW/2 - 4, LH-12*mm, 8, 2.6, 90, TEAL)
    c.setFillColor(col(FOREST)); c.setFont("Display", 19); c.drawCentredString(LW/2, LH-21*mm, "Betina Potap")
    c.setFillColor(col(TEALD)); c.setFont("Sans", 6.5)
    c.drawCentredString(LW/2, LH-25*mm, "A L I M E N T O S   N A T U R A L E S")
    # nombre (achica si es muy largo)
    nsz = 12
    while pdfmetrics.stringWidth(p["nombre"], "Serif", nsz) > LW-18*mm and nsz > 9:
        nsz -= 0.5
    c.setFillColor(col(FOREST)); c.setFont("Serif", nsz); c.drawCentredString(LW/2, LH-33*mm, p["nombre"])
    claims = "   ·   ".join(p.get("claims", DEFAULT_CLAIMS))
    c.setFillColor(col(GOLD)); c.setFont("SansB", 7.5); c.drawCentredString(LW/2, LH-38*mm, claims)
    c.setStrokeColor(col(SAGE)); c.setLineWidth(0.5); c.line(8*mm, LH-40*mm, LW-8*mm, LH-40*mm)
    # ingredientes + datos (adaptativo: si la lista es larga, achica para que entre)
    ing = "Ingredientes: " + p["ingredientes"]
    nlines = len(simpleSplit(ing, "Sans", 7, LW-16*mm))
    if nlines <= 2:
        isz, ild, fsz, fld, gap = 7, 9, 7, 9.5, 4
    else:
        isz, ild, fsz, fld, gap = 6, 7.5, 6, 8, 4
    y = LH - 43*mm
    y = wrap(ing, 8*mm, y, isz, LW-16*mm, ild, "Sans", INK) - gap
    c.setFont("Sans", fsz); c.setFillColor(col(INK))
    c.drawString(8*mm, y, "Sin conservantes. Conservar en lugar fresco y seco."); y -= fld
    c.drawString(8*mm, y, "Elaborado por Betina Potap. Colegiales. CABA."); y -= fld
    c.drawString(8*mm, y, "Fecha de elaboración: ___ / ___ / ___")
    c.setFillColor(col(TEALD)); c.setFont("SansB", 6.5)
    c.drawCentredString(LW/2, 4*mm, "@betinapotap.naturista   ·   WhatsApp 11 6629 3150")
    c.showPage()

def tarjeta():
    TW, TH = 90*mm, 55*mm
    c.setPageSize((TW, TH))
    c.setFillColor(col(FOREST)); c.rect(0, 0, TW, TH, fill=1, stroke=0)
    c.setStrokeColor(col(SAGE)); c.setLineWidth(0.7); c.setStrokeAlpha(0.5)
    c.rect(3*mm, 3*mm, TW-6*mm, TH-6*mm, fill=0, stroke=1); c.setStrokeAlpha(1)
    leaf(TW/2 - 5, TH-12*mm, 10, 3.2, 90, GOLD)
    c.setFillColor(col(CREAM)); c.setFont("Script", 22); c.drawCentredString(TW/2, TH-23*mm, "¡Gracias!")
    c.setFillColor(col(CREAM)); c.setFont("Serif", 11); c.drawCentredString(TW/2, TH-31*mm, "Hecho a mano para tu equipo")
    wrap("Comida natural, sin gluten, sin lácteos y sin azúcar. Para que coman todos, sin que nadie quede afuera.",
         10*mm, TH-37*mm, 7.5, TW-20*mm, 9.5, "Sans", SAGE, "center")
    c.setFillColor(col(GOLD)); c.setFont("SansB", 7)
    c.drawCentredString(TW/2, 7*mm, "@betinapotap.naturista   ·   11 6629 3150")
    c.showPage()

for p in PRODUCTOS:
    etiqueta(p)
tarjeta()
c.save()
print(f"Generado: Etiquetas-Betina-Potap.pdf ({len(PRODUCTOS)} etiquetas + tarjeta)")
