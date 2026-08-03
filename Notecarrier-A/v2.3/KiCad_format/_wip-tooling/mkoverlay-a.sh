#!/bin/zsh
S=/private/tmp/claude-501/-Users-roblauer-Documents-GitHub-blues-note-hardware/26345e84-f61c-4c64-85bd-58e534b0269f/scratchpad
cd "$S"
FAB="$1"; PORT="$2"; OUT="$3"; DPI="${4:-600}"
# film frame: board occupies film x -75..0, y 0..68  -> origin (-75/25.4, 0) window 75x68mm
gerbv --export=png --output=/tmp/af.png --dpi=$DPI --border=0 --origin=-2.9528x0.0 --window_inch=2.9528x2.6772 "$FAB" 2>/dev/null
# kicad frame: x 55..130, y 72..140 -> gerber y = -kicad_y  => origin (55/25.4, -140/25.4)
gerbv --export=png --output=/tmp/ap.png --dpi=$DPI --border=0 --origin=2.1654x-5.5118 --window_inch=2.9528x2.6772 "$PORT" 2>/dev/null
magick /tmp/af.png -colorspace gray -threshold 10% /tmp/afm.png
magick /tmp/ap.png -colorspace gray -threshold 10% /tmp/apm.png
magick /tmp/afm.png /tmp/apm.png \( -size $(magick identify -format '%wx%h' /tmp/afm.png) xc:black \) -combine "$OUT"
FO=$(magick /tmp/afm.png /tmp/apm.png -compose minus_src -composite -format "%[fx:mean*w*h]" info:)
PO=$(magick /tmp/apm.png /tmp/afm.png -compose minus_src -composite -format "%[fx:mean*w*h]" info:)
TOT=$(magick /tmp/afm.png -format "%[fx:mean*w*h]" info:)
echo "$OUT fab-only=$FO port-only=$PO fab-total=$TOT"
