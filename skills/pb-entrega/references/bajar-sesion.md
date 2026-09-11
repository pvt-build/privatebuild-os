# Bajar una sesión — protocolo completo

De una sesión de entrega grabada (o anotada) a una fila en **📞 Llamadas** con `Tipo` =
Sesión de entrega, sin que se pierda nada y sin inventar nada.

Por qué importa: los cuatro medidores de `pb-success` (adherencia, primer resultado, tu deuda,
autonomía) se leen de estas filas. Si la sesión no se baja, no existe para el sistema.

---

## 1. Reconocer la fuente y separar las piezas

| Fuente | Cómo se reconoce | Qué suele traer | Qué suele faltar |
|---|---|---|---|
| Fathom | Link `fathom.video/...`, líneas `[MM:SS] Nombre:`, bloque de próximos pasos | Resumen IA, acciones, transcript, link | El correo de resumen no trae el transcript; el link compartido puede pedir inicio de sesión |
| Zoom | Archivo `.vtt` o `.txt`, marcas `00:12:34 --> ...` | Transcript con hablantes | Resumen y acciones (si no usa el asistente) |
| Google Meet | Documento "Notas" o "Transcripción" en Drive | Resumen y transcript | Acciones separadas por dueño |
| Otra grabadora (Otter, tl;dv, etc.) | Formato propio con timestamps | Transcript y resumen | Varía |
| Notas a mano / audio | Texto libre o nota de voz | Lo que el dueño recuerda | Transcript, citas textuales |

Separa en cinco piezas antes de escribir nada:
1. **Link** de la grabación (si existe).
2. **Resumen** — contexto, temas, decisiones.
3. **Acciones** — separadas por dueño: cliente / tú. Si no vienen marcadas, infiere por el verbo
   ("te mando…" = tú; "voy a publicar…" = cliente) y confírmalo.
4. **Números** revisados en la sesión (ventas, conversaciones, publicaciones, lo que sea).
5. **Transcript** — intacto.

Si una pieza no viene, se marca como faltante. No se rellena. Si hace falta una cita textual y
solo hay resumen, se pide el transcript pegado; nunca se escribe una "cita" reconstruida.

---

## 2. Ubicar al cliente y no duplicar

1. Busca al cliente en **👥 Leads y clientes**. Debe estar en `Etapa` = Cliente activo. Si no
   existe, avisa y no crees una ficha a medias (eso es de `pb-ventas`).
2. Busca en **📞 Llamadas** si la sesión ya se cargó: mismo link en `Transcript`, o mismo `Lead`
   y misma `Fecha` con `Tipo` = Sesión de entrega.
3. Si existe → **actualiza esa fila**. Si no → crea una. Nunca dos filas para la misma sesión.
4. Si no hay link, usa el título "<Cliente> — Sesión N — DD/MM" como clave y déjalo anotado.

---

## 3. Confirmar los hechos de negocio antes de escribirlos

Una suposición marcada como hecho es peor que un campo vacío: el cliente puede tomar decisiones
sobre información falsa, y tú puedes renovar o no sobre ella.

1. Extrae toda afirmación con implicancia de negocio que **no sea literal** del texto pegado:
   un cierre, una pérdida, un monto, una decisión, quién es quién.
2. Preséntalas con letras, una por línea, sin diluir:
   - A) "Cerró el cliente que estaba negociando, con pago en dos cuotas." ¿Correcto?
   - B) "Perdió la otra venta por precio, según lo que contó." ¿Lo doy por bueno?
3. Espera sí / no / corrección antes de escribir esos datos como definitivos.
4. Lo que quede sin confirmar se escribe igual, marcado: **"reportado por el cliente, sin verificar"**.

No aplica a lo que es literalmente el texto pegado; aplica a toda interpretación encima.

---

## 4. Mapeo pieza → campo en 📞 Llamadas

| Pieza | Propiedad | Qué va |
|---|---|---|
| Cliente | `Lead` | Relación a su ficha en 👥 Leads y clientes |
| — | `Llamada` (título) | "<Cliente> — Sesión N — DD/MM" |
| Fecha real de la sesión | `Fecha` | La fecha en que ocurrió, no la de hoy |
| — | `Tipo` | Sesión de entrega |
| Próxima sesión y entregable con fecha | `Resultado` | Siguiente paso con fecha (si ambos quedaron con fecha; si no, se exige) |
| Lo que frenó al cliente | `Objeción principal` | En una sesión de entrega se lee como **bloqueo principal**, en una frase |
| Ejecución del entregable de la semana | `Escala 1-10` | 1 = no lo tocó · 5 = la mitad · 10 = completo. Es el dato de adherencia |
| Hallazgo de la sesión | `Aprendizaje` | Lo que esta sesión enseñó (una línea). Si se repite en otro cliente → 🔁 |
| Link o texto | `Transcript` | El link de la grabación, o el texto si no hay link |

Todo lo demás va en el **cuerpo de la página** de la fila, con esta plantilla:

```
[Ver grabación](<link>) · <min> min · <DD/MM/AAAA>

## Resumen
<3-5 líneas: qué se trabajó, decisión clave, siguiente paso>

## Entregable de la semana
<Sí / No> — <cuál era>. <Si no: qué lo frenó.>

## Resultado del período
<número y fecha> — o "sin resultado todavía". Confirmado / reportado sin verificar.

## Bloqueo
<el bloqueo principal> · <Detectado / En trabajo / Resuelto>

## Compromisos del cliente
- [ ] <qué> — <fecha>

## Compromisos míos
- [ ] <qué> — prometido <fecha> — entrega <fecha>

## Entre sesiones
<lo que llegó por chat desde la sesión anterior y es entrega real: feedback, casos, audios>

## Próxima sesión
<fecha> — foco: <una frase>

## Números revisados
<crudos, con contexto>

## Transcript
<verbatim o enlace a subpágina si es largo>
```

Si el transcript es largo, va en una subpágina "Transcript — <Cliente> Sesión N". Si lo
comprimes para leerlo sin la grabación: une las líneas seguidas del mismo hablante, quita
saludos y relleno, divide por tema con `## [MM:SS] Tema`, y cierra con "Momentos clave para la
próxima sesión". La sustancia no se toca.

---

## 5. Actualizar lo que depende de la sesión

- **Ficha del cliente** (👥 Leads y clientes): `Próximo paso` (el entregable de la semana) y
  `Fecha próximo paso` (la próxima sesión). No se toca `Etapa`.
- **Roadmap del cliente** (subpágina de 07 · Entrega): acciones nuevas, estado de la fase
  (solo con datos confirmados), compromisos tuyos abiertos.
- **Mensaje al cliente** (borrador, no se envía solo): sus compromisos de esta sesión y el
  enlace al roadmap. Nunca tus notas internas.

---

## 6. Mínimos de cierre — no se cierra con huecos

Antes de dar la sesión por bajada, estos no pueden quedar vacíos:
- `Lead`, `Fecha`, `Tipo`
- Entregable de la semana: sí / no
- Compromisos del cliente con fecha
- Compromisos tuyos con fecha (o "ninguno")
- Próxima sesión con fecha

Si falta alguno: "Antes de dar esto por bajado me faltan: X, Y. Dámelos." Sin suavizar y sin
rellenar con un valor "seguro".

---

## 7. Cruzar contra la cartera → 🔁 Aprendizajes

Una sesión sola se resume; la cartera se cruza. Después de bajar, revisa las últimas sesiones de
**los otros clientes activos** en 📞 Llamadas y busca:

| Qué se repite | En cuántos clientes | Qué se hace |
|---|---|---|
| El mismo bloqueo | 2+ | Fila en 🔁 Aprendizajes. `Área que corrige`: la que produce ese bloqueo (Entrega si es el entregable, Oferta si se prometió mal, Avatar si no era para ti) |
| La misma duda o explicación | 2+ | Fila en 🔁 Aprendizajes + candidato a recurso (modo De repetido a proceso) |
| La misma duda o explicación | 3 veces, en total | Se convierte en SOP o recurso ya |
| El mismo punto del onboarding que falla | 2+ | Fila en 🔁 Aprendizajes, `Área que corrige`: Entrega |
| Un compromiso tuyo con más de 7 días | cualquiera | Se nombra primero en la próxima sesión; se avisa a `pb-success` |

Formato de la fila: `Aprendizaje` (una frase), `Área que corrige`, `Fuente` = Entrega,
`Qué cambia` (la corrección concreta), `Estado` = Pendiente, `Fecha` = hoy.

---

## 8. El chat entre sesiones

El canal no cambia qué es: si el chat trae un caso real (una cotización para revisar, una
objeción en audio, una pieza para corregir), es entrega asíncrona.
- Se suma a la sección "Entre sesiones" de la sesión más cercana. No abre fila nueva ni suma al
  número de sesión.
- Adjuntos: se guardan el mismo día en la carpeta del cliente, con nombre
  `AAAA-MM-DD_nombre-original_quien-envía` (fecha real del mensaje).
- Un audio que no se puede transcribir en el momento se guarda igual y se anota "pendiente de
  transcribir". No desaparece.
- Coordinación de horarios y saludos no se bajan: son ruido.

---

## Antes de la sesión — preparación de 5 minutos

Cuando el dueño dice "prepárame para la sesión con X". Formato fijo: listas cortas, se lee en
5 minutos, no se argumenta.
1. **Compromisos abiertos** — de cada lado, con fecha y días de atraso.
2. **Lo que quedó pendiente** de la sesión anterior.
3. **Lo que llegó por chat** desde entonces y el cliente no sabe que quedó registrado.
4. **El cuello vigente** — uno, no el historial.
5. **1-2 preguntas para abrir** — desde el punto 3 o directo al cuello.

Cierre obligatorio: si hay un compromiso tuyo vencido, la sesión abre con él, dicho por ti.
