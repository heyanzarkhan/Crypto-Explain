# Crypto, Explained — Animated Video

A ~7-minute minimal animated YouTube explainer built with [Manim Community](https://www.manim.community/).
Covers cryptocurrency, USDT, blockchain, wallets / transactions, and P2P — including the trust & risk side of each.

> **Watch:** [`final.mp4`](final.mp4) (720p, ~5 MB)

```
crypto-explain/
├── final.mp4            ← the rendered video (720p)
├── theme.py             ← colors, fonts, shape & icon helpers
├── crypto_video.py      ← all 7 scenes
├── style_test.py        ← 25 s style preview (used to lock the look)
├── script.md            ← narration for ElevenLabs / your own VO
├── render_all.sh        ← renders every scene + concatenates a new final.mp4
└── media/               ← (gitignored) Manim build output
```

---

## Quick start

```bash
# already installed during setup — re-activate the venv whenever you come back
source .venv/bin/activate

# fast preview (720p)
bash render_all.sh preview

# production render (1080p)
bash render_all.sh
```

Output appears at `media/videos/crypto_video/720p30/final.mp4` (or `1080p30/`).

### Render a single scene while iterating

```bash
manim -qm crypto_video.py WhatIsBlockchain     # 720p
manim -qh crypto_video.py WhatIsBlockchain     # 1080p
manim -qk crypto_video.py WhatIsBlockchain     # 4K
```

---

## Scene structure & timings

| # | Scene class                | Topic                          | Length  |
| - | -------------------------- | ------------------------------ | ------- |
| 1 | `Intro`                    | hook + title                   | ~13 s   |
| 2 | `WhatIsCrypto`             | bank vs. crypto, networks, BTC/ETH/SOL | ~66 s |
| 3 | `WhatIsUSDT`               | volatility, stablecoin, 1 USDT = $1 | ~54 s |
| 4 | `WhatIsBlockchain`         | notebook → blocks → chain, tampering | ~89 s |
| 5 | `WalletsAndTransactions`   | wallet, public/private keys, block explorer | ~89 s |
| 6 | `WhatIsP2P`                | bank middleman → direct mesh   | ~61 s   |
| 7 | `Outro`                    | recap + close                  | ~25 s   |
|   |                            | **TOTAL**                      | **~6:37** |

Each scene is paced to match the corresponding section in `script.md`.

---

## Adding voiceover (ElevenLabs workflow)

1. Open `script.md`. Each numbered section is one narration block.
2. In ElevenLabs, generate each block as its own MP3:
   ```
   01_intro.mp3
   02_crypto.mp3
   03_usdt.mp3
   04_blockchain.mp3
   05_wallets.mp3
   06_p2p.mp3
   07_outro.mp3
   ```
   Suggested voices: **Brian** (warm) or **Charlotte** (clear).
   Settings: Stability ~ 50, Similarity ~ 70, Style ~ 10, Speaker boost on.
3. Drop all 7 audio files + `final.mp4` into your editor (CapCut / Premiere / DaVinci).
4. Place each MP3 at the start of its matching scene. Scenes already have ~2–4 s of breathing room at the end so the narration fits even if you record slightly long.
5. Add background music at ~ −24 dB (lo-fi piano works well).
6. Export at 1080p H.264 for YouTube.

---

## Tweaking the look

Everything visual is centralized in `theme.py`:

- **Background, ink, accent colors** — top of the file
- **Font** — `FONT_SANS = "Helvetica Neue"` (change to "Inter", "SF Pro", "Geist", etc.)
- **Reusable shapes** — `block()`, `chip()`, `card()`, `wallet_icon()`, `bank_icon()`, `phone_icon()`, `coin_icon()`, `globe_icon()`

Change one value in `theme.py` and every scene picks it up on re-render.

---

## Re-rendering after edits

```bash
# edit theme.py or crypto_video.py
bash render_all.sh preview         # ~3 min on M-series Mac
```

For a single scene during iteration, prefer `-ql` (very fast 480p):

```bash
manim -ql crypto_video.py WhatIsUSDT
```
