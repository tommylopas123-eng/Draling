# Draling — Aprendé a Automatizar (ruta de 8 semanas)

> Plan práctico para pasar de cero a vender automatizaciones reales.
> Regla: **cada semana se construye algo que funciona.** Nada de mirar cursos
> de 40 horas sin tocar nada.

---

## El stack de Draling (qué herramientas aprender y por qué)

| Herramienta | Para qué | Costo |
|-------------|----------|-------|
| **n8n** ⭐ | El cerebro: conecta apps y arma flujos (la herramienta principal a dominar) | Gratis (self-hosted) o cloud ~€20/mes |
| **Google Sheets** | La "base de datos" que toda pyme entiende | Gratis |
| **WhatsApp Business + Cloud API de Meta** | El canal #1 de las pymes argentinas | App gratis; API paga por conversación (~USD 20-40/mes por cliente) |
| **Claude / API de IA** | La inteligencia: leer mensajes, extraer datos de pedidos, redactar respuestas | Pago por uso (centavos por mensaje) |
| **Make.com** | Alternativa visual más fácil que n8n (bueno para arrancar rápido) | Plan gratis: 1.000 operaciones/mes |
| **Claude Code** 😉 | Tu copiloto: te escribe los flujos, los scripts y te destraba cuando te trabás | Ya lo tenés |

**¿Por qué n8n como herramienta principal?** Es la más demandada del mercado
freelance de automatización (tarifas 67% más altas que otros servicios de IA según
Upwork 2026), es gratis para practicar, y no dependés de los precios de Zapier/Make
cuando tengas muchos clientes.

---

## Las 8 semanas

### Semana 1 — Fundamentos: pensar en flujos
**Objetivo:** entender qué es un trigger (disparador), una acción y un flujo.
- Crear cuenta gratis en **Make.com** y hacer el tutorial inicial (1 hora).
- **Proyecto:** "Cuando llega un mail con la palabra 'pedido' → guardar remitente y texto en una planilla de Google Sheets."
- Concepto clave: toda automatización es `CUANDO pasa X → HACÉ Y`.

### Semana 2 — n8n básico
**Objetivo:** reproducir lo de la semana 1 pero en n8n.
- Crear cuenta en n8n cloud (prueba gratis) o pedirme que te ayude a instalarlo gratis.
- Aprender: nodos, credenciales, ejecutar paso a paso, ver los datos entre nodos.
- **Proyecto:** formulario de Google Forms → fila en Sheets → mail automático de "recibimos tu consulta".

### Semana 3 — Sumar IA a los flujos
**Objetivo:** que la IA lea texto desordenado y devuelva datos ordenados.
- En n8n, usar el nodo de IA (Claude/OpenAI) con un prompt simple.
- **Proyecto (el más importante de todos):** pegar un mensaje real de pedido
  ("Hola! mandame 2 kg de granola y 3 mieles para el local de Cabildo") →
  la IA devuelve: producto, cantidad, cliente → se carga solo en Sheets.
- Esto es EXACTAMENTE lo que vas a vender. Practicalo hasta que salga en 5 minutos.

### Semana 4 — WhatsApp nivel 1
**Objetivo:** automatizar lo que se puede sin API.
- WhatsApp Business (app gratis): mensaje de bienvenida, ausencia, respuestas rápidas, catálogo.
- Entender qué es la **WhatsApp Cloud API** de Meta: crear cuenta de desarrollador y enviar tu primer mensaje de prueba (gratis en sandbox).
- **Proyecto:** configurar WhatsApp Business completo para Betina (¡cliente real!).

### Semana 5 — WhatsApp nivel 2: el bot real
**Objetivo:** un bot que responde solo.
- Conectar WhatsApp Cloud API → n8n (webhook) → IA → respuesta.
- **Proyecto:** bot que responde precios y horarios del catálogo de Betina,
  y si no sabe, dice "te contacto con Betina" y avisa por mail/Telegram.
- Pedime ayuda con esto: es el paso más técnico, pero una vez armado se
  **reutiliza para todos los clientes** (cambia el catálogo, no el flujo).

### Semana 6 — Cobranzas y reportes
**Objetivo:** dos automatizaciones simples que se venden fácil.
- **Proyecto A:** planilla de deudores → todos los lunes el flujo manda recordatorio
  de pago por WhatsApp/mail a quien debe.
- **Proyecto B:** planilla de ventas → todos los lunes 8am llega un resumen automático:
  total vendido, top productos, quién debe.

### Semana 7 — Empaquetar y demostrar
**Objetivo:** convertir lo aprendido en productos vendibles.
- Armar 3 demos grabadas (pantalla + voz): bot de pedidos, recordatorio de cobros, reporte semanal.
- Escribir la "receta" de cada una: qué incluye, cuánto tarda en implementarse, precio.
- Estas demos son el contenido de tus redes (ver `PLAN-REDES.md`) y tu material de venta.

### Semana 8 — Primer cliente real
**Objetivo:** implementar en un negocio que no sea el de tu familia.
- Elegir el prospecto más caliente de `PROSPECTOS.csv`.
- Ofrecer: diagnóstico gratis → implementación con descuento a cambio de testimonio.
- Documentar TODO: horas ahorradas, mensajes respondidos, antes/después → tu primer caso de éxito público.

---

## Recursos (gratis, en español o fáciles)

- **n8n docs oficiales** (docs.n8n.io) + su canal de YouTube.
- YouTube en español: buscar "n8n español tutorial" y "n8n WhatsApp" — hay decenas de tutoriales paso a paso actualizados.
- Comunidades: grupo de Facebook "n8n en español", comunidad de n8n (community.n8n.io).
- **Meta for Developers** → documentación de WhatsApp Cloud API (tiene modo de prueba gratis).
- **Yo (Claude):** pedime "armame el flujo de n8n para X" o "explicame este error" — puedo escribirte los flujos, los prompts y el código que haga falta.

## Reglas de oro

1. **Construí, no mires.** 1 hora de armar flujos vale más que 5 horas de videos.
2. **Todo lo que aprendas, aplicalo primero en el negocio de Betina.** Es tu laboratorio real y gratis.
3. **Armá una vez, vendé muchas veces.** Elegí automatizaciones repetibles por rubro.
4. **Guardá cada flujo que armes** (n8n exporta JSON) — ese es tu inventario de productos.
5. **Trabado más de 30 min = preguntame.** No pierdas tardes enteras con un error.
