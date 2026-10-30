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
# the port as first published (before the Rev-11 regeneration)
git show 71ee488:Notecarrier-X/v1.2/KiCad_format/Notecarrier-X.kicad_pcb > work/port.kicad_pcb
python3 transplant.py work/port.kicad_pcb work/dev.kicad_pcb work/rev11.kicad_pcb out.kicad_pcb \
    --moved R4 --models P1,P2 --check-exclusions ../../Notecarrier-X.kicad_pro
# then set the title-block date and run _Tools/kicad_validation/run_all.py notecarrier-x
```

Zones keep their UUIDs from run to run. A zone that matches one in the port
keeps the port's UUID; pours match on net, layers and priority, and rule areas
on outline and flags. Any other zone gets a UUID derived from its identity. This
matters because DRC exclusions in the `.kicad_pro` name zones by UUID (XM has
two), and `--check-exclusions` fails if any of them would dangle. Tracks, vias
and graphics still get fresh UUIDs and a different order from the importer on
every run. So a re-run reproduces the board structurally (same footprints, pads,
nets, tracks, vias, zone fills and graphics, plus identical zone UUIDs) rather
than byte for byte.
