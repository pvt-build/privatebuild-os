#!/usr/bin/env python3
"""Arma el marketplace de Private Build OS desde una sola fuente: catalogo/areas.json.

Genera:
  dist/<skill>.md       cada skill disponible en UN archivo (SKILL.md + anexos), lista
                        para copiar y pegar en Claude o ChatGPT
  dist/catalogo.json    el catálogo completo en JSON
  index.html            la vitrina, con el catálogo incrustado
  skills/pvt-arsenal-agent/references/mapa-skills.md
                        el mapa que lee pvt-arsenal-agent para rutear (no se edita a mano)

Uso:  python3 scripts/build.py
"""
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
DIST = ROOT / "dist"
FM = re.compile(r"^---\n(.*?)\n---\n", re.S)
REPO = "https://github.com/pvt-build/privatebuild-os"


def frontmatter(texto, origen):
    m = FM.match(texto)
    if not m:
        sys.exit(f"{origen}: SKILL.md sin frontmatter")
    bloque, cuerpo = m.group(1), texto[m.end():]
    name = re.search(r"^name:\s*(\S+)", bloque, re.M).group(1)
    desc = re.search(r"^description:\s*(?:>-?\n)?(.*)", bloque, re.M | re.S).group(1)
    return name, " ".join(desc.split()), cuerpo.strip()


def paquete(item, name, cuerpo, refs):
    cabecera = f"""<!-- Private Build OS · {name} · {date.today().isoformat()} · {REPO} -->

# Cómo usar este archivo

- **Tú:** pega todo este texto en un chat nuevo de Claude o ChatGPT, o súbelo como
  archivo a un Proyecto para no pegarlo cada vez. Después escribe: **"{item['frase']}"**.
- **Para la IA que lo lee:** esto es una skill de Private Build OS. Trabaja con el
  usuario siguiendo estas instrucciones al pie de la letra, de a una pregunta, en español
  neutro con "tú". Antes de afirmar cualquier dato del negocio, búscalo en su
  repositorio (archivos del Proyecto, Notion "🏗️ Private Build OS", la carpeta
  `~/PrivateBuildOS/` o Google Drive "Private Build OS") y di de dónde salió. Si no está,
  pregúntalo: nunca lo inventes. Cuando el texto mencione `references/<archivo>.md`, ese
  contenido está en los anexos al final de este archivo.

---

"""
    partes = [cabecera, cuerpo]
    for ref in refs:
        partes.append(f"\n\n---\n\n# Anexo · references/{ref.name}\n\n{ref.read_text(encoding='utf-8').strip()}")
    return "".join(partes) + "\n"


def mapa_md(areas, arsenal):
    lineas = [
        "# Mapa del arsenal — qué skill sirve para qué en tu negocio",
        "",
        "> Generado por `scripts/build.py` desde `catalogo/areas.json`. No se edita a mano.",
        "> **Disponible** = se usa hoy. **Próximamente** = existe en el arsenal de Private Build",
        "> y se está convirtiendo a versión transferible: si el problema es de esa skill, dilo y",
        "> resuélvelo con la skill disponible del área.",
        "",
    ]
    for a in areas:
        lineas += [f"## {a['n']} · {a['area']} — {a['promesa']}", "", "| Skill | Estado | Para qué sirve | Frase para abrirla |", "|---|---|---|---|"]
        for s in arsenal:
            if s["n"] == a["n"]:
                estado = "Disponible" if s["estado"] == "disponible" else "Próximamente"
                frase = f"\"{s['frase']}\"" if s.get("frase") else "—"
                lineas.append(f"| `{s['skill']}` | {estado} | {s['para_que']} | {frase} |")
        lineas.append("")
    lineas += [
        "## ¿Qué pregunta está contestando esto?",
        "",
        "Para rutear algo que el dueño trae sin área:",
        "",
        "| Si lo que trae contesta… | Área | Skill |",
        "|---|---|---|",
        "| ¿Dónde guardo esto, de dónde sacaste ese dato? | Base | `pvt-backend-agent` |",
        "| ¿Por qué hago esto, hacia dónde va, esta decisión grande conviene? | Foundations | `pvt-founder-agent` |",
        "| ¿Qué vendo, qué incluye, cuánto cuesta, cómo lo presento? | Oferta | `pvt-offer-agent` |",
        "| ¿A quién le hablo, a quién dejo ir, este lead es para mí? | Avatar | `pvt-avatar-agent` |",
        "| ¿Qué publico, cómo llego a más gente correcta? | Contenido | `pvt-content-agent` |",
        "| ¿Quién me escribió, dónde anoto esto, a quién le respondo? | Captura | `pvt-setter-agent` |",
        "| ¿Cómo llevo la llamada, qué respondo a esta objeción? | Ventas | `pvt-closing-agent` |",
        "| ¿Cómo cumplo lo prometido sin comerme la semana? | Entrega | `pvt-consulting-agent` |",
        "| ¿Qué me dicen los clientes que ya pasaron, quién renueva? | Success | `pvt-success-agent` |",
        "",
        "## El loop",
        "",
        "```",
        "01 Foundations → 02 Oferta → 03 Avatar → 04 Contenido → 05 Captura → 06 Ventas → 07 Entrega",
        "      ↑                                                                              |",
        "      └──────────────────────── 08 Success (mide y devuelve) ←───────────────────────┘",
        "```",
        "",
        "- Un cliente que no vuelve habla de **Entrega**. Uno que llegó y no era para ti, de",
        "  **Avatar**. Uno que pidió descuento sin objetar el valor, de **Oferta**.",
        "",
    ]
    return "\n".join(lineas)


def main():
    cat = json.loads((ROOT / "catalogo" / "areas.json").read_text(encoding="utf-8"))
    areas, arsenal = cat["areas"], cat["arsenal"]
    nombres = [s["skill"] for s in arsenal]
    if len(nombres) != len(set(nombres)):
        sys.exit("areas.json: hay skills repetidas en 'arsenal'")
    DIST.mkdir(exist_ok=True)
    for viejo in DIST.glob("*.md"):
        viejo.unlink()

    for s in arsenal:
        area = next(a for a in areas if a["n"] == s["n"])
        s["area"] = area["area"]
        s["pagina"] = cat["sitio_areas"] + ("" if area["slug"] == "sistemas" else area["slug"])
        if s["estado"] != "disponible":
            continue
        carpeta = SKILLS / s["skill"]
        if not (carpeta / "SKILL.md").is_file():
            sys.exit(f"{s['skill']} está 'disponible' pero no existe {carpeta}/SKILL.md")
        name, desc, cuerpo = frontmatter((carpeta / "SKILL.md").read_text(encoding="utf-8"), carpeta)
        if name != s["skill"]:
            sys.exit(f"{carpeta}: name '{name}' no coincide con '{s['skill']}'")
        if len(desc) > 1024:
            sys.exit(f"{name}: la description pasa de 1024 caracteres ({len(desc)})")
        refs = sorted((carpeta / "references").glob("*.md")) if (carpeta / "references").is_dir() else []
        if s["skill"] == "pvt-arsenal-agent":
            (carpeta / "references" / "mapa-skills.md").write_text(mapa_md(areas, arsenal), encoding="utf-8")
            refs = sorted((carpeta / "references").glob("*.md"))
        md = paquete(s, name, cuerpo, refs)
        (DIST / f"{name}.md").write_text(md, encoding="utf-8")
        s.update(archivo=f"dist/{name}.md", fuente=f"{REPO}/tree/main/skills/{name}", palabras=len(md.split()), anexos=len(refs))
        print(f"  {name:<22} {len(md.split()):>6} palabras · {len(refs)} anexos")

    sueltas = sorted(p.name for p in SKILLS.iterdir() if p.is_dir() and p.name not in nombres)
    if sueltas:
        sys.exit(f"skills/ tiene carpetas fuera de areas.json: {sueltas}")

    catalogo = {"generado": date.today().isoformat(), "areas": areas, "arsenal": arsenal}
    (DIST / "catalogo.json").write_text(json.dumps(catalogo, ensure_ascii=False, indent=1), encoding="utf-8")

    index = ROOT / "index.html"
    html = index.read_text(encoding="utf-8")
    incrustado = json.dumps(catalogo, ensure_ascii=False).replace("</", "<\\/")
    html, n = re.subn(r'(<script id="catalogo" type="application/json">)(.*?)(</script>)',
                      lambda m: m.group(1) + incrustado + m.group(3), html, flags=re.S)
    if n != 1:
        sys.exit('index.html: no encontré <script id="catalogo">')
    index.write_text(html, encoding="utf-8")
    disp = sum(1 for s in arsenal if s["estado"] == "disponible")
    print(f"OK · {disp} disponibles · {len(arsenal) - disp} próximamente · vitrina y mapa actualizados")


if __name__ == "__main__":
    main()
