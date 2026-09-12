# Revisión del loop — de lo que pasó a una corrección por área

Fuente de verdad del modo **Revisión del loop** de `pvt-success-agent`. Es lo que hace
que la octava área no venga después de las otras siete, sino encima: mide lo que
produjeron y les devuelve la corrección.

> Sin la octava, las otras siete se construyen una vez y se quedan como quedaron.

La información siempre existe. Lo que falta casi nunca es el dato: es el circuito
que lo devuelve al área que lo tiene que corregir.

---

## 1 · Cadencia

| Situación del negocio | Cadencia | Ventana que se lee |
|---|---|---|
| 3+ clientes activos o 10+ conversaciones nuevas por semana | Semanal, 20 minutos | Los últimos 7 días |
| Menos que eso | Mensual, 45 minutos | Los últimos 30 días |
| Menos de 3 clientes cerrados en total | Mensual, y todo lo que salga se reporta como **señal**, no como patrón | Todo el histórico |

Siempre el mismo día. Una revisión que se mueve de fecha deja de hacerse.
Se corre a mano tres veces antes de automatizar cualquier parte.

---

## 2 · Qué se lee, en este orden

1. **🔁 Aprendizajes** — todas las filas con `Estado = Pendiente`. Primero lo que
   las otras áreas ya anotaron; después lo nuevo.
2. **👥 Leads y clientes** — filas cuya `Etapa` cambió en la ventana, sobre todo a
   `Perdido`, `No es para mí`, `Renovó` y `Cliente activo`. De cada una: `Canal de
   origen`, `Pieza de origen`, `Fit avatar`, `Dolor`, `Objeción`, `Notas`.
3. **📞 Llamadas** — las de la ventana: `Tipo`, `Resultado`, `Objeción principal`,
   `Escala 1-10`, `Aprendizaje`.
4. **🎬 Contenido** — piezas `Publicada` en la ventana: `Formato`, `Gancho`, `Dolor
   que toca`, `Métrica principal`, `Conversaciones generadas`, `Veredicto`.
5. **Registro semanal de cartera** (tabla en `08 · Success`) — medidores en rojo.
6. **⚖️ Decisiones** — las de la ventana, para saber si un resultado viene de una
   decisión tomada.

### Chequeo de higiene antes de concluir

No se saca patrón de un registro roto. Cuenta los huecos:

- Leads con `Etapa` sin mover en más de 14 días y sin `Fecha próximo paso`.
- Llamadas sin `Resultado` o sin `Objeción principal`.
- Filas en `Perdido` o `No es para mí` sin `Notas`.
- Leads sin `Canal de origen` o sin `Pieza de origen`.
- Piezas `Publicada` sin `Conversaciones generadas`.

Si los huecos pasan de un tercio de las filas de la ventana, la primera corrección
de la revisión es de registro (normalmente **05 · Captura**) y todo lo demás se
reporta como hipótesis. Nunca rellenes un hueco con una estimación presentada
como dato.

---

## 3 · La tabla de ruteo — qué síntoma habla de qué área

Es el corazón del modo. Un evento con un cliente siempre es información de un área.

| Síntoma en los datos | Área que corrige | Por qué esa y no otra |
|---|---|---|
| Cliente que no vuelve (no renueva, no sube, se va) | **07 · Entrega** | Lo que entregaste no produjo algo que quiera repetir |
| Dos "no" seguidos de adherencia en 2+ clientes | **07 · Entrega** | El entregable no cabe en la semana real del cliente: es diseño, no disciplina |
| Deuda tuya en rojo con varios clientes a la vez | **07 · Entrega** | El tiempo tuyo que cuesta cada cliente no está declarado ni limitado |
| Pide algo fuera de alcance en 2+ clientes | **07 · Entrega** (límite) o **02 · Oferta** (si lo pagarían) | Sin límite escrito, cada cliente pide algo distinto |
| Llegó alguien que no era para ti (`No es para mí`, `Fit avatar: Bajo` que llegó a llamada) | **03 · Avatar** | El documento de avatar no excluye ese perfil |
| Varios de fit bajo vienen de la **misma pieza** | **04 · Contenido** | El avatar está bien escrito; la pieza atrae al equivocado |
| Pidió descuento sin objetar el valor | **02 · Oferta** | El problema es el precio o su presentación, no la calidad |
| Aceptó el precio sin ninguna objeción, varias veces | **02 · Oferta** | El valor percibido está muy por encima de lo que pides. Se corrige en el cliente siguiente |
| Esperaba algo que no recibió, en 2+ clientes | **02 · Oferta** | Se prometió mal. Con un solo cliente es **06 · Ventas** (se vendió mal en esa llamada) |
| Lo que más valoró no está escrito en la oferta | **02 · Oferta** | Esa es la promesa real y hoy no está al frente |
| Pieza con alcance y cero conversaciones | **04 · Contenido** | Entretiene, no califica |
| Pieza que trae conversaciones que terminan en cliente que renueva | **04 · Contenido** | Ley del ganador: se replica, no se celebra |
| Lead que escribió y no tuvo respuesta, o quedó sin próximo paso | **05 · Captura** | Se perdió entre el mensaje y la conversación |
| No se sabe de dónde vino un cliente | **05 · Captura** | Sin origen no se puede medir qué pieza rinde |
| "Lo pienso" sin fecha, o la misma objeción en 2 llamadas | **06 · Ventas** | La conversación no llegó a una decisión con ventana |
| La misma objeción en 3+ llamadas con `Fit avatar: Alto` | **02 · Oferta** | Ya no es técnica de venta: la oferta tiene un hueco |
| Una decisión tomada contradice la meta a 90 días, o un cliente entró fuera del plan | **01 · Foundations** | La lógica del negocio no filtró la decisión |
| Continuidad abierta tarde, medidores sin llenar, resultado no anotado | **08 · Success** | El circuito mismo está roto |

Regla de desempate: si un síntoma apunta a dos áreas, gana **la que está antes en
el orden 01 → 07**. Un área con la anterior abierta se construye dos veces.

---

## 4 · Cómo se procesa una fila de 🔁 Aprendizajes

Cada fila `Pendiente` termina en uno de tres destinos, en la misma revisión:

| Destino | Cuándo | Qué se escribe |
|---|---|---|
| **Sigue Pendiente, con handoff** | Es corrección real y no está aplicada | `Qué cambia` reescrito como corrección concreta + `Área que corrige` verificada |
| **Aplicado** | La pieza ya cambió en la página del área (se ve, no "se habló") | `Estado = Aplicado` |
| **Descartado** | Anécdota de un caso sin costo, duplicada o contradicha por el dato | `Estado = Descartado` + motivo en una línea en `Qué cambia` |

### La corrección concreta tiene cuatro partes

`verbo + pieza del área + cómo + evidencia`

| ✕ Aprendizaje vago | ✓ Corrección concreta |
|---|---|
| "Hay que mejorar el onboarding" | "Agregar las 4 condiciones de cierre del onboarding a 07 · Entrega. Evidencia: 2 clientes llegaron a la sesión 1 sin acceso" |
| "Los leads de ese reel eran malos" | "Excluir en 03 · Avatar a quien no factura todavía. Evidencia: 3 de 4 `No es para mí` del mes con ese perfil" |
| "Hay que cobrar más" | "Subir el precio de lista en 02 · Oferta para el cliente siguiente. Evidencia: 3 cierres seguidos sin ninguna objeción de precio" |

### Umbrales de repetición

| Cuántos casos distintos | Qué es | Qué se hace |
|---|---|---|
| 1 | **Señal** | Se anota. No se corrige el área, salvo que el costo de ese caso sea alto |
| 2 | **Patrón** | Corrección a la pieza del área |
| 3+ | **Regla** | La corrección cambia la pieza del área y se escribe como regla en su página |

Deduplica siempre: dos filas con la misma causa son una sola corrección con más
evidencia, no dos correcciones.

### Una corrección por área afectada

Máximo **una** corrección por área por revisión: la más cara. Siete correcciones a
la misma área en una semana no se aplican; una sí. Las demás quedan `Pendiente`
para la próxima revisión.

---

## 5 · El Cuello

Solo un área tiene `Cuello = true` en 🧭 Tablero de áreas.

1. Cuenta, por área, cuántos clientes o leads perdidos en la ventana explica su
   corrección.
2. El Cuello es la que **explica más pérdida**. Empate → la que va antes en el orden.
3. Si el registro está demasiado roto para contar, el Cuello es **08 · Success** o
   **05 · Captura**: sin dato no hay loop.
4. Mejorar un área que no es el cuello es trabajo real con progreso cero. Dilo si
   el dueño del negocio quiere trabajar en otra.
5. Si el Cuello cambió, avisa a `pvt-founder-agent`: el "cuello actual" del Documento
   de contexto lo mantiene ella.

---

## 6 · Leer el contenido con criterio de loop

Lo que importa de 🎬 Contenido no es qué pieza tuvo más alcance, sino **qué pieza
trajo clientes que se quedan**. Se cruza `Pieza de origen` de 👥 Leads y clientes
con el `Veredicto` de la pieza.

Escalera de intención (cada peldaño vale más que el anterior):

1. Vio y no saltó → el gancho aguanta.
2. Guardó o compartió → es útil.
3. **Escribió o comentó pidiendo algo** → aquí empieza el lead.
4. Tuvo conversación → hay interés real.
5. Agendó y compró → hay dinero.
6. **Renovó o refirió** → la pieza trae al cliente correcto. Este peldaño solo lo ve Success.

Reglas:

- `Conversaciones generadas` manda sobre `Métrica principal`. Una pieza chica que
  trae conversaciones le gana a una grande que no trae ninguna. Los likes no
  son criterio.
- **Ley del ganador:** una pieza que trae clientes que renuevan no se celebra, se
  replica. El brief a `pvt-content-agent` es: mismo formato, gancho y cierre, cinco
  piezas cambiando solo el tema.
- Mezcla del lote que se sugiere: 70% lo que ya funciona, 20% variación (cambia
  gancho o formato), 10% apuesta nueva. Sin el 10% el sistema deja de descubrir.
- Una regla de contenido pide **5 piezas** del mismo tipo con el mismo resultado.
  Con menos, es señal y se dice así.

---

## 7 · El reporte — formato fijo

```
REVISIÓN DEL LOOP · <semana o mes> · <fecha>
Leído: <n> movimientos en 👥 · <n> llamadas · <n> piezas · <n> aprendizajes pendientes
Higiene: <huecos encontrados, o "registro completo">

| Área | Qué pasó (evidencia, n casos) | Corrección | Pasa a | Revisar el |
|---|---|---|---|---|

Cuello: <área> — <por qué, en una línea con el número>
Señales anotadas sin corregir: <lista corta>
Aprendizajes procesados: <n> Pendiente con handoff · <n> Aplicado · <n> Descartado
Una acción esta semana: <verbo + qué + fecha>
```

Nada de párrafos. Si la tabla pasa de 8 filas, hay correcciones de más: quédate
con una por área.

---

## 8 · El handoff a la hermana — bloque copiable

```
HANDOFF · de 08 Success a <NN Área> (pvt-*)
Aprendizaje: <título de la fila en 🔁 Aprendizajes>
Evidencia: <n casos, cuáles, en qué fechas>
Qué cambia: <verbo + pieza + cómo>
Cómo se ve hecho: <la pieza corregida en la página del área>
Se revisa en la próxima revisión del loop: <fecha>
```

La hermana aplica la corrección en su página. Success la marca `Aplicado` cuando
la ve escrita ahí, no cuando se acordó.

---

## 9 · Medido mal y medido bien

| Situación | ✕ Impresión | ✓ Dato |
|---|---|---|
| Un cliente no renovó | "No era buen momento para él" | "Medidor 01 en rojo desde la sesión 5; continuidad abierta en la última sesión, no en el punto medio. Corrige 07 · Entrega (entregable más chico) y 08 · Success (marca del punto medio)" |
| Llegaron varios leads que no calificaban | "El algoritmo está trayendo gente rara" | "3 de 5 `No es para mí` del mes vienen de la misma pieza. El avatar ya los excluye. Corrige 04 · Contenido: matar esa pieza o cambiar el dolor que toca" |
| Tres cierres sin objeción de precio | "Estoy vendiendo muy bien" | "Tres cierres seguidos sin ninguna objeción de precio: el precio está bajo. Corrige 02 · Oferta en el cliente siguiente, no en los actuales" |
