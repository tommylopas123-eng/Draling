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

## Flujo de trabajo
- Mantener actualizado `betina-potap/PLAN.md` (marcar `[x]` lo completado).
- Commitear y pushear los cambios a la rama de trabajo.
