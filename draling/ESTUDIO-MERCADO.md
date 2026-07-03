# Draling — Estudio de Mercado

> Investigación web realizada el 2026-07-03. Skills usadas: `prospecting`,
> `competitor-analysis`, `icp-builder`. Fuentes al final del documento.
> Lista de prospección accionable: `PROSPECTOS.csv` (también en Google Sheets).

---

## 1. Resumen ejecutivo (lo más importante)

1. **El momento es AHORA.** El 42% de las pymes argentinas ya usa IA, y el 85%
   de las que la usan empezaron en 2024-2025. El mercado se está despertando:
   todavía sos temprano, pero ya no hace falta evangelizar desde cero.
2. **El gap es exactamente lo que hace Draling.** El ~80% de las pymes que "usan IA"
   solo usan ChatGPT para generar contenido. Casi ninguna automatizó procesos
   reales (atención, pedidos, carga de datos). Y 6 de cada 10 pymes de LatAm dicen
   que la IA no les genera valor medible → **necesitan alguien que se la implemente**.
3. **WhatsApp es el campo de batalla.** El 78% de los consumidores argentinos
   prefiere contactar a las empresas por WhatsApp y espera respuesta en ≤5 minutos.
   El negocio que tarda, pierde la venta. Ahí está el dolor más urgente y fácil de vender.
4. **Hay competencia, pero deja huecos.** Existen plataformas DIY (ManyChat, Basework)
   y agencias (ConnectIA, AutomaxIA, Tecnobrain). El hueco de Draling: **servicio
   cercano, precio accesible y en días** para la pyme chica que no va a configurar
   nada sola y a la que las agencias grandes le cobran caro.
5. **Los precios del mercado validan nuestro modelo:** proyectos de automatización
   freelance arrancan en ~USD/EUR 300; plataformas cobran USD 50-200/mes.
   Draling puede cobrar **USD 150-500 por implementación + USD 50-150/mes de
   mantenimiento** y quedar barato frente a agencias y accesible para pymes.

---

## 2. Tamaño y momento del mercado

| Dato | Valor | Fuente |
|------|-------|--------|
| Mercado de IA en América Latina (2025) | USD 5.790 millones | Fortune Business Insights |
| Proyección 2033 | USD 34.620 millones (crece 22,9% anual) | Fortune Business Insights |
| Pymes argentinas que ya usan IA | 42% | Encuesta nacional (nadia.ar) / Ámbito |
| Empezaron a usarla en 2024-2025 | 85% de las que usan | Ámbito / Infobae |
| Solo la usan para contenido (ChatGPT) | ~80% | Ámbito |
| Pymes LatAm sin valor medible de la IA | 6 de cada 10 | WEF |
| Argentinos que prefieren WhatsApp para contactar empresas | 78% | iasistemas |
| Respuesta esperada por el cliente | ≤ 5 minutos | iasistemas |

**Lectura:** la adopción explota pero es superficial. La pyme ya escuchó de IA
(no hay que convencerla de que existe), pero no sabe pasar de ChatGPT a
"mi negocio funciona solo". Ese puente es el producto de Draling.

---

## 3. Competencia

### Mapa competitivo

| Tipo | Ejemplos | Precio aprox. | Dónde fallan (hueco para Draling) |
|------|----------|---------------|------------------------------------|
| **Plataformas DIY** | ManyChat (desde USD 15/mes), Basework, Chatsell, Clientify | USD 15-200/mes | La pyme tiene que configurarla sola. No sabe, no tiene tiempo, le da miedo. |
| **Agencias de automatización IA** | ConnectIA, AutomaxIA, MindAI, Tecnobrain, Ropofy | Proyectos de cientos a miles de USD | Apuntan a empresas medianas; poco personalizadas o caras para el comercio chico. |
| **Plataformas enterprise** | Botmaker, edna.ai | USD cientos/mes + setup | Precio y complejidad enterprise. Fuera del alcance de la pyme. |
| **Freelancers n8n/Make** | Independientes en Workana/Freelancer | Desde ~USD 300/proyecto | Calidad dispareja, sin acompañamiento ni mantenimiento. |
| **No hacer nada / contratar gente** | — | Sueldo: caro | El status quo: es el verdadero competidor #1. |

### Costos técnicos de referencia (para armar precios)
- ManyChat: gratis hasta 1.000 contactos, luego desde USD 15/mes.
- Costo de conversaciones de Meta (WhatsApp API): USD 20-40/mes para una pyme típica.
- n8n: gratis self-hosted (VPS €5-15/mes) o cloud desde €20-24/mes.
- **Conclusión:** el costo técnico de una automatización típica es USD 20-60/mes.
  Todo lo que cobres por encima es margen por el servicio y el conocimiento.

### Posicionamiento de Draling
> "La agencia que le habla al dueño del negocio, no al gerente de sistemas:
> automatización funcionando en días, precio fijo, soporte por WhatsApp, en tu idioma."

---

## 4. Segmentos objetivo (priorizados)

Criterios: (a) dolor de WhatsApp/carga manual, (b) capacidad de pago,
(c) facilidad de acceso para nosotros, (d) repetibilidad de la solución.

| # | Segmento | Dolor principal | Por qué priorizarlo |
|---|----------|-----------------|----------------------|
| 1 | **Dietéticas y alimentos naturales (CABA)** | Pedidos por WhatsApp + catálogo + carga manual | Ya lo conocemos por dentro (caso Betina). Solución repetible: mismo bot para todas. |
| 2 | **Distribuidoras y mayoristas chicos** | Toma de pedidos B2B a mano, cobranzas | Ticket más alto, dolor enorme de carga de pedidos. Red de contactos de Betina. |
| 3 | **Gastronomía (delivery, cafés, restaurantes)** | Pedidos y reservas por WhatsApp fuera de horario | Rubro más activo en WhatsApp; miles en CABA; se pierde venta cada noche. |
| 4 | **Clínicas, consultorios y estética** | Turnos: agendar, confirmar, recordar (ausentismo) | Recordatorio de turnos = automatización simple con ROI clarísimo. |
| 5 | **Gimnasios y estudios (yoga, pilates)** | Consultas repetidas, cobros mensuales, ausencias | Cobro recurrente → recordatorio de pago automático se vende solo. |
| 6 | **Inmobiliarias chicas** | Responder consultas de portales, coordinar visitas | Cada consulta no respondida = comisión perdida. Ticket alto. |
| 7 | **E-commerce chicos (Instagram + TiendaNube)** | Preguntas repetidas (talles, envíos, stock) | Digitalizados a medias: ya venden online, no automatizan atención. |
| 8 | **Estudios contables y jurídicos** | Recolección de documentos, recordatorios de vencimientos | Pagan bien, dolor recurrente todos los meses (vencimientos AFIP/ARCA). |
| 9 | **Startups chicas / agencias de marketing** | Operaciones manuales al crecer (reportes, onboarding) | Entienden el valor rápido; pueden tercerizar automatizaciones a Draling. |

**Anti-objetivo (no gastar tiempo):** empresas grandes con IT propio, negocios
con poquísimas consultas, quien pide "un sistema" gigante a medida.

---

## 5. A quiénes contactar primero (embudo concreto)

### Tanda 0 — Esta semana (contactos calientes, gratis)
1. **Betina Potap – Alimentos Naturales**: cliente #1. Terminar/armar sus
   automatizaciones (pedidos, catálogo, seguimiento) y documentar TODO como caso de éxito.
2. **La red del proyecto Betina**: dietéticas, coworkings con cafetería y
   distribuidores ya relevados en `betina-potap/prospectos-tanda1.csv` — muchos
   son también candidatos a automatizar su atención/pedidos.
3. **Círculo cercano**: conocidos de la familia con negocio (el primer cliente
   pago casi siempre sale de ahí).

### Tanda 1 — Semanas 2-4 (prospección fría local)
- **Google Maps** (la fuente #1 para pymes locales): buscar por rubro + barrio
  (ej. "dietética Belgrano", "inmobiliaria Núñez"), abrir perfil → WhatsApp/IG.
  Meta: 10 contactos nuevos por día, 15 minutos.
- **Instagram**: negocios que publican seguido pero responden lento (mirar
  comentarios sin responder = señal de dolor). DM corto + oferta de diagnóstico.
- **LinkedIn**: dueños y gerentes de pymes de los segmentos 2, 8 y 9.
  Conectar con nota personalizada, sin vender en el primer mensaje.

### Cómo calificar (30 segundos por prospecto — checklist)
- [ ] ¿Recibe consultas/pedidos por WhatsApp o Instagram todos los días?
- [ ] ¿Es el dueño quien responde (o alguien pagado para eso)?
- [ ] ¿Tiene entre 2 y 50 empleados (hay plata pero no hay IT)?
- [ ] ¿Muestra señales de desborde? (responde tarde, "solo WhatsApp", comentarios sin responder)

3-4 ✓ = contactar ya. 2 ✓ = lista B. 0-1 ✓ = descartar.

### El detalle operativo por segmento está en `PROSPECTOS.csv`
(dónde encontrarlos, búsqueda exacta, oferta inicial y primer mensaje sugerido).

---

## 6. Precios recomendados para Draling (validados contra mercado)

| Servicio | Precio Draling | Referencia de mercado |
|----------|---------------|------------------------|
| Diagnóstico (30 min) | **Gratis** | Estándar del rubro para abrir puerta |
| Automatización simple (recordatorios, respuestas automáticas) | **USD 150-250 fijo** | Freelance desde ~USD 300 → quedamos agresivos |
| Automatización media (bot WhatsApp con IA + carga a planilla) | **USD 300-500 fijo** | Agencias cobran mucho más; plataformas no incluyen servicio |
| Mantenimiento + soporte | **USD 50-150/mes** | Plataformas solas ya cuestan USD 50-200/mes |
| Primeros 1-2 clientes | **-50% o gratis** a cambio de testimonio y caso documentado | Inversión en prueba social |

**Regla de venta:** siempre traducir el precio a horas ahorradas
("te ahorra 10 hs/mes del dueño: se paga solo el primer mes").

---

## 7. Riesgos y cómo cubrirlos

| Riesgo | Mitigación |
|--------|------------|
| La pyme no paga en dólares / sensibilidad al precio | Cobrar en pesos ajustable, precio fijo por proyecto, mostrar ROI en horas. |
| Plataformas DIY bajan precios y se hacen más fáciles | Nuestro valor no es la herramienta, es la implementación + soporte cercano. |
| Meta cambia precios/reglas de WhatsApp API | Diversificar: mail, planillas, reportes, cobranzas — no solo bots de WhatsApp. |
| Un solo fundador, tiempo limitado | Soluciones repetibles por segmento (armar 1 vez, vender N veces). |

---

## 8. Fuentes

- [Ámbito — Se acelera la adopción de IA en las pymes](https://www.ambito.com/negocios/se-acelera-la-adopcion-ia-las-pymes-aunque-el-grueso-se-concentra-herramientas-basicas-n6277298)
- [Infobae — Las pymes argentinas apuestan por la IA](https://www.infobae.com/economia/2026/05/05/las-pymes-argentinas-apuestan-por-la-inteligencia-artificial-para-agilizar-gestiones/)
- [nadia.ar — Encuesta nacional de adopción de IA en pymes](https://nadia.ar/investigacion/encuesta-pymes.html)
- [Perfil — 4 de cada 10 pymes usan IA pero pocas miden impacto](https://www.perfil.com/noticias/economia/cuatro-de-cada-diez-pymes-argentinas-ya-usan-ia-pero-pocas-miden-su-impacto-a40.phtml)
- [WEF — Acelerar la IA en América Latina](https://es.weforum.org/stories/2026/01/acelerar-la-ia-en-america-latina/)
- [Fortune Business Insights — Mercado mundial de IA](https://www.fortunebusinessinsights.com/industry-reports/artificial-intelligence-market-100114)
- [iasistemas — Automatización de marketing para pymes: WhatsApp como canal principal](https://iasistemas.com/blog/automatizacion-marketing-pymes-argentina)
- [Basework — Guía chatbot WhatsApp Argentina 2026](https://www.basework.com.ar/blog/chatbot-whatsapp-argentina)
- [ConnectIA](https://connectia.online/) · [AutomaxIA](https://automaxia.com/) · [MindAI](https://mindai-agency.com/agencia-automatizacion-ia/chatbots-para-empresas/) · [Tecnobrain](https://tecnobrain.ar/automatizacion-e-inteligencia-artificial-en-pymes) · [Ropofy](https://ropofy.com/blog/inteligencia-artificial/chatbot-ia-argentina-pymes/)
- [n8nhispano — Cuánto cuesta automatizar con n8n](https://n8nhispano.com/cuanto-cuesta-automatizar-con-n8n-guia-de-costes-reales-2026/)
- [n8n.io — Precios](https://n8n.io/pricing/)
- [Javadex — Ganar dinero con IA 2026](https://www.javadex.es/blog/ganar-dinero-con-ia-principiantes-desde-casa-sin-experiencia-2026)
- [leadcanvas — Cómo buscar empresas en WhatsApp](https://www.leadcanvas.app/blog/como-buscar-empresas-en-whatsapp)
