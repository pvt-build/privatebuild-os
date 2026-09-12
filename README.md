# Private Build OS · Las 8 áreas de un negocio, como skills

**by Private Build**

Todo negocio de servicios, coaching o consultoría tiene ocho áreas — funcionando o no.
El desorden nunca es falta de trabajo: es una de las ocho que nadie construyó, y las
otras siete compensándola a pulso.

Este repo es el **arsenal de skills de Private Build, en versión transferible**, ordenado
por esas ocho áreas. Cada skill es el método: qué preguntar, en qué orden construir y
contra qué medir. Tus datos no viven en la skill: viven en **tu repositorio** —tu
máquina, tu Notion o la nube—, y la skill los lee y verifica antes de afirmar algo. Por
eso usar la skill le ahorra a la IA inventar: trabaja sobre lo que tú ya validaste.

**Marketplace (copia y pega la skill que necesitas):** https://pvt-build.github.io/privatebuild-os/
**Manual para instalar todas en Claude Code (con tu repositorio):** https://pvt-build.github.io/privatebuild-os/onboarding/

## Tres formas de usarlas

| Forma | Tiempo | Cómo |
|---|---|---|
| **Copiar y pegar** | 30 s | En el marketplace, botón *Copiar skill* → pégala en un chat de Claude o ChatGPT → escribe su frase de arranque |
| **Proyecto con todas** | 5 min | Sube los archivos de `dist/` a un Proyecto de Claude o ChatGPT |
| **Sistema completo** | 40 min | Claude Code + tu repositorio + ChatGPT auditando — sigue el manual de onboarding |

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

## Las skills disponibles

El mapa completo del arsenal (33 skills transferibles por área, disponibles y
próximamente, y para qué sirve cada una) se genera en
[`skills/pvt-arsenal-agent/references/mapa-skills.md`](skills/pvt-arsenal-agent/references/mapa-skills.md).

| # | Área | Qué resuelve | Skill | Para abrirla |
|---|---|---|---|---|
| 00 | Base | El mapa: diagnóstico, cuello y qué skill usar | `pvt-arsenal-agent` | "arrancar private build os" |
| 00 | Base | El repositorio: tu máquina, tu Notion o la nube | `pvt-backend-agent` | "arma mi repositorio" |
| 01 | Foundations | La lógica del negocio y hacia dónde va | `pvt-founder-agent` | "diagnostica mis foundations" |
| 02 | Oferta | Qué vendes y a qué precio | `pvt-offer-agent` | "arma mi oferta" |
| 03 | Avatar | A quién le vendes y a quién no | `pvt-avatar-agent` | "arma mi avatar" |
| 04 | Contenido | Cómo llegan los correctos hasta ti | `pvt-content-agent` | "qué publico esta semana" |
| 05 | Captura | Dónde quedan los que te escriben | `pvt-setter-agent` | "barre mi bandeja" |
| 06 | Ventas | Conducir la conversación hasta el sí | `pvt-closing-agent` | "prepárame para la llamada con [lead]" |
| 07 | Entrega | Cumplir sin que te cueste la semana | `pvt-consulting-agent` | "diseña mi entrega" |
| 08 | Success | El loop que sostiene a los otros siete | `pvt-success-agent` | "revisión del loop" |

Las siete primeras se leen en orden. **La octava no viene después: viene encima** — mide
lo que las otras siete produjeron y devuelve la corrección a cada una.

---

## Cómo trabajan juntas: Claude + tu repositorio + GPT

| Pieza | Rol |
|---|---|
| **Claude + skills** | Construye: arma cada pieza del área con el método |
| **Tu repositorio** | Recuerda y verifica: tu carpeta `~/PrivateBuildOS/`, tu Notion "🏗️ Private Build OS" o Google Drive "Private Build OS". Misma estructura en los tres (Documento de contexto, 8 áreas, 6 bases). Lo que no quedó ahí no pasó |
| **ChatGPT / Codex** | Audita: segunda opinión sobre las piezas importantes, con el mismo criterio |
| **Tú** | Decides: aceptas o rechazas cada punto |

- `pvt-backend-agent` arma el repositorio donde elijas: ver
  [`repositorio.md`](skills/pvt-backend-agent/references/repositorio.md) y
  [`esquema.md`](skills/pvt-backend-agent/references/esquema.md).
- El cruce con GPT (instrucciones del Proyecto de ChatGPT listas para pegar):
  [`skills/pvt-arsenal-agent/references/gpt-cruzado.md`](skills/pvt-arsenal-agent/references/gpt-cruzado.md).
- Para Codex: `npx skills add https://github.com/pvt-build/privatebuild-os -g -a codex -y`

---

## Cinco reglas que atraviesan todas

1. **El cuello manda sobre el orden.** Mejorar un área que no es el cuello es trabajo
   real con progreso cero.
2. **Se cierra una antes de abrir la siguiente.** Un área con la anterior abierta se
   construye dos veces.
3. **Manual antes que automático.** Tres veces a mano antes de apalancarlo con IA:
   automatizar un proceso que no sirve no reduce trabajo, escala el error.
4. **Si algo no encuentra su área, no falta una categoría: falta dueño.**
5. **Nunca inventar un dato del negocio.** Se verifica en el repositorio y se cita; si no
   está, se pregunta.

---

## Cómo se suma o libera una skill

Nombres: siempre `pvt-[dominio]-agent`, el mismo nombre que tiene en el arsenal de
Private Build (lo gobierna `pvt-arsenal-agent`).

1. Crea su carpeta en `skills/<nombre>/` con `SKILL.md` (y `references/` si hace falta),
   ya convertida: sin datos de nadie, con el bloque de repositorio y verificación.
2. En `catalogo/areas.json`, cambia su `estado` a `disponible` y agrega su `frase`.
3. Corre `python3 scripts/build.py` → genera `dist/<nombre>.md`, la vitrina y el mapa del arsenal.
4. Commit y push. La vitrina se actualiza sola en GitHub Pages.

## Actualizar

Cuando mejoremos las skills, dile a Claude *"actualiza las skills"* o corre:

```
npx skills update -g -y
```

## Qué no hacen

- No mandan tu información a Private Build ni a terceros. Solo leen y escriben en tu
  repositorio, con el acceso que tú autorizas.
- No envían mensajes por ti: redactan borradores, tú mandas.
- No reemplazan tu criterio: lo ordenan y lo auditan.

---

*Private Build OS es el sistema de Private Build para founders que quieren escalar con
sistemas, no con más horas.*
