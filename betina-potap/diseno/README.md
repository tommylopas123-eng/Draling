# Diseño del catálogo — Betina Potap

Acá vive todo lo necesario para regenerar y editar el **catálogo comercial PDF**.

## Archivos
- `generar_catalogo.py` — script que genera `../Catalogo-Comercial-Betina-Potap.pdf`.
- `FILOSOFIA-Jardin-Sereno.md` — la filosofía de diseño (estética del catálogo).

## Cómo regenerar el catálogo
```bash
cd betina-potap
pip install reportlab          # si no está instalado
python3 diseno/generar_catalogo.py
```
Genera `betina-potap/Catalogo-Comercial-Betina-Potap.pdf`.

## Cómo editarlo
- **Precios / textos de los boxes:** en `generar_catalogo.py`, buscar las llamadas
  `box_card(...)` (una por cada propuesta). Los argumentos son, en orden:
  número, título, descripción, qué incluye y **precio** (el 5º). El alto de cada
  tarjeta se calcula solo según el contenido, así que no hay que tocar medidas.
- **Contacto:** buscar `11 6629 3150` y `@betinapotap.naturista`.
- **Colores / fuentes:** variables al principio del script (CREAM, FOREST, TEAL, etc.)
  y el bloque `reg(...)` con las tipografías.

## Previsualizar páginas como imagen
```bash
pip install pymupdf
python3 -c "import fitz; d=fitz.open('Catalogo-Comercial-Betina-Potap.pdf'); [p.get_pixmap(dpi=90).save(f'pag-{i+1}.png') for i,p in enumerate(d)]"
```

## Dependencias
- `reportlab` (genera el PDF)
- Fuentes: `.claude/skills/canvas-design/canvas-fonts/` (skill canvas-design, Apache 2.0)
- `pymupdf` (opcional, solo para previsualizar)

> ⚠️ IMPORTANTE: este script es la ÚNICA fuente del catálogo. Cualquier cambio al
> catálogo se hace acá y se regenera el PDF. No editar el PDF a mano.
> Pendiente: sumar fotos de productos y ajustar precios finales (ver `../PLAN.md`).
