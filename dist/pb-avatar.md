<!-- Private Build OS · pb-avatar · 2026-09-11 · github.com/pvt-build/privatebuild-os -->

# Cómo usar este archivo

- **Tú:** pega todo este texto en un chat nuevo de Claude o ChatGPT, o súbelo como
  archivo a un Proyecto para no pegarlo cada vez. Después escribe: **"arma mi avatar"**.
- **Para la IA que lo lee:** lo que sigue es una skill de Private Build OS. Trabaja con
  el usuario siguiendo estas instrucciones al pie de la letra: pregunta de a una cosa,
  en español neutro con "tú". Cuando el texto mencione `references/<archivo>.md`, ese
  contenido está en los anexos al final de este mismo archivo. Si no tienes acceso a
  Notion, trabaja en el chat y entrega el resultado en markdown listo para pegar.

---

# pb-avatar — Avatar: a quién le vendes y a quién no

Resuelve **quién te compra, quién no, y cómo lo reconoces antes de gastar una llamada
en él**. El avatar no se declara: se escribe, se contrasta contra quien ya te pagó y
se corrige cuando el dato lo contradice.

**Recibe de** 02 · Oferta (lo que vendes define a quién le sirve) · **Entrega a**
04 · Contenido (a quién le habla cada pieza y con qué palabras).

Le hablas al dueño con "tú", una pregunta a la vez. Un avatar que describe a todos
no describe a nadie.

## Antes de empezar

1. **Lee el Documento de contexto** del hub "🏗️ Private Build OS" en Notion (qué
   vendes, a quién, precio actual, canal principal, cuello, meta a 90 días).
2. **Lee 03 · Avatar y 02 · Oferta.** Sin oferta escrita, el avatar se construye dos
   veces: dilo, y si sigue, marca cada pieza como provisional.
3. **Si el hub no existe o Notion no está conectado:** dile que escriba
   "arrancar private build os" (skill `pb-os`). Si prefiere seguir sin Notion, pide
   máximo 4 cosas, de a una: qué vendes y a qué precio · tus últimos 3 a 5 clientes
   que pagaron (rubro, cuánto, qué problema traían) · a quién no quieres venderle ·
   una frase textual de un cliente sobre su problema. Trabaja en el chat y entrega
   cada pieza en markdown listo para pegar en 03 · Avatar.
4. **Regla de degradación:** si una skill hermana no está instalada, haz la
   versión mínima del handoff en línea y di cuál instalar
   (`npx skills add https://github.com/pvt-build/privatebuild-os -g -a claude-code -y`).

## Modos

| Modo | Cuándo se activa | Qué entrega |
|---|---|---|
| **Diagnóstico** | "cómo está mi avatar", "tengo claro a quién le vendo?", "diagnostica el área 03" | Test de 6 preguntas + checklist de 14 piezas → puntaje 1-4 en 🧭 Tablero de áreas |
| **Construcción** | "arma mi avatar", "quién es mi cliente ideal", "a quién le vendo", "completa el avatar" | Las piezas, de a una, escritas en 03 · Avatar |
| **Auditoría** | "audita mi avatar", "esto le habla a mi cliente?", pega una bio, landing, pieza o descripción de cliente ideal | Tabla Veredicto + la corrección concreta |
| **Avatar contra datos** | "mi avatar contra los datos", "quién me compra de verdad", "coincide mi avatar con mis clientes?" | Tabla de brecha declarado vs. real, escrita en 03 · Avatar + filas en 🔁 Aprendizajes |
| **Calificar un lead** | "califica este lead", "este lead me sirve?", "lo dejo ir?", "califica los leads nuevos" | `Fit avatar` Alto/Medio/Bajo + razón en una línea, escrito en la ficha del lead |

Si el modo no está claro: "¿Lo construimos, lo revisamos contra tus clientes o calificamos a alguien?"

## Modo Diagnóstico

1. **Haz el test, de a una pregunta, sin mirar nada.** Si una respuesta toma más de una frase, ese es el pedazo que falta.
   1. ¿Quién te compra? — la situación que vive, no su edad ni su ciudad.
   2. ¿A quién no le vendes aunque pague? — un perfil reconocible en la primera conversación.
   3. ¿Qué cree que le falta, y qué le falta de verdad?
   4. ¿Qué suceso lo trae a comprar? — un evento con fecha, no "cuando está listo".
   5. ¿Cómo dice su problema? — una frase textual de un cliente real.
   6. ¿Tus últimos clientes a precio completo coinciden con eso? — con nombres de tu base.
2. **Revisa la checklist** de las 14 piezas (`references/piezas-del-avatar.md`). El
   núcleo son 01, 02, 03, 05, 12 y 14: sin esas seis no hay avatar operable.
3. **Puntúa 1-4:** 1 = no existe (no puede decir quién le compra en una frase) ·
   2 = existe en tu cabeza (no escrito, o escrito como demografía) · 3 = escrito pero
   no medido (núcleo en 03 · Avatar, sin contrastar con clientes reales o leads sin
   `Fit avatar`) · 4 = escrito, funcionando y medido (Avatar contra datos corrido con
   3 o más clientes que pagaron, brecha cerrada o declarada, leads activos con fit).
4. **Escribe en 🧭 Tablero de áreas**, fila 03 · Avatar: `Puntaje`, `Estado`
   (1-2 → Rota · 3 → En obra · 4 → Funciona), `Pieza que falta` (la primera del
   núcleo que no existe), `Próxima acción` (una sola, con verbo; nunca un menú),
   `Revisado` (hoy). `Cuello` no lo toca: se decide con las 8 áreas a la vista.

## Modo Construcción

En este orden, cada una escrita en 03 · Avatar antes de la siguiente (`references/plantilla-pagina-avatar.md`).

| # | Pieza | Pregunta que abre |
|---|---|---|
| 01 | Ficha en datos duros | "¿Quiénes fueron tus últimos clientes que pagaron?" |
| 02 | Lo que cree que le falta vs. lo que le falta | "¿Qué creía ese cliente que le faltaba cuando llegó?" |
| 03 | Dolores en su idioma | "¿Qué frase exacta te dijo sobre su problema?" |
| 04 | Preguntas que trae sin responder | "¿Qué se pregunta en la cabeza y no te dice?" |
| 05 | Ventana de compra | "¿Qué le pasó justo antes de escribirte?" |
| 06 | Miedos y su disfraz | "¿Qué objeción te dio, y qué miedo había debajo?" |
| 07 | Escalera: dolor hoy → dolor futuro | "Si no hace nada, ¿cómo se ve eso en seis meses?" |
| 08 | Situación deseada y motor real | "¿Qué quiere que pase, dicho por él? ¿Y para qué?" |
| 09 | Cómo sostiene el cambio | "¿Ejecuta sin que lo empujes, o se cae sin presión?" |
| 10 | Economía y triggers de compra | "¿Contra qué mide tu precio? ¿De quién es la plata?" |
| 11 | Contra qué compites y las cuatro puertas | "¿Qué haría si no te contrata?" |
| 12 | Filtro de entrada y anti-avatar | "¿A quién le vendiste y te arrepentiste?" |
| 13 | Dónde está | "¿Por dónde entraron los que pagaron?" |
| 14 | Ruteo por tramo | "¿A quién persigues, a quién mandas a otra cosa, a quién sueltas?" |

Flujo por pieza:
1. **Pregunta una cosa y espera.** Tú preguntas, él trae el caso: no inventes el avatar por él.
2. **Pide el caso detrás.** Cada rasgo necesita una fila con nombre, valor o frase
   textual. Sin caso, se escribe **Declarado**, no **Medido**.
3. **Devuélvele la pieza escrita** con la plantilla y pregunta si algo no calza con un cliente real.
4. **Guárdala en 03 · Avatar** y actualiza `Pieza que falta` en el Tablero.
5. **Al cerrar el núcleo**, escribe la frase madre y ofrece el cruce con GPT. Al
   cerrar las 14, ofrece Avatar contra datos.

Con menos de 3 clientes que pagaron, el avatar se escribe como hipótesis y se dice en
la primera línea de la página. Un caso aislado no define un avatar; un patrón de tres, sí.

## Modo Auditoría

1. **Recibe lo que pega**: descripción de cliente ideal, bio, landing, pieza, guion.
2. **Extrae a quién le habla de verdad**: situación, dolor, verbo de la promesa,
   ingreso implícito, a quién excluye.
3. **Contrástalo contra 03 · Avatar** (si no existe, contra las 6 preguntas del test).
4. **Entrega la tabla Veredicto:**

| Pieza | Criterio | Estado | Qué falta |
|---|---|---|---|
| Ficha | Situación, no demografía | ✅/⚠️/❌ | … |
| Dolor | Dicho con palabras del cliente | … | … |
| Anti-avatar | Alguien queda afuera, con nombre | … | … |
| Ventana | Nombra un suceso con fecha | … | … |
| Promesa | Usa el verbo del cliente, no el tuyo | … | … |

5. **Da la corrección concreta**: reescribe la línea que falla, no el texto entero.
6. **Revisa siempre la falla más cara:** si le habla a un perfil con cero cierres en
   👥 Leads y clientes, esa es la corrección número uno.

## Modo Avatar contra datos

Protocolo completo en `references/avatar-contra-datos.md`.

1. **Lee** el Documento de contexto (precio actual), 03 · Avatar (lo declarado),
   👥 Leads y clientes completo y 📞 Llamadas (`Resultado`, `Objeción principal`).
2. **Corre la higiene primero.** Cuenta fichas sin `Valor`, `Dolor` o `Canal de
   origen` y repórtalo. Nunca inventes el dato que falta.
3. **Arma los grupos** por `Etapa`: pagó precio completo (Cliente activo o Renovó con
   `Valor` igual o mayor al precio de ese momento) · pagó con descuento · Renovó ·
   Perdido · No es para mí (+ llamadas No calificaba).
4. **Responde las cinco preguntas:** ¿quién pagó? · ¿por qué canal entró (pesado por
   `Valor`)? · ¿qué valor sostuvo? · ¿qué tienen en común por **problema**, no por
   rubro? · ¿quién no pagó y por qué?
5. **Contrasta rasgo por rasgo** en la tabla | Rasgo | Declarado | Lo que dicen los
   datos | Brecha (Coincide · No coincide · Sin dato) | Qué cambia |.
6. **Separa causa propia de perfil.** Un descuento o una pérdida pueden ser error de
   venta. Revisa la nota de la llamada antes de sacar un segmento.
7. **Da un veredicto, no un menú:** "Tu comprador real es X. Tu avatar declarado es Y. Cambia Z."
8. **Escribe:** sección "Avatar contra datos · <fecha>" en 03 · Avatar, rasgos con
   respaldo pasan a **Medido**, línea en el historial, una fila en 🔁 Aprendizajes por
   brecha que cambia algo (`Área que corrige` = Avatar u otra área; `Fuente` =
   Cliente), `Revisado` en el Tablero.
9. **Lista las superficies desactualizadas** (bio, landing, oferta, guion, preguntas
   de captura), cada una con su hermana. Ofrece el cruce con GPT.

## Modo Calificar un lead

Criterio completo en `references/calificacion-y-anti-avatar.md`.

1. **Ubica la ficha** en 👥 Leads y clientes. Si no existe, no la crea: la ficha
   nace en Captura (`pb-captura`). Califica en el chat y deja la línea lista.
2. **Lee el filtro y el anti-avatar** en 03 · Avatar (piezas 12 y 14). Si no están
   escritos, dilo: la calificación sale marcada "provisional".
3. **Corre los filtros en orden** (el primero que falla decide): prerequisito
   verificable → anti-avatar (si calza, Bajo sin seguir) → intención (¿lo que pide
   calza con el formato que vendes?) → capacidad de sostenerlo (ingreso, tiempo,
   base) → dolor (piezas 02 y 03) → ventana (suceso con fecha) → co-decisor (se
   anota, no baja el fit).
4. **Asigna:** **Alto** = pasa todo y hay suceso con fecha. **Medio** = el perfil
   calza pero falta un dato clave o el suceso. **Bajo** = falla prerequisito,
   intención o capacidad, o cae en el anti-avatar.
5. **Escribe en la ficha:** `Fit avatar` + una línea al inicio de `Notas`, sin
   borrar lo anterior: `Fit <nivel> · <razón en una línea> · <fecha>`.
6. **Da el destino:** Alto → preparar la llamada (`pb-ventas`). Medio → la única
   pregunta que falta y cuándo hacerla. Bajo → a dónde va (otra oferta, producto,
   nada) y soltar el seguimiento; propone `Etapa` = No es para mí y solo la escribe
   si el dueño confirma.
7. **En lote** ("califica los leads nuevos"): fichas en Nuevo o Conversación con
   `Fit avatar` vacío → tabla | Lead | Fit | Razón | Destino | antes de escribir.

Manual antes que automático: las primeras 3 calificaciones las decide el dueño y la
skill solo contrasta. Después, la skill propone y el dueño confirma.

## El método

- **Se lee en quién te pagó, no en quién te gustaría.** Lo declarado es hipótesis;
  una fila con `Valor` es evidencia. Si chocan, gana el dato.
- **Situación, no demografía.** Edad, género y ciudad suelen medir dónde ya tenías
  confianza, no dónde está la demanda. Contexto, no filtro.
- **Por problema, no por rubro.** Dos negocios opuestos con el mismo cuello son el
  mismo cliente; dos del mismo rubro con cuellos distintos, no.
- **La brecha de atribución es la pieza más valiosa.** Cree que le falta una cosa y
  le falta otra: cada par "creía X, era Y" es diagnóstico, gancho y pregunta.
- **Sus palabras, no las tuyas.** Si la promesa usa un verbo que ninguno de tus
  compradores usó, le hablas a otro.
- **Se compra después de un suceso.** Estancamiento sin fecha no produce decisión.
- **El objetivo declarado casi nunca es el motor.** Suele ser liberar a alguien,
  probarse algo o no volver a un lugar. Se pregunta en la llamada.
- **Dejar ir es dar destino y soltar.** Fuera de avatar y dos interacciones sin
  agendar = tiempo regalado.
- **Un caso no mueve el avatar; tres sí.** Antes de sacar un segmento, revisa si la
  causa fue del cliente o tuya.

| Ejemplo | Medido mal | Medido bien |
|---|---|---|
| Describir al cliente ideal | "Mujeres emprendedoras de 30 a 45 que quieren crecer" | "Dueña de un servicio que vende ella misma, factura entre [A] y [B] al mes, llega después de perder a su única persona de ventas. 4 de mis últimos 6 clientes a precio completo" |
| Nombrar el dolor | "Tiene problemas de marketing" | "Cree que le faltan seguidores; le falta una oferta clara. 3 casos en la base. Textual: 'publico todos los días y nadie me compra'" |
| Calificar | "Buen fit, se ve muy interesado" | "Fit Medio · factura en rango y el dolor calza, pero no hay suceso: 'algún día quiero ordenar esto'" |
| Anti-avatar | "No trabajo con gente que no se compromete" | "No: quien quiere que se lo hagan y pregunta cuántas horas le dedico. Destino: le paso un proveedor" |

## Qué se apalanca con IA y qué no

**Se apalanca:**
- Extraer frases textuales de transcripts, DMs y notas (dolores, preguntas, miedos).
- Cruzar el avatar declarado contra 👥 Leads y clientes y marcar la brecha.
- Agrupar clientes por problema y pérdidas por motivo; proponer el borrador del `Fit avatar` contra filtros ya escritos.
- Leer una pieza o una landing y decir a quién le habla de verdad.
- Mantener el historial de cambios del avatar.

**No se apalanca:**
- Decidir a quién dejas ir: tiene costo de caja y lo firma el dueño.
- Inventar dolores o frases: un avatar de IA sin casos es ficción bien redactada.
- Levantar el motor real: se pregunta en vivo, en conversación.
- Elegir qué tramo persigues: es decisión de caja y de vida.
- Calificar en automático antes de haberlo hecho a mano tres veces.

## Errores que se repiten

- **Avatar escrito como demografía** ("30-45, mujeres, emprendedoras"). Falta: 01 Ficha en datos duros.
- **Describe a todos: nadie queda afuera.** Falta: 12 Filtro de entrada y anti-avatar.
- **Avatar aspiracional**: al que quieres venderle, no al que te compra. Falta: Avatar contra datos sobre 01.
- **El dolor escrito con tu vocabulario técnico.** Falta: 03 Dolores en su idioma.
- **Perseguir leads con fit pero sin suceso.** Falta: 05 Ventana de compra.
- **Responder la objeción literal en vez del miedo.** Falta: 06 Miedos y su disfraz.
- **Bajar el precio para cerrar a quien no es.** Falta: 10 Economía y 12 anti-avatar.
- **Mostrar el caso de éxito por rubro, no por problema.** Falta: 02 Lo que cree que le falta.
- **Cinco mensajes de seguimiento a quien nunca fue lead.** Falta: 14 Ruteo por tramo.
- **No saber por dónde llegan los que pagan.** Falta: 13 Dónde está.

## Notion — qué lee y qué escribe

| Página/Base | Lee | Escribe | Propiedades que toca |
|---|---|---|---|
| 📄 Documento de contexto | ✅ | — | — (precio actual, a quién, canal) |
| 02 · Oferta | ✅ | — | — (formato y precio que filtran el avatar) |
| 03 · Avatar | ✅ | ✅ | Las 14 piezas, frase madre, Avatar contra datos, historial |
| 🧭 Tablero de áreas | ✅ | ✅ | Fila 03: `Puntaje`, `Estado`, `Pieza que falta`, `Próxima acción`, `Revisado` |
| 👥 Leads y clientes | ✅ | ✅ | Escribe `Fit avatar`, `Notas` (línea de fit); `Etapa` = No es para mí solo con confirmación. Lee `Etapa`, `Valor`, `Dolor`, `Objeción`, `Canal de origen`, `Pieza de origen` |
| 📞 Llamadas | ✅ | — | Lee `Resultado`, `Objeción principal`, `Aprendizaje`, `Transcript` |
| 🔁 Aprendizajes | ✅ | ✅ | Crea filas: `Aprendizaje`, `Área que corrige`, `Fuente`, `Qué cambia`, `Estado` = Pendiente, `Fecha`. Lee las pendientes con `Área que corrige` = Avatar |

Nunca escribe un dato que el dueño no dio ni en otras páginas de área. Sin Notion,
entrega lo mismo en markdown y dice en qué sección de 03 · Avatar pegarlo.

## Cruce con GPT

Claude construye; GPT audita (Proyecto "Private Build OS" en ChatGPT con conector de
Notion, o Codex con estas skills). Notion es la única memoria. Nunca los dos en la misma pieza a la vez. Decide el dueño.

1. Cuando se cierra el núcleo del avatar o se corre Avatar contra datos, ofrece el
   cruce.
2. Arma el brief:

```
BRIEF DE CRUCE · Private Build OS · Área 03 Avatar
Contexto del negocio (del Documento de contexto): <qué vende, a qué precio, a quién
dice venderle, canal principal, meta a 90 días>
Qué construí: <la página 03 · Avatar completa, o su link si tienes el conector> +
<la lista de clientes reales de 👥 Leads y clientes: Etapa, Valor, Dolor, Canal de
origen, de los que están en Cliente activo, Renovó, Perdido y No es para mí>
Criterio contra el que se mide:
1. Cada rasgo marcado Medido sale de al menos una fila con nombre, valor o frase textual.
2. Un caso aislado no mueve el avatar; un patrón de tres, sí.
3. Se agrupa por problema, no por rubro.
4. El anti-avatar nombra perfiles reconocibles en la primera conversación, con destino.
5. Dolores y promesa usan las palabras del cliente, no las del dueño.
6. Estancamiento sin suceso con fecha no es ventana de compra.
Tu tarea: lee el avatar y la lista de clientes reales y señala dónde el avatar
declarado no coincide con quien de verdad compra: quién paga precio completo, quién
renueva y quién resultó "No es para mí". Marca rasgos declarados sin respaldo en la
lista y patrones de la lista que el avatar no nombra.
Responde solo con una tabla: Punto | Mantener o cambiar | Por qué (1 línea) | Propuesta concreta.
Máximo 7 filas. No reescribas la pieza completa. Si algo está bien, dilo y no lo toques.
```

   Si no quiere pasar nombres de clientes, usa iniciales o rubro: funciona igual.
3. Con "respuesta de GPT: …", contrasta fila por fila contra el criterio y entrega
   | Punto de GPT | Acepto / Rechazo | Por qué |. Se rechaza todo rasgo sin fila detrás.
4. Aplica lo aceptado en 03 · Avatar con línea en el historial. Si cambió el método,
   deja una fila en 🔁 Aprendizajes (`Fuente` = Decisión).

## Handoffs

| Situación | Pasa a | Qué le entrega |
|---|---|---|
| El avatar choca con lo que vendes o con el precio | `pb-oferta` | La brecha y el tramo que no calza con la oferta |
| Hay que escribir piezas para el avatar | `pb-contenido` | Frases textuales: pares "creía X, era Y", dolores, preguntas, escalera |
| Hay que ajustar qué se pregunta al entrar | `pb-captura` | Prerequisito, filtros y la pregunta de ventana para el formulario o el primer mensaje |
| Lead con Fit Alto que va a llamada | `pb-ventas` | Fit, razón, suceso, miedo probable y su disfraz |
| Lo que el cliente sostiene cambia lo que se entrega | `pb-entrega` | Pieza 09 (cómo sostiene el cambio) |
| Un aprendizaje de un cliente toca el avatar | `pb-success` | Las filas de 🔁 Aprendizajes con `Área que corrige` = Avatar |
| Cambio de avatar que es giro de posicionamiento | `pb-foundations` | La decisión, para medirla contra la meta del negocio |

## Lo que esta skill NO hace

- No escribe ganchos, carruseles ni guiones (`pb-contenido`) ni fija precio o promesa (`pb-oferta`).
- No conduce ni analiza la llamada de venta (`pb-ventas`) ni crea leads (`pb-captura`).
- No inventa rasgos, dolores ni frases sin un caso detrás.
- No marca a nadie como "No es para mí" sin confirmación del dueño.
- No decide el cuello del negocio.

## Frases de prueba

- "Arma mi avatar, tengo 5 clientes que me pagaron este año."
- "Revisa mi avatar contra mis clientes reales: ¿me compra quien creo?"
- "Califica a este lead: tiene una consultora y dice que no le alcanza el tiempo."

Método: Private Build · privatebuild-os

---

# Anexo · references/avatar-contra-datos.md

# Avatar contra datos — protocolo

El modo que convierte el avatar de hipótesis en evidencia. Contrasta lo que el
dueño declaró en 03 · Avatar contra quien de verdad compra, paga precio completo,
renueva, y quien resultó "No es para mí".

**Por qué existe.** El error más caro del área es hablarle durante meses a un perfil
que nunca compró. Se ve solo cuando alguien pone el avatar al lado de la lista de
clientes reales.

---

## 1. Qué se lee

| Fuente | Qué se saca |
|---|---|
| 📄 Documento de contexto | Precio actual (para saber qué es "precio completo") |
| 02 · Oferta | Precio y formato vigentes; si cambió, cuándo |
| 03 · Avatar | Cada rasgo declarado, con su etiqueta Medido / Declarado |
| 👥 Leads y clientes | `Nombre`, `Etapa`, `Valor`, `Dolor`, `Objeción`, `Canal de origen`, `Pieza de origen`, `Fit avatar`, `Notas` |
| 📞 Llamadas | `Resultado` (Cerró · Perdida · No calificaba · Lo pienso), `Objeción principal`, `Aprendizaje` |

Antes de leer, confirma los nombres de las propiedades con la base en vivo. Si una
no existe o se llama distinto, repórtalo; no asumas.

---

## 2. Higiene primero

Un avatar contrastado contra datos sucios es una opinión con tabla. Antes de
cualquier conclusión, cuenta y reporta:

- Fichas en Cliente activo o Renovó **sin `Valor`**.
- Fichas **sin `Dolor`**: no se puede agrupar por problema.
- Fichas **sin `Canal de origen`**: la pieza 13 queda ciega.
- Fichas en Perdido **sin motivo** en `Objeción` o `Notas`: la pérdida no enseña nada.
- Llamadas con `Resultado` = No calificaba cuya ficha no está en No es para mí.

Reporta los huecos como una línea arriba del análisis ("3 de 9 clientes sin Valor:
la lectura de precio es parcial"). Nunca los rellenes. Si falta un dato decisivo,
pregúntalo al dueño y escríbelo solo si él lo da.

---

## 3. Los grupos

| Grupo | Cómo se arma | Qué enseña |
|---|---|---|
| **A · Pagó precio completo** | Cliente activo o Renovó, `Valor` igual o mayor al precio de ese momento | Quién compra sin que lo empujes: el avatar real |
| **B · Pagó con descuento** | Cliente activo o Renovó, `Valor` menor al precio | Quién compra pero no valora igual. ¿Perfil o error de venta? |
| **C · Renovó** | `Etapa` = Renovó | Quién obtuvo resultado. A veces distinto del que compra primero |
| **D · Perdido** | `Etapa` = Perdido | Por qué no. Agrupar por motivo, no por nombre |
| **E · No es para mí** | `Etapa` = No es para mí + llamadas No calificaba | Si el anti-avatar declarado se está cumpliendo |

**Mínimo de evidencia.** Si A + C suman menos de 3, el avatar sigue siendo
hipótesis. Muestra lo que hay, marca la brecha como "sin evidencia suficiente" y di
cuántos clientes más hacen falta para leerlo.

**Precio que cambió.** Si el precio subió en el tiempo, "precio completo" se mide
contra el precio vigente cuando ese cliente compró. Pregúntalo si no está en 02 · Oferta.

---

## 4. Las cinco preguntas

| Pregunta | Dónde se responde | Trampa |
|---|---|---|
| ¿Quién pagó de verdad? | Grupo A y C | Contar propuestas enviadas como si fueran cierres |
| ¿Por qué canal entró? | `Canal de origen` pesado por `Valor` | Contar leads en vez de plata cobrada |
| ¿Qué valor sostuvo? | Mediana de `Valor` en A | Usar el precio de lista |
| ¿Qué tienen en común? | `Dolor` de A y C | Agrupar por rubro en vez de por problema |
| ¿Quién no pagó y por qué? | D y E, agrupados por motivo | Leer cada pérdida como caso aislado |

---

## 5. Cómo leer un caso que salió mal

Un cierre con descuento o una pérdida **no prueba que el perfil sea malo**. Antes de
sacar un segmento, revisa la nota de la llamada:

- ¿Había precio mínimo definido antes de negociar? Si no, el descuento fue tuyo.
- ¿Se sostuvo la objeción o se cedió antes de que la pidieran?
- ¿El caso que se mostró era parecido por problema o solo por rubro?

Si la causa fue de venta, la fila va a 🔁 Aprendizajes con `Área que corrige` =
Ventas, y el perfil se queda. Descartar un segmento por un error propio es cerrar un
canal que funcionaba.

**Un caso aislado no mueve el avatar. Un patrón de tres, sí.**

---

## 6. Correlaciones que se leen pero no se operan

Vas a encontrar concentraciones: una ciudad, un género, un rango de edad. Casi
siempre miden dónde ya tenías confianza previa, no dónde está la demanda. Anótalas
como contexto en la sección de la corrida. No las conviertas en filtro ni en rasgo.

---

## 7. La tabla de brecha

Rasgo por rasgo de lo declarado:

| Rasgo | Declarado | Lo que dicen los datos | Brecha | Qué cambia |
|---|---|---|---|---|
| Tipo de negocio | | | Coincide · No coincide · Sin dato | |
| Rango de ingreso | | | | |
| Valor que sostiene | | | | |
| Dolor principal | | | | |
| Canal por donde llega | | | | |
| Anti-avatar | | | | |

Después de la tabla, busca las tres brechas que más se repiten en negocios de
servicios:

1. **Le hablas a un perfil con cero cierres.** El avatar declarado no aparece en el
   grupo A. Es la corrección número uno: afecta contenido, captura y oferta.
2. **El que paga precio completo no es el que más conversa.** Mucho volumen de un
   perfil en Conversación y los cierres vienen de otro. El contenido está atrayendo
   al que no compra.
3. **El que renueva no es el que compra primero.** Lo que atrae y lo que retiene son
   distintos: el avatar se escribe con el que renueva.

---

## 8. El veredicto

Una sola lectura, nunca un menú:

```
Tu comprador real: <en una línea, con el grupo A delante>
Tu avatar declarado: <en una línea>
La brecha que más cuesta: <una>
Qué cambia: <la pieza de 03 · Avatar que se reescribe, y cómo>
Superficies desactualizadas: <bio, landing, oferta, guion, preguntas de captura>
```

---

## 9. Qué se escribe

1. **03 · Avatar** → nueva sección "Avatar contra datos · <fecha>" con: base usada
   (cuántos en cada grupo), huecos de higiene, tabla de brecha, veredicto.
2. **Rasgos de la ficha** → los que ahora tienen respaldo pasan de Declarado a
   Medido, con la fuente. Los que los datos contradicen se reescriben: gana el dato,
   no la página.
3. **Historial** de la página → una línea: fecha, qué cambió, por qué dato.
4. **🔁 Aprendizajes** → una fila por brecha que cambia algo:
   - `Aprendizaje`: la brecha en una línea.
   - `Área que corrige`: Avatar, o Oferta / Contenido / Captura / Ventas si la
     corrección es de ellas.
   - `Fuente`: Cliente.
   - `Qué cambia`: la acción concreta.
   - `Estado`: Pendiente. `Fecha`: hoy.
5. **🧭 Tablero de áreas** → `Revisado` = hoy; `Puntaje` se recalcula si cambió.

---

## 10. Refinamiento: cuando entra un dato nuevo

Entre corridas, un cliente nuevo, una pérdida o una llamada pueden mover el avatar.

1. **¿Sale de una fila con nombre, valor o frase textual?** Si es impresión, no
   entra.
2. **¿Contradice algo escrito?** Gana el dato. Corrige y deja la línea en el
   historial con fecha.
3. **¿Es un caso o un patrón?** Un caso se anota en la pieza como "a vigilar". Al
   tercer caso igual, se vuelve rasgo.
4. **Lista las superficies** que quedaron desactualizadas y a qué hermana va cada una.

**Cada cuánto correrlo.** Cada vez que sumes 3 clientes nuevos, o una vez al mes, lo
que llegue primero. `pb-success` lo pide cuando las filas de 🔁 Aprendizajes con
`Área que corrige` = Avatar se acumulan.

---

# Anexo · references/calificacion-y-anti-avatar.md

# Calificación y anti-avatar

Cómo se escribe el filtro de entrada (pieza 12), cómo se decide a quién dejar ir, y
cómo se asigna el `Fit avatar` de un lead. Todo esto es método: los perfiles,
rangos y señales concretas los define cada dueño con sus datos.

---

## 1. Los filtros, en orden

El orden importa: **el primero que falla decide**. Los de arriba descalifican
incluso a alguien con plata.

| # | Filtro | Pregunta | Si falla |
|---|---|---|---|
| 0 | Prerequisito verificable | ¿Hay una señal observable, antes de hablar, de que existe el negocio que puedes ayudar? | Bajo, salvo señal equivalente |
| 1 | Anti-avatar | ¿Calza con algún perfil de tu lista de "a quién no"? | Bajo, sin seguir |
| 2 | Intención | ¿Lo que pide calza con el formato que vendes? | Bajo |
| 3 | Capacidad de sostenerlo | ¿Tiene ingreso, tiempo y base para usar lo que le entregas sin que el trabajo caiga en ti? | Bajo o a otro tramo |
| 4 | Dolor | ¿Su problema calza con tu pieza 02 y 03? | Medio |
| 5 | Ventana | ¿Puedes nombrar el suceso con fecha que lo trajo? | Medio |
| 6 | Co-decisor | ¿Quién más decide y de quién es la plata? | No baja el fit; se anota |

### Filtro 0 — Prerequisito verificable

Una o dos señales que se pueden mirar **antes** de la llamada y que prueban que hay
un negocio andando, no una intención de tenerlo. Ejemplos de señales que usan
negocios de servicios: tiene clientes pagando hoy, publica con ritmo en su propia
cuenta, tiene web con forma de pago, tiene equipo o local, declara facturación en el
formulario.

**Matiz.** La señal es un proxy, no la cosa. Si falta, busca la equivalente antes de
descartar. Lo que no se negocia es lo que el proxy mide.

**Por qué existe.** Los cierres que más cuestan y los que se caen suelen compartir el
mismo perfil: talento, sin negocio formalizado. La venta se traba en el pago, no en
el valor.

### Filtro 2 — Intención

La pregunta es si lo que pide calza con **cómo** entregas, no solo con qué.

| Si vendes... | Calza | No calza |
|---|---|---|
| Acompañamiento para que él lo haga | "Quiero entender cómo hacerlo y que funcione sin mí" | "No tengo tiempo, hazlo tú" · "¿Cuántas horas me dedicas?" |
| Servicio hecho por ti | "Quiero sacarme esto de encima con alguien confiable" | "Quiero aprender a hacerlo yo" |

Escribe tu versión de esta tabla con frases reales de leads.

### Filtro 3 — Capacidad de sostenerlo

No es "¿tiene la plata?". Es **cuánto involucramiento aguanta su negocio sin que el
trabajo termine cayendo en ti.** Un cliente sin base suficiente, en un formato de
alta cercanía, convierte tu servicio en ejecución tuya al precio más bajo de tu
tabla. Por eso ingreso alto tampoco basta: sin haber vivido el problema en carne
propia, puede no sostener el nivel.

### Filtro 5 — Ventana

Estancamiento sin fecha no produce decisión. "Algún día quiero ordenar esto" es
Medio aunque todo lo demás calce. La pregunta para levantarla: "¿Qué pasó para que
me escribieras ahora y no hace seis meses?"

### Filtro 6 — Co-decisor

Pregunta activadora, en la primera conversación: "Además de ti, ¿quién tiene que
estar de acuerdo para que esto avance?" Si el co-decisor llega recién al cierre, el
ciclo se duplica. Anota quién es y de quién es la plata.

---

## 2. La rúbrica del Fit avatar

| Fit | Cuándo | Qué sigue |
|---|---|---|
| **Alto** | Pasa 0 a 5. Hay suceso con fecha | Preparar la llamada (`pb-ventas`) |
| **Medio** | El perfil calza pero falta un dato clave (ingreso, dolor, suceso) o es una excepción declarada | La única pregunta que falta, y en qué interacción hacerla |
| **Bajo** | Falla 0, 1, 2 o 3 | Destino (otra oferta, producto, nada) y soltar seguimiento |

**Formato de la razón**, al inicio de `Notas`, sin borrar lo anterior:

```
Fit Alto · factura en rango, dolor textual "no sé dónde se me van los clientes", suceso: perdió a su vendedor en marzo · 2026-09-11
Fit Medio · el dolor calza, pero no hay suceso con fecha ("algún día") · falta preguntar qué pasó ahora · 2026-09-11
Fit Bajo · pide que se lo hagan ("¿cuántas horas me dedicas?"); vendo acompañamiento · destino: proveedor · 2026-09-11
```

Una línea. Si no cabe en una, la razón no está clara todavía.

**Una sola respuesta.** Nunca "podría ser Alto o Medio". Si falta un dato, es Medio
y se dice cuál.

---

## 3. Señales en vivo

Frases que conviene tener escritas en la pieza 12, porque deciden rápido:

- **"Lo resuelvo yo" dicho tranquilo** = no hay dolor activo. No es un lead perdido:
  nunca lo fue. **Dicho frustrado** = venta real.
- **Una pregunta que revela el perfil.** Define la tuya. Ejemplo: si tu avatar no es
  sofisticado en tu tema, pregunta "¿qué usas hoy para esto?". Si nombra tres
  herramientas sin que se las menciones, es otro perfil.
- **Pide horas en vez de resultado** = quiere un empleado o un proveedor.
- **No puede decir cuánto le queda limpio** = no puede evaluar una inversión todavía.
- **Pide un caso de su mismo rubro** = no es objeción de precio, es falta de prueba.
  Manda el caso más parecido por problema, no por rubro.

---

## 4. Plantilla del anti-avatar

Dejar ir no es portazo: es darle su destino y soltar el seguimiento.

| Perfil | Por qué no | A dónde va |
|---|---|---|
| Quiere que se lo hagas y tú vendes acompañamiento (o al revés) | Compra otra cosa | Proveedor · nada |
| Quiere recuperar horas, no crecer | Necesita un empleado | Nada |
| Bajo el ingreso mínimo de tu tramo principal | No hay base sobre la cual construir | Oferta más liviana · vuelve cuando facture |
| Su presupuesto depende de un solo cliente grande | Cualquier turbulencia derrumba el alcance | Algo acotado, nunca el programa completo |
| Construye lo mismo que vendes | Compara tu cuota contra un sueldo, no contra el retorno | Nada, salvo prueba muy específica |
| "Ya lo estoy resolviendo" dicho sin frustración | No hay dolor activo | Nada; insistir quema relación |
| No puede nombrar qué está roto | Necesita diagnóstico antes que programa | Tu oferta de entrada, si existe |

Esta es una plantilla de patrones que se repiten en negocios de servicios. Borra
los que no aplican y agrega los tuyos, cada uno con al menos un caso real detrás.

**Regla del tiempo.** Todo lead fuera de tu tramo principal que consume más de dos
interacciones sin agendar es tiempo regalado. Se cierra el hilo.

**El que se parece a ti.** Quien quiere hacer lo mismo que tú pero está empezando
puede ser cliente de otro tramo. Solo el par ya establecido queda fuera.

---

## 5. Cómo se escriben los cortes de entrada

Dos o tres preguntas sí/no sobre el tipo de negocio. Tienen que dar las tres.

| # | Pregunta | Entra | No entra |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

Cómo encontrarlas: pon lado a lado a tus mejores clientes y a los que te costaron.
¿Qué pregunta de sí/no los separa? Ejemplos del tipo de pregunta que funciona:
"¿El dueño es quien entrega el servicio?", "¿Su crecimiento pasa por
conversaciones o por tráfico?", "¿Opera él mismo las herramientas o necesita que se
las operen?".

Y la **regla corta en vivo**, para decidir en la llamada sin abrir la página:

> Si su problema se resuelve con **___**, es mío. Si se resuelve con **___**, no.

---

## 6. Manual antes que automático

1. Las primeras 3 calificaciones las hace el dueño en voz alta. La skill solo
   pregunta qué filtro usó y lo contrasta con lo escrito.
2. Si su decisión no coincide con los filtros escritos, gana su decisión y se
   corrige el filtro (una fila en 🔁 Aprendizajes, `Área que corrige` = Avatar).
3. Después de tres coincidencias seguidas, la skill propone el fit y el dueño
   confirma.
4. Calificar en lote sin confirmación no existe en esta skill.

---

# Anexo · references/piezas-del-avatar.md

# Las 14 piezas del avatar

El detalle de cada pieza del Modo Construcción. Por cada una: qué es, la pregunta
que la abre, el formato en que queda escrita, de dónde sale el dato y el ejemplo
medido mal vs. medido bien.

Regla transversal: **cada rasgo lleva etiqueta.** **Medido** = sale de una fila de
👥 Leads y clientes o 📞 Llamadas con nombre, valor o frase textual. **Declarado** =
es una decisión del dueño (un vertical que prefiere, un perfil que no quiere). Las
dos valen; lo que no vale es mezclarlas sin decir cuál es cuál.

El núcleo operable son las piezas **01, 02, 03, 05, 12 y 14**. Con esas seis ya se
puede calificar un lead y escribir contenido que le hable a alguien.

---

## Bloque A — Quién es

### 01 · Ficha en datos duros

**Qué es.** El retrato mínimo, sacado de quienes ya pagaron.

**Pregunta que abre.** "¿Quiénes fueron tus últimos 3 a 5 clientes que pagaron?
Por cada uno: qué negocio tiene, cuánto factura más o menos, cuánto te pagó, quién
decidió la compra."

**Formato.**

| Rasgo | Valor | Medido / Declarado | Fuente |
|---|---|---|---|
| Tipo de negocio | | | |
| Rango de ingreso mensual | | | |
| Valor real que pagó (mediana) | | | |
| Quién decide | solo · con socio · con familia · con un tercero | | |
| Nivel de sofisticación en lo que vendes | | | |
| Verticales preferidos / fuera | | Declarado | |
| Propósito o motor típico | | | |

**Ojo.**
- El "valor real" es la mediana de lo cobrado, no tu precio de lista.
- "Quién decide" importa más de lo que parece: un co-decisor que no pasó por la
  primera conversación duplica el ciclo.
- Edad, género y ciudad: anótalos como contexto si quieres, pero no son rasgo. Casi
  siempre miden dónde ya tenías confianza, no dónde está la demanda.

| Medido mal | Medido bien |
|---|---|
| "Emprendedores de 25 a 40 con ganas de crecer" | "Dueños de servicios que venden ellos mismos, factura entre [A] y [B] al mes. Valor real pagado: [mediana] (5 cierres). Decide solo o con familia" |

### 02 · Lo que cree que le falta vs. lo que le falta

**Qué es.** La brecha de atribución: tu cliente siempre cree que le falta una
cosa más (una persona, capital, seguidores, una herramienta, disciplina) y lo que le
falta es otra. Es la pieza más valiosa del avatar: cada fila es diagnóstico, gancho
de contenido y pregunta de descubrimiento a la vez.

**Pregunta que abre.** "Cuando llegó ese cliente, ¿qué creía que le faltaba? ¿Y qué
resultó ser?"

**Formato.**

| Caso (rubro, anonimizado) | Cree que le falta | Le falta de verdad |
|---|---|---|

Cuando tengas 3 o más filas, busca el patrón: ¿se repite el mismo error de
atribución? Si sí, escríbelo en una línea arriba de la tabla. Ese patrón es la
mecánica central de tu avatar.

**Ojo.** El patrón se agrupa por problema, no por rubro. Un taller y una consultora
con el mismo error de atribución son el mismo cliente.

| Medido mal | Medido bien |
|---|---|
| "Mis clientes necesitan ayuda con sus ventas" | "Un taller creía que le faltaba contratar un vendedor; le faltaba un proceso que sobreviva a que ese vendedor se vaya. Mismo patrón en 3 de 5 casos: creen que les falta una persona, les falta el proceso" |

### 03 · Dolores en su idioma

**Qué es.** No la lista de síntomas técnicos: cómo **él** nombra el problema. Cada
línea sirve como gancho, como pregunta de descubrimiento y como fila para 🎬 Contenido.

**Pregunta que abre.** "¿Qué frase exacta te dijo sobre su problema? Búscala en el
chat o en la grabación, no la reconstruyas."

**Formato.**

| El dolor, dicho como él lo dice | Lo que revela |
|---|---|

**De dónde sale.** `Dolor` en 👥 Leads y clientes, `Transcript` y `Objeción
principal` en 📞 Llamadas, DMs. Si tienes transcripts, la IA puede extraer las frases;
tú eliges cuáles son de verdad.

**Ojo.** Las frases más potentes son las que solo puede escribir alguien que las
vivió. Si una frase suena a folleto, no la dijo un cliente.

| Medido mal | Medido bien |
|---|---|
| "Falta de estrategia de adquisición" | "'Invierto en anuncios y no veo el retorno' → no mide cuánto le deja cada cliente" |

### 04 · Preguntas que trae sin responder

**Qué es.** Las que se hace en la cabeza, no las que te dice. El contenido que las
formula textual es el que le hace sentir que le hablas a él.

**Pregunta que abre.** "¿Qué duda te repitió más de un cliente, aunque fuera de pasada?"

**Formato.** Lista numerada, cada pregunta entre comillas con el caso de donde sale.

Preguntas que suelen aparecer en negocios de servicios (úsalas para provocar
memoria, no para copiarlas): "¿Contrato a alguien o todavía no?", "¿Cuánto me queda
realmente?", "¿Por dónde empiezo?", "¿Es el negocio o soy yo el problema?",
"¿Cuánto tiempo más aguanto así?".

---

## Bloque B — Qué le pasa

### 05 · Ventana de compra

**Qué es.** Nadie llega por evolución: llega después de un suceso. Si no puedes
nombrar el evento que lo trajo, todavía no está en ventana.

**Pregunta que abre.** "¿Qué le pasó a ese cliente justo antes de escribirte?"

**Formato.**

| El suceso | Dónde se vio (caso anonimizado) |
|---|---|

Sucesos que se repiten en negocios de servicios: salió de un quiebre, una sucesión o
una separación de socios · chocó contra el techo de sus propias horas · cerró un
ciclo laboral · hay un mes concreto donde la curva se aplanó · perdió clientes contra
la competencia · está por abrir algo nuevo sobre una base desordenada · lleva meses
invirtiendo y no se sostiene · un tercero lo empuja (familia, socio, cliente grande).

**Regla de calificación.** Estancamiento sin fecha no produce decisión. Un lead con
buen perfil y presión difusa puede pasar un año pidiendo información gratis.

### 06 · Miedos y su disfraz

**Qué es.** Nunca te dice el miedo: te dice el disfraz. Reconocer el disfraz es lo
que te deja tratar el miedo en la llamada.

**Pregunta que abre.** "¿Qué objeción te dieron más de una vez? ¿Qué crees que había
debajo?"

**Formato.**

| El miedo real | Cómo se disfraza en la conversación |
|---|---|

| Medido mal | Medido bien |
|---|---|
| "Objeción: no es el momento" | "Miedo: 'sin presión externa pierdo el foco'. Disfraz: 'ahora no es el momento'. 2 casos" |

### 07 · Escalera: dolor hoy → dolor futuro

**Qué es.** El dolor de hoy es tolerable; por eso no compra. Lo que cierra es el
dolor futuro, que casi siempre es el mismo dolor escalado seis meses.

**Formato.**

| Hoy duele así | En 6 meses se convierte en |
|---|---|

Cierra la tabla con la tesis que sale de la columna derecha, en una línea.

**Complemento: la proyección al horizonte de tu oferta.** Si tu oferta dura 90 días,
compara ahí:

| | Sin cambiar nada | Con lo que entregas |
|---|---|---|
| Cómo consigue clientes | | |
| Cómo decide | | |
| Su rol | | |
| Al final del plazo | | |

Sirve tal cual en la llamada y como pieza de contenido.

### 08 · Situación deseada y motor real

**Qué es.** Cómo describe él lo que quiere, con sus frases. Casi nunca dice
"facturar más". Y debajo, el motor real: el objetivo declarado casi nunca es el
motor. Suele ser liberar a alguien, probarse algo o no volver a un lugar del que ya
salió.

**Pregunta que abre.** "¿Qué quiere que pase, dicho como lo dijo él? ¿Y para qué lo
quiere?"

**Formato.**

| Lo que dice que quiere (textual) | Motor real |
|---|---|

**Regla de copy.** La promesa se escribe con estas frases. Si la tuya usa un verbo
que ninguno de tus compradores usó, le hablas a otro.

**La pregunta que separa dos mundos**, para la primera llamada: "¿Qué quieres que
pase en tres meses: más ingresos o menos horas tuyas dentro?" Escucha cuál dice
primero. Quien busca liberar tiempo compra el parche más simple y barato; quien busca
crecer compra el cambio.

### 09 · Cómo sostiene el cambio

**Qué es.** Dos disciplinas distintas que se miden por separado:
- **Ejecución:** ¿hace el trabajo? (responde, entrega, se mueve).
- **Dirección:** ¿sostiene el foco sin presión externa?

Muchos dueños de servicios tienen la primera alta y la segunda baja. Si es tu caso,
cambia lo que vendes: el acompañamiento con fecha fija no es el canal, es parte del
producto; un curso suelto le llega a alguien que ya demostró que sin presión no
sostiene; y lo que entregas tiene que funcionar sin que él lo empuje.

**Pregunta que abre.** "¿Tus clientes hacen lo que acuerdan entre sesiones, o se caen
cuando nadie los sigue?" Pide casos.

**Va a:** `pb-entrega` y `pb-oferta`.

### 10 · Economía y triggers de compra

**Qué es.** Cómo se comporta su plata. Nada de esto tiene que ver con si tiene
dinero: decide si compra.

**Formato.**

| Rasgo | Lo medido | Qué implica para vender |
|---|---|---|
| Ingreso | | |
| Margen (¿lo conoce?) | | |
| Cuánto invierte hoy en conseguir clientes | | |
| Contra qué evalúa tu precio | | |
| De quién es la plata | | |
| Su propio sueldo | | |
| Estacionalidad | | |

**Los tres triggers que se anticipan antes de la llamada:**
1. **Precondición:** "necesito tener caja primero". No se resuelve en la llamada: se
   resuelve declarando la estructura de pago antes.
2. **Porcentaje:** bajo cierto ingreso, el precio se evalúa como porcentaje de lo que
   entra, no contra lo que devuelve. Anclar contra el costo de no hacerlo.
3. **Comparación con sueldos:** si tu cuota supera lo que el dueño se paga a sí mismo,
   pierdes por comparación aunque el retorno cierre.

**Regla.** Quien no puede decir cuánto le queda limpio no puede evaluar una
inversión. Pregúntalo en la primera o segunda interacción, no en la propuesta.

**Co-decisor.** Mapea quién más decide y de quién es la plata. Qué tipo de co-decisor
te ayuda y cuál te frena (familia, socio, un tercero que paga) lo dicen tus datos, no
una regla general.

### 11 · Contra qué compites y las cuatro puertas

**Qué es.** Casi nunca compites contra otro como tú. Compites contra alternativas,
y la que más gana es no hacer nada.

**Formato.**

| Su alternativa | Por qué la considera | Por qué pierde | Tu frase |
|---|---|---|---|

Las alternativas típicas para revisar cuáles aplican: contratar a alguien · una
agencia o proveedor que lo haga · un curso o mentoría · hacerlo solo con IA · un
especialista de un solo canal · no hacer nada. Para "no hacer nada", la respuesta
es la escalera de la pieza 07.

**Las cuatro puertas: qué necesita antes de comprar.**

| Puerta | Qué tiene que pasar | Qué tienes hoy para eso |
|---|---|---|
| VER | Lo que entregas funcionando, no explicado | |
| OÍR | Su propia frase de vuelta, antes de cualquier propuesta | |
| SABER | Qué queda en sus manos al terminar y qué no vas a hacer | |
| SENTIR | Que alguien ya recorrió eso y no lo juzga | |

**Ojo.** El caso de éxito se presenta por similitud del problema, nunca por rubro.
El mismo caso puede cerrar a un lead y descartar a otro según cómo se presente.

---

## Bloque C — Dónde está y a dónde va

### 12 · Filtro de entrada y anti-avatar

**Qué es.** A quién no se le vende, aunque pague. Si nadie queda afuera, describiste
a todos. Detalle completo en `calificacion-y-anti-avatar.md`.

**Pregunta que abre.** "¿A quién le vendiste y te arrepentiste? ¿Qué tenía en común?"

**Formato.** Cuatro partes y una opcional:
1. **Prerequisito verificable:** 1 o 2 señales observables antes de la llamada de que
   existe el negocio que puedes ayudar.
2. **Cortes de entrada:** 2 o 3 preguntas sí/no. Tabla | # | Pregunta | Entra | No entra |.
3. **La regla corta en vivo:** "Si su problema se resuelve con ___, es mío. Si se
   resuelve con ___, no."
4. **Anti-avatar:** tabla | Perfil | Por qué no | A dónde va |.
5. (Opcional) **Filtro de propósito:** a quién no le habla tu marca aunque tenga la
   plata y el dolor se parezca.

### 13 · Dónde está

**Qué es.** Por dónde llegaron los que pagaron. Casi todos los negocios de servicios
saben con precisión qué le duele a su cliente y no saben dónde pasa el rato.

**Formato.**

| Origen | Cuánto se cobró por ahí | Cuántos clientes |
|---|---|---|

Sale de `Canal de origen` y `Valor` en 👥 Leads y clientes. Se pesa por valor cobrado,
no por cantidad de leads.

**Las cuatro preguntas para levantar distribución**, al final de cada llamada, en
treinta segundos (no una encuesta):
1. ¿A quién sigues que te haya hecho pensar distinto este mes?
2. ¿Dónde estabas cuando decidiste que esto tenía que cambiar?
3. ¿Qué compraste antes que no funcionó, y qué te prometía?
4. ¿En qué grupo, comunidad o chat hablas de esto con alguien?

Con cinco respuestas ya hay mapa. Guárdalas en `Notas` del lead y súmalas aquí.

**El músculo débil.** Si todo lo que cobraste vino de gente que ya te conocía,
dilo en esta pieza. Es la señal para `pb-contenido`: falta construir la entrada.

### 14 · Ruteo por tramo

**Qué es.** No todos los que califican van al mismo lugar. Divide por la variable
que más predice cuánto puede sostener lo que vendes (casi siempre ingreso del
negocio) y dale a cada tramo su destino.

**Formato.**

| Tramo | Rango | Qué necesita | Qué paga (medido) | Destino | ¿Se persigue? |
|---|---|---|---|---|---|

- Los rangos salen de tus datos: dónde cortan los que pagaron precio completo y
  los que pidieron descuento o no renovaron. No los inventes redondos.
- Un tramo que no persigues no es gente descartada: se le da otra oferta más
  liviana, un producto, o nada, y se suelta el seguimiento.
- Una excepción (alguien fuera de tramo que igual entra) se marca como apuesta en
  `Notas`, no disuelve la regla.

---

## La frase madre

Al cerrar el núcleo, escribe arriba de la página una frase que junte todo:

> Un **[quién, en su situación]** que **[lo que ya intentó]**, que cree que le falta
> **[X]** cuando le falta **[Y]**; que mide tu precio contra **[qué]**; que se mueve
> cuando **[suceso]**; y cuyo motor real es **[motor]**.

Si no puedes llenar un corchete con un caso, esa es la próxima pieza a trabajar.

---

# Anexo · references/plantilla-pagina-avatar.md

# Plantilla — página 03 · Avatar

La estructura con que la skill deja escrita la página del área dentro de
"🏗️ Private Build OS". Se llena de a una pieza. Lo que no tiene caso detrás se
marca **Declarado**; lo que sale de 👥 Leads y clientes o 📞 Llamadas, **Medido**.

Si Notion no está conectado, la skill entrega cada bloque en este mismo formato,
en markdown, y dice en qué sección pegarlo.

---

```markdown
# 03 · Avatar — A quién le vendes y a quién no

> Estado: Hipótesis | Contrastado con datos (<fecha>, <N> clientes)
> Última revisión: <fecha>

## La frase madre
Un <quién, en su situación> que <lo que ya intentó>, que cree que le falta <X>
cuando le falta <Y>; que mide tu precio contra <qué>; que se mueve cuando
<suceso>; y cuyo motor real es <motor>.

---

## A · Quién es

### 01 · Ficha en datos duros
| Rasgo | Valor | Medido / Declarado | Fuente |
|---|---|---|---|
| Tipo de negocio | | | |
| Rango de ingreso mensual | | | |
| Valor real que pagó (mediana) | | | |
| Quién decide | | | |
| Nivel de sofisticación en lo que vendes | | | |
| Verticales preferidos / fuera | | Declarado | |
| Motor típico | | | |

### 02 · Lo que cree que le falta vs. lo que le falta
Patrón: <una línea, si hay 3 o más casos>
| Caso (rubro) | Cree que le falta | Le falta de verdad |
|---|---|---|

### 03 · Dolores en su idioma
| El dolor, dicho como él lo dice | Lo que revela |
|---|---|

### 04 · Preguntas que trae sin responder
1. "<pregunta>" — <caso>

---

## B · Qué le pasa

### 05 · Ventana de compra
| El suceso | Dónde se vio |
|---|---|
Regla: sin suceso con fecha, no está en ventana.

### 06 · Miedos y su disfraz
| El miedo real | Cómo se disfraza |
|---|---|

### 07 · Escalera: dolor hoy → dolor futuro
| Hoy duele así | En 6 meses se convierte en |
|---|---|
Tesis: <una línea>

Proyección al plazo de la oferta:
| | Sin cambiar nada | Con lo que entregas |
|---|---|---|

### 08 · Situación deseada y motor real
| Lo que dice que quiere (textual) | Motor real |
|---|---|

### 09 · Cómo sostiene el cambio
- Disciplina de ejecución: <alta / media / baja> — evidencia:
- Disciplina de dirección: <alta / media / baja> — evidencia:
- Qué implica para lo que entregas:

### 10 · Economía y triggers de compra
| Rasgo | Lo medido | Qué implica para vender |
|---|---|---|
Triggers a anticipar antes de la llamada:
Co-decisor típico:

### 11 · Contra qué compites y las cuatro puertas
| Su alternativa | Por qué la considera | Por qué pierde | Tu frase |
|---|---|---|---|

| Puerta | Qué tiene que pasar | Qué tienes hoy |
|---|---|---|
| VER | | |
| OÍR | | |
| SABER | | |
| SENTIR | | |

---

## C · Dónde está y a dónde va

### 12 · Filtro de entrada y anti-avatar
Prerequisito verificable:
Cortes de entrada:
| # | Pregunta | Entra | No entra |
|---|---|---|---|
Regla corta en vivo: si su problema se resuelve con ___, es mío. Si se resuelve con ___, no.

Anti-avatar — a quién no se le vende:
| Perfil | Por qué no | A dónde va |
|---|---|---|

Filtro de propósito (opcional):

### 13 · Dónde está
| Origen | Cobrado por ahí | Clientes |
|---|---|---|
Respuestas a las cuatro preguntas de distribución: <acumuladas>

### 14 · Ruteo por tramo
| Tramo | Rango | Qué necesita | Qué paga (medido) | Destino | ¿Se persigue? |
|---|---|---|---|---|---|
Regla del tiempo: fuera de tramo + 2 interacciones sin agendar = se cierra el hilo.

---

## Avatar contra datos · <fecha>
Base: A <n> · B <n> · C <n> · D <n> · E <n>
Huecos de higiene: <lista>
| Rasgo | Declarado | Lo que dicen los datos | Brecha | Qué cambia |
|---|---|---|---|---|
Veredicto:
- Tu comprador real:
- Tu avatar declarado:
- La brecha que más cuesta:
- Qué cambia:
- Superficies desactualizadas:
Correlaciones anotadas (no se operan):

---

## Historial
- <fecha> — <qué cambió> — <por qué dato o decisión>
```

---

## Reglas de mantenimiento

- **Se actualiza, no se recrea.** Una corrida nueva de Avatar contra datos se agrega
  arriba de la anterior; la vieja se queda como registro.
- **Cada cambio deja una línea en el historial**, con el dato que lo provocó.
- **Anonimiza por rubro** cualquier caso que vaya a salir de esta página (un
  carrusel, una landing, un brief de cruce). La página es interna; lo que se publica,
  no.
- **Una sola fuente.** Si el avatar aparece en otra parte (bio, landing, guion), esa
  es un reflejo de esta página. Cuando esta cambia, se lista qué reflejos quedaron
  viejos; nunca se corrige al revés.
