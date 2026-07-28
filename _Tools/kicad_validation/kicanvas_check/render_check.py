#!/usr/bin/env python3
"""Headless kicanvas render check for KiCad schematic/board files.

For each input file, serves a minimal page embedding the vendored kicanvas.js
(`<kicanvas-embed src=...>`), loads it in headless Chromium (Playwright),
fails on any console error / page error, screenshots the result, and applies a
non-blank heuristic (pixel standard deviation via ImageMagick).

Usage:
    render_check.py --out <screenshot-dir> file1.kicad_sch [file2.kicad_pcb ...]

Exit 0 = every file rendered without errors and non-blank; 1 otherwise.
The screenshots still require human eyeballing — this gate only proves
kicanvas can parse and paint the files.
"""

import argparse
import http.server
import shutil
import socket
import subprocess
import sys
import tempfile
import threading
from pathlib import Path

from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent

PAGE = """<!DOCTYPE html>
<html><head><meta charset="utf-8"><script type="module" src="/kicanvas.js"></script>
<style>html,body{{margin:0;height:100%}}kicanvas-embed{{display:block;width:100%;height:100vh}}</style>
</head><body>
<kicanvas-embed src="/{fname}" controls="none"></kicanvas-embed>
</body></html>
"""

# Messages kicanvas emits that are not parse/render failures.
CONSOLE_IGNORE = ("favicon", "Download the Vue Devtools")


def serve(directory: Path):
    handler = lambda *a, **kw: http.server.SimpleHTTPRequestHandler(
        *a, directory=str(directory), **kw)
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        port = s.getsockname()[1]
    httpd = http.server.ThreadingHTTPServer(("127.0.0.1", port), handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd, port


def stddev(png: Path) -> float:
    r = subprocess.run(["magick", str(png), "-colorspace", "Gray",
                        "-format", "%[fx:standard_deviation]", "info:"],
                       capture_output=True, text=True)
    try:
        return float(r.stdout.strip())
    except ValueError:
        return -1.0


def check_file(target: Path, out_dir: Path, browser) -> list[str]:
    problems = []
    with tempfile.TemporaryDirectory() as td:
        tdir = Path(td)
        shutil.copy(HERE / "kicanvas.js", tdir / "kicanvas.js")
        shutil.copy(target, tdir / target.name)
        (tdir / "index.html").write_text(PAGE.format(fname=target.name))
        httpd, port = serve(tdir)
        try:
            page = browser.new_page(viewport={"width": 1600, "height": 1200})
            errors = []
            page.on("console", lambda m: errors.append(f"console.{m.type}: {m.text}")
                    if m.type in ("error",) and not any(i in m.text for i in CONSOLE_IGNORE) else None)
            page.on("pageerror", lambda e: errors.append(f"pageerror: {e}"))
            page.goto(f"http://127.0.0.1:{port}/", wait_until="networkidle")
            page.wait_for_timeout(3000)
            shot = out_dir / f"kicanvas-{target.stem}{target.suffix.replace('.', '_')}.png"
            page.screenshot(path=str(shot))
            page.close()
            if errors:
                problems.extend(f"{target.name}: {e}" for e in errors)
            sd = stddev(shot)
            if sd < 0.005:
                problems.append(f"{target.name}: screenshot looks blank "
                                f"(stddev={sd:.4f}) — see {shot.name}")
        finally:
            httpd.shutdown()
    return problems


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", required=True, type=Path, help="screenshot output dir")
    ap.add_argument("files", nargs="+", type=Path)
    args = ap.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    all_problems = []
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        for f in args.files:
            print(f"  kicanvas: {f.name} ...", flush=True)
            probs = check_file(f, args.out, browser)
            all_problems.extend(probs)
            print("    " + ("OK" if not probs else "\n    ".join(probs)))
        browser.close()

    if all_problems:
        print(f"\nRESULT: FAIL ({len(all_problems)} problem(s))")
        sys.exit(1)
    print("\nRESULT: PASS — all files rendered in kicanvas without errors.")
    sys.exit(0)


if __name__ == "__main__":
    main()
