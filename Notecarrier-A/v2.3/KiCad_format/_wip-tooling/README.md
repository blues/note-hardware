# Conversion tooling for the (incomplete) Notecarrier-A v2.3 port

These scripts reconstructed the v2.3 board from the published Allegro artwork
films — see [`../STATUS-INCOMPLETE.md`](../STATUS-INCOMPLETE.md) for what they
achieved and where the port is blocked. They are committed so the approach is
reproducible, not as runnable tools: they were written for the porting Docker
container (`kicad/kicad:9.0.9`, this repository mounted at `/blues`, scratch
files at `/scratch`), so every hardcoded path must be adapted before running
them anywhere else.
