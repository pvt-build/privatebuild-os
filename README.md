# Private Build OS · Las 8 áreas de un negocio, como skills

**by Private Build**

Todo negocio de servicios, coaching o consultoría tiene ocho áreas — funcionando o no.
El desorden nunca es falta de trabajo: es una de las ocho que nadie construyó, y las
otras siete compensándola a pulso.

Este repo son esas ocho áreas convertidas en skills para Claude: cada una sabe qué
preguntar, en qué orden construir, contra qué medir y dónde dejarlo escrito en tu Notion.
Más una de entrada que diagnostica cuál está rota hoy.

**Marketplace (copia y pega la skill que necesitas):** https://pvt-build.github.io/privatebuild-os/
**Manual para instalar las 9 en Claude Code + Notion:** https://pvt-build.github.io/privatebuild-os/onboarding/

## Tres formas de usarlas

| Forma | Tiempo | Cómo |
|---|---|---|
| **Copiar y pegar** | 30 s | En el marketplace, botón *Copiar skill* → pégala en un chat de Claude o ChatGPT → escribe su frase de arranque |
| **Proyecto con las 9** | 5 min | Sube los 9 archivos de `dist/` a un Proyecto de Claude o ChatGPT |
| **Sistema completo** | 40 min | Claude Code + Notion + ChatGPT auditando — sigue el manual de onboarding |

---

## Instalar (una línea)

En Claude (app de escritorio, pestaña **Code**), pega y presiona enter:

```
npx skills add https://github.com/pvt-build/privatebuild-os -g -a claude-code -y
```

Cierra y abre la app. Después escribe:

```
arrancar private build os
```

---

## Las 9 skills

| # | Área | Qué resuelve | Skill | Para abrirla |
|---|---|---|---|---|
| — | Entrada | Diagnóstico, arma tu Notion, encuentra el cuello | `pb-os` | "arrancar private build os" |
| 01 | Foundations | La lógica del negocio y hacia dónde va | `pb-foundations` | "diagnostica mis foundations" |
| 02 | Oferta | Qué vendes y a qué precio | `pb-oferta` | "arma mi oferta" |
| 03 | Avatar | A quién le vendes y a quién no | `pb-avatar` | "arma mi avatar" |
| 04 | Contenido | Cómo llegan los correctos hasta ti | `pb-contenido` | "qué publico esta semana" |
| 05 | Captura | Dónde quedan los que te escriben | `pb-captura` | "barre mi bandeja" |
| 06 | Ventas | Conducir la conversación hasta el sí | `pb-ventas` | "prepárame para la llamada con [lead]" |
| 07 | Entrega | Cumplir sin que te cueste la semana | `pb-entrega` | "diseña mi entrega" |
| 08 | Success | El loop que sostiene a los otros siete | `pb-success` | "revisión del loop" |

Las siete primeras se leen en orden. **La octava no viene después: viene encima** — mide
lo que las otras siete produjeron y devuelve la corrección a cada una.

---

## Cómo trabajan juntas: Claude + Notion + GPT

| Pieza | Rol |
|---|---|
| **Claude + skills** | Construye: arma cada pieza del área con el método |
| **Notion** | Recuerda: la página 🏗️ Private Build OS (Documento de contexto, 8 áreas, 6 bases). Lo que no quedó en Notion no pasó |
| **ChatGPT / Codex** | Audita: segunda opinión sobre las piezas importantes, con el mismo criterio |
| **Tú** | Decides: aceptas o rechazas cada punto |

- `pb-os` arma el Notion completo en el arranque: ver
  [`skills/pb-os/references/notion-schema.md`](skills/pb-os/references/notion-schema.md).
- El cruce con GPT (instrucciones del Proyecto de ChatGPT listas para pegar):
  [`skills/pb-os/references/gpt-cruzado.md`](skills/pb-os/references/gpt-cruzado.md).
- Para Codex: `npx skills add https://github.com/pvt-build/privatebuild-os -g -a codex -y`

---

## Cuatro reglas que atraviesan las nueve

1. **El cuello manda sobre el orden.** Mejorar un área que no es el cuello es trabajo
   real con progreso cero.
2. **Se cierra una antes de abrir la siguiente.** Un área con la anterior abierta se
   construye dos veces.
3. **Manual antes que automático.** Tres veces a mano antes de apalancarlo con IA:
   automatizar un proceso que no sirve no reduce trabajo, escala el error.
4. **Si algo no encuentra su área, no falta una categoría: falta dueño.**

---

## Cómo se suma una skill nueva

1. Crea su carpeta en `skills/<nombre>/` con `SKILL.md` (y `references/` si hace falta).
2. Agrega su entrada en `catalogo/areas.json` (área, promesa, frase, señales, qué necesitas).
3. Corre `python3 scripts/build.py` → genera `dist/<nombre>.md` (versión de un solo archivo para copiar y pegar) y actualiza la vitrina.
4. Commit y push. La vitrina se actualiza sola en GitHub Pages.

## Actualizar

Cuando mejoremos las skills, dile a Claude *"actualiza las skills"* o corre:

```
npx skills update -g -y
```

## Qué no hacen

- No mandan tu información a Private Build ni a terceros. Solo leen y escriben en tu
  Notion, con el acceso que tú autorizas.
- No envían mensajes por ti: redactan borradores, tú mandas.
- No reemplazan tu criterio: lo ordenan y lo auditan.

---

*Private Build OS es el sistema de Private Build para founders que quieren escalar con
sistemas, no con más horas.*
