# Esquema de Notion — Private Build OS

Fuente única de nombres. Las 9 skills buscan estas páginas y bases **por su nombre
exacto** (emoji incluido). Cambiar un nombre acá rompe a las otras.

Usa las herramientas del conector de Notion que tengas disponibles (buscar, crear
página, crear base de datos, crear filas). Si el conector no permite crear bases, crea
las páginas y entrega las bases como tablas markdown para que el cliente las cree con
"/database" — y dile exactamente qué columnas poner.

## Orden de creación

1. Busca si ya existe "🏗️ Private Build OS". Si existe, **no dupliques**: pregunta si
   se actualiza o se crea "🏗️ Private Build OS (2)".
2. Crea la página **🏗️ Private Build OS** en el nivel más alto que permita el conector
   (espacio privado del cliente si no hay otra opción).
3. Dentro, en este orden:

### 📄 Documento de contexto (página)

Secciones fijas (títulos H2), llenas con las respuestas del arranque:

- **Qué hago y para quién** — una frase.
- **Qué vendo y a qué precio** — la oferta principal.
- **Mi mejor cliente hoy** — rubro, etapa, qué le dolía.
- **Canales vivos** — los marcados en el diagnóstico.
- **Facturación mensual aproximada** — o "no declarada".
- **Lo que más me frena hoy** — en sus palabras.
- **Meta a 90 días** — verificable.
- **Cuello actual** — el área y por qué (lo escribe pb-os; lo mantiene pb-foundations).
- **Última actualización** — fecha.

Lo leen **todas** las skills antes de trabajar. Lo mantiene `pb-foundations`.

### Las 8 páginas de área

Nombres exactos: **01 · Foundations**, **02 · Oferta**, **03 · Avatar**,
**04 · Contenido**, **05 · Captura**, **06 · Ventas**, **07 · Entrega**,
**08 · Success**.

Contenido inicial de cada una (lo reemplaza la skill del área al construir):

- Callout: "Qué resuelve: <promesa del área>. Skill: pb-<área>. Frase para abrirla:
  <frase>."
- H2 **Estado**: puntaje del diagnóstico y la respuesta que dio.
- H2 **Piezas** — vacío, lo llena la skill.

### Las 6 bases de datos (dentro del hub)

**1. 🧭 Tablero de áreas**

| Propiedad | Tipo | Valores |
|---|---|---|
| Área | title | |
| N° | number | 1–8 |
| Puntaje | number | 1–4 |
| Estado | select | Rota · En obra · Funciona |
| Cuello | checkbox | solo una fila en true |
| Pieza que falta | text | |
| Próxima acción | text | |
| Revisado | date | |

Crea las 8 filas con el resultado del diagnóstico.

**2. 👥 Leads y clientes**

| Propiedad | Tipo | Valores |
|---|---|---|
| Nombre | title | |
| Etapa | select | Nuevo · Conversación · Llamada agendada · Propuesta · Cliente activo · Perdido · Renovó · No es para mí |
| Canal de origen | select | Contenido · Anuncios · Referido · Outbound · Otro |
| Pieza de origen | text | |
| Fit avatar | select | Alto · Medio · Bajo |
| Dolor | text | |
| Objeción | text | |
| Próximo paso | text | |
| Fecha próximo paso | date | |
| Valor | number | |
| Notas | text | |

**3. 📞 Llamadas**

| Propiedad | Tipo | Valores |
|---|---|---|
| Llamada | title | |
| Lead | relation | → 👥 Leads y clientes |
| Fecha | date | |
| Tipo | select | Descubrimiento · Cierre · Seguimiento · Sesión de entrega |
| Resultado | select | Cerró · Siguiente paso con fecha · Lo pienso · Perdida · No calificaba |
| Objeción principal | text | |
| Escala 1-10 | number | |
| Aprendizaje | text | |
| Transcript | text o url | |

**4. 🎬 Contenido**

| Propiedad | Tipo | Valores |
|---|---|---|
| Pieza | title | |
| Formato | select | Reel · Carrusel · Post · Historia · Video largo · Email · Otro |
| Gancho | text | |
| Dolor que toca | text | |
| Estado | select | Idea · Guion · Producción · Publicada · Descartada |
| Publicada | date | |
| Métrica principal | number | |
| Conversaciones generadas | number | |
| Veredicto | select | Repetir · Ajustar · Matar |

**5. 🔁 Aprendizajes**

| Propiedad | Tipo | Valores |
|---|---|---|
| Aprendizaje | title | |
| Área que corrige | select | Foundations · Oferta · Avatar · Contenido · Captura · Ventas · Entrega · Success |
| Fuente | select | Cliente · Llamada · Pieza · Entrega · Decisión |
| Qué cambia | text | |
| Estado | select | Pendiente · Aplicado · Descartado |
| Fecha | date | |

La alimentan todas las skills. La procesa `pb-success`.

**6. ⚖️ Decisiones**

| Propiedad | Tipo | Valores |
|---|---|---|
| Decisión | title | |
| Tipo de leverage | multi-select | Operativo · Financiero · Capital humano · Relacional · Temporal |
| Veredicto 8 criterios | select | Avanza · Ajustar · No ahora |
| Fecha | date | |
| Resultado | text | |

La usa `pb-foundations`.

## Quién escribe dónde

| Skill | Escribe en |
|---|---|
| pb-os | Hub, Documento de contexto (creación), 8 páginas (esqueleto), Tablero de áreas (las 8 filas + `Cuello`) |
| pb-foundations | 01 · Foundations, Documento de contexto (mantenimiento), ⚖️ Decisiones |
| pb-oferta | 02 · Oferta · en 👥 Leads y clientes solo `Notas` (link al pitch) |
| pb-avatar | 03 · Avatar · en 👥 Leads y clientes `Fit avatar` y una línea en `Notas`; `Etapa` = No es para mí solo si el dueño lo confirma |
| pb-contenido | 04 · Contenido, 🎬 Contenido |
| pb-captura | 05 · Captura, 👥 Leads y clientes · en 🎬 Contenido crea filas `Idea` y suma 1 a `Conversaciones generadas` de la pieza que trajo al lead |
| pb-ventas | 06 · Ventas, 📞 Llamadas, `Etapa` / `Próximo paso` / `Valor` en 👥 Leads y clientes |
| pb-entrega | 07 · Entrega, 📞 Llamadas (Tipo = Sesión de entrega) |
| pb-success | 08 · Success, 🔁 Aprendizajes (procesa), 🧭 Tablero de áreas (`Cuello`, `Próxima acción`, `Revisado`), `Etapa` = Renovó |

Todas pueden **agregar** filas a 🔁 Aprendizajes y actualizar su propia fila del
🧭 Tablero de áreas (`Puntaje`, `Estado`, `Pieza que falta`, `Próxima acción`,
`Revisado`). **`Cuello` solo lo mueven `pb-os` y `pb-success`**, mirando las 8 juntas.

## Convenciones compartidas

- **Puntaje → Estado:** 1–2 = Rota · 3 = En obra · 4 = Funciona. Igual en las 9.
- **📞 Llamadas con `Tipo` = Sesión de entrega** (las escribe `pb-entrega`, las lee
  `pb-success` para medir adherencia): `Escala 1-10` = cuánto ejecutó el cliente lo de la
  semana (1 no lo tocó · 10 completo) · `Objeción principal` = bloqueo principal de la
  sesión · `Resultado` = Siguiente paso con fecha. Compromisos de cada lado y próxima
  sesión van en el cuerpo de la página.
- **Ningún lead sin `Próximo paso` con fecha**, ni siquiera los cerrados o perdidos: el
  filtro de vencidos de la revisión semanal depende de eso.
