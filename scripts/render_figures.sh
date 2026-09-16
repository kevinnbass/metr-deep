#!/usr/bin/env bash
# Render figures/*.html (or the stems given) to figures/png/<stem>.png with the bundled headless Chromium, then crop
# trailing background rows so each PNG ends where the figure ends. No network, no install.
set -u
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CH="$(ls -d "$HOME"/.cache/ms-playwright/chromium-*/chrome-linux*/chrome 2>/dev/null | sort | tail -1)"
[ -x "$CH" ] || { echo "no headless chromium found under ~/.cache/ms-playwright"; exit 1; }
mkdir -p "$ROOT/figures/png"; W="${WIDTH:-1500}"; H="${HEIGHT:-7000}"; ok=0; fail=0
if [ $# -gt 0 ]; then files=(); for s in "$@"; do files+=("$ROOT/figures/$s.html"); done; else files=("$ROOT"/figures/*.html); fi
for f in "${files[@]}"; do
  stem="$(basename "$f" .html)"; out="$ROOT/figures/png/$stem.png"
  timeout 120 "$CH" --headless=new --no-sandbox --disable-gpu --hide-scrollbars --window-size=${W},${H} --virtual-time-budget=3000 \
      --screenshot="$out" "file://$f" >/dev/null 2>&1 || { fail=$((fail+1)); echo "FAIL $stem"; continue; }
  python3 - "$out" <<'PY'
import sys; from PIL import Image
p=sys.argv[1]; im=Image.open(p).convert("RGB"); w,h=im.size; bg=im.getpixel((w-1,h-1)); px=im.load()
y=h-1
while y>0 and all(px[x,y]==bg for x in range(0,w,7)): y-=1
im.crop((0,0,w,min(h,y+48))).save(p)
PY
  ok=$((ok+1)); echo "PNG $stem.png"
done
echo "rendered ok=$ok fail=$fail -> $ROOT/figures/png/"; [ "$fail" = 0 ]
