#!/usr/bin/env python3
"""Compose the one-image summary of Tuesday 24 November 2026 world news.

Design: a newspaper front page. Every letter is drawn with PIL so the
text can never garble, and all graphics are PIL primitives too, which
keeps the output byte-for-byte deterministic across runs.

Stories (all verified against wire reporting on 2026-11-24 JST):
  lead    Nvidia reinstates Jensen Huang as CEO 11 days after he quit;
          shares +33%, Nasdaq +6.5%, S&P 500 +4.7% (Reuters).
  grid    Ukraine sea drones sink Russian corvette Merkury off Libya;
          Russian strikes kill 15 across Kyiv region;
          COP31 talks collapse in Antalya with no deal;
          Indonesia candy-factory fire kills 24, ~30 missing;
          Virginia & Oregon sue Musk companies over Grok images;
          Rep. Jimmy Gomez resigns after House ethics findings.
  ticker  UN chief seeks AI risk framework within a year;
          India pledges $1.6B to help Nepal rebuild after floods;
          storms threaten messy Thanksgiving travel in the U.S.;
          CAS rules today on Senegal's AFCON title appeal.
"""

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (247, 242, 231)
INK = (24, 24, 28)
MUTED = (92, 88, 80)
RED = (164, 32, 28)
NAVY = (16, 34, 64)
PANEL = (255, 253, 247)
LINE = (40, 40, 44)
GOLD = (255, 196, 64)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        trial = (cur + " " + w_).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, xy, text, fnt, fill, max_w, leading):
    x, y = xy
    for ln in wrap(draw, text, fnt, max_w):
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y


def centered(draw, y, text, fnt, fill):
    tw = draw.textlength(text, font=fnt)
    draw.text(((W - tw) / 2, y), text, font=fnt, fill=fill)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 44  # page margin

    # ---- masthead ------------------------------------------------------
    d.line([(M, 26), (W - M, 26)], fill=LINE, width=5)
    d.line([(M, 36), (W - M, 36)], fill=LINE, width=2)
    centered(d, 46, "THE WORLD TODAY", font(SERIF_B, 58), INK)
    centered(d, 118, "ONE IMAGE  ·  THE DAY'S WORLD NEWS", font(SANS_B, 18), MUTED)

    # ---- date band -------------------------------------------------------
    d.rectangle([0, 150, W, 206], fill=NAVY)
    centered(d, 160, "TUESDAY  24  NOVEMBER  2026", font(SANS_B, 40), (255, 255, 255))

    # ---- lead story --------------------------------------------------------
    y = 224
    d.text((M, y), "MARKETS  ·  TECH  ·  THE DAY'S BIG STORY", font=font(SANS_B, 20), fill=RED)
    y += 30
    hf = font(SERIF_B, 48)
    y = text_block(d, (M, y), "HUANG RETURNS TO NVIDIA —", hf, INK, W - 2 * M, 56)
    y = text_block(d, (M, y), "AND WALL STREET ERUPTS", hf, INK, W - 2 * M, 56)
    y += 6
    y = text_block(
        d, (M, y),
        "Founder Jensen Huang is back as CEO just 11 days after quitting, "
        "after President Trump pressed for his return — and investors "
        "answered with a record relief rally.",
        font(SERIF, 22), (52, 50, 46), W - 2 * M, 28)
    y += 12

    # stats strip: the three numbers of the rally
    d.rectangle([M, y, W - M, y + 58], fill=(13, 22, 40))
    d.text((M + 20, y + 8), "MONDAY'S", font=font(SANS_B, 17), fill=(170, 178, 190))
    d.text((M + 20, y + 30), "RELIEF RALLY", font=font(SANS_B, 17), fill=(170, 178, 190))
    stats = "NVIDIA +33%      NASDAQ +6.5%      S&P 500 +4.7%"
    sf = font(SANS_B, 31)
    sw = d.textlength(stats, font=sf)
    d.text((W - M - 20 - sw, y + 13), stats, font=sf, fill=(255, 255, 255))
    y += 58 + 18

    # ---- secondary grid: 2 columns x 3 rows --------------------------------
    stories = [
        ("UKRAINE WAR", "Sea drones sink Russian warship off Libya",
         "Russia's fleet struck far from home waters."),
        ("KYIV", "Russian strikes kill 15 across Kyiv region",
         "Apartment block hit in Dymer; toll rose Monday."),
        ("CLIMATE", "COP31 talks collapse with no deal",
         "Fossil-fuel wording split the Antalya summit."),
        ("INDONESIA", "Factory fire kills 24, 30 still missing",
         "Rescuers still search the Banten wreckage."),
        ("AI SAFETY", "U.S. states sue Musk firms over Grok images",
         "Sued over missing safeguards on 'spicy mode'."),
        ("WASHINGTON", "Rep. Gomez resigns after ethics findings",
         "House panel found evidence of misconduct."),
    ]
    gap = 18
    col_w = (W - 2 * M - gap) // 2
    row_h = 126
    tag_f = font(SANS_B, 17)
    head_f = font(SERIF_B, 23)
    body_f = font(SANS, 16)
    for i, (tag, head, body) in enumerate(stories):
        cx = M + (i % 2) * (col_w + gap)
        cy = y + (i // 2) * (row_h + 10)
        d.rectangle([cx, cy, cx + col_w, cy + row_h], fill=PANEL, outline=LINE, width=2)
        d.rectangle([cx, cy, cx + col_w, cy + 28], fill=INK)
        d.text((cx + 12, cy + 5), tag, font=tag_f, fill=(255, 255, 255))
        hy = text_block(d, (cx + 12, cy + 36), head, head_f, INK, col_w - 24, 27)
        d.text((cx + 12, hy + 4), body, font=body_f, fill=(70, 67, 60))
    y += 3 * (row_h + 10) + 4

    # ---- footer ticker -------------------------------------------------------
    d.rectangle([0, y, W, H], fill=INK)
    d.text((M, y + 12), "ALSO TODAY", font=font(SANS_B, 19), fill=GOLD)
    ticker = ("UN chief seeks an AI risk framework within a year  •  "
              "India pledges $1.6B to help Nepal rebuild after floods  •  "
              "Storms threaten messy Thanksgiving travel  •  "
              "CAS rules today on Senegal's AFCON title appeal")
    text_block(d, (M, y + 42), ticker, font(SANS, 19), (238, 236, 228), W - 2 * M, 25)

    img.save("entry.png", format="PNG", optimize=True)
    print("wrote entry.png")


if __name__ == "__main__":
    main()
