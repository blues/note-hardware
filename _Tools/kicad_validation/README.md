# KiCad Port Validation Harness

Tooling used to validate the KiCad ports of Blues hardware designs against
their original CAD outputs. Every `KiCad_format/` directory added to this
repository since 2026 was gated through this harness; the resulting reports
and diff images live in each product's `KiCad_format/validation/` folder
(deliberately excluded from the RAG index — see
`_Tools/extract_for_rag/extract.py`).

## Policy

**Accuracy over coverage.** A ported board ships only if every gate below
passes or the failure is explicitly justified in the board's
`documentation/Porting-Notes.md`. A board that cannot be proven against its
original fab outputs is dropped, not shipped.

| Gate | Tool | Proves |
|---|---|---|
| ERC | `kicad-cli sch erc --exit-code-violations` | schematic is electrically well-formed |
| DRC | `kicad-cli pcb drc --exit-code-violations --schematic-parity` | board passes rules and matches its schematic |
| BOM | `bom_compare.py` | 100% refdes/value/MPN match vs the shipped BOM spreadsheet |
| NETLIST | `netlist_compare.py` | connectivity partition identical to the shipped ODB++ netlist (boards that ship ODB++) |
| GERBER-DIFF | `gerber_diff.py` | per-layer raster diff vs the shipped fab package (human-reviewed; also proves the source revision matches the published release) |
| KICANVAS | `kicanvas_check/render_check.py` | every sheet + board parses and paints in KiCanvas, headless Chromium, zero console errors |
| RAG | `_Tools/extract_for_rag/extract.py` | the new `.kicad_sch` files parse in the RAG pipeline that runs in CI |

## Setup

```sh
python3 -m venv .venv
./.venv/bin/pip install playwright pymupdf openpyxl xlrd pyyaml
./.venv/bin/playwright install chromium
brew install gerbv imagemagick
# KiCad 9.x — kicad-cli expected at ~/Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli
# (override with KICAD_CLI env var)
# blues-kicad-lib checkout expected at ../../../blues-kicad-lib
# (override with BLUES_KICAD_LIB_DIR env var; only 3D models depend on it)
```

## Running

```sh
./.venv/bin/python run_all.py mojo
```

Board names and per-board configuration (BOM spreadsheet parsing rules,
gerber layer/extension maps, ODB++ locations) live in `boards.yaml`.
Individual tools can be run standalone; each has a `--help`.

## Notes

- `kicanvas_check/kicanvas.js` is a vendored copy of
  [KiCanvas](https://github.com/theacodes/kicanvas) (MIT-style license, © Alethea
  Katherine Flowers), fetched from <https://kicanvas.org/kicanvas/kicanvas.js>
  on 2026-07-28. Vendoring pins the version so render results are reproducible.
- The gerber-diff recipe (gerbv @ 1200 dpi over the board outline, ImageMagick
  channel-combine) follows the method documented in
  `Notecarrier-F/v1.3/KiCad_format/documentation/Porting-Notes.md`.
- KiCad file format target for new ports: **KiCad 9** (sch `20250114`, pcb
  `20241229`). Gate G0 (2026-07-28) verified KiCanvas renders KiCad 9 formats
  cleanly, including a 9-format resave of the existing Notecarrier-A port.
  The four pre-existing ports remain KiCad 7 on purpose — they open fine in
  KiCad 9 and KiCanvas, and resaving would orphan their validation artifacts.
