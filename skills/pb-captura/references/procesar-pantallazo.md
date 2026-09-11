# Procesar un pantallazo — extraer una vez, despachar a donde toca

Un solo pantallazo de una conversación trae, a la vez: un cambio de estado de un lead,
materia prima de contenido y a veces un ángulo de venta. Si se procesa en tres lugares
distintos, se pierde en dos. Aquí se lee **una vez** y sale convertido en lo que cada
área necesita.

**Mandato: depositar, no desarrollar.** Esta skill deja la ficha y las notas. El guion
de la pieza lo hace `pb-contenido`; la respuesta a la objeción en llamada, `pb-ventas`.

## Paso 1 — La ficha de extracción

| Campo | Qué capturar |
|---|---|
| **Quién** | Nombre o usuario. Si no aparece, dilo explícito |
| **Qué tipo** | Lead nuevo · lead conocido · cliente activo · network · otro |
| **Superficie** | Instagram · WhatsApp · LinkedIn · email · otra |
| **Frases textuales** | 2 a 4 citas **literales**. No las parafrasees: son la materia prima |
| **Señal comercial** | Dolor, objeción, etapa del negocio, plazo, quién decide |
| **Fecha del material** | Si es visible |

**No inventes.** Si un campo no está en el material, queda vacío. Un dato inventado en
👥 es peor que un campo vacío, porque alguien va a decidir con él.

## Paso 2 — Ficha en 👥 Leads y clientes

Busca primero por nombre y por usuario. **Existe** → propone el cambio campo por campo
y por qué. **No existe** → propone la ficha completa.

| Propiedad | Cómo se llena |
|---|---|
| `Nombre` | Nombre visible; si solo hay usuario, el usuario |
| `Etapa` | Nuevo (primer contacto) · Conversación (hay intercambio) · Llamada agendada · Propuesta · Cliente activo · Perdido · Renovó · No es para mí |
| `Canal de origen` | **Qué lo trajo**, no la app: Contenido · Anuncios · Referido · Outbound · Otro. Un DM de Instagram puede venir de un referido |
| `Pieza de origen` | La pieza que lo trajo si la nombra ("vi tu reel de…") o se deduce. Si no, vacío |
| `Fit avatar` | Alto · Medio · Bajo, contra 03 · Avatar. Si no hay avatar escrito, márcalo como hipótesis en `Notas` |
| `Dolor` | Con **sus palabras**, entre comillas. No tu diagnóstico |
| `Objeción` | Solo si la dijo. Textual |
| `Próximo paso` | Verbo + qué: "Hacerle T2: qué probó antes", "Confirmar jueves 16:00" |
| `Fecha próximo paso` | Siempre. Sin fecha, la ficha no se guarda |
| `Notas` | Superficie · capas validadas y la que falta · fecha del material |

### Las 4 capas sobre el texto

| Capa | Validada si… | Si falta, el próximo paso es… |
|---|---|---|
| 01 · Es el dueño | Dice "mi negocio", "decido yo", o nombra a quien decide y lo trae | Preguntar quién más participa de la decisión |
| 02 · Dolor visible | **Él** lo nombró, no lo dedujiste tú | Una pregunta de situación (T1) |
| 03 · Acepta un diagnóstico | Respondió que sí a revisar su caso | Ofrecer el diagnóstico con dos bloques de horario |
| 04 · Entrega 3 datos | Etapa, dolor principal y qué probó antes están en el chat | Pedir el que falta, uno, antes de dar la hora |

La capa que falta **define el próximo paso**. Si están las cuatro: llamada con fecha.

### Etapas terminales también llevan próximo paso

- `No es para mí` → Próximo paso "Cerrar con un no cálido" + fecha; una vez enviado,
  "Cerrado — <motivo en 3 palabras>" y la fecha del cierre.
- `Perdido` → recontacto con fecha **y motivo** si la puerta queda abierta; si no,
  "Cerrado — <motivo>" + fecha.

Así ninguna fila queda sin próximo paso, y el filtro de vencidos no se ensucia.

## Paso 3 — Las salidas (solo las que aplican)

No fuerces las tres. "Esta salida no aplica" es una respuesta válida.

**A · Contenido** (si hay una frase que duele, una creencia equivocada, un patrón que
se repite o una cifra real). Fila en 🎬 Contenido:
- `Pieza`: el ángulo, no el tema ("Por qué contestar rápido vale más que contestar bien").
- `Dolor que toca`: la frase textual, **sin el nombre de la persona**.
- `Estado`: Idea.
Un material puede sostener varias piezas para públicos distintos: propón todas las que
sostenga sin forzar. Nunca expongas a una persona identificable; el contenido usa el
patrón, no el caso.

**B · Ventas** (si hay objeción, propuesta en juego o llamada agendada). Deja la
objeción textual en `Objeción` y el handoff a `pb-ventas`: qué dijo, qué hay debajo
(una línea) y en qué capa quedó.

**C · Aprendizaje** (si el material muestra algo que corrige otra área: el avatar no
calza, la oferta no se entiende, una pieza trae gente equivocada). Fila en
🔁 Aprendizajes con `Área que corrige`, `Fuente` (Cliente o Pieza), `Qué cambia` en una
línea y `Estado` Pendiente.

## Paso 4 — Salida y confirmación

```
📥 <Quién> — <tipo> · <superficie> · <fecha>

Textual: "<cita 1>" · "<cita 2>"
Señal: <una línea>
Capas: 01 ✅ · 02 ✅ · 03 ⚠️ · 04 ❌ (falta qué probó antes)

👥 Ficha (<Nueva | Actualiza: campos>)
Etapa: … · Canal de origen: … · Pieza de origen: … · Fit avatar: …
Dolor: "…" · Objeción: …
Próximo paso: … · Fecha: …

🎬 Contenido: <ángulo> · Dolor que toca: "<frase sin nombre>"
📞 Para pb-ventas: <objeción y capa>
🔁 Aprendizaje: <área que corrige> — <qué cambia>

¿Lo escribo? (ficha / contenido / todo / nada)
```

Omite las salidas que no aplican; no escribas "N/A". Si el cliente dijo "aplica
directo", escribe sin preguntar y muestra lo escrito.

**Borrador de respuesta:** solo si lo pide. Se redacta con
`setting-y-seguimiento.md` y lo manda él.

## Ejemplo — procesado mal vs procesado bien

Material: una dueña de un estudio de pilates escribe por Instagram: *"Vi tu video de la
agenda vacía. Me pasa igual: tengo 40 alumnas pero los martes y jueves quedan clases
con 3 personas. Probé con promociones y no funcionó. ¿Tú haces asesorías?"*

**Mal:**
> Lead interesada en asesoría. Tiene problemas de agenda. Responder.

Sin fecha, sin fuente, sin sus palabras, dolor parafraseado, y "responder" no es un paso.

**Bien:**
> 👥 Nueva · Etapa: Conversación · Canal de origen: Contenido · Pieza de origen: video
> "agenda vacía" · Fit avatar: Alto
> Dolor: "los martes y jueves quedan clases con 3 personas"
> Capas: 01 ⚠️ (dueña, confirmar si decide sola) · 02 ✅ · 03 ⚠️ (preguntó por asesorías,
> no aceptó diagnóstico) · 04 ✅ (etapa, dolor y "probé con promociones")
> Próximo paso: responder hoy, ofrecer diagnóstico con dos bloques · hoy 15:00
> 🎬 Idea: "Por qué las promociones no llenan los días flojos" · Dolor que toca:
> "probé con promociones y no funcionó"
> 🎬 En la pieza "agenda vacía": Conversaciones generadas +1

La ficha dice qué sigue y cuándo, guarda sus palabras y le devuelve a Contenido cuál
pieza está trayendo conversaciones.
