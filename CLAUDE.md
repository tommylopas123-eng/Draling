# Replai — Guía para Claude

## Contexto
- **Replai**: empresa a futuro (ver `VISION.md`) — plataforma de automatización con IA para empresas.
- **Proyecto actual**: ayudar al negocio de la madre del usuario, **Betina Potap –
  Alimentos Naturales** (CABA), a vender a empresas/startups (canal B2B).
  - Info del negocio: `betina-potap/EMPRESA.md`
  - Catálogo: `betina-potap/CATALOGO.md`
  - Análisis B2B y recomendaciones: `betina-potap/ANALISIS-B2B.md`
  - Plan con checklist: `betina-potap/PLAN.md`

## Idioma
- Responder siempre en **español** (el usuario es de Argentina).

## Uso proactivo de skills (IMPORTANTE)
- Hay skills instaladas en `.claude/skills/` (marketing, ventas B2B, landing pages,
  competencia, precios, etc.). Ver `SKILLS-RECOMENDADAS.md` y `.claude/skills/ATTRIBUTION.md`.
- **Cada vez que una tarea coincida con una skill instalada, USARLA automáticamente
  sin que el usuario lo pida.** Ejemplos:
  - Estudiar competencia → `competitor-analysis` / `competitor-profiling`
  - Definir público/ICP → `icp-builder` / `product-marketing`
  - Escribir textos de venta → `copywriting`
  - Precios / combos → `pricing` / `offers`
  - Contactar empresas → `prospecting` + `cold-email`
  - Material de venta → `sales-enablement`
  - Landing page → `write-landing`
  - Redes / calendario → `social` / `content-calendar`
  - SEO local (CABA) → `local-seo`
- Mencionar brevemente qué skill se está usando, pero no pedir permiso para usarla.

## Formato de entrega al usuario (IMPORTANTE)
- El usuario **no tiene Excel ni lee archivos .md/.docx** cómodamente.
- **Documentos/material → entregar como GOOGLE DOCS** (NO PDFs). Método que funciona y
  NO se traba: armar el contenido como **HTML** y subirlo con el Google Drive MCP
  (`mcp__Google_Drive__create_file`) usando `contentMimeType: text/html` → Drive lo
  convierte solo en Google Doc con formato (títulos, tablas, negritas). Pasar el link.
  - ⚠️ NO usar PDF ni LibreOffice/`soffice` (está roto en el entorno) ni intentar
    generar PDFs: se traba. Siempre Google Doc vía Drive MCP.
- **Datos/planillas → subir a Google Sheets** (Google Drive MCP: subir el CSV con
  `contentMimeType: text/csv` para que se convierta en planilla de Google), y pasar el link.
- Mantener los `.md` y `.csv` en el repo como fuente, pero lo que se le manda al
  usuario va en Google Docs / Google Sheets.
- Carpeta de Drive: "replai" > "Betina Potap empresa"
  (id `1rRspj4i9fItQppKFZ1ItA71DsV8MGu4D`, cuenta tommylopas123@gmail.com).

## Flujo de trabajo
- Mantener actualizado `betina-potap/PLAN.md` (marcar `[x]` lo completado).
- Commitear y pushear los cambios a la rama de trabajo.
