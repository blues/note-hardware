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

**A gate must be able to fail.** Three of these gates once computed the right
thing and then did not act on it — the BOM comparison treated a missing MPN as
agreement, the placement gate left residuals out of its verdict, and the gerber
diff collected structural problems and exited 0 regardless. Each is now covered
by a regression suite that injects the specific defect and asserts a non-zero
exit:

    .venv/bin/python test_gerber_diff.py --board scoop     # one board's gerber gate
    .venv/bin/python test_gerber_diff.py --all-boards      # every board vs its baseline
    .venv/bin/python test_gates.py --board mojo            # BOM + placement gates

Those suites read each gate's `--json` summary rather than its printed report.
That matters: earlier versions classified failures by matching message text and
so ignored whole categories they had not enumerated, and one checked only a
failure's label and accepted arbitrary damage as a known defect. Anything acting
on a gate result should use the JSON.

**A gate that does not run has not passed.** `run_all.py` fails any gate that is
missing configuration or is requested via `--skip`, unless the board records the
reason under `skip_gates.<GATE>` in `boards.yaml`. That keeps every omission
machine-readable and reviewable in the diff, rather than depending on someone
remembering the right command line.

| Gate | Tool | Proves |
|---|---|---|
| ERC | `kicad-cli sch erc --exit-code-violations` | schematic is electrically well-formed |
| DRC | `kicad-cli pcb drc --exit-code-violations --schematic-parity` | board passes rules and matches its schematic |
| BOM | `bom_compare.py` | 100% refdes/value/MPN match vs the shipped BOM spreadsheet |
| NETLIST | `netlist_compare.py` | connectivity partition identical to the shipped ODB++ or IPC-D-356 netlist (boards that ship one) |
| GERBER-DIFF | `gerber_diff.py` | per-layer raster diff vs the shipped fab package (human-reviewed; also proves the source revision matches the published release) |
| PNP | `pnp_compare.py` | side/rotation/position match vs the shipped pick-and-place file — the only gate that checks against the *released build* rather than the design sources |
| KICANVAS | `kicanvas_check/render_check.py` | every sheet + board parses and paints in KiCanvas, headless Chromium, zero console errors |
| RAG | `_Tools/extract_for_rag/extract.py` | the new `.kicad_sch` files parse in the RAG pipeline that runs in CI |

**What a gerber baseline does and does not promise.** A board's committed
`validation/gerber-baseline.yaml` freezes each layer's reviewed difference; the
gate allows that value + 0.01, so *growth* past the reviewed magnitude fails.
Within that bound it is only a drift detector: on a layer whose frozen value is
well above the class default (e.g. a disclaimed X-series copper layer), a new
defect smaller than the reviewed one would not trip the number on its own.
That is why every baseline entry must be reviewed against its diff image when
frozen, and why the images stay committed for re-review.

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
  The four pre-existing ports (Notecarrier-A v2.0, -B v2.1, -F v1.3, -Pi v1.1)
  were **upgraded to KiCad 9** on this branch, after an audit verified the
  upgrade is lossless: every fabrication layer is geometrically identical at
  600 dpi before and after, drill files are textually identical, and the
  netlists are unchanged. Their zone fills are *not* refilled — these ports
  depend on the preserved fills, and refilling changes copper.
