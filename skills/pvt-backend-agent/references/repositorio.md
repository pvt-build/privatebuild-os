# El repositorio — tres lugares, una estructura

Las tres opciones guardan exactamente lo mismo, con los mismos nombres
(`esquema.md`). Cambia solo el formato: páginas y bases en Notion, archivos `.md`
y `.csv` en tu máquina o en la nube.

## Opción 1 · Notion

Página **🏗️ Private Build OS** con adentro:

- 📄 Documento de contexto (página)
- 01 · Foundations … 08 · Success (8 páginas)
- 🧭 Tablero de áreas · 👥 Leads y clientes · 📞 Llamadas · 🎬 Contenido ·
  🔁 Aprendizajes · ⚖️ Decisiones (6 bases de datos)

Se crea con el conector de Notion. Si el conector no permite crear bases, crea las
páginas y entrega cada base como tabla markdown con sus columnas, para que el dueño la
cree con `/database`.

## Opción 2 · Tu máquina

```
~/PrivateBuildOS/
├── 00-contexto.md              Documento de contexto (secciones H2 fijas)
├── areas/
│   ├── 01-foundations.md
│   ├── 02-oferta.md
│   ├── 03-avatar.md
│   ├── 04-contenido.md
│   ├── 05-captura.md
│   ├── 06-ventas.md
│   ├── 07-entrega.md
│   └── 08-success.md
└── bases/
    ├── tablero-de-areas.csv
    ├── leads-y-clientes.csv
    ├── llamadas.csv
    ├── contenido.csv
    ├── aprendizajes.csv
    └── decisiones.csv
```

Reglas:
- **CSV con encabezados idénticos** a los nombres de propiedad de `esquema.md`
  (`Nombre,Etapa,Canal de origen,…`). UTF-8, separador coma, fechas `AAAA-MM-DD`.
- La relación `Lead` de 📞 Llamadas se guarda con el `Nombre` exacto del lead.
- Multi-select (`Tipo de leverage`) se guarda separado por `;`.
- Checkbox (`Cuello`) se guarda como `sí` / vacío.
- Primera línea de `00-contexto.md`: `Repositorio: Máquina (~/PrivateBuildOS)`.
- **Respaldo:** es una carpeta normal. Si quieres historial, que Claude Code la
  inicialice como repositorio git privado.

Para usarla en un chat web (sin disco): sube la carpeta completa a los archivos del
Proyecto. La IA la lee, pero no puede escribir: al final te entrega los cambios para que
los pegues.

## Opción 3 · La nube (Google Drive)

La misma estructura de la Opción 2, dentro de una carpeta **Private Build OS** en tu
Google Drive. Los `.csv` se pueden abrir como Hojas de cálculo de Google sin cambiar
nada.

- Se crea y se lee con el conector de Google Drive (Claude o ChatGPT).
- Primera línea de `00-contexto.md`: `Repositorio: Nube (Drive/Private Build OS)`.
- Si el conector solo permite leer, la IA te entrega los archivos listos y tú los subes.

## Cuál elegir

| Si… | Elige |
|---|---|
| Ya usas Notion todos los días | Notion |
| Trabajas en Claude Code y no quieres más cuentas | Tu máquina |
| Trabajas con equipo o desde varios computadores | La nube |
| Vas a usar ChatGPT como auditor | Notion o la nube (ChatGPT no ve tu disco) |

Se puede cambiar después sin perder nada: `pvt-backend-agent` → "migra mi repositorio".
