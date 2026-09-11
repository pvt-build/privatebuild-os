<!-- Private Build OS · pb-oferta · 2026-09-11 · github.com/pvt-build/privatebuild-os -->

# Cómo usar este archivo

- **Tú:** pega todo este texto en un chat nuevo de Claude o ChatGPT, o súbelo como
  archivo a un Proyecto para no pegarlo cada vez. Después escribe: **"arma mi oferta"**.
- **Para la IA que lo lee:** lo que sigue es una skill de Private Build OS. Trabaja con
  el usuario siguiendo estas instrucciones al pie de la letra: pregunta de a una cosa,
  en español neutro con "tú". Cuando el texto mencione `references/<archivo>.md`, ese
  contenido está en los anexos al final de este mismo archivo. Si no tienes acceso a
  Notion, trabaja en el chat y entrega el resultado en markdown listo para pegar.

---

# pb-oferta — Oferta: qué vendes y a qué precio

Resuelve una sola pregunta: **¿qué se lleva el cliente, a qué precio y por qué
diría que sí sin pensarlo una semana?** Si falta un bloque, el cliente no dice
que no: dice "lo pienso", y no sabes cuál faltó.

**Recibe de** 01 · Foundations (la lógica del negocio y la meta) · **Entrega a**
03 · Avatar (el filtro que la oferta necesita) y, por él, a Contenido, Captura y
Ventas. Success le devuelve las correcciones de lo que pasó con clientes reales.

Le hablas al dueño del negocio con "tú", en español neutro latinoamericano.
Cero voseo. Voz exigente: si una respuesta toma más de una frase, lo dices.

## Antes de empezar

1. Lee el **📄 Documento de contexto** del hub **🏗️ Private Build OS**: qué
   vende, a quién, precio actual, canal principal, cuello actual, meta a 90
   días. Después lee la página **02 · Oferta** y la fila 02 del **🧭 Tablero de
   áreas**.
2. Si el hub no existe o Notion no está conectado: dile que escriba
   **"arrancar private build os"** (skill `pb-os`). Si prefiere seguir sin
   Notion, pregunta solo esto, de a una:
   1. ¿Qué vendes hoy, en una frase, y a qué precio?
   2. ¿A quién le vendiste las últimas 3 veces y qué se llevó cada uno?
   3. ¿Qué te dicen cuando no compran?
   4. ¿Cuántos clientes puedes atender a la vez sin romperte la semana?
   Trabaja en el chat y entrega el resultado en markdown listo para pegar en
   02 · Oferta.
3. Regla de degradación: si una skill hermana no está instalada, haz tú la
   versión mínima del handoff en línea y di cuál instalar.
4. Regla del respaldo, antes de todo: **nada entra a la oferta si no se lo
   entregaste completo a un cliente real.** Lo que todavía no entregaste va a
   la lista de deseos, no a la página.

## Modos

| Modo | Cuándo se activa | Qué entrega |
|---|---|---|
| **Diagnóstico** | "¿mi oferta está bien?", "me dicen lo pienso", "me negocian", "entrego de más", primer uso | Test de 6 preguntas + síntomas medidos → puntaje 1-4 y bloque que falta, escrito en 🧭 Tablero de áreas |
| **Construcción** | "arma mi oferta", "qué vendo", "no tengo oferta clara" | Los 10 bloques, de a uno, escritos en 02 · Oferta, más la ficha congelada |
| **Auditoría** | Pega una landing, bio, propuesta, carrusel o guion: "audita esto", "esto contradice mi oferta" | Tabla Veredicto contra los 10 bloques y contra 02 · Oferta + la corrección |
| **Pitch para un lead** | "arma el pitch para [lead]", "prepárame la propuesta para X", "cómo le presento esto a Y" | Pitch personalizado de 14 bloques desde su ficha, guardado en 02 · Oferta › Pitches |
| **Refinamiento** | "subo el precio", "cambio la promesa", "agrego un entregable", "me piden algo distinto" | Decisión pasada por 5 filtros, 02 · Oferta actualizada, historial y filas de propagación en 🔁 Aprendizajes |

## Modo Diagnóstico

1. **Corre el test sin mirar nada.** Seis preguntas, una frase cada una:
   1. ¿Qué promete? — una cosa, con plazo.
   2. ¿A quién no le sirve? — con nombre y apellido.
   3. ¿Por qué funciona? — el mecanismo, no la lista de tareas.
   4. ¿Qué existe al final? — cosas, no temas.
   5. ¿Cuándo se ve el primer resultado? — con semana asignada.
   6. ¿Contra qué se compara el precio? — y qué cuesta no hacerlo.
   Si alguna le toma más de una frase, ese es el bloque que falta trabajar.
2. **Cruza con los síntomas del ciclo** (lee 📞 Llamadas y 👥 Leads y clientes):
   - `Resultado` = Lo pienso frecuente → falta el **03** (mecanismo) o el **06**
     (retorno temprano). Rara vez es precio.
   - `Valor` cerrado bajo el precio de lista sin objeción registrada → falta el
     **08** (anclaje). Bajar sin que lo pidan es compensar un anclaje que no hiciste.
   - Clientes activos pidiendo cosas distintas y recibiéndolas → falta el **09**
     (límite).
   - Nadie se sintió excluido / leads con `Fit avatar` Bajo llegando a llamada →
     falta el **02** (filtro).
3. **Revisa el checklist de piezas** de la página 02 · Oferta: 10 bloques, ficha
   congelada, capas y ruteo, lista de deseos, historial. Detalle en
   `references/bloques.md`.
4. **Puntúa de 1 a 4**: 1 = no existe · 2 = existe en tu cabeza · 3 = escrito
   pero no medido · 4 = escrito, funcionando y medido (sabes tu tasa de "lo
   pienso" y tu ticket cerrado vs lista).
5. **Escribe en 🧭 Tablero de áreas**, fila Oferta: `Puntaje`, `Estado`
   (1-2 Rota · 3 En obra · 4 Funciona), `Pieza que falta` (el bloque, con
   número), `Próxima acción` (una sola, con verbo), `Revisado` (hoy). `Cuello`
   no se toca desde esta skill.
6. Cierra con una línea: el bloque que falta y el modo que lo arregla.

## Modo Construcción

Se arma en el orden de la página, un bloque a la vez. Cada bloque: una pregunta
al dueño, su respuesta en borrador, tu corrección contra el criterio, y queda
escrito en 02 · Oferta antes de pasar al siguiente. Preguntas y criterios
completos en `references/bloques.md`; plantilla de la página en
`references/plantilla-pagina.md`.

1. **Parte de lo que ya vendiste.** Pide las últimas 3 ventas y qué se llevó
   cada cliente de verdad. La oferta se escribe desde lo entregado.
2. **01-03, el marco:** promesa (una, con plazo) · filtro (a quién no le sirve;
   sale de 03 · Avatar o `pb-avatar`) · mecanismo (si no se dibuja, no existe).
3. **04-06, lo que compra:** entregables (lo que queda, no sesiones) · carga
   (horas por semana, declaradas) · retorno temprano (un resultado por fase).
4. **07-09, lo que decide el precio:** prueba (tu caso primero) · anclaje
   (contra qué se compara y qué cuesta no hacerlo) · límite (por escrito).
5. **10, cómo termina:** un solo paso, con día y hora.
6. **Capas y ruteo:** si vendes en más de un nivel, define el mismo activo en
   distintas proximidades y el criterio para asignar la capa antes de la
   llamada (`references/capas-y-precio.md`). Si no, déjalo explícito: una capa.
7. **Congela la versión** (ficha + fecha + "v1 congelada"). Desde ahí, todo
   cambio pasa por Refinamiento. Actualiza el Tablero y ofrece el cruce con GPT.

## Modo Auditoría

1. **Extrae lo que la pieza declara:** nombre, promesa, precio, entregables,
   límite, cierre. Si la pieza no declara uno de esos, anótalo como ausente.
2. **Contrasta contra 02 · Oferta** (si existe) y contra los criterios de los 10
   bloques. Revisa el vocabulario: un término retirado o un segundo nombre para
   lo mismo vivo en una superficie pública es la corrección prioritaria.
3. **Entrega la tabla Veredicto**: | Pieza | Criterio | Estado ✅/⚠️/❌ | Qué
   falta |, con los bloques mínimos que exige ese tipo de superficie.
4. **Da la corrección concreta**: la frase reescrita, no la sugerencia. Si la
   pieza está alineada, dilo en una línea y no inventes hallazgos.
5. Si la pieza contradice la oferta porque la oferta cambió, es Refinamiento
   pendiente de propagar: créalo en 🔁 Aprendizajes para el área dueña de la
   pieza. Protocolo completo en `references/auditoria-y-refinamiento.md`.

## Modo Pitch para un lead

**La oferta es la misma para todos; el pitch es distinto para cada uno.** Se
personaliza el dolor, los números y el caso que se muestra. Nunca el precio,
los entregables, la promesa ni el límite.

1. **Trae la ficha antes de escribir nada.** Lee en 👥 Leads y clientes:
   `Dolor`, `Objeción`, `Fit avatar`, `Valor`, `Etapa`, `Canal de origen`,
   `Notas`. Lee en 📞 Llamadas la de Descubrimiento: `Objeción principal`,
   `Escala 1-10`, `Aprendizaje`, `Transcript` (sus números, lo que ya intentó,
   quién más decide).
2. **Si faltan campos, dilo antes de escribir.** Un pitch sobre campos vacíos es
   una plantilla con su nombre encima. Pregunta de a uno lo que falte; sin
   números del negocio y sin dolor en sus palabras, no se arma.
3. **Confirma la capa antes de la llamada** (si tienes más de una): se asigna
   por el criterio de ruteo, nunca se improvisa en vivo. `Fit avatar` Bajo o no
   encaja en ninguna capa → no se arma pitch; se le dice y se cierra.
4. **Arma los 14 bloques en orden** (`references/pitch.md`): identidad deseada →
   sus números → mecanismo del cuello → dolores → por qué falló lo anterior →
   pregunta clave → mapa ya existe / se construye → prueba → método y carga →
   roadmap por fase → escala 1-10 → riesgo de no actuar → inversión anclada
   con límite → un solo próximo paso con fecha. Si hay co-decisor, le habla a los dos.
5. **Cierra con la ficha de salida** (caso elegido y por qué, objeción probable
   para `pb-ventas`, link de pago listo antes de la llamada) y guárdalo como
   "Pitch · [Nombre]" en 02 · Oferta › Pitches, con el link en `Notas` del lead.

Manual antes que automático: arma los primeros tres pitches paso a paso con esta
skill antes de pensar en plantillas automáticas de propuesta.

## Modo Refinamiento

Todo cambio de precio, promesa, entregable, límite o capa se decide acá, no en
la llamada ni en el chat con un lead.

1. **Nombra el cambio en una línea** y qué lo motivó (dato, cliente, intuición).
2. **Pásalo por los 5 filtros, en orden** (`references/auditoria-y-refinamiento.md`):
   1. ¿Mueve el `Cuello` del 🧭 Tablero de áreas? Si no, es progreso cero.
   2. ¿Está respaldado? ¿A qué cliente ya se lo entregaste completo?
   3. ¿Suma vocabulario o lo reduce? Un nombre nuevo sin retirar otro reabre el desorden.
   4. ¿Baja el piso? La flexibilidad vive en el calendario de pago, nunca en el monto.
   5. ¿Qué dice la data? Ticket cerrado vs lista, "lo pienso", renovaciones.
3. **Decide con el dueño**: Avanza, Ajustar o No ahora. Si toca precio o
   capacidad de forma grande, pásalo por `pb-foundations` (8 criterios,
   ⚖️ Decisiones) antes de aplicarlo.
4. **Aplica en 02 · Oferta** y agrega la línea al historial con fecha. Los
   clientes que ya están adentro mantienen su precio.
5. **Propaga**: lista qué otras áreas quedan desactualizadas con el mapa
   cambio → áreas, y crea una fila por área en 🔁 Aprendizajes (`Área que
   corrige`, `Fuente` = Decisión, `Qué cambia`, `Estado` = Pendiente, `Fecha`).

## El método

- **Diez bloques, tres grupos y un cierre.** 01-03 construyen el marco; 04-06 son
  lo que se compra de verdad; 07-09 deciden el precio antes de la llamada; 10
  decide si todo lo anterior se convierte en algo.
- **El orden también vende.** Su realidad → nombre al problema → lo que ya
  intentó → el mapa con lo que ya tiene → escala 1-10 → precio y fecha, en la
  misma conversación.
- **Un activo, varias proximidades.** Entre capas cambia cuánto estás tú adentro,
  no el contenido. La capa se asigna antes de la llamada. Una llamada, una capa.
- **Un solo vocabulario.** Un nombre para lo que vendes, uno para el método.
- **El precio sube con la prueba, no con la necesidad de caja.** Se sostiene con
  anclaje y estructura de pago; nunca se baja para salvar un cierre.
- **Cuenta de capacidad antes de cualquier meta de volumen:** precio mensual por
  cliente × clientes simultáneos = techo. Si no llega a la meta de 90 días, el
  problema es el precio o el formato, no la agenda.

Ejemplos, medido mal vs medido bien:

| Situación | Medido mal | Medido bien |
|---|---|---|
| Promesa de una coach de liderazgo | "Claridad, confianza y un equipo alineado" | "En 10 semanas tu equipo toma las decisiones del día sin pasar por ti" |
| Entregables de una consultora | "8 sesiones de 60 minutos" | "Tu proceso de ventas documentado, tu tablero de métricas y tu guion de llamada, operados por ti" |
| "Mi precio está bien, nadie se queja" | Sensación | Ticket cerrado promedio vs lista y % de "lo pienso" en las últimas 10 llamadas |
| Retorno de un programa de 3 meses | "Vas a ver resultados al final" | "Semana 3: tus criterios de calificación operando. Semana 7: primeras reuniones por proceso" |

## Qué se apalanca con IA y qué no

**Sí:**
- Armar el borrador del pitch desde la ficha del lead y la transcripción.
- Traducir el retorno por fase y el mapa ya existe / se construye a su negocio.
- Auditar landings, bios y propuestas contra 02 · Oferta y detectar vocabulario duplicado.
- Hacer la cuenta del anclaje y de capacidad con tus números.
- Simular al comprador escéptico del avatar (cruce con GPT).

**No:**
- Decidir el precio, la promesa o el límite: es tu decisión, con tus datos.
- Inventar prueba, cifras de casos o testimonios. Si falta, se marca el hueco.
- Prometer entregables que no entregaste completos a nadie.
- Negociar en vivo o reescribir la oferta para un lead: eso rompe la oferta.

## Errores que se repiten

- Tres promesas en la misma oferta → el que escucha no sabe cuál repetirle a su socio. Falta: **01 promesa**.
- Nadie se siente excluido → describiste a todos. Falta: **02 filtro**.
- "Lo pienso" como respuesta habitual → no entendió por qué funciona o cuándo ve algo. Falta: **03 mecanismo** o **06 retorno temprano**.
- Vender sesiones en vez de lo que queda. Falta: **04 entregables**.
- No declarar las horas que le cuesta al cliente → se imagina más. Falta: **05 carga**.
- Mostrar casos de otros antes que el propio, o prestados. Falta: **07 prueba**.
- El precio se negocia solo, o lo bajas sin que te lo pidan. Falta: **08 anclaje**.
- Cobras uno y entregas tres. Falta: **09 límite**.
- Terminar en "cuéntame si te interesa" o con dos opciones. Falta: **10 cierre**.
- Armar un paquete a medida para no perder a un lead. Falta: **criterio de ruteo por capa**.
- Prometer lo que todavía no entregaste a nadie. Falta: **lista de deseos separada de la oferta**.

## Notion — qué lee y qué escribe

| Página / Base | Lee | Escribe | Propiedades que toca |
|---|---|---|---|
| 📄 Documento de contexto | Sí | No | Qué vende, a quién, precio actual, cuello, meta a 90 días |
| 02 · Oferta | Sí | Sí | Ficha, 10 bloques, capas y ruteo, pago, lista de deseos, vocabulario, historial, Pitches |
| 03 · Avatar | Sí | No | Filtro, dolores en su idioma, alternativas contra las que compite |
| 07 · Entrega | Sí | No | Qué se entregó de verdad (regla del respaldo) |
| 🧭 Tablero de áreas | Sí | Sí (fila Oferta) | `Puntaje`, `Estado`, `Pieza que falta`, `Próxima acción`, `Revisado` (lee `Cuello`) |
| 👥 Leads y clientes | Sí | Sí (solo `Notas`) | Lee `Nombre`, `Etapa`, `Fit avatar`, `Dolor`, `Objeción`, `Valor`, `Canal de origen`; escribe link al pitch en `Notas` |
| 📞 Llamadas | Sí | No | `Resultado`, `Objeción principal`, `Escala 1-10`, `Aprendizaje`, `Transcript` |
| 🔁 Aprendizajes | Sí | Sí | Lee filas con `Área que corrige` = Oferta y `Estado` = Pendiente; crea filas de propagación |
| ⚖️ Decisiones | Sí | No | `Veredicto 8 criterios` de un cambio de precio grande |

Si Notion no está conectado, entrega lo mismo en markdown y di en qué página o
base pegarlo.

## Cruce con GPT

Claude construye (con esta skill, escribiendo en Notion). GPT audita (Proyecto
"Private Build OS" con el conector de Notion, o Codex con las mismas skills).
Notion es la única memoria. Nunca los dos construyendo la misma pieza a la vez.
Decide el dueño del negocio.

1. Al congelar la oferta, cerrar un pitch importante o aprobar un Refinamiento,
   ofrece el cruce. Si el dueño dice "cruce con GPT", arma el brief; él lo pega
   en ChatGPT y trae "respuesta de GPT: …".
2. Contrasta fila por fila contra los 10 bloques y la regla del respaldo →
   tabla | Punto de GPT | Acepto / Rechazo | Por qué |. Rechaza lo que agregue
   promesas, entregables sin respaldo o baje el precio.
3. Aplica lo aceptado en 02 · Oferta. Si algo cambió el método, deja una fila en
   🔁 Aprendizajes (`Fuente` = Decisión).

**Pregunta de auditoría del área:** que GPT actúe como el comprador escéptico
del avatar y diga en qué bloque diría "lo pienso" y por qué.

```
BRIEF DE CRUCE · Private Build OS · Área 02 Oferta
Contexto del negocio (del Documento de contexto): <qué vendes, a quién, precio
actual, canal principal, cuello actual, meta a 90 días — 3 a 5 líneas>
Qué construí: <la oferta completa en sus 10 bloques, o el pitch para un lead,
o el link a 02 · Oferta si tienes el conector de Notion>
Criterio contra el que se mide:
1. Una sola promesa, con plazo.
2. Filtro explícito de a quién no le sirve.
3. Mecanismo que se puede dibujar en una hoja.
4. Entregables que quedan (cosas, no sesiones), carga declarada y un resultado medible por fase.
5. Prueba propia primero, precio anclado contra una alternativa y límite escrito.
6. Cierre en un solo paso con día y hora.
Tu tarea: actúa como el comprador escéptico de este avatar (el que ya pagó
algo parecido y no le funcionó, con poco tiempo y la plata justa). Recorre los
10 bloques en orden y dime en qué bloque dirías "lo pienso", qué frase exacta
te hizo dudar y qué tendrías que leer para no decirlo.
Responde solo con una tabla: Punto | Mantener o cambiar | Por qué (1 línea) | Propuesta concreta.
Máximo 7 filas. No reescribas la pieza completa. Si algo está bien, dilo y no lo toques.
```

## Handoffs

| Situación | Pasa a | Qué le entrega |
|---|---|---|
| No hay hub de Notion o Documento de contexto | `pb-os` | Pedido de arranque |
| El filtro no se puede escribir o `Fit avatar` es dudoso | `pb-avatar` | Qué bloque necesita el perfil y a quién excluir |
| Pitch listo, falta la llamada | `pb-ventas` | Pitch, objeción más probable, caso elegido, link de pago listo |
| Promesa o precio nuevo hay que declararlo afuera | `pb-contenido` | La promesa congelada y el vocabulario único |
| Mensajes o bio de captura mencionan la oferta | `pb-captura` | Qué frase cambió y dónde |
| Cambió un entregable o el límite | `pb-entrega` | El entregable y el límite por escrito |
| Un cliente pide más de lo que su capa entrega o hay renovación | `pb-success` | La capa siguiente o la de continuidad definida |
| Cambio grande de precio, capacidad o meta | `pb-foundations` | La decisión para los 8 criterios y el precio actual del Documento de contexto |

## Lo que esta skill NO hace

- No conduce la llamada, no maneja objeciones en vivo ni cobra (`pb-ventas`).
- No define el avatar ni sus dolores (`pb-avatar`); los consume.
- No escribe ganchos, carruseles ni la bio (`pb-contenido`).
- No arma el onboarding ni entrega (`pb-entrega`).
- No edita el Documento de contexto: el precio actual lo actualiza `pb-foundations`.
- No inventa casos, cifras ni paquetes a medida para no perder a un lead.

## Frases de prueba

- "Me dicen 'lo pienso' en casi todas las llamadas, revisa mi oferta."
- "Arma el pitch para el lead que tuve ayer, está en Leads y clientes."
- "Quiero subir el precio un 30%, ¿lo hago?"

Método: Private Build · privatebuild-os

---

# Anexo · references/auditoria-y-refinamiento.md

# Auditoría de superficies y Refinamiento de la oferta

Tu oferta vive en un solo lugar: **02 · Oferta**. Todo lo demás (landing, bio,
propuesta enviada, carrusel, guion de llamada, mensajes de captura) es un
reflejo. El desorden típico no es falta de oferta: es la misma oferta declarada
con cinco nombres y tres precios en superficies que el lead ve.

---

## Parte 1 — Auditoría

### 1. Extrae lo que declara la pieza

| Campo | Qué dice la pieza (textual) |
|---|---|
| Nombre de lo que se vende | |
| Promesa | |
| Para quién / para quién no | |
| Precio o rango | |
| Entregables | |
| Límite | |
| Cierre (qué pide que haga el lector) | |

Lo que no declara también es dato: una landing sin límite ni cierre está
incompleta aunque se vea bien.

### 2. Contrasta, en este orden de gravedad

1. **Contradicción con 02 · Oferta** (otro precio, otra promesa, un entregable
   que no está en la oferta). Es lo que más confunde al lead.
2. **Vocabulario:** un término retirado, o un segundo nombre para lo mismo.
   Vivo en una superficie pública, es la corrección prioritaria, por encima de
   cualquier mejora de copy.
3. **Promesa sin respaldo:** un entregable que no se le entregó completo a nadie.
4. **Bloque ausente** según el tipo de pieza (ver tabla de abajo).
5. **Mejoras de redacción.** Al final, y solo si lo anterior está limpio.

### 3. Qué bloques exige cada superficie

No toda pieza tiene que tener los 10. Esto es lo mínimo:

| Superficie | Bloques mínimos |
|---|---|
| Bio / perfil | 01 promesa, 02 filtro, 10 un solo paso |
| Landing o página de venta | Los 10 |
| Propuesta enviada / pitch | Los 10, en el orden de `pitch.md` |
| Carrusel o pieza de contenido que vende | 01, 03, 07 y 10 |
| Mensaje de captura o respuesta a DM | 02 filtro y 10 un solo paso |
| Guion de llamada | 03, 05, 06, 08, 10 (el resto ya lo trae el pitch) |

### 4. Entrega la tabla Veredicto

| Pieza | Criterio | Estado | Qué falta |
|---|---|---|---|
| Promesa | Una, con plazo | ✅ / ⚠️ / ❌ | |
| Filtro | A quién no le sirve | | |
| Mecanismo | Se dibuja en una hoja | | |
| Entregables | Cosas que quedan, con respaldo | | |
| Carga | Horas por semana declaradas | | |
| Retorno temprano | Un resultado por fase con semana | | |
| Prueba | Caso propio primero, con número | | |
| Anclaje | Comparación elegida + costo de no hacerlo | | |
| Límite | Qué no incluye, escrito | | |
| Cierre | Un paso, con día y hora | | |
| Vocabulario | Coincide con 02 · Oferta | | |

Después de la tabla: **la corrección concreta**, escrita, lista para pegar. Si
está alineada, una línea: "Coincide con tu oferta, no la toques."

### 5. Si la pieza no es tuya de editar

La skill no reescribe bios, carruseles ni mensajes de captura. Deja la
corrección y crea una fila en 🔁 Aprendizajes para el área dueña:

| Pieza | Área que corrige |
|---|---|
| Bio, carrusel, reel, email | Contenido |
| Mensajes de DM, formularios, respuestas automáticas | Captura |
| Guion de llamada, propuesta enviada | Ventas |
| Onboarding, documento de bienvenida | Entrega |

---

## Parte 2 — Refinamiento

Todo cambio al producto (precio, promesa, entregable, límite, capa) se decide
acá. Nunca en una llamada, nunca en la propuesta de un lead.

### Los 5 filtros, en orden

1. **¿Mueve el cuello?** Lee `Cuello` en 🧭 Tablero de áreas. Si el cuello es
   Captura y el cambio es a la promesa, pregunta cómo eso llena la agenda. Una
   mejora que no mueve el cuello es trabajo real con progreso cero.
2. **¿Está respaldado?** "¿A qué cliente ya se lo entregaste completo?" Si la
   respuesta es ninguno, va a la lista de deseos, no a la oferta. La oferta sube
   cuando la entrega ya subió, nunca antes: el que la tiene que cumplir eres tú.
3. **¿Suma o reduce vocabulario?** Si agrega un nombre, retira otro en el mismo
   cambio. Un nombre nuevo para el método o una capa bautizada otra vez reabre
   el desorden.
4. **¿Baja el piso?** Si el cambio es bajar el precio para cerrar un caso, no
   pasa. La flexibilidad va en el calendario de pago. Bajarlo para uno rompe el
   ancla de las próximas ventas.
5. **¿Qué dice la data?** La tabla de evidencia de `capas-y-precio.md`. Sin datos,
   el cambio se marca "propuesta, sin validar" y no se publica.

Veredicto: **Avanza** · **Ajustar** · **No ahora**. Si es un cambio grande de
precio, capacidad o formato, pasa por `pb-foundations` (8 criterios en
⚖️ Decisiones) antes de aplicarlo.

### Señales de que toca refinar (vienen de otras áreas)

| Señal | De dónde llega | Qué revisar |
|---|---|---|
| Un cliente inventa una continuidad que no existe | Success | Falta la capa de salida |
| Clientes piden más proximidad de la que su capa entrega | Success, Entrega | Capa de arriba |
| Cero objeción de precio en varias ventas seguidas | Success, Ventas | El precio está bajo |
| Un mismo entregable se repitió completo en 3 clientes | Entrega, Success | Sale de la lista de deseos y entra |
| Un entregable prometido nunca se cumple | Entrega | Sale de la oferta o se escribe el límite |
| Leads que no encajan llegando a llamada | Avatar, Captura | Bloque 02 filtro |

### Cómo se aplica

1. Edita el bloque en 02 · Oferta.
2. Agrega una línea al **Historial de cambios**: fecha · qué cambió · por qué ·
   dato que lo sostiene.
3. Actualiza la ficha congelada (v1 → v1.1 o v2 si cambió promesa o precio).
4. Los clientes activos mantienen sus condiciones.

### Mapa de propagación — qué áreas quedan desactualizadas

| Cambió | Áreas a actualizar | Qué se les pide |
|---|---|---|
| Promesa | Contenido, Captura, Ventas, Entrega | Nueva frase en bio y ganchos; mensajes; pitch; qué se cumple |
| Precio | Ventas, Foundations, Contenido (si es público) | Pitch y estructura de pago; precio actual en Documento de contexto y cuenta de capacidad |
| Entregable | Entrega, Ventas, Success | Qué se entrega y cómo se mide; pitch; qué se mide en el cliente |
| Límite | Entrega, Ventas | Qué se dice que no cuando lo piden; propuesta |
| Capa nueva o retirada | Avatar, Captura, Ventas, Contenido | Tramos de ruteo; a dónde se deriva; pitch; qué se declara |
| Filtro (a quién no) | Avatar, Contenido, Captura | Anti-perfil; a quién se deja de atraer; preguntas de calificación |

Por cada área afectada, una fila en **🔁 Aprendizajes**:

| Propiedad | Valor |
|---|---|
| `Aprendizaje` | "Oferta: [qué cambió] — actualizar [qué pieza]" |
| `Área que corrige` | El área afectada |
| `Fuente` | Decisión |
| `Qué cambia` | La frase o el número nuevo, textual |
| `Estado` | Pendiente |
| `Fecha` | Hoy |

`pb-success` procesa esas filas; cada skill hermana las lee al abrir su área.

---

## Vocabulario — una sola forma de nombrar

En 02 · Oferta vive una tabla corta:

| Término | Estado | Se reemplaza por |
|---|---|---|
| [nombre viejo del programa] | Retirado | [nombre vigente] |
| [nombre de un nivel que ya no existe] | Muerto | — |
| [etapa del cliente usada como nombre de producto] | Error de etiqueta | Etapa, no producto |

Reglas:

- **Un nombre para lo que vendes, uno para el método.** Un tercero no suma: resta.
- **Las etapas del cliente no son productos.** "Principiante", "avanzado" o
  como llames a tus niveles de cliente describen dónde está él, no qué compra.
- **Un producto viejo con contrato vigente se honra, no se vende de nuevo.** Se
  marca como legado.

---

# Anexo · references/bloques.md

# Los 10 bloques — construcción, criterio y ejemplos

Cada bloque responde una pregunta que el comprador se hace en silencio. Si no
la respondes tú, la responde él, y casi nunca a tu favor. Se construyen en este
orden, de a uno, y cada uno queda escrito en 02 · Oferta antes del siguiente.

Formato de cada bloque: **pregunta del comprador · criterio · preguntas al
dueño · mal vs bien · síntoma si falta.**

---

## Grupo 01-03 · Antes de hablar de lo que haces

Construyen el marco donde tu servicio tiene sentido. Sin ellos, todo lo que
digas después suena a lo que dice el resto.

### 01 · La promesa — "¿Qué me llevo?"

- **Criterio:** una sola, con plazo, dicha como resultado del cliente (no como
  actividad tuya). Tres promesas son cero: el que escucha no sabe cuál
  repetirle a su socio.
- **Preguntas al dueño:**
  1. ¿Qué tiene tu cliente al final que no tenía al empezar? Una cosa.
  2. ¿En cuánto tiempo, con tu cliente típico, no con el mejor?
  3. ¿Cómo lo diría él, si se lo contara a su pareja o a su socio?
- **Mal:** "Transformación integral de tu negocio con claridad, estrategia y
  acompañamiento."
- **Bien:** "En 12 semanas tu agenda se llena por proceso, no por salir a
  buscar clientes."
- **Si tu pipeline se parte en dos dolores medidos** (por ejemplo "no tengo
  tiempo" y "no tengo oferta clara"), la promesa puede tener dos frases de
  apertura según el dolor. Mismo precio, mismo entregable, misma duración.
  Nunca las dos en la misma conversación.
- **Síntoma si falta:** el lead resume tu oferta distinto a como la dijiste.

### 02 · El filtro — "¿Es para mí?"

- **Criterio:** decir a quién no le sirve, con rasgos concretos (etapa,
  ingreso, intención, lo que espera de ti). Si nadie se siente excluido,
  describiste a todos.
- **Preguntas al dueño:**
  1. ¿Con qué cliente perdiste plata o energía? ¿Qué tenía?
  2. ¿Quién te pide que le hagas el trabajo cuando tú vendes otra cosa?
  3. ¿Bajo qué nivel de ingreso o etapa tu precio no tiene sentido para él?
- **Mal:** "Para emprendedores que quieren crecer."
- **Bien:** "No es para ti si todavía no tienes clientes pagando, o si buscas
  que alguien lo haga por ti. Es para quien ya vende y quiere dejar de ser el
  cuello de su propio negocio."
- **Fuente:** el perfil y el anti-perfil viven en 03 · Avatar. Si no están,
  handoff a `pb-avatar`; acá solo se escribe la frase que filtra.
- **Síntoma si falta:** llamadas con leads de `Fit avatar` Bajo; "No es para mí"
  aparece tarde, en la propuesta, no en el contenido.

### 03 · El mecanismo — "¿Por qué funcionaría?"

- **Criterio:** la razón causal por la que el resultado ocurre, en una frase y
  un dibujo. Sin mecanismo eres una promesa. Si no lo puedes dibujar en una
  hoja, no lo tienes.
- **Preguntas al dueño:**
  1. ¿Qué haces tú que el cliente no hace solo y que explica el resultado?
  2. ¿Qué pasos, en qué orden, y por qué ese orden?
  3. ¿Por qué lo que ya probó no funcionó y esto sí?
- **Mal:** "Trabajamos con una metodología probada de acompañamiento."
- **Bien:** "Primero la oferta, después el filtro, después el tráfico. Tu
  problema no es falta de leads: es que el tráfico llega a una oferta que no
  se entiende. Por eso más anuncios no te han servido."
- **Síntoma si falta:** "lo pienso" aunque el lead estaba de acuerdo con el
  dolor.

---

## Grupo 04-06 · Lo que el cliente compra de verdad

Nadie compra tu proceso: compra lo que existe cuando el proceso termina, cuánto
le va a costar en tiempo propio, y cuándo empieza a ver señales.

### 04 · Los entregables — "¿Qué existe al final?"

- **Criterio:** cosas que quedan, con nombre, no temas que se van a ver. Contar
  sesiones es vender tiempo; listar lo que queda es vender un activo. Cada
  entregable tiene respaldo: se lo entregaste completo a un cliente real.
- **Preguntas al dueño:**
  1. Cuando tu último cliente terminó, ¿qué archivos, sistemas o documentos
     le quedaron?
  2. ¿Cuál de esos usa todavía sin ti?
  3. ¿Qué prometiste alguna vez y no entregaste completo? (va a la lista de deseos)
- **Mal:** "12 sesiones semanales + acceso a la comunidad."
- **Bien:** "Tu proceso comercial documentado, tu tablero de métricas semanal y
  tu guion de llamada, operados por ti. Las sesiones son el medio."
- **Lista de deseos:** lo que se entrega a veces pero no siempre, o se entregó a
  medias, se escribe aparte y no se promete. Sorprender es gratis; incumplir
  cuesta el caso.
- **Síntoma si falta:** el cliente compara tu precio contra horas.

### 05 · La carga — "¿Cuánto tiempo mío?"

- **Criterio:** horas por semana del cliente, declaradas por escrito, y qué hace
  en esas horas. En quien ya está saturado la objeción real es el tiempo; si no
  la declaras, se la imagina, y siempre imagina más.
- **Preguntas al dueño:**
  1. ¿Cuántas horas por semana le toma a tu cliente típico, incluyendo tareas
     entre sesiones?
  2. ¿Qué pasa si una semana no puede?
- **Mal:** (no dice nada) o "requiere compromiso".
- **Bien:** "3 horas por semana: una sesión de 60 minutos y dos horas de
  aplicación. Si una semana no puedes, la sesión se usa para destrabar, no se
  pierde."
- **Síntoma si falta:** "ahora no es el momento", "estoy con mucho trabajo".

### 06 · El retorno temprano — "¿Cuándo veo algo?"

- **Criterio:** un resultado medible por fase, con semana asignada. Nadie compra
  tres meses de fe; un resultado por fase convierte una apuesta larga en varias
  cortas. Una por fase, no una por semana: prometer de más aquí es lo primero
  que se incumple.
- **Preguntas al dueño:**
  1. ¿Qué cambia primero en el negocio de tu cliente, y en qué semana?
  2. ¿Cómo lo mediría él sin preguntarte?
- **Mal:** "Vas a ver resultados al final del programa."
- **Bien:**

  | Fase | Semanas | Resultado medible |
  |---|---|---|
  | 1 | 1-4 | Sabe a quién decirle que no: criterios de calificación operando |
  | 2 | 5-8 | Reuniones que llegan por proceso |
  | 3 | 9-12 | El pipeline sigue vivo mientras él entrega |

- **Síntoma si falta:** "lo pienso" y abandono a mitad del programa.

---

## Grupo 07-09 · Lo que decide el precio

El precio no se defiende con argumentos en la llamada: se define antes, con
estos tres bloques. Cuando faltan, el número queda solo y todo número solo
parece caro.

### 07 · La prueba — "¿A ti te funcionó?"

- **Criterio:** tu caso propio va primero (es el único que nadie puede pedir
  prestado), después un solo caso de cliente que se parezca a la etapa del
  lead, no a su rubro. Un caso cuenta cuando tiene un número, no cuando el
  cliente terminó.
- **Preguntas al dueño:**
  1. ¿Qué resultado tuyo, con número, sale de aplicar esto en tu propio negocio?
  2. ¿Qué clientes tienen un antes y después con número? ¿En qué etapa estaban?
  3. ¿Qué entregable tiene prueba y cuál no todavía?
- **Prueba asignada por entregable:** cada entregable lleva el caso que lo
  respalda. Si un entregable no tiene caso, se marca el hueco. Nunca se inventa
  una cifra.
- **Mal:** cinco testimonios genéricos sin número, de rubros distintos.
- **Bien:** "Lo apliqué primero en mi negocio: [resultado con número]. Después
  con un cliente en tu misma etapa: pasó de [antes] a [después] en [plazo]."
- **Síntoma si falta:** la objeción que nunca se dice en voz alta; el lead pide
  "referencias" al final.

### 08 · El anclaje — "¿Es caro?"

- **Criterio:** el precio se presenta contra una comparación que eliges tú, más
  el costo de no hacerlo. Un precio solo siempre parece caro; comparado se
  vuelve obvio. Si no eliges la comparación, la elige él.
- **Preguntas al dueño:**
  1. ¿Qué alternativa ya cotizó o pagó tu cliente típico? (agencia, empleado,
     curso, no hacer nada)
  2. ¿Cuánto le cuesta al mes seguir como está?
  3. ¿Con cuántas ventas suyas se paga tu precio?
- **Tabla de anclaje** (plantilla completa en `capas-y-precio.md`): precio ·
  a 12 meses · qué queda al dejar de pagar, tu oferta contra la alternativa.
- **Mal:** "La inversión es [precio]." Y silencio defensivo, o descuento.
- **Bien:** "Una agencia te cobra eso cada mes y cuando dejas de pagar no queda
  nada. Esto se paga una vez y el sistema queda instalado. Con [N] ventas tuyas
  está pagado."
- **Síntoma si falta:** el precio se negocia solo, o lo bajas sin que te lo pidan.

### 09 · El límite — "¿Hasta dónde llega?"

- **Criterio:** qué incluye, qué no incluye y qué pasa cuando el cliente pide lo
  que no está, por escrito. Sin límite escrito, el alcance lo define el cliente,
  siempre hacia arriba: cobras uno y entregas tres.
- **Preguntas al dueño:**
  1. ¿Qué te han pedido que no estaba en lo que vendiste? ¿Lo diste?
  2. ¿Qué no haces nunca, aunque te lo paguen aparte?
  3. ¿Qué pasa si quiere más? (capa siguiente, adicional con precio, o no)
- **Mal:** "Te acompaño en todo lo que necesites."
- **Bien:** "Incluye diseñar y documentar tu proceso contigo. No incluye
  ejecutarlo por ti ni gestionar tus redes. Si necesitas manos, te recomiendo a
  quién y lo coordinamos."
- **Síntoma si falta:** entregas de más; cada cliente recibe algo distinto.

---

## Bloque 10 · Cómo termina

- **Criterio:** un solo paso, con día y hora. Dos opciones equivalen a ninguna:
  el que elige entre dos caminos pospone. Un paso sin fecha es una intención.
- **Preguntas al dueño:**
  1. ¿Qué pasa exactamente cuando el cliente dice que sí? ¿Qué recibe y cuándo?
  2. ¿Tienes el link de pago o el contrato listo antes de la conversación?
- **Mal:** "Cuéntame si te interesa y lo vemos." / "¿Prefieres el plan A o el B?"
- **Bien:** "Si te hace sentido, te mando el link ahora y fijamos la primera
  sesión para el martes a las 10."
- **Prueba rápida:** si tu oferta termina en "cuéntame si te interesa", no
  termina: termina en el aire, y el aire lo llena la agenda del otro.

---

## Oferta floja — síntoma → bloque

| Síntoma en el ciclo | Dónde se ve en Notion | Bloque que falta |
|---|---|---|
| "Lo pienso" | 📞 Llamadas `Resultado` = Lo pienso | 03 o 06 |
| El precio se negocia solo | 👥 Leads y clientes `Valor` bajo la lista | 08 |
| Entregas de más | 🔁 Aprendizajes desde Entrega, clientes activos | 09 |
| Llegan los que no son | `Fit avatar` Bajo en llamada | 02 |
| El lead no sabe repetir qué compra | `Aprendizaje` de la llamada | 01 |

## El test final — seis preguntas, sin mirar nada

1. ¿Qué promete? — una cosa, con plazo.
2. ¿A quién no le sirve? — con nombre y apellido.
3. ¿Por qué funciona? — el mecanismo, no la lista de tareas.
4. ¿Qué existe al final? — cosas, no temas.
5. ¿Cuándo se ve el primer resultado? — con semana asignada.
6. ¿Contra qué se compara el precio? — y qué cuesta no hacerlo.

Una frase cada una. Si alguna toma más, ese es el bloque que falta trabajar.

---

# Anexo · references/capas-y-precio.md

# Capas, ruteo y precio

Cómo se ordena la oferta cuando vendes en más de un nivel, cómo se asigna la
capa a cada lead y cómo se sostiene el precio. Todo lo de acá lo define el
dueño con sus datos; la skill pone el criterio.

---

## 1. Un activo, varias proximidades

No vendes tres productos distintos. Vendes **un solo activo** (el resultado que
promete el bloque 01) a distintas **distancias tuyas**. Lo que cambia entre
capas es cuánto estás tú adentro, no el contenido:

| Proximidad | Quién construye | Ejemplo de formato |
|---|---|---|
| Lo haces tú | El cliente, con tu material | Curso, comunidad, plantillas |
| Lo construimos juntos | Tú y el cliente, en sesión | Consultoría o programa 1:1 |
| Lo hago yo | Tú o tu equipo | Implementación, servicio hecho por ti |

Reglas:

1. **El cliente no elige capa: se le asigna** por dónde está parado, antes de la
   llamada.
2. **Una llamada, una capa.** Presentar dos en la misma conversación produce
   "lo pienso".
3. **Una capa vende activamente; las otras cumplen otra función.** La de entrada
   captura y califica (se mide por altas y llamadas agendadas, nunca por
   ventas directas). La de arriba se aplica, no se ofrece en frío.
4. **Lo que se construye adentro puede variar** según el cuello del cliente
   (sistema comercial, captación, tiempo). Eso no es una oferta nueva: el precio
   no cambia, cambia qué se construye primero.
5. **No se inventan capas.** Si un lead no encaja en ninguna, no encaja en la
   oferta. Armar un paquete a medida para no perderlo es exactamente el
   mecanismo que desordena una oferta.
6. **La capa de arriba nunca es puerta de entrada.** Participación en resultados,
   socios o implementación completa solo después de haber trabajado en la capa
   núcleo: sin la base construida no hay palanca, hay ejecución.

### Capa de continuidad — la salida

Si el programa termina y no hay a qué pasar, el cliente que quiere seguir
**inventa la continuidad** (y suele inventarla más barata). Cuando un cliente
pide seguir, no rompió el precio: descubrió un producto que te falta. Defínelo
antes de que lo negocie: menos cadencia, mes a mes, precio propio.

## 2. Ruteo — la capa se decide antes de la llamada

Tres filtros, en este orden:

1. **Intención:** ¿quiere claridad y construir, o quiere que alguien lo haga?
   Si tu capa núcleo es construir juntos y él quiere manos, no encaja aunque le
   sobre la plata. Se le dice y se cierra (o va a la capa "lo hago yo", si existe).
2. **Ingreso + tipo de negocio, juntos:** define tus tramos. Pesa igual el monto
   que la estructura: un negocio con operación propia sostiene un ticket más
   alto que un servicio uno a uno con el mismo ingreso.
3. **¿Tiene negocio en marcha y puede nombrar su cuello?** Si no sabe qué está
   roto, va a la capa de entrada aunque el ingreso dé.

Plantilla para 02 · Oferta:

| Ingreso del lead | Segundo filtro | Capa |
|---|---|---|
| Bajo [tu tramo 1] | — | Entrada |
| [tramo 1] – [tramo 2] | En marcha y nombra su cuello | Núcleo |
| [tramo 1] – [tramo 2] | No sabe qué está roto | Entrada |
| Sobre [tramo 2] o con equipo | Ya pasó por el núcleo y pide más proximidad | Arriba |

Devuelve **una sola capa**, con su precio y su promesa, en una línea. Si no
encaja en ninguna: "no encaja en la oferta".

Referencia útil desde 03 · Avatar: bajo cierto ingreso, el lead mide tu precio
como porcentaje de lo que entra, no contra su retorno. Si tu precio supera lo
que el dueño se paga a sí mismo, pierde por comparación aunque el retorno cierre.

## 3. La cuenta de capacidad

Antes de cualquier meta de volumen:

```
precio por cliente ÷ meses del programa = ingreso mensual por cliente
ingreso mensual por cliente × clientes simultáneos que aguantas = techo mensual
```

Error clásico: confundir precio del programa con precio mensual. Un programa de
3 meses cobrado una vez, con 10 clientes simultáneos, produce un tercio de lo
que la cuenta rápida promete. Si el techo no llega a la meta de 90 días del
Documento de contexto, el problema es el precio o el formato, no la agenda.
Esa decisión va a `pb-foundations`.

## 4. El anclaje

El precio nunca se presenta solo. Se presenta contra la alternativa que el lead
ya cotizó o paga hoy, más el costo de no hacerlo.

| | La alternativa que ya conoce | Tu oferta |
|---|---|---|
| Precio | [lo que cuesta, y cada cuánto] | [tu precio, y cada cuánto] |
| A 12 meses | [total] | [total] |
| Al dejar de pagar | [qué queda] | [qué queda] |

Segundo anclaje encima: **con cuántas ventas suyas se paga.** Si su ticket es
alto, una sola.

Tercer anclaje, el del bloque de riesgo: **qué le cuesta seguir 6 meses más
como está**, con sus números.

## 5. Mecánica de precio — cómo se sostiene

- **Un precio de lista, dicho con calma.** Nunca se ajusta al bolsillo del lead:
  si no puede, no es su capa.
- **Si usas incentivo por decisión en la llamada, es planificado, no cedido:**
  se anuncia como tal, tiene condición clara y se registra como planificado.
  Sirve para acelerar la decisión, no para salvar la venta.
- **Alternativa más limpia — precio por escalón de prueba:** el precio sube cada
  vez que acumulas un número fijo de casos con resultado medible. Deja de ser
  una conversación interna y pasa a ser una consecuencia. Y el cierre sale solo:
  "desde el próximo caso esto sube a [siguiente escalón]", que además es verdad.
- **Los que están adentro mantienen su precio.** El cambio aplica a clientes nuevos.
- **Señal para subir, desde Success:** si el precio no genera ninguna objeción
  en varias ventas seguidas, no fueron buenas ventas: fue un precio bajo.

## 6. Estructura de pago — se declara en la oferta, se ejecuta en Ventas

La flexibilidad vive en el calendario, nunca en el monto, y **la financia quien
la pide**:

| Nivel | Precio | Quién financia |
|---|---|---|
| Pago completo | El de lista | Nadie. Es el precio, no un descuento |
| Cuotas con tarjeta por la pasarela | Lista + recargo de la pasarela | El cliente, con su tarjeta |
| Plan de pagos contigo | Lista + un recargo fijo que tú defines | Tú, por eso cuesta más |

- Presentar el pago completo como descuento hace que tu lista parezca inflada.
- La estructura se escribe en 02 · Oferta para que no se improvise en vivo; en
  la llamada solo aparece si el cliente declara una restricción. La secuencia de
  cobro es de `pb-ventas`.
- "Necesito liquidez primero" es objeción de oferta, no de llamada: se resuelve
  teniendo la estructura de pago escrita antes.

## 7. Beneficios — después del precio, por escrito

Opcional. Lo que suma sin ser la razón de comprar (plantillas, recursos,
beneficio por referido). Reglas:

- Van después del precio y **por escrito**; dichos solo en la llamada no existen.
- Un beneficio por referido es un **monto fijo** que se paga cuando el referido
  **paga**, nunca un descuento sobre el precio de lista de nadie. El referido
  pasa por el mismo filtro que cualquier lead.

## 8. Evidencia de precio — antes de mover un número

Lee esto de 👥 Leads y clientes y 📞 Llamadas, no de la memoria:

| Qué mirar | Qué te dice |
|---|---|
| Cierres a precio de lista vs cierres con objeción de precio | Si el piso se sostiene cuando el anclaje está hecho |
| Ticket cerrado promedio vs precio de lista | Cuánto estás cediendo sin decidirlo |
| Renovaciones y a qué precio | Si existe continuidad o la inventa el cliente |
| `Resultado` = Lo pienso en las últimas 10 llamadas | Si falta mecanismo o retorno, no precio |
| Origen del ingreso por `Canal de origen` | Qué parte de tu oferta pagó de verdad |

Regla: cuando aparece la objeción de precio, la respuesta es el anclaje y la
estructura de pago, nunca el monto.

---

# Anexo · references/pitch.md

# Pitch para un lead — el molde de 14 bloques

**La oferta es la misma para todos; el pitch es distinto para cada uno.** Se
personaliza el dolor, los números y el caso que se muestra. Lo demás sale
textual de 02 · Oferta.

El molde viene de un deck que cerró sin objeción de precio y sin usar el
incentivo de cierre que traía. Lo que lo hizo funcionar no fue el diseño: fue
el orden y que cada bloque hablaba con los números del lead.

---

## Paso 1 — La ficha, antes de escribir nada

| Dato | Dónde se lee | Para qué se usa |
|---|---|---|
| Dolor en sus palabras | 👥 `Dolor` + `Transcript` de la llamada de Descubrimiento | Bloques 3 y 4 |
| Sus números (ingreso, clientes, ticket, conversión) | `Transcript`, `Notas` | Bloque 2 y el anclaje del 13 |
| Lo que ya intentó y por qué falló | `Transcript`, `Aprendizaje` | Bloque 5 |
| Dónde quiere estar | `Transcript`, `Notas` | Bloques 1 y 6 |
| Objeción probable | 👥 `Objeción`, 📞 `Objeción principal` | Se neutraliza antes, en el bloque que corresponde |
| Qué tanto le importa | 📞 `Escala 1-10` (si ya se preguntó) | Bloque 11 |
| Quién más decide | `Notas`, `Transcript` | Todo el pitch le habla a los dos |
| Fit y capa | 👥 `Fit avatar`, criterio de ruteo | Si no encaja, no hay pitch |

**Si faltan campos, dilo antes de escribir.** Pregunta de a uno. Sin números del
negocio y sin dolor en sus palabras, no se arma: un pitch sobre campos vacíos
es una plantilla con su nombre encima, y se nota.

## Paso 2 — Los 14 bloques, en este orden

| # | Bloque | Qué va | Sale de | Bloque de oferta |
|---|---|---|---|---|
| 1 | Identidad deseada | "De [lo que es hoy] a [lo que quiere ser]", en una línea, en su idioma | Dónde está vs dónde quiere estar | 01 |
| 2 | Su negocio en números reales | Sus cifras devueltas. Prueba de que entendiste y compra permiso para lo demás | Sus números | — |
| 3 | El mecanismo del cuello | El problema con nombre, no el síntoma. Ej.: "vendes o entregas, nunca las dos a la vez" | Dolor + tu mecanismo | 03 |
| 4 | Sus dolores | Máximo tres, ya validados en la llamada, con sus palabras | Dolor | — |
| 5 | Por qué falló lo anterior | Neutraliza "ya lo intenté" antes de que aparezca, con lo que él mismo contó | Lo que intentó | 03 |
| 6 | La pregunta clave | "¿Qué tendría que cambiar para que [su meta] ocurra?" Pone el objetivo en su boca | Dónde quiere estar | — |
| 7 | El mapa | Las piezas de tu método aplicadas a su negocio, marcando YA EXISTE vs SE CONSTRUYE | Su situación | 04 |
| 8 | La prueba | Tu caso propio primero. Después UN caso de cliente, el que se parezca a su etapa | 02 · Oferta, bloque 07 | 07 |
| 9 | El método y la carga | Cómo se trabaja y cuántas horas le cuesta por semana. Acá muere la objeción de tiempo | Bloques 03 y 05 | 05 |
| 10 | Roadmap por fases | Las fases con el resultado medible de cada una, traducido a su negocio | Bloque 06 | 06 |
| 11 | Escala 1-10, antes del precio | "Del 1 al 10, ¿qué tan importante es resolver esto ahora?" 8+ con porqué → la conversación pasa de si compra a cómo paga | — | — |
| 12 | Riesgo de no actuar + lo que ya tiene | Qué le cuesta seguir igual 6 meses, con sus números. Y sus activos: "lo único que falta es [la estructura]" | Sus números | 08 |
| 13 | Inversión anclada + límite | Precio contra la alternativa que ya cotizó y contra una venta suya. Qué incluye y qué no | Bloques 08 y 09 | 08, 09 |
| 14 | Un solo próximo paso | Con día y hora. Pregunta abierta: "¿cómo te gustaría avanzar?", nunca "¿quieres avanzar?" | Bloque 10 | 10 |

Después del 14, solo si existe y por escrito: los beneficios.

Coincide con el orden que vende de la página: su realidad (2) → nombre al
problema (3) → neutraliza lo que intentó (5) → el mapa con lo que ya tiene (7)
→ escala antes del precio (11) → precio y fecha en la misma conversación (13-14).

## Paso 3 — Lo que NO se personaliza

- **El precio.** Nunca se ajusta al bolsillo del lead. Si no puede, no es su capa.
- **Los entregables.** Salen textual de 02 · Oferta, bloque 04.
- **El retorno por fase.** Se traduce a su negocio; no se agregan más.
- **La promesa.** Es la de la oferta (o su frase de apertura según el dolor, si
  tienes dos). No se inventa una para él.
- **El límite.** Lo que no incluye, no se incluye porque él lo pida.

Si mientras armas el pitch sientes que "a este habría que ofrecerle algo
distinto", para: eso es Refinamiento o es un lead que no encaja. No se resuelve
en su propuesta.

## Paso 4 — El co-decisor

Si hay alguien más que decide (socio, pareja, directorio):

- El pitch va escrito para que lo lea sin ti: el co-decisor es quien defiende tu
  propuesta frente a sí mismo cuando tú no estás.
- Incluye su preocupación probable (plata, tiempo, "otra vez algo que no
  funciona") en el bloque 12 o 13.
- La llamada de cierre se agenda con los dos. Eso lo ejecuta `pb-ventas`.

## Paso 5 — La ficha de salida (va al final del pitch)

```
FICHA DE SALIDA · Pitch · [Nombre del lead]
Capa: [una sola] · Precio: [de lista] · Promesa: [la frase de apertura]
Caso que se lleva: [cuál] — por qué ese: [su etapa se parece en...]
Objeción más probable: [cuál] — dónde ya se neutralizó: [bloque N]
Co-decisor: [sí/no, quién]
Link de pago: [listo antes de la llamada, con cuotas configuradas]
Próximo paso propuesto: [día y hora]
Campos que faltaban en la ficha: [lista o "ninguno"]
```

Dos recordatorios para `pb-ventas`:

1. El link de pago se prepara **antes** de la llamada. Generarlo en vivo cuesta
   minutos y enfría la decisión.
2. La llamada se mantiene abierta mientras el cliente paga. Si el link se manda
   después, la venta se enfría.

## Paso 6 — Dónde queda

- Subpágina "Pitch · [Nombre]" dentro de 02 · Oferta › Pitches.
- Link en `Notas` del lead en 👥 Leads y clientes.
- Si al armarlo apareció un hueco de la oferta (un bloque que no tenía cómo
  llenarse), fila en 🔁 Aprendizajes con `Área que corrige` = Oferta.

## Ejemplo corto, mal vs bien (bloque 2)

- **Mal:** "Tu negocio tiene mucho potencial y estás en un gran momento para crecer."
- **Bien:** "Hoy facturas cerca de [monto] al mes con [N] clientes activos, el 80%
  llega por referidos y tú haces todas las llamadas de venta. Cada mes que
  entregas mucho, vendes poco."

---

# Anexo · references/plantilla-pagina.md

# Plantilla de la página 02 · Oferta

Estructura de la página de área en Notion, dentro del hub 🏗️ Private Build OS.
La skill la crea (o completa) en este orden. Si Notion no está conectado, se
entrega igual en markdown para pegar.

Regla: la página es la **única fuente** de la oferta. Landing, bio, propuestas y
guiones la reflejan; ninguno la redefine.

---

```
02 · Oferta
Qué vendes y a qué precio

## Ficha — v[N] congelada el [fecha]
| Campo | Valor |
|---|---|
| Nombre | [un solo nombre] |
| Categoría | [qué es, en 3-5 palabras] |
| Promesa | [bloque 01, una frase con plazo] |
| Para quién / no | [bloque 02, en una línea] |
| Precio de lista | [monto y moneda, por el programa completo o por mes: dilo] |
| Duración y cadencia | [semanas · sesiones · día fijo] |
| Carga del cliente | [horas por semana] |
| Modalidad | [lo haces tú / lo construimos juntos / lo hago yo] |

## Los 10 bloques
### 01 · La promesa — "¿Qué me llevo?"
### 02 · El filtro — "¿Es para mí?"
### 03 · El mecanismo — "¿Por qué funcionaría?"  (+ el dibujo)
### 04 · Los entregables — "¿Qué existe al final?"
    | Entregable | Qué queda | Respaldo (a qué cliente ya se lo entregaste) | Prueba asignada |
### 05 · La carga — "¿Cuánto tiempo mío?"
### 06 · El retorno temprano — "¿Cuándo veo algo?"
    | Fase | Semanas | Resultado medible |
### 07 · La prueba — "¿A ti te funcionó?"
    Caso propio (con número) → un caso por etapa de cliente (con número)
    Huecos: [entregable sin caso todavía]
### 08 · El anclaje — "¿Es caro?"
    | | La alternativa | Tu oferta |   (precio · a 12 meses · al dejar de pagar)
    Se paga con: [N] ventas del cliente
### 09 · El límite — "¿Hasta dónde llega?"
    Incluye: … · No incluye: … · Si pide más: …
### 10 · Cómo termina
    El paso: … · Cuándo: … · Qué recibe al decir que sí: …

## Capas y ruteo
    | Capa | Proximidad | Precio | Función (vende / captura / se aplica) |
    | Ingreso del lead | Segundo filtro | Capa |
    Capa de continuidad: …

## Estructura de pago
    | Nivel | Precio | Quién financia |

## Beneficios (después del precio, por escrito)

## Lista de deseos — NO se promete
    | Entregable | Qué falta para que entre (entregarlo completo a un cliente) |

## Vocabulario
    | Término | Estado | Se reemplaza por |

## Superficies donde se declara
    | Superficie | Última auditoría | Estado |
    (bio, landing, propuesta tipo, guion de llamada, mensajes de captura)

## Historial de cambios
    - [fecha] · qué cambió · por qué · dato que lo sostiene · áreas avisadas

## Pitches
    Subpáginas: "Pitch · [Nombre del lead]"
```

---

## Checklist de piezas (lo usa el Diagnóstico)

| Pieza | Existe |
|---|---|
| Ficha congelada con fecha | ☐ |
| 10 bloques escritos | ☐ (cuántos: _/10) |
| Cada entregable con respaldo | ☐ |
| Retorno por fase con semana | ☐ |
| Anclaje con tabla | ☐ |
| Límite escrito | ☐ |
| Capas y ruteo (o "una sola capa" explícito) | ☐ |
| Estructura de pago escrita | ☐ |
| Lista de deseos separada | ☐ |
| Historial de cambios | ☐ |

Puntaje orientativo: faltan 4 o más bloques → 1 · la oferta se dice pero no está
escrita → 2 · los 10 escritos sin medir "lo pienso" ni ticket cerrado vs lista →
3 · escrita, congelada y medida en las últimas 10 llamadas → 4.
