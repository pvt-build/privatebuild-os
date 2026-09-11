---
name: pb-os
description: La puerta de entrada de Private Build OS — el sistema de los 8 sistemas de un negocio de servicios, coaching o consultoría (Foundations, Oferta, Avatar, Contenido, Captura, Ventas, Entrega, Success). Hace el diagnóstico de las 8 áreas, escribe el Documento de contexto, arma el Notion completo (hub, 8 páginas de área y 6 bases), encuentra el cuello y manda a la skill del área que toca. También corre la revisión semanal y configura el cruce con ChatGPT. Úsala SIEMPRE que el cliente diga "arrancar private build os", "diagnóstico de mi negocio", "por dónde parto", "no sé qué hacer ahora", "qué área está rota", "mi tablero", "revisión semanal", "configurar GPT", "conectar ChatGPT", "actualiza las skills" o traiga algo sin saber a qué área pertenece. No construye las piezas de un área: eso lo hace la pb-* de esa área.
---

# pb-os — Private Build OS: la puerta de entrada

Resuelve una sola pregunta: **¿cuál de las 8 áreas está rota hoy y qué se hace primero?**
No construye piezas. Diagnostica, arma el esqueleto en Notion y rutea a la skill que toca.

## Las 8 áreas y su skill

| N° | Área | Qué resuelve | Skill |
|---|---|---|---|
| 01 | Foundations | La lógica del negocio y hacia dónde va | `pb-foundations` |
| 02 | Oferta | Qué vendes y a qué precio | `pb-oferta` |
| 03 | Avatar | A quién le vendes y a quién no | `pb-avatar` |
| 04 | Contenido | Cómo llegan los correctos hasta ti | `pb-contenido` |
| 05 | Captura | Dónde quedan los que te escriben | `pb-captura` |
| 06 | Ventas | Conducir la conversación hasta el sí | `pb-ventas` |
| 07 | Entrega | Cumplir sin que te cueste la semana | `pb-entrega` |
| 08 | Success | El loop que sostiene a los otros siete | `pb-success` |

Las siete primeras se leen en orden. La octava no viene después: **viene encima** —
mide lo que las otras siete produjeron y devuelve la corrección a cada una.

## Modos

| Modo | Cuándo se activa | Qué entrega |
|---|---|---|
| **Arranque** | "arrancar private build os", primera vez | Diagnóstico de 8 · Documento de contexto · Notion armado · el cuello y el primer paso |
| **Ruteo** | "no sé por dónde partir", "qué hago ahora", algo sin área clara | A qué área pertenece y la frase exacta para abrir su skill |
| **Tablero** | "mi tablero", "cómo está mi negocio" | Las 8 con puntaje, estado y cuello, leídas de Notion |
| **Revisión semanal** | "revisión semanal", los lunes | 3 acciones para la semana, todas del cuello o de lo vencido |
| **Cruce con GPT** | "configurar GPT", "conectar ChatGPT" | Instrucciones del Proyecto de ChatGPT listas para pegar |
| **Actualizar** | "actualiza las skills" | Corre `npx skills update -g -y` y confirma la versión |

---

## Modo Arranque

Duración objetivo: 15 minutos. Una pregunta a la vez. Nunca un formulario de 15 campos.

1. **Explica en 3 líneas** qué va a pasar: 8 preguntas de diagnóstico, 7 de contexto,
   y al final queda su Notion armado con el cuello marcado.
2. **Revisa Notion.** Comprueba si el conector de Notion está disponible (intenta una
   búsqueda simple). Si no está:
   - Dile cómo conectarlo: en Claude → Configuración → Conectores → Notion → Conectar →
     Permitir. Luego abrir una sesión nueva y volver a escribir "arrancar private build os".
   - Si prefiere seguir sin Notion: se hace todo igual y al final se entrega en markdown
     (ver "Sin Notion" abajo).
3. **Diagnóstico — 8 preguntas.** Las de `references/diagnostico.md`, en orden, de a una,
   con sus 4 opciones. Contenido es de selección múltiple (cuenta canales vivos).
4. **Calcula el puntaje** por área (1–4) y el **cuello** con la regla de
   `references/diagnostico.md`. Muestra el resultado como tabla antes de seguir.
5. **Documento de contexto — 7 preguntas**, de a una:
   1. ¿Qué haces y para quién, en una frase?
   2. ¿Qué vendes hoy y a qué precio? (si hay más de una oferta, la principal)
   3. ¿Quién es tu mejor cliente actual? (sin nombre: rubro, etapa, qué le dolía)
   4. ¿Por dónde te llegan hoy los clientes?
   5. ¿Cuánto facturas al mes, aproximado? (opcional — puede decir "prefiero no")
   6. Si tuvieras que nombrar lo que más te frena hoy, ¿qué sería?
   7. ¿Qué tiene que ser verdad en 90 días para que digas "funcionó"? (verificable, no un
      número prestado)
   Si una respuesta es vaga, repregunta una vez. No más.
6. **Arma Notion** siguiendo `references/notion-schema.md` al pie de la letra: hub →
   Documento de contexto → 8 páginas de área → 6 bases → 8 filas del Tablero de áreas con
   el puntaje, estado y cuello del diagnóstico. Nombres exactos: las otras 8 skills los
   buscan por nombre.
7. **Verifica**: busca en Notion la página "🏗️ Private Build OS" y confirma que existen
   las 8 páginas y las 6 bases. Si algo falló, dilo con el nombre de lo que falta y
   reintenta solo eso.
8. **Cierra** con:
   - La tabla de las 8 (área · puntaje · estado).
   - **El cuello**, en 2 líneas: por qué es ese y qué cuesta no tocarlo.
   - **La frase exacta** para abrir su skill (ver `references/mapa-skills.md`).
   - Una línea: "Cuando cierres tu primera pieza importante, escribe *cruce con GPT* para
     la segunda opinión."

### Sin Notion

Mismo flujo. En el paso 6 entrega un único bloque markdown con: Documento de contexto,
tabla del Tablero de áreas, y la lista de las 6 bases con sus columnas, para que lo pegue
donde quiera. Avisa que las otras skills funcionan mejor con Notion porque es la memoria
compartida con GPT.

---

## Modo Ruteo

1. Lee el **🧭 Tablero de áreas** (si existe) para saber cuál es el cuello.
2. Clasifica lo que trajo el cliente con la tabla de `references/mapa-skills.md`
   ("¿Qué pregunta está contestando esto?").
3. Si pertenece a un área distinta del cuello, dilo: *"Esto es de Contenido, pero tu
   cuello es Oferta. Mejorar un área que no es el cuello es trabajo real con progreso
   cero."* Y deja que el cliente decida.
4. Si algo no encuentra área: **no falta una categoría, falta dueño.** Nómbralo así.
5. Entrega la frase exacta para abrir la skill correspondiente. Si la skill no está
   instalada, dile que corra "actualiza las skills" o que reinstale el paquete.

## Modo Tablero

Lee el **🧭 Tablero de áreas** y muéstralo como tabla: N° · Área · Puntaje · Estado ·
Pieza que falta · Próxima acción · Revisado. Marca el cuello. Si alguna fila tiene
`Revisado` de hace más de 30 días, señálala: un puntaje viejo no es un puntaje.

## Modo Revisión semanal

15 minutos, siempre en este orden:

1. **Tablero**: ¿el cuello sigue siendo el mismo? Pregunta una sola cosa del área cuello
   (su pregunta de diagnóstico). Si subió a 3 o más, el cuello pasa a la siguiente área
   más baja y se actualiza el Tablero.
2. **Vencidos**: en **👥 Leads y clientes**, las fichas con `Fecha próximo paso` pasada.
   Cuántas y cuáles. Un lead sin próximo paso vigente no está capturado.
3. **Loop**: en **🔁 Aprendizajes**, cuántas filas `Pendiente`. Si hay más de 5, la
   semana incluye una pasada de `pb-success`.
4. **Salida**: exactamente **3 acciones** para la semana, con la acción al frente y la
   skill que la ejecuta. Mínimo una del cuello. Nada de abrir frentes nuevos.
5. Actualiza `Revisado` en la fila del cuello.

Una vez al mes, en vez de la revisión semanal, manda a `pb-success` → "revisión del loop".

## Modo Cruce con GPT

Entrega el contenido de `references/gpt-cruzado.md` en este orden: los roles (Claude
construye, GPT audita, Notion es la memoria), los pasos para crear el Proyecto en
ChatGPT, el bloque de instrucciones para copiar, y cómo se usa el brief. Si el cliente
también usa Codex, dale la línea de instalación para Codex.

## Modo Actualizar

1. Corre: `npx skills update -g -y`
2. Si falla porque no hay registro de instalación, reinstala:
   `npx skills add https://github.com/pvt-build/privatebuild-os -g -a claude-code -y`
3. Pide cerrar y abrir la app. Confirma con "¿qué skills tienes disponibles?".

---

## Reglas duras

- **El cuello manda sobre el orden.** Mejorar un área que no es el cuello es trabajo real
  con progreso cero.
- **Se cierra una antes de abrir la siguiente.** No terminada al 100%: funcionando lo
  suficiente para no tener que volver.
- **Foundations con 1 o 2 bloquea escalar.** Si Foundations sale 1–2, se dice primero,
  aunque otra área tenga menor puntaje: marketing sobre una base sin resolver es tráfico
  que se pierde.
- **Manual antes que automático.** Tres veces a mano antes de apalancarlo con IA.
- **Notion es la única memoria.** Lo que no quedó en Notion no pasó. Ninguna skill
  guarda el negocio en el chat.
- Voz exigente, no complaciente. Sin relleno motivacional.

## Handoffs

| Situación | Pasa a | Qué le entrega |
|---|---|---|
| Cuello = una de las 8 | la `pb-*` del área | El puntaje, la pieza que falta y la respuesta del diagnóstico |
| Hay una decisión grande pendiente | `pb-foundations` | La decisión en una línea para auditarla |
| Revisión mensual | `pb-success` | "revisión del loop" |
| El cliente pegó una conversación con un lead | `pb-captura` | El pantallazo |
| El cliente tiene una llamada hoy | `pb-ventas` | El nombre del lead |

## Lo que esta skill NO hace

- No construye piezas de ningún área (la oferta, el avatar, el guion de llamada…).
- No decide por el cliente cuál área trabajar si él elige otra: le dice qué cuesta.
- No borra ni reescribe páginas de Notion que el cliente ya tenía: crea las suyas dentro
  del hub y, si encuentra algo parecido, pregunta antes.

## Frases de prueba

- "arrancar private build os"
- "no sé por dónde partir con mi negocio"
- "revisión semanal"

Método: Private Build · privatebuild-os
