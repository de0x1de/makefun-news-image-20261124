# News Image — Tuesday 24 November 2026

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/de0x1de/makefun-news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/de0x1de/makefun-news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

A one-image summary of the world's news of **Tuesday 24 November 2026**,
drawn as a newspaper front page: a big date band, one lead story with the
day's market numbers, six secondary stories in a grid, and a footer
ticker with four more.

## The day's stories

- **Lead — Huang returns to Nvidia, and Wall Street erupts.** Jensen
  Huang is back as CEO just 11 days after quitting, after President
  Trump pressed for his return; Nvidia shares jumped about 33%, the
  Nasdaq 6.5% and the S&P 500 4.7% in a record relief rally.
- Ukraine's sea drones sink the Russian corvette Merkury off Libya.
- Russian strikes kill 15 across the Kyiv region.
- COP31 climate talks collapse in Antalya with no deal.
- A candy-factory fire in Banten, Indonesia kills 24, with 30 missing.
- Virginia and Oregon sue Musk's companies over Grok's sexualised images.
- Rep. Jimmy Gomez resigns after House ethics findings.
- Ticker: the UN chief seeks an AI risk framework within a year; India
  pledges $1.6B to help Nepal rebuild after floods; storms threaten
  messy Thanksgiving travel; CAS rules on Senegal's AFCON title appeal.

Every headline was checked against wire reporting (Reuters, AP,
Al Jazeera, CNA and others) on the day itself.

## How it works

- `entry.png` — the finished image (1024×1024 PNG, well under 1 MiB).
  All lettering is drawn programmatically, so no text can garble.
- `compose.py` — the generator that draws `entry.png` from scratch
  with PIL; running it twice yields byte-identical output.
- `main.py` — the submitted program. It copies the repository's
  `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (default
  `/output/entry.png`), verifying the PNG signature and the 1 MiB
  limit first. No network, fully deterministic.

## License

MIT — see `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=tjxzfppk&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>
