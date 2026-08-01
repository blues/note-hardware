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


def gerber_bbox_inches(path):
    """Bounding box of all coordinates in a gerber file, in inches.

    Parses the %FS format spec (integer/decimal digits) and %MO units, then
    scans every X/Y coordinate. Good enough for board outline layers, which
    is all we use it for (fixing a common render window)."""
    import re
    text = Path(path).read_text(errors="replace")
    fs = re.search(r"%FS[LT]?[AI]X(\d)(\d)Y(\d)(\d)\*%", text)
    if not fs:
        raise SystemExit(f"no %FS spec in {path}")
    xdec, ydec = int(fs.group(2)), int(fs.group(4))
    scale = 25.4 if "%MOMM*%" in text else 1.0  # convert mm -> inch at the end
    xs, ys = [], []
    cx = cy = 0.0
    for m in re.finditer(
            r"(?:X(-?\d+))?(?:Y(-?\d+))?(?:I(-?\d+))?(?:J(-?\d+))?D0([123])\*", text):
        x = int(m.group(1)) / 10**xdec if m.group(1) else cx
        y = int(m.group(2)) / 10**ydec if m.group(2) else cy
        xs.append(x)
        ys.append(y)
        if m.group(3) or m.group(4):
            # Arc: I/J are offsets from the start point to the arc center.
            # Conservatively include the full circle bounding box.
            i = int(m.group(3)) / 10**xdec if m.group(3) else 0.0
            j = int(m.group(4)) / 10**ydec if m.group(4) else 0.0
            ax, ay = cx + i, cy + j
            r = ((x - ax) ** 2 + (y - ay) ** 2) ** 0.5
            xs.extend([ax - r, ax + r])
            ys.extend([ay - r, ay + r])
        cx, cy = x, y
    if not xs or not ys:
        raise SystemExit(f"no coordinates found in {path}")
    if scale == 25.4:
        xs = [x / 25.4 for x in xs]
        ys = [y / 25.4 for y in ys]
    return min(xs), min(ys), max(xs), max(ys)


MARGIN_IN = 0.05


def render(outline, layer_file, out_png, bbox):
    x0, y0, x1, y1 = bbox
    w = round((x1 - x0) + 2 * MARGIN_IN, 4)
    h = round((y1 - y0) + 2 * MARGIN_IN, 4)
    ox = round(x0 - MARGIN_IN, 4)
    oy = round(y0 - MARGIN_IN, 4)
    cmd = [GERBV, "--background=#FFFFFF", f"--foreground={FG}", f"--foreground={FG}",
           f"--origin={ox}x{oy}",
           f"--window_inch={w}x{h}",
           outline, layer_file, "--export=png", f"--dpi={DPI}", "-o", str(out_png)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0 or not Path(out_png).exists():
        raise SystemExit(f"gerbv failed for {layer_file}:\n{r.stderr[-2000:]}")


def render_single(layer_file, out_png, bbox):
    """Render one gerber alone in a fixed window (no outline overlay)."""
    x0, y0, x1, y1 = bbox
    w = round((x1 - x0) + 2 * MARGIN_IN, 4)
    h = round((y1 - y0) + 2 * MARGIN_IN, 4)
    ox = round(x0 - MARGIN_IN, 4)
    oy = round(y0 - MARGIN_IN, 4)
    cmd = [GERBV, "--background=#FFFFFF", f"--foreground={FG}",
           f"--origin={ox}x{oy}", f"--window_inch={w}x{h}",
           layer_file, "--export=png", f"--dpi={DPI}", "-o", str(out_png)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0 or not Path(out_png).exists():
        raise SystemExit(f"gerbv failed for {layer_file}:\n{r.stderr[-2000:]}")


def size(png):
    r = subprocess.run([MAGICK, "identify", "-format", "%wx%h", str(png)],
                       capture_output=True, text=True)
    return r.stdout.strip()


def ink_fraction(png):
    """Fraction of the canvas covered by drawn copper. A render that comes back
    blank means the layer, the window or the file glob is wrong - which used to
    pass silently because nobody looked inside the image."""
    r = subprocess.run([MAGICK, str(png), "-colorspace", "Gray",
                        "-format", "%[fx:1-mean]", "info:"],
                       capture_output=True, text=True)
    try:
        return float(r.stdout.strip())
    except ValueError:
        return 0.0


def mean_difference(a, b):
    """Mean per-pixel difference between two renders, 0.0 = identical."""
    r = subprocess.run([MAGICK, str(a), str(b), "-compose", "difference",
                        "-composite", "-colorspace", "Gray",
                        "-format", "%[fx:mean]", "info:"],
                       capture_output=True, text=True)
    try:
        return float(r.stdout.strip())
    except ValueError:
        return 1.0


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--board", required=True)
    ap.add_argument("--config", required=True, type=Path)
    ap.add_argument("--kicad-dir", required=True, type=Path, help="dir with KiCad-exported gerbers")
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--repo", type=Path, default=Path("."),
                    help="repo root, for resolving original_zip / original_dir")
    args = ap.parse_args()

    cfg = yaml.safe_load(args.config.read_text())["boards"][args.board]["gerbers"]
    # Prefer the committed archive: a bare original_dir pointing at somebody's
    # scratch directory cannot be reproduced in CI or another checkout.
    if cfg.get("original_zip"):
        import zipfile
        zpath = args.repo / cfg["original_zip"]
        orig_dir = args.out / "_shipped"
        orig_dir.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(zpath) as z:
            z.extractall(orig_dir)
        # Packages vary: some put the gerbers at the root, others under a
        # Gerber/ subdirectory alongside a fabrication PDF. Locate the directory
        # that actually holds the outline layer rather than guessing.
        want = cfg["outline"]["original"]
        if not glob.glob(str(orig_dir / want)):
            hit = next((d for d in sorted(orig_dir.rglob("*"))
                        if d.is_dir() and glob.glob(str(d / want))), None)
            if hit is None:
                raise SystemExit(
                    f"{cfg['original_zip']} contains no {want!r} at any level")
            orig_dir = hit
    else:
        orig_dir = Path(cfg["original_dir"])
        if not orig_dir.is_absolute():
            orig_dir = args.repo / orig_dir
    tool = cfg.get("original_tool", "Original")
    args.out.mkdir(parents=True, exist_ok=True)

    k_outline = one(cfg["outline"]["kicad"], args.kicad_dir)
    o_outline = one(cfg["outline"]["original"], orig_dir)
    # Optional explicit render windows ([x0, y0, x1, y1] inches, gerber
    # coordinate frame per side). Needed when the shipped films carry a
    # drawing frame (e.g. Allegro artwork films) that breaks bbox-based
    # auto-alignment.
    win = cfg.get("window", {})
    k_bbox = tuple(win["kicad"]) if "kicad" in win else gerber_bbox_inches(k_outline)
    o_bbox = tuple(win["original"]) if "original" in win else gerber_bbox_inches(o_outline)
    # Silkscreen legitimately differs everywhere: Altium and KiCad stroke text
    # with different font metrics, so glyphs land a fraction of a millimetre
    # apart even when the port is exact. Copper, mask and paste have no such
    # excuse and are held to a tight threshold. Either can be overridden per
    # board, as a single number or a per-layer mapping.
    thr_cfg = cfg.get("max_mean_difference", {})
    if not isinstance(thr_cfg, dict):
        thr_cfg = {"default": float(thr_cfg)}

    def threshold(layer):
        if layer in thr_cfg:
            return float(thr_cfg[layer])
        if "Silkscreen" in layer or "Overlay" in layer:
            return float(thr_cfg.get("silkscreen", 0.06))
        return float(thr_cfg.get("default", 0.02))

    problems = []
    # The two renders only mean anything if they frame the same board. A shipped
    # outline layer that also carries a drawing frame or dimension artwork spans
    # far more than the board, which silently renders the two sides at different
    # scales - they then look like separate copies of the board rather than an
    # overlay, and every per-pixel comparison downstream is meaningless.
    kw, kh = k_bbox[2] - k_bbox[0], k_bbox[3] - k_bbox[1]
    ow, oh = o_bbox[2] - o_bbox[0], o_bbox[3] - o_bbox[1]
    if max(abs(kw - ow), abs(kh - oh)) > 0.05:
        problems.append(
            f"outline extents differ: KiCad {kw:.3f}x{kh:.3f} in vs "
            f"{cfg.get('original_tool', 'original')} {ow:.3f}x{oh:.3f} in. The "
            f"shipped outline probably includes a drawing frame or dimension "
            f"artwork; set an explicit `window:` for this board, or point "
            f"`outline.original` at a layer that carries only the board edge.")

    for layer, m in cfg["layers"].items():
        k_png = args.out / f"{layer}-KiCad.png"
        o_png = args.out / f"{layer}-{tool}.png"
        d_png = args.out / f"{layer}-diff.png"
        if m.get("negative"):
            # Altium internal-plane layers are negative images: drawn content
            # is where copper is ABSENT. Render each side alone, then convert
            # the original to a positive within the board interior.
            render_single(one(m["kicad"], args.kicad_dir), k_png, k_bbox)
            neg = args.out / f"{layer}-{tool}-negative.png"
            render_single(one(m["original"], orig_dir), neg, o_bbox)
            omask = args.out / f"{layer}-mask.png"
            render_single(o_outline, omask, o_bbox)
            # interior mask: flood the outside black, keep interior white
            subprocess.run([MAGICK, str(omask), "-colorspace", "Gray", "-fuzz", "40%",
                            "-fill", "black", "-draw", "color 0,0 floodfill",
                            "-threshold", "50%", str(omask)], check=True)
            # positive copper (dark) = interior AND NOT drawn
            subprocess.run([MAGICK, str(omask), "(", str(neg), "-colorspace", "Gray",
                            "-threshold", "80%", ")", "-compose", "multiply",
                            "-composite", "-negate", "-negate", str(o_png)], check=True)
            # o_png now: white background outside+drawn, dark copper... invert
            # to match the KiCad convention (copper dark on white):
            subprocess.run([MAGICK, str(o_png), "-negate", str(o_png)], check=True)
        else:
            render(k_outline, one(m["kicad"], args.kicad_dir), k_png, k_bbox)
            if cfg.get("original_has_outline"):
                # shipped films already draw the board outline (e.g. Allegro
                # artwork films) - render them alone
                render_single(one(m["original"], orig_dir), o_png, o_bbox)
            else:
                render(o_outline, one(m["original"], orig_dir), o_png, o_bbox)

        ks, os_ = size(k_png), size(o_png)
        if ks != os_:
            # Sub-pixel rounding can differ by 1px; pad to the larger size.
            w = max(int(ks.split("x")[0]), int(os_.split("x")[0]))
            h = max(int(ks.split("x")[1]), int(os_.split("x")[1]))
            if abs(int(ks.split("x")[0]) - int(os_.split("x")[0])) > 2 or \
               abs(int(ks.split("x")[1]) - int(os_.split("x")[1])) > 2:
                problems.append(f"{layer}: window size mismatch KiCad {ks} vs {tool} {os_} "
                                f"— check board outline equivalence")
            for p in (k_png, o_png):
                subprocess.run([MAGICK, "mogrify", "-background", "white",
                                "-gravity", "SouthWest", "-extent", f"{w}x{h}",
                                "+repage", str(p)], check=True)

        subprocess.run(
            [MAGICK, "(", str(k_png), "-grayscale", "Rec709Luminance", ")",
             "(", str(o_png), "-grayscale", "Rec709Luminance", ")",
             "(", "-clone", "0-1", "-compose", "darken", "-composite", ")",
             "-channel", "RGB", "-combine", str(d_png)], check=True)

        k_ink, o_ink = ink_fraction(k_png), ink_fraction(o_png)
        for who, frac, png in (("KiCad", k_ink, k_png), (tool, o_ink, o_png)):
            if frac < 1e-5:
                problems.append(f"{layer}: the {who} render {png.name} is blank "
                                f"- nothing was drawn, so the comparison is empty")
        diff = mean_difference(k_png, o_png)
        max_diff = threshold(layer)
        flag = ""
        if diff > max_diff:
            problems.append(f"{layer}: mean per-pixel difference {diff:.4f} "
                            f"exceeds the {max_diff} threshold - the two renders "
                            f"do not describe the same artwork")
            flag = "   <-- OVER THRESHOLD"
        print(f"  {layer}: rendered -> {d_png.name}  "
              f"(ink KiCad {k_ink:.4f} / {tool} {o_ink:.4f}, "
              f"mean diff {diff:.4f}){flag}")

    if problems:
        print("\nNotes (review these first):")
        for p in problems:
            print(f"  - {p}")
    print(f"\nDone. Review the *-diff.png files in {args.out} — KiCad-only content "
          f"appears in one color channel, {tool}-only in another.")
    print(f"\nRESULT: {'FAIL' if problems else 'PASS'} - "
          f"{len(cfg['layers'])} layers rendered, {len(problems)} structural problem(s)")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
