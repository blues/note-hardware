# extract_for_rag

Converts the **Tier-1** hardware design files in this repo into clean **HTML pages + a
`sitemap.xml`** under [`rag-extracted/`](rag-extracted/), published to **GitHub Pages** and indexed
by ragpi's **`sitemap` connector** (which powers the AI hardware chatbot). Raw schematic/drawing
PDFs and proprietary CAD files don't index well — naive PDF text extraction turns a schematic into
token salad — so this tool produces search-friendly pages instead. Each page links back to its
original source file (GitHub blob URL).

> Why HTML + sitemap, not markdown? ragpi's `github_readme` connector only fetches a repo/dir's
> single `README.md` (GitHub "get README" API) — it can't index arbitrary `.md` files. The
> `sitemap` connector crawls HTML over HTTP, which is why the output is published to Pages.

## What it indexes (Tier 1)

| Source | Output (`<source>.html`) |
|---|---|
| BOMs (`*.xlsx`, `*.csv` — excluding pick-and-place) | HTML tables (per sheet) |
| KiCad schematics (`*.kicad_sch`) | parsed component table + net/label list |
| Schematic PDFs (`*.pdf` whose name/path says "schematic"/"sch", or the `100xxxx_…_Rev-NN` convention) | per-page description from a vision model (VLM) |

Page bodies live in `<main>` (with the source-file link) so ragpi's crawler — which keeps
`<main>`/`<body>` and strips `nav/header/footer/img/...` — indexes the real content. The
`<title>` becomes the page title; tables and links survive the HTML→text conversion.

**Not indexed** (by design): dimension/assembly drawing PDFs, `README.md`, pick-and-place (`.pnp`),
Gerbers/`.zip` fab packages, board files (`.brd`), 3D models (`.step`/`.stp`/`.stl`), Altium
binaries, everything under `_Legacy Hardware/`, and everything under `KiCad_format/validation/`
(QA port-comparison artifacts — Gerber-diff PNGs plus BOMs re-exported from both OrCAD/Altium and
KiCad, which are ~90-93% replicants of the canonical board BOM).

**BOM dedup:** after selection, if two BOMs for the same board share ≥90% of their reference
designators, only one is kept (prefers `.xlsx` over `.csv`, then the shortest path). This drops
exact duplicates (e.g. Notecarrier-CX's Production BOM stored in two folders) while keeping
genuinely distinct BOMs such as Swan Carrier vs Feather.

## Version selection

Dedupe is **per (product, doc-type)**: for each product and doc-type we keep only the files from
the newest `vX.Y` folder that actually contains that doc-type. This avoids indexing the same board
twice while preserving coverage when a newer revision only adds an unrelated document (e.g.
Notecarrier-A's schematic/BOM/KiCad live in `v2.0`; `v2.3` only adds a PCB doc, so `v2.0` is kept
for those types).

## Usage

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt

export OPENAI_API_KEY=sk-...        # required for schematic-PDF extraction
export RAG_VLM_MODEL=gpt-5.5        # optional; defaults to gpt-5.5
# optional URL overrides (defaults: Pages URL + GitHub blob):
export RAG_BASE_URL=https://blues.github.io/note-hardware/
export RAG_SOURCE_BASE_URL=https://github.com/blues/note-hardware/blob/master/

python extract.py --changed-from changed.txt   # default mode (incremental): re-extract changed/missing
python extract.py                  # incremental, no diff: generate missing + prune only
python extract.py --full           # explicit clean rebuild (wipe + regenerate everything)
python extract.py --full --no-vlm  # rebuild BOM/KiCad only, skip the costly PDF vision step
```

Every run also (re)writes `sitemap.xml` (listing the full current selection) and a `.nojekyll`
marker. `<loc>` URLs are `RAG_BASE_URL` + the percent-encoded page path.

**Incremental is the default**; `--full` is the explicit clean-rebuild opt-in. `--changed-from`
takes a file of newline-separated repo-relative source paths (CI feeds it `git diff --name-only`).
Each incremental run **reconciles output against the current selection**:
- a selected file is regenerated if its source changed **or** it has no HTML yet (e.g. a
  newly-added version folder);
- HTML whose source was deleted **or superseded by a newer version** is pruned.

So adding a new `vX.Y` folder correctly resets that product — the new version's files are
generated and the old version's are dropped — without re-running unchanged files (e.g. a schematic
that only exists at the older version, and didn't change, is left as-is). Untouched, still-selected
files are never regenerated.

**Regeneration is a clean slate.** A `--full` run deletes existing outputs for the doc-types it is
about to regenerate *before* extracting, so a file that fails to re-extract (or is no longer
selected) is absent rather than left stale, then prunes any remaining orphans and empty dirs.
Exception: under `--no-vlm`, schematic outputs are preserved (not deleted), since that mode can't
rebuild them. A production full rebuild (`workflow_dispatch` with the API key set) therefore wipes
and regenerates everything.

## Automation

[`.github/workflows/rag-extract.yml`](../../.github/workflows/rag-extract.yml) re-runs this tool on
every merge to `master` (**incrementally** by default), commits the refreshed output under
`_Tools/extract_for_rag/rag-extracted/`, and **publishes that folder to GitHub Pages** (the `deploy`
job). The workflow ignores pushes that only touch the output dir so its own commit doesn't
retrigger it. A clean full rebuild is opt-in via `workflow_dispatch` (`full: true`).

Requires (one-time): repo **Settings → Pages → Source = GitHub Actions**, the `OPENAI_API_KEY`
**secret** (a credential — never a variable), and a **public** repo (ragpi crawls the Pages site
over plain HTTP). Optional repo **variables**: `RAG_VLM_MODEL`, `RAG_BASE_URL`, `RAG_SOURCE_BASE_URL`.

**Search indexing:** every page carries `<meta name="robots" content="noindex, nofollow">` (the
authoritative control on a project `*.github.io` path) and a root `robots.txt` allows only the
`Ragpi` crawler. ragpi ignores robots-meta, so it still indexes; public search engines won't.

## Out of scope

Creating/configuring the ragpi `sitemap` source that points at the published sitemap
(`sitemap_url: https://blues.github.io/note-hardware/sitemap.xml`), and the cadence on which it
re-syncs, are handled separately.
