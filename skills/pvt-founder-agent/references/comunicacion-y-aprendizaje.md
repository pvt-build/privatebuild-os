# Cómo comunicas y cómo aprendes — Ethos, Pathos, Logos y las dos capas

La confianza en público no se construye con un pitch: se construye con tres piezas, y hacen falta
las tres juntas. Sola, cada una se siente incompleta:

| Solo esta | Se siente como |
|---|---|
| Ethos | Currículum sin alma |
| Pathos | Storytelling sin sustancia |
| Logos | Informe que nadie termina de leer |

Las tres viven en el **banco de credibilidad** de 01 · Foundations. Salen de ahí a `pvt-content-agent`
(piezas) y a `pvt-closing-agent` (prueba en llamada). La IA ordena la historia que viviste; no te da una.

## 1. Ethos — credibilidad que se demuestra

Un patrón que no se puede fingir: hiciste lo que dices, en público, más de una vez, y mostraste
también cuando no funcionó a la primera.

**Regla:** no es "cuenta que lo probaste". Es cuenta *cómo y cuándo falló* antes de funcionar. El
error nombrado con especificidad convierte una afirmación en credibilidad.

| ✕ Sin ethos | ✓ Con ethos |
|---|---|
| "Acá está el proceso de onboarding que uso con mis clientes." | "Este onboarding lo corrí primero con mis tres primeros clientes. En la primera versión pedía todo el material el día uno y dos se trabaron una semana. La versión que uso hoy pide una cosa por día; nació de ese error." |

Preguntas (de a una):
1. ¿Lo hiciste tú, con tus manos, antes de enseñarlo?
2. ¿Puedes nombrar la fecha o el caso concreto donde lo probaste por primera vez?
3. ¿Qué error real cometiste haciéndolo, y qué corregiste después?
4. ¿Qué parte de tu proceso omites porque "no se ve bien"? Probablemente sea tu ethos más fuerte.

Criterios de auditoría:
- Hay un "yo lo hice" con fecha o caso → ✅ / sin fecha → ⚠️ / solo afirmación → ❌
- El error está nombrado con detalle (qué se rompió, por qué) → ✅ / genérico ("tuve que ajustar") → ⚠️
- La corrección se conecta con la versión actual → ✅

## 2. Pathos — conexión

La gente no recuerda argumentos: recuerda cómo se sintió. Solo resultados pulidos generan
admiración a distancia, no conexión. La conexión aparece con la duda real, con el detalle exacto
que la hace creíble.

**Regla:** la duda sin detalle es queja; la duda con fecha, número o decisión concreta es Pathos.

| ✕ Resultado pulido | ✓ Con detalle real |
|---|---|
| "Subí mis precios y me fue bien." Nadie se reconoce ahí. | "La noche antes de mandar la propuesta con el precio nuevo la reescribí tres veces con el precio viejo. La mandé igual. El cliente respondió al día siguiente con una sola pregunta: cuándo empezábamos." |

Preguntas:
1. ¿Cuál fue el momento exacto en que dudaste de que esto iba a funcionar?
2. ¿Qué dato concreto (fecha, número, decisión) hace esa duda real y no genérica?
3. ¿Qué normalmente omites de esa historia porque "no queda bien"?
4. Si alguien leyera solo esa historia, ¿se sentiría reflejado o solo te admiraría a distancia?

Criterios de auditoría:
- Hay un momento de duda identificable → ✅ / "fue difícil" → ❌
- Tiene al menos un dato (fecha, número, decisión) → ✅
- No está inventado ni exagerado → si hay sospecha, se pregunta. **Nunca se fabrica Pathos**: la
  duda inventada se nota y quema la credibilidad que sí tenías.

## 3. Logos — evidencia dura

Sin Logos, Ethos y Pathos se sienten bien pero no convencen a quien decide con la cabeza. Dos
piezas que se complementan: **el caso** (un resultado real con cifra) y **el sistema** (el proceso
replicable detrás, que prueba que no fue suerte).

**Regla:** un caso sin sistema se siente anecdótico; un sistema sin caso se siente teórico. La cifra
prueba que pasó; el paso a paso prueba que es replicable.

| ✕ Opinión | ✓ Caso + sistema |
|---|---|
| "Mi método funciona muy bien." | "Con este método una clienta pasó de cerrar 2 de cada 10 llamadas a 4 de cada 10 en dos meses. Este es el paso que cambió: dejó de mandar la propuesta por escrito y la presentó en la misma llamada." |

Preguntas:
1. ¿Qué cifra o resultado concreto respalda esta afirmación?
2. ¿Puedes nombrar el caso real detrás (tipo de cliente, fecha, número)?
3. ¿Existe el sistema replicable detrás, o fue suerte una vez?
4. Si alguien pidiera la prueba ahora mismo, ¿la tienes a la mano o hay que fabricarla?

Si hay que fabricarla, no la tienes. Se escribe "no existe todavía" y la próxima acción es generar
el registro (`pvt-consulting-agent` mide el resultado del cliente; `pvt-success-agent` lo recoge).

Criterios de auditoría:
- Hay cifra → ✅ / "muchos", "bastante" → ❌
- Hay sistema nombrado (qué se hizo distinto) → ✅
- El cliente del caso no queda identificable sin su permiso → ✅ (ver capa privada)

## 4. Plantilla del banco de credibilidad (01 · Foundations)

```
BANCO DE CREDIBILIDAD · actualizado el <fecha>

ETHOS — el error mejor contado
Qué hice: <…> · Cuándo: <…> · Qué se rompió: <…> · Qué corregí: <…>

PATHOS — la duda con dato
El momento: <…> · El dato que lo hace real: <…> · Qué hice igual: <…>

LOGOS — caso + sistema
Caso: <tipo de cliente> pasó de <X> a <Y> en <tiempo> · Sistema: <el paso que cambió>
Prueba a la mano: <dónde está el registro>

Usado en: <pieza o llamada, fecha>
```

## 5. Privado vs transferible — las dos capas de un aprendizaje

Todo founder acumula aprendizajes tocando decisiones privadas: societarias, legales, familiares,
con clientes. **La capa privada nunca se comparte tal cual. El principio transferible sí,
anonimizado.** Se enseña el patrón, nunca el detalle que compromete a un tercero.

| ✕ Capa privada | ✓ Principio transferible |
|---|---|
| Quién dijo qué, los montos, los nombres, la negociación. No sale, ni anonimizada, ni "entre nosotros". | "Un acuerdo sin fecha de salida escrita no es un acuerdo: es una deuda con quien tenga más aguante." Enseña sin exponer. |

**Test de identificabilidad:** si al leerlo alguien que conoce a las partes puede identificar
quién es, todavía es capa privada, no importa cuánto se haya anonimizado. Cambiar el nombre no
basta si quedan el rubro, la ciudad, el monto o la fecha.

Protocolo:
1. El cliente cuenta el episodio completo en el chat. **Eso no se guarda en Notion.**
2. Preguntas: ¿quién es el tercero involucrado (socio, cliente, familia)? ¿Qué parte nunca se
   comparte?
3. Devuelves solo el principio: una o dos frases, sin nombres, montos, fechas ni rasgos
   identificables. Formato útil: *"<situación genérica> no es <lo que parece>: es <lo que realmente
   es>"*, o *"Antes de <acción>, <condición>"*.
4. Pasas el test de identificabilidad en voz alta. Si falla, se generaliza más.
5. Se guarda en 01 · Foundations, bloque "Aprendizajes transferibles": el principio, la fecha y en
   qué se usó. Nada de la capa privada.

Por qué la IA sirve acá: es una tarea de reescritura, y el cliente está demasiado cerca del caso
para ver qué lo delata.

Criterios de auditoría (cuando pega un post o un texto que ya escribió):
- No hay nombres, montos ni detalles que identifiquen → ✅
- Pasa el test de identificabilidad → ✅ / duda razonable → ⚠️ y se generaliza
- Enseña un principio aplicable a otro negocio → ✅ / solo narra el conflicto → ❌
- Si el texto expone a un tercero, el veredicto es **no publicar** esa versión; se reescribe como
  principio.
