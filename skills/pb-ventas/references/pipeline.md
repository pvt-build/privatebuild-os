# Pipeline — higiene y qué lead mover esta semana

Un pipeline calculado sobre una llamada que nunca pasó no vale nada. Por eso la
higiene va antes que la prioridad, siempre.

## Qué se lee

- 👥 Leads y clientes: filas con `Etapa` en Conversación, Llamada agendada o Propuesta. Propiedades: `Nombre`, `Etapa`, `Canal de origen`, `Fit avatar`, `Dolor`, `Objeción`, `Próximo paso`, `Fecha próximo paso`, `Valor`, `Notas`.
- 📞 Llamadas: todas las filas relacionadas con esos leads (`Lead`, `Fecha`, `Tipo`, `Resultado`).

Antes de consultar, confirma que las propiedades existen con esos nombres. Si una no está, repórtalo como hallazgo; no lo corrijas en silencio.

## Paso 1 · Higiene

| Chequeo | Cómo se detecta | Qué significa |
|---|---|---|
| **Huérfano** | `Etapa` = Llamada agendada, `Fecha próximo paso` ya pasó, y no hay fila en 📞 Llamadas con esa fecha | La llamada no pasó, o pasó y no se registró. Las dos piden una decisión hoy |
| **Fecha vencida** | `Fecha próximo paso` anterior a hoy, sin llamada ni cambio de `Etapa` | La próxima acción nunca se ejecutó |
| **Sin próximo paso** | `Próximo paso` vacío, o sin `Fecha próximo paso` | No es pipeline: es una lista de nombres |
| **Pausa sin gatillo** | `Notas` o `Próximo paso` dice "esperar", "reactivar cuando…" sin condición ni fecha | Postergación. Una pausa con gatillo claro no es problema |
| **Etapa incoherente** | La `Etapa` no coincide con el último `Resultado` en 📞 Llamadas (ej. Resultado "Cerró" y Etapa "Propuesta") | El registro miente sobre dónde está el lead |
| **Registro débil** | Muchos leads en Llamada agendada o Propuesta y pocas filas en 📞 Llamadas | Alerta estructural: el hábito de registrar después de cada llamada no está firme. Se reporta una vez, no como N tareas |

### Umbrales de frescura

Días desde la última fila en 📞 Llamadas (o desde la fecha más reciente escrita en `Notas`, si es posterior: léela, no la asumas).

| Días sin movimiento | Lectura |
|---|---|
| < 7 | Sano. No entra al reporte salvo fecha vencida |
| 7-21 | Atención, si no hay llamada registrada |
| > 21 sin llamada registrada | Crítico: la próxima acción nunca se ejecutó |
| > 60 sin llamada y sin fecha de reactivación | Candidato a cerrar: pregunta si pasa a Perdido |

**Nunca marques un lead como Perdido sin preguntar.** Puede que la llamada haya pasado y no se cargó.

## Paso 2 · Prioridad de la semana

Orden, de mayor a menor peso:

1. Huérfano o fecha vencida sin resolver (siempre primero, independiente del valor).
2. `Valor` más alto entre los que quedan.
3. Más días sin movimiento.
4. Conversación abierta hace mucho que nunca pasó a llamada formal: interés alto con ciclo nunca formalizado.

Los leads que comparten el mismo hueco exacto (por ejemplo, cinco en Conversación sin próximo paso) no se listan uno por uno: se resuelven con un mensaje tipo.

### Lectura por situación (el porqué de cada fila)

| Situación del lead | Lectura | Movimiento |
|---|---|---|
| `Valor` alto y conversación abierta hace semanas | El riesgo no es el precio: es que se enfríe | Ponerle fecha a una llamada |
| "Lo pienso" sin fecha en la última llamada | No es pipeline activo | Un mensaje que nombre qué tiene que pensar + dos fechas |
| "Se mueve cuando vea un caso como el suyo" | No es objeción de precio: es falta de prueba | Mandar el caso más parecido por estructura, no por rubro |
| Falta el co-decisor | El ciclo se duplica si no entra | Proponer la conjunta con dos horarios |
| Referido con `Fit avatar` Alto | Potencial alto | Acelerar: llamada esta semana |
| Cliente activo que termina pronto | La renovación se conversa antes de que venza | Pasar a `pb-success` |

## Paso 3 · La foto, sin inflarla

| Bloque | Qué suma |
|---|---|
| **Comprometido** | `Valor` de los leads en Propuesta con `Fecha próximo paso` esta semana |
| **Posible** | `Valor` de los leads en Llamada agendada con fecha futura |
| **Fuera de la cuenta** | Todo lo huérfano, vencido, sin próximo paso o en pausa sin gatillo |

- Tasas de cierre por etapa: solo con 10 llamadas registradas o más, calculadas desde el `Resultado` de 📞 Llamadas del propio negocio. Antes de eso no hay proyección, y se dice.
- Si `Valor` está vacío, no se completa con un supuesto: se deja fuera de la suma y se reporta cuántos faltan.

## Paso 4 · Pérdidas: se leen por motivo, no por nombre

Agrupa los leads en Perdido y No es para mí por el motivo en `Notas`:

| Motivo que se repite | A qué área apunta | Qué se hace |
|---|---|---|
| Precio + no era perfil | Avatar / Captura | Señal de calificación, no de cierre. No se persigue |
| Quería otra cosa | Contenido / Oferta | Revisar qué prometió la pieza que lo trajo |
| Etapa equivocada (todavía no) | Captura | Puede volver: recontacto con fecha y motivo |
| Objeción no resuelta en la llamada | Ventas | Al análisis post-llamada; si se repite, a la biblioteca de reencuadres |

Un caso aislado no mueve nada. Un patrón de tres va a 🔁 Aprendizajes con su `Área que corrige`.

## Salida del modo Pipeline

```
PIPELINE · semana del <fecha>

Higiene
- Huérfanos: <n> — <nombres>
- Fechas vencidas: <n> — <nombres>
- Sin próximo paso: <n>
- Alerta estructural: <si aplica, una línea>

Los 3 leads a mover esta semana
1. <Nombre> — <porqué en una línea> — <acción> — <día>
   Mensaje: "<texto listo para copiar>"
2. …
3. …

Foto: comprometido <suma> · posible <suma> · fuera de la cuenta <n leads>
Pérdidas del mes por motivo: <motivo: n>

Para confirmar antes de escribir en Notion: <cambios de Etapa / Próximo paso / Fecha próximo paso>
```

Nada se escribe en 👥 Leads y clientes sin su confirmación, salvo que diga "aplica directo". Ningún campo vacío se rellena con un valor inventado.
