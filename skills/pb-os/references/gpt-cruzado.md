# Cruce con GPT — Claude construye, GPT audita, Notion recuerda

## Por qué dos IAs

Una sola IA que construye y se revisa a sí misma tiende a darse la razón. El cruce separa
los roles para que la segunda opinión no venga del mismo que escribió la pieza.

| Rol | Quién | Qué hace | Qué NO hace |
|---|---|---|---|
| **Constructor** | Claude + las skills pb-* | Arma la pieza con el método del área y la guarda en Notion | Auditarse a sí mismo como veredicto final |
| **Auditor** | ChatGPT (Proyecto "Private Build OS") o Codex | Lee la pieza y dice qué cambiaría, en tabla | Reescribir la pieza entera o construir en paralelo |
| **Memoria** | Notion (🏗️ Private Build OS) | Guarda el negocio, las piezas y las decisiones | — |
| **Decide** | El dueño del negocio | Acepta o rechaza cada punto, con el criterio del área | — |

Reglas:
- **Notion es la única memoria.** Ninguno de los dos chats "sabe" el negocio: lo leen.
- **Nunca los dos construyendo la misma pieza a la vez.** Se pisan y nadie es dueño.
- **El cruce se usa en piezas importantes**, no en todo: una oferta, un avatar, un
  guion de llamada, una decisión grande, el mix del mes. No en un post suelto.

## Configurar ChatGPT (una vez, ~7 minutos)

1. En ChatGPT, crea un **Proyecto** llamado **Private Build OS**.
2. En las **instrucciones del proyecto**, pega el bloque de abajo.
3. Sube a los **archivos del proyecto** los `SKILL.md` de las 9 skills (descárgalos desde
   `https://github.com/pvt-build/privatebuild-os` → botón *Code* → *Download ZIP*; están
   en la carpeta `skills/`). Son el criterio contra el que GPT audita.
4. Activa el conector de **Notion** en ChatGPT (en la configuración de ChatGPT, sección
   de conectores o apps) y dale acceso a la página 🏗️ Private Build OS. Si tu plan no lo
   tiene, no pasa nada: el brief ya lleva la pieza completa pegada.

### Instrucciones del proyecto (copiar tal cual)

```
Eres el auditor de Private Build OS de mi negocio. Claude construye las piezas; tú las auditas. No construyes en paralelo.

La memoria del negocio vive en Notion, en la página "🏗️ Private Build OS": un Documento de contexto, 8 páginas de área (Foundations, Oferta, Avatar, Contenido, Captura, Ventas, Entrega, Success) y 6 bases (Tablero de áreas, Leads y clientes, Llamadas, Contenido, Aprendizajes, Decisiones). Si tienes el conector de Notion, lee el Documento de contexto antes de responder.

Los archivos de este proyecto (SKILL.md de cada área) son el criterio contra el que mides. Cuando audites una pieza de un área, usa las reglas de ese archivo, no tu opinión general.

Cuando te pegue un BRIEF DE CRUCE:
- Responde solo con una tabla: Punto | Mantener o cambiar | Por qué (1 línea) | Propuesta concreta.
- Máximo 7 filas. No reescribas la pieza completa.
- Si algo está bien, dilo y no lo toques.
- Voz exigente, no complaciente. Sin relleno.
- Si te falta un dato del negocio, pregúntalo. No lo inventes.

Idioma: español neutro latinoamericano, tratando de tú.
```

## Codex (opcional, si usas el agente de OpenAI en tu computador)

Las mismas skills se instalan en Codex con:

```
npx skills add https://github.com/pvt-build/privatebuild-os -g -a codex -y
```

Con eso Codex audita con el mismo criterio, leyendo los mismos archivos.

## El flujo, cada vez

1. **Claude construye** la pieza con la skill del área y la guarda en Notion.
2. Escribes **"cruce con GPT"** → la skill arma el **Brief de cruce** (bloque listo
   para copiar, con la pregunta de auditoría propia del área).
3. Lo pegas en el Proyecto de ChatGPT.
4. Copias la respuesta y la traes a Claude: **"respuesta de GPT: …"**
5. La skill contrasta cada fila contra el criterio del área y devuelve:

   | Punto de GPT | Acepto / Rechazo | Por qué |
   |---|---|---|

6. Aplica lo aceptado en Notion. Si algo cambió el método (no solo la pieza), deja una
   fila en **🔁 Aprendizajes**.

## Formato del Brief de cruce

```
BRIEF DE CRUCE · Private Build OS · Área <NN> <Área>
Contexto del negocio (del Documento de contexto): <3-5 líneas>
Qué construí: <la pieza completa, o el link de Notion si GPT tiene el conector>
Criterio contra el que se mide: <las 3-6 reglas del área que aplican>
Tu tarea: <pregunta de auditoría específica del área>
Responde solo con una tabla: Punto | Mantener o cambiar | Por qué (1 línea) | Propuesta concreta.
Máximo 7 filas. No reescribas la pieza completa. Si algo está bien, dilo y no lo toques.
```

## Cuándo GPT se equivoca

Rechaza un punto de GPT cuando:
- Contradice el criterio del área (ej. propone tres promesas en la oferta).
- Pide agregar algo que el cliente no puede sostener hoy (más canales con el cuello en
  Oferta).
- Suaviza para caer bien (criterio: voz exigente, no complaciente).
- Inventa un dato del negocio que no está en Notion.

Rechazar también es resultado: queda escrito por qué, y la próxima vez el brief lo dice.
