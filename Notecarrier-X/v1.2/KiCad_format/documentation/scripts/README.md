# Board regeneration scripts (Notecarrier-X and -XM, v1.2)

These scripts regenerated the `.kicad_pcb` of the Notecarrier-X and
Notecarrier-XM v1.2 ports from the design house's Rev-11 release snapshots,
keeping everything else in each published port. Porting-Notes explains why
and how this was verified. The Altium sources are internal, so they are not
in this repository.

| Script | Runs with | Purpose |
|---|---|---|
| `sanitize_fonts.py` | any Python 3 with `olefile` | Copies a PcbDoc and zeroes the padding after each `Texts6` font name. This works around a KiCad 9.0.9 importer defect that drops TrueType faces. |
| `pcb_import.py` | KiCad 9.0.9's bundled Python (`KiCad.app/Contents/Frameworks/Python.framework/Versions/Current/bin/python3`) | Headless Altium PcbDoc → `.kicad_pcb` import. |
| `transplant.py` | Python 3 + `git` | Swaps the Rev-11 geometry into the published port's board. |

```sh
# per board: X (moved part R4) and XM (moved part R2)
python3 sanitize_fonts.py Rev-11/Notecarrier-X.PcbDoc work/Notecarrier-X.PcbDoc
$KICAD_PY pcb_import.py work/Notecarrier-X.PcbDoc work/rev11.kicad_pcb
$KICAD_PY pcb_import.py dev-state/Notecarrier-X.PcbDoc work/dev.kicad_pcb   # the source the port was first made from
python3 transplant.py Notecarrier-X.kicad_pcb work/dev.kicad_pcb work/rev11.kicad_pcb out.kicad_pcb \
    --moved R4 --models P1,P2
# then set the title-block date and run _Tools/kicad_validation/run_all.py notecarrier-x
```

The importer assigns fresh UUIDs and object order on every run, so a re-run
reproduces the board structurally (same footprints, pads, nets, tracks, vias,
zone fills and graphics), not byte for byte.
