# Notecarrier-A v2.3 — KiCad port, WORK IN PROGRESS (not usable yet)

> ## ⚠️ This is an unfinished port. Do not use it for manufacturing, and do not treat it as a KiCad equivalent of the v2.3 board.
>
> It is committed only so the work is not lost and can be picked up later.
> **[`STATUS-INCOMPLETE.md`](STATUS-INCOMPLETE.md) is the authoritative
> description of what is verified, what is missing, and what would unlock the
> rest — read it first.**
>
> For a usable KiCad reference for the A form factor, use
> **[Notecarrier-A v2.0](../../v2.0/KiCad_format)**, which is a complete,
> validated port.

## Why it is unfinished

The Notecarrier-A is authored in OrCAD/Allegro, for which no KiCad importer
exists. v2.3 (internal Allegro **v20**) turned out to be a **re-layout** rather
than a small revision — 51 of 94 parts moved, some by 30–40 mm, and roughly
75 % of vias changed — so it cannot be delta-ported from the v2.0 KiCad port
the way [Notecarrier-Pi v2.0](../../../Notecarrier-Pi/v2.0/KiCad_format) was.
The copper therefore has to be reconstructed from the published artwork films,
and that reconstruction is currently blocked on one specific problem: Allegro
writes each copper pour as a single self-touching contour whose clearance areas
are *even-odd* holes, which KiCad's polygon API fills as solid copper. Details,
including what has already been ruled out, are in
[`STATUS-INCOMPLETE.md`](STATUS-INCOMPLETE.md).

## What is already done and verified

* Schematic is complete and passes ERC with 0 errors, and its BOM matches the
  internal v19 BOM exactly (87/87 electrical refdes). This covers the v2.3
  electrical changes: the micro-USB → USB-C swap (J11, Amphenol
  `12402012E212A`) with the R32/R33 5.1 kΩ CC pull-downs, and the removal of
  J2 and its supporting parts.
* 86 of 92 footprints are placed pad-exact against the published films; the
  remaining six deviate identically in the already-validated v2.0 port, so
  they are a pre-existing footprint characteristic rather than a placement
  error.
* All copper (1 469 traces and vias) is reconstructed from the published v20
  films and currently matches them to within 1.6–3.1 % per layer.

## Contents

| Path | Description |
|---|---|
| `STATUS-INCOMPLETE.md` | **Authoritative status**: what is proven, what remains, what would unlock it |
| `Notecarrier-A.kicad_sch` + `_Power` / `_Connector` sheets | Schematic — complete, ERC-clean |
| `Notecarrier-A.kicad_pcb` | Board — copper reconstructed, **pours and silkscreen unfinished, DRC not clean** |
| `Notecarrier-A-local.pretty/` | The new USB-C footprint, built from the film's pad and drill data |
| `Notecarrier-A.kicad_pro` / `.kicad_prl` / `.kicad_dru` / `.kicad_wks` | Project, rules and drawing sheet |
| `sym-lib-table` / `fp-lib-table` | Library tables |
| `_wip-tooling/` | The conversion and verification scripts used so far, kept so the work is resumable (not part of the design) |

## Provenance

The published v2.3 board file and gerber package are byte-identical (md5) to
the internal Allegro **v20** release; the matching schematic is internal
**v19**. Those internal sources are conversion inputs only and are not part of
this repository. The published fab package, board file and drawings in the
parent folder remain the manufacturing ground truth for the shipped product.
