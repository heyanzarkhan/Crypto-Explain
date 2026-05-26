#!/usr/bin/env bash
# Render every scene in crypto_video.py and concatenate into final.mp4
#
# Usage:
#     bash render_all.sh              # 1080p30 production render
#     bash render_all.sh preview      # 720p30 fast preview
#
set -euo pipefail

cd "$(dirname "$0")"
source .venv/bin/activate

QUALITY_FLAG="-qh"        # 1080p
QUALITY_DIR="1080p30"
if [[ "${1:-}" == "preview" ]]; then
    QUALITY_FLAG="-qm"
    QUALITY_DIR="720p30"
fi

SCENES=(Intro WhatIsCrypto WhatIsUSDT WhatIsBlockchain WalletsAndTransactions WhatIsP2P Outro)

echo "▶ rendering ${#SCENES[@]} scenes at ${QUALITY_DIR}…"
for s in "${SCENES[@]}"; do
    echo "  · $s"
    manim $QUALITY_FLAG crypto_video.py "$s" >/dev/null
done

# concatenate
OUT_DIR="media/videos/crypto_video/${QUALITY_DIR}"
LIST_FILE="$OUT_DIR/concat.txt"
echo "▶ concatenating into final.mp4…"
: > "$LIST_FILE"
for s in "${SCENES[@]}"; do
    echo "file '${s}.mp4'" >> "$LIST_FILE"
done

ffmpeg -y -hide_banner -loglevel error -f concat -safe 0 \
    -i "$LIST_FILE" -c copy "$OUT_DIR/final.mp4"

echo "✓ done — $OUT_DIR/final.mp4"
open "$OUT_DIR/final.mp4" 2>/dev/null || true
