# Cygnet v1.2 — Altium ➜ KiCad 9 Porting Notes

Ported from the internal Altium Designer sources for Cygnet v1.2 (four
schematic sheets + PcbDoc) with KiCad 9.0.9's **File → Import → Non-KiCad
Project** importer plus the scripted cleanup and validation battery in
[`_Tools/kicad_validation/`](../../../../_Tools/kicad_validation/). Follows
the conventions of the Mojo v1.1 port (see its Porting-Notes for the shared
importer background: empty-`(instances)` fix, render-cache stripping, font
handling).

## Structure

- Altium project sheets `CYGNET {REVISION, CPU, POWER, FEATHER CONNECTOR}
  v1.2.SchDoc` became a KiCad hierarchy: root `Cygnet.kicad_sch` with child
  sheets `Cygnet_CPU`, `Cygnet_Power`, `Cygnet_Feather-Connector`.
- The **REVISION sheet was not ported** (house convention); its history table
  is reproduced in the README.
- 4-layer board. Altium layer names are kept as KiCad layer aliases
  (`Top Layer`, `L2`, `L3`, `Bottom Layer`). Both inner layers are routed
  signal/power layers (no negative planes despite the Altium stackup naming
  Int1 (GND)/Int2 (PWR)).

## Import quirks and fixes

- **Connectivity proven against the PcbDoc.** A fresh headless import of the
  Altium board provides the authoritative pad→net map; the KiCad schematic
  netlist was reconciled until **59/59 nets (≥2 nodes) match exactly** (see
  `validation/netlist-compare.txt`). Three real import defects were found and
  fixed this way:
  1. a **40 µm wire gap** split +VUSB on the Power sheet (importer artifact);
  2. a **local label** `+3V3_USB` fragmented that rail per-sheet — converted
     to a global label (Altium net scope was global);
  3. the BOOT button's second contact pair (pins 1/2) sat 0.5 mm off its
     wire stubs.
- **Functional designators** BOOT/RST/USER violate KiCad annotation and were
  renamed SW1/SW2/SW3 (mapping applied when comparing against the shipped
  BOM, which uses the original names).
- **Altium port symbols** (`*_CIRCLE`/`*_ARROW`/`*_BAR`) import as KiCad
  power symbols whose hidden `power_in` pins join the global nets. They must
  stay `power_in` (a passive pin loses the global-net semantics). Because
  most of these "power" ports are really I/O signals (A0–A5, D5–D13, SDA…),
  ERC's `power_pin_not_driven` check is meaningless here and is demoted to a
  warning in the project settings.
- **kicad-cli ERC segfault**: normalizing the imported symbol lib nicknames
  (as done on Mojo) makes kicad-cli 9.0.9's ERC crash on this project — the
  original nicknames (`Blues Wireless`, `Cygnet v1.2-altium-import`) are kept
  and both are aliased to the merged `Cygnet-altium-import.kicad_sym` in
  `sym-lib-table` instead.
- **Castellated edges**: the CST* castellation pads and the USB shell pads
  (J6 MP1/MP2) are marked with KiCad's *castellated* pad property so the
  0 mm edge-clearance design checks clean.
- **U2's thermal pad** carries GND in the layout but has no pin in the
  Altium symbol; the pad's net is set directly on the board (warning noted
  during *Update PCB from Schematic*).
- **Unused inner-layer annular rings**: Altium suppresses annular rings of
  through pads/vias on layers where nothing connects; the equivalent KiCad
  option (*remove unused layers*, keep start/end) is enabled on all PTH pads
  and vias (202 of them).

  > **⚠️ This did not fully work, and the original note here claimed it did.**
  > `In1_Cu` still carries roughly fifty annular rings that the shipped
  > `*.G1` does not: KiCad draws 0.0322 ink against Altium's 0.0288, and
  > **10.5 % of the drawn area differs**. `In2_Cu` matches at 0.1 %, as do both
  > outer copper layers, so this is specific to inner layer 1.
  >
  > This was always visible in the committed `validation/In1_Cu-diff.png` — the
  > scattered green dots are exactly these rings — but the gerber gate passed it,
  > because it compared an absolute mean difference over the whole canvas and
  > fifty small pads are a rounding error at that scale. The rebuilt gate
  > normalises against the drawn area and now fails the board.
  >
  > **Unresolved.** The tracks themselves match exactly, so this is not a routing
  > difference; it is whether unconnected inner-layer pads are plotted. Whoever
  > picks this up should establish whether `kicad-cli pcb export gerbers`
  > honours *remove unused layers* without recomputed connectivity, and if not,
  > whether the GUI export matches the fab. Until then Cygnet's fabrication
  > equivalence on `In1_Cu` is **not proven**, and the board's GERBER-DIFF gate
  > is expected to fail rather than being tuned to pass.
- **Two ~5 µm track-end near-misses** (net A4 and SWCLK on L3) — physically
  connected on the manufactured board but below KiCad's connectivity
  tolerance — were closed by snapping the track ends to the via centres.
- Two sheet-spanning decorative lines on the Feather Connector sheet imported
  as wires; converted to graphic polylines.
- Zone fills for the Top/Bottom pours are the **original Altium fills**
  (restored verbatim after an accidental refill; do not refill — cf. the
  Notecarrier-A port README).

## Design-rule alignment (from the shipped `.RUL`)

| Rule | Altium | KiCad setting |
|---|---|---|
| Copper clearance | 4 mil (0.1016 mm) | 0.1015 mm (float-rounding guard), netclasses + zones |
| Track width min | 4 mil | 0.1 mm |
| Board edge clearance | castellated | 0 mm + castellated pad properties |
| Via | 0.35 mm / 0.2 mm drill | minima set accordingly (annular 0.07 mm) |
| Thermal spokes / solder-mask bridges | not enforced / as manufactured | `min_resolved_spokes 1`, `solder_mask_bridge` demoted to warning |
| Severity baseline | — | copied from the Notecarrier-A port |

## Validation results (see `../validation/`)

| Gate | Result |
|---|---|
| ERC / DRC (error severity, incl. schematic parity) | **0 / 0** |
| Netlist vs Altium PcbDoc | **59/59 exact** |
| BOM vs `Cygnet v1.2 BOM.xlsx` | exact (78 refdes; BOM lines listing several equivalent value spellings accepted) |
| Gerber raster diff (10 layers incl. L2/L3) | **`In1_Cu` FAILS** — 10.5 % of the drawn area differs (see the annular-ring note above). Every other layer matches: outer copper 0.1–0.2 %, `In2_Cu` 0.1 %, paste ≤0.1 %, mask 2.3–4.0 %; silk text shows the usual TrueType metric offsets. The "≤0.7 % mean channel diff" originally recorded here was an absolute figure over the whole canvas, which is why fifty missing pads did not register. |
| KiCanvas / RAG extract | render + parse clean |
