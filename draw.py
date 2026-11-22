#!/usr/bin/env python3
"""news-image-20261122: paint the 22 November 2026 front page.

Renders "THE WORLD TODAY" as a 1024x1024 newspaper front page from the
AI-made hero illustration (hero.png) and the day's verified stories, and
writes entry.png next to this file. Pure Pillow, no network, deterministic:
same inputs give the same bytes every run.
"""

import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
SIZE = 1024
PAPER = (246, 241, 225)
INK = (26, 24, 20)
FAINT = (96, 90, 78)
RED = (155, 28, 28)
BAND = (30, 28, 26)
RULE = (150, 142, 124)

SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SERIF_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF_ITALIC = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap; returns a list of lines that fit in width px."""
    lines = []
    for chunk in text.split("\n"):
        words = chunk.split()
        line = ""
        for word in words:
            trial = (line + " " + word).strip()
            if draw.textlength(trial, font=fnt) <= width:
                line = trial
            else:
                if line:
                    lines.append(line)
                line = word
        if line:
            lines.append(line)
    return lines


def text_block(draw, x, y, text, fnt, width, leading, color=INK):
    """Draw wrapped text; returns the y just below the last line."""
    for line in wrap(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=color)
        y += leading
    return y


def centered(draw, y, text, fnt, color=INK):
    w = draw.textlength(text, font=fnt)
    draw.text(((SIZE - w) / 2, y), text, font=fnt, fill=color)
    return y + fnt.size


def rule(draw, y, x0=30, x1=994, color=RULE, width=1):
    draw.line([(x0, y), (x1, y)], fill=color, width=width)


# ---------------------------------------------------------------- stories

LEAD_HEADLINE = "GULF IN FLAMES AGAIN"
LEAD_DECK = ("Tehran claims two US bases hit; Washington says the barrage was "
             "intercepted -- the fourth attack on Bahrain in nine days.")
LEAD_COL_A = ("Iran's Revolutionary Guards struck two US military sites in "
              "Bahrain on Saturday night, Sheikh Isa Air Base and the US "
              "Navy Fifth Fleet headquarters at Juffair, in the fourth "
              "Iranian attack on the island kingdom in nine days.")
LEAD_COL_B = ("Bahrain sounded air-raid sirens and told residents to take "
              "shelter; a civilian industrial facility was hit and set on "
              "fire. US Central Command said defences intercepted the "
              "incoming weapons and reported no US damage or casualties. "
              "Tehran called the barrage retaliation for US strikes.")

SECONDARY = [
    ("BALTIC SEA",
     "Drones set Russian cargo ship ablaze",
     "The sanctioned Sparta II, bound for Kaliningrad, drifted burning "
     "into Finnish waters; its 16 crew took to lifeboats."),
    ("UKRAINE",
     "Missiles kill boy, 7, and paramedic",
     "A Russian 'triple-tap' strike on Kryvyi Rih, Zelenskyy's hometown, "
     "wounded 60 and hit rescuers as they worked."),
    ("CLIMATE",
     "COP31: 'a good deal or no deal'",
     "Talks in Antalya spill into overtime with fossil fuels stripped "
     "from the draft and a $120bn finance target dropped."),
]

NUMBERS = [
    ("4", "Iranian attacks on Bahrain in nine days"),
    ("6.9", "magnitude of Peru's Andes quake"),
    ("723", "seats contested in Hong Kong's vote"),
    ("98.5%", "of tariffs the EU-Indonesia deal scraps"),
]

# Six sections x 3 self-contained headlines each.
SECTIONS = [
    ("MIDDLE EAST", [
        "Trump seeks a permanent nuclear accord with Iran",
        "Two tankers hit by mystery blasts off Oman",
        "Blast at Basra power plant kills four, wounds 30",
    ]),
    ("EUROPE", [
        "Estonia to close its border with Russia",
        "Berlin rallies the Coalition of the Willing",
        "Denmark: Russia plotted to kill a US-Ukrainian",
    ]),
    ("AMERICAS", [
        "Mexico seizes 'El Chapo Isidro' in bloody raid",
        "Bolsonaro taken to intensive care in Brasilia",
        "Pentagon redraws US-Canada defence ties",
    ]),
    ("ASIA & PACIFIC", [
        "Hong Kong votes for its Election Committee",
        "Trump, Xi and Putin meet in Shenzhen",
        "Modi opens the Nitish Setu bridge in Bihar",
    ]),
    ("WORLD", [
        "Peru shaken by magnitude 6.9 quake",
        "UN peacekeepers hand south Lebanon to army",
        "FBI probes hack of its criminal database",
    ]),
    ("SPORT & CULTURE", [
        "Arsenal six points clear after Newcastle draw",
        "Ireland stun world champions South Africa",
        "'Spitting Image' co-creator Peter Fluck dies at 85",
    ]),
]

ALSO_TODAY = ("Crude oil -3%  |  EU budget $224bn below draft  |  S. Korea: $75,000 "
              "exam-cheating bounty  |  France protests, week 6  |  M6.8 quake off Timor-Leste")


# ---------------------------------------------------------------- painting

def hero_crop():
    """Centre-crop the hero to a wide banner, keeping missiles and skyline."""
    img = Image.open(os.path.join(HERE, "hero.png")).convert("RGB")
    img = img.resize((964, 642), Image.LANCZOS)
    return img.crop((0, 176, 964, 398))


def main():
    page = Image.new("RGB", (SIZE, SIZE), PAPER)
    d = ImageDraw.Draw(page)

    # double outer border
    d.rectangle([8, 8, SIZE - 9, SIZE - 9], outline=INK, width=2)
    d.rectangle([15, 15, SIZE - 16, SIZE - 16], outline=RULE, width=1)

    # ---- masthead
    centered(d, 26, "THE WORLD TODAY", font(SERIF_BOLD, 60))
    y = 94
    left = "SUNDAY, 22 NOVEMBER 2026"
    right = "ONE IMAGE  -  THE WHOLE DAY"
    f_small = font(SANS_BOLD, 13)
    d.text((30, y), left, font=f_small, fill=INK)
    rw = d.textlength(right, font=f_small)
    d.text((994 - rw, y), right, font=f_small, fill=INK)
    mid = "27 STORIES  -  6 SECTIONS"
    mw = d.textlength(mid, font=f_small)
    d.text(((SIZE - mw) / 2, y), mid, font=f_small, fill=FAINT)
    rule(d, 116, width=2)

    # ---- lead headline + deck
    centered(d, 124, LEAD_HEADLINE, font(SERIF_BOLD, 44), color=RED)
    centered(d, 168, LEAD_DECK, font(SERIF_ITALIC, 16))

    # ---- hero banner
    banner = hero_crop()
    page.paste(banner, (30, 192))
    d.rectangle([30, 192, 993, 413], outline=INK, width=2)
    d.text((30, 418), "Interceptors climb over a Gulf port as air-raid sirens sound in Bahrain. "
                      "Illustration: AI-generated.", font=font(SERIF_ITALIC, 11), fill=FAINT)

    # ---- lead text, two columns
    f_lead = font(SERIF, 13)
    col_w = 472
    end_a = text_block(d, 30, 438, LEAD_COL_A, f_lead, col_w, 18)
    end_b = text_block(d, 522, 438, LEAD_COL_B, f_lead, col_w, 18)
    rule(d, 552)

    # ---- three secondary stories
    sec_y = 560
    col_w = 306
    for i, (kicker, head, deck) in enumerate(SECONDARY):
        x = 30 + i * 322
        d.text((x, sec_y), kicker, font=font(SANS_BOLD, 11), fill=RED)
        y2 = text_block(d, x, sec_y + 16, head, font(SERIF_BOLD, 15), col_w, 18)
        text_block(d, x, y2 + 2, deck, font(SERIF, 12), col_w, 15, color=FAINT)
    rule(d, 648)

    # ---- by the numbers band
    d.rectangle([30, 654, 993, 702], fill=BAND)
    band_w = 964 / len(NUMBERS)
    for i, (num, label) in enumerate(NUMBERS):
        cx = 30 + band_w * i + band_w / 2
        f_num = font(SERIF_BOLD, 20)
        nw = d.textlength(num, font=f_num)
        d.text((cx - nw / 2, 657), num, font=f_num, fill=(250, 246, 236))
        f_lab = font(SANS, 10)
        lw = d.textlength(label, font=f_lab)
        d.text((cx - lw / 2, 685), label, font=f_lab, fill=(196, 190, 174))

    # ---- six sections, 3 columns x 2 rows
    grid_y = 710
    cell_w = 306
    cell_h = 126
    for idx, (title, items) in enumerate(SECTIONS):
        col = idx % 3
        row = idx // 3
        x = 30 + col * 322
        y = grid_y + row * (cell_h + 6)
        d.text((x, y), title, font=font(SANS_BOLD, 12), fill=RED)
        rule(d, y + 16, x0=x, x1=x + cell_w, color=INK, width=1)
        iy = y + 22
        for head in items:
            lines = wrap(d, head, font(SERIF_BOLD, 12), cell_w)
            assert len(lines) <= 2, f"headline too long: {head}"
            iy = text_block(d, x, iy, head, font(SERIF_BOLD, 12), cell_w, 14)
            iy += 5
        assert iy <= y + cell_h + 2, f"section {title} overflow: {iy} > {y + cell_h}"

    # ---- also today
    rule(d, 974, width=2)
    d.text((30, 980), "ALSO TODAY:  " + ALSO_TODAY, font=font(SANS_BOLD, 11), fill=INK)

    out = os.path.join(HERE, "entry.png")
    page.save(out, "PNG", optimize=True)
    print(f"wrote {out} {os.path.getsize(out)} bytes")


if __name__ == "__main__":
    main()
