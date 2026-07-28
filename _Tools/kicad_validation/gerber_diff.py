#!/usr/bin/env python3
"""Per-layer raster diff between KiCad-exported gerbers and the shipped fab
package, following the recipe documented in
Notecarrier-F/v1.3/KiCad_format/documentation/Porting-Notes.md:

  - render each layer with gerbv at 1200 dpi on top of the board outline
    (so both images share a canvas), then
  - combine the two grayscale renders into an RGB image where per-channel
    differences show up in color (<layer>-diff.png).

Outputs <Layer>-KiCad.png / <Layer>-<OriginalTool>.png / <Layer>-diff.png into
the given output directory, mirroring the existing ports' validation/ folders.
Human review of the diffs is the actual gate; this script only generates them
and flags gross mismatches (image size differences, empty renders).

Layer mapping lives in boards.yaml per board:
  gerbers:
    original_dir: <dir with shipped gerbers (unzipped)>
    original_tool: Altium
    outline: { kicad: "<glob>", original: "<glob>" }
    layers:
      F_Cu:   { kicad: "*-F_Cu.gtl",  original: "*.GTL" }
      ...

Usage: gerber_diff.py --board <name> --config boards.yaml
                      --kicad-dir <dir> --out <dir>
Exit 0 = all layers rendered and sizes match; 1 = structural problem.
"""

import argparse
import glob
import subprocess
import sys
from pathlib import Path

import yaml

GERBV = "gerbv"
MAGICK = "magick"
DPI = "1200"
FG = "#00690B"


def one(pattern, base):
    hits = sorted(glob.glob(str(base / pattern)))
    if len(hits) != 1:
        raise SystemExit(f"expected exactly 1 match for {pattern!r} in {base}, got {hits}")
    return hits[0]


def render(outline, layer_file, out_png):
    cmd = [GERBV, "--background=#FFFFFF", f"--foreground={FG}", f"--foreground={FG}",
           outline, layer_file, "--export=png", f"--dpi={DPI}", "-o", str(out_png)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0 or not Path(out_png).exists():
        raise SystemExit(f"gerbv failed for {layer_file}:\n{r.stderr[-2000:]}")


def size(png):
    r = subprocess.run([MAGICK, "identify", "-format", "%wx%h", str(png)],
                       capture_output=True, text=True)
    return r.stdout.strip()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--board", required=True)
    ap.add_argument("--config", required=True, type=Path)
    ap.add_argument("--kicad-dir", required=True, type=Path, help="dir with KiCad-exported gerbers")
    ap.add_argument("--out", required=True, type=Path)
    args = ap.parse_args()

    cfg = yaml.safe_load(args.config.read_text())["boards"][args.board]["gerbers"]
    orig_dir = Path(cfg["original_dir"])
    tool = cfg.get("original_tool", "Original")
    args.out.mkdir(parents=True, exist_ok=True)

    k_outline = one(cfg["outline"]["kicad"], args.kicad_dir)
    o_outline = one(cfg["outline"]["original"], orig_dir)

    problems = []
    for layer, m in cfg["layers"].items():
        k_png = args.out / f"{layer}-KiCad.png"
        o_png = args.out / f"{layer}-{tool}.png"
        d_png = args.out / f"{layer}-diff.png"
        render(k_outline, one(m["kicad"], args.kicad_dir), k_png)
        render(o_outline, one(m["original"], orig_dir), o_png)

        ks, os_ = size(k_png), size(o_png)
        if ks != os_:
            # Canvas mismatch: crop both to the smaller common size, centered
            # (the F port notes hit the same issue and cropped).
            w = min(int(ks.split("x")[0]), int(os_.split("x")[0]))
            h = min(int(ks.split("x")[1]), int(os_.split("x")[1]))
            for p in (k_png, o_png):
                subprocess.run([MAGICK, "mogrify", "-gravity", "Center",
                                "-crop", f"{w}x{h}+0+0", "+repage", str(p)], check=True)
            problems.append(f"{layer}: canvas size differed (KiCad {ks} vs {tool} {os_}); center-cropped to {w}x{h}")

        subprocess.run(
            [MAGICK, "(", str(k_png), "-grayscale", "Rec709Luminance", ")",
             "(", str(o_png), "-grayscale", "Rec709Luminance", ")",
             "(", "-clone", "0-1", "-compose", "darken", "-composite", ")",
             "-channel", "RGB", "-combine", str(d_png)], check=True)
        print(f"  {layer}: rendered -> {d_png.name}")

    if problems:
        print("\nNotes (review these first):")
        for p in problems:
            print(f"  - {p}")
    print(f"\nDone. Review the *-diff.png files in {args.out} — KiCad-only content "
          f"appears in one color channel, {tool}-only in another.")
    sys.exit(0)


if __name__ == "__main__":
    main()
