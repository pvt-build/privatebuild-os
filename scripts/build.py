#!/usr/bin/env python3
"""Arma la vitrina de Private Build OS.

Lee catalogo/areas.json + skills/<skill>/SKILL.md (+ references/) y genera:
  dist/<skill>.md       la skill completa en UN archivo, lista para copiar y pegar
                        en Claude o ChatGPT (o subir como archivo a un Proyecto)
  dist/catalogo.json    el catálogo en JSON
  index.html            la vitrina, con el catálogo incrustado

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


def frontmatter(texto):
    """Devuelve (name, description, cuerpo) sin depender de PyYAML."""
    m = FM.match(texto)
    if not m:
        sys.exit("SKILL.md sin frontmatter")
    bloque, cuerpo = m.group(1), texto[m.end():]
    name = re.search(r"^name:\s*(\S+)", bloque, re.M).group(1)
    desc = re.search(r"^description:\s*(?:>-?\n)?(.*)", bloque, re.M | re.S).group(1)
    desc = " ".join(linea.strip() for linea in desc.splitlines()).strip()
    return name, desc, cuerpo.strip()


def resumen(desc):
    """La primera frase de la descripción, sin el prefijo 'Área NN de Private Build OS'."""
    primera = re.split(r"(?<=\.)\s", desc, maxsplit=1)[0]
    primera = re.sub(r"^Área \d+\s*(·\s*\w+\s*)?de Private Build OS\s*[:—-]\s*", "", primera)
    return primera[0].upper() + primera[1:]


def paquete(meta, name, cuerpo, refs):
    hoy = date.today().isoformat()
    cabecera = f"""<!-- Private Build OS · {name} · {hoy} · github.com/pvt-build/privatebuild-os -->

# Cómo usar este archivo

- **Tú:** pega todo este texto en un chat nuevo de Claude o ChatGPT, o súbelo como
  archivo a un Proyecto para no pegarlo cada vez. Después escribe: **"{meta['frase']}"**.
- **Para la IA que lo lee:** lo que sigue es una skill de Private Build OS. Trabaja con
  el usuario siguiendo estas instrucciones al pie de la letra: pregunta de a una cosa,
  en español neutro con "tú". Cuando el texto mencione `references/<archivo>.md`, ese
  contenido está en los anexos al final de este mismo archivo. Si no tienes acceso a
  Notion, trabaja en el chat y entrega el resultado en markdown listo para pegar.

---

"""
    partes = [cabecera, cuerpo]
    for ref in refs:
        partes.append(f"\n\n---\n\n# Anexo · references/{ref.name}\n\n{ref.read_text(encoding='utf-8').strip()}")
    return "".join(partes) + "\n"


def main():
    cat = json.loads((ROOT / "catalogo" / "areas.json").read_text(encoding="utf-8"))
    DIST.mkdir(exist_ok=True)
    salida = []
    for meta in cat["skills"]:
        carpeta = SKILLS / meta["skill"]
        texto = (carpeta / "SKILL.md").read_text(encoding="utf-8")
        name, desc, cuerpo = frontmatter(texto)
        if name != meta["skill"]:
            sys.exit(f"{carpeta}: name '{name}' no coincide con '{meta['skill']}'")
        refs = sorted((carpeta / "references").glob("*.md")) if (carpeta / "references").is_dir() else []
        md = paquete(meta, name, cuerpo, refs)
        (DIST / f"{name}.md").write_text(md, encoding="utf-8")
        salida.append({
            **meta,
            "resumen": resumen(desc),
            "descripcion": desc,
            "archivo": f"dist/{name}.md",
            "fuente": f"https://github.com/pvt-build/privatebuild-os/tree/main/skills/{name}",
            "pagina": cat["sitio_areas"] + ("" if meta["slug"] == "sistemas" else meta["slug"]),
            "palabras": len(md.split()),
            "anexos": len(refs),
        })
        print(f"  {name:<16} {len(md.split()):>6} palabras · {len(refs)} anexos")
    catalogo = {"generado": date.today().isoformat(), "skills": salida}
    (DIST / "catalogo.json").write_text(json.dumps(catalogo, ensure_ascii=False, indent=1), encoding="utf-8")

    # La vitrina lleva el catálogo adentro: carga sin pedir nada a la red.
    index = ROOT / "index.html"
    html = index.read_text(encoding="utf-8")
    incrustado = json.dumps(catalogo, ensure_ascii=False).replace("</", "<\\/")
    html, n = re.subn(
        r'(<script id="catalogo" type="application/json">)(.*?)(</script>)',
        lambda m: m.group(1) + incrustado + m.group(3),
        html,
        flags=re.S,
    )
    if n != 1:
        sys.exit("index.html: no encontré <script id=\"catalogo\">")
    index.write_text(html, encoding="utf-8")
    print(f"OK · {len(salida)} skills → dist/ + index.html")


if __name__ == "__main__":
    main()
