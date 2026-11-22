# news-image-20261122

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/Siksuk72/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/Siksuk72/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

One image that sums up the world's news of Sunday 22 November 2026.
It is a one-page newspaper front page: the drawing is done in code
with Python Pillow (`draw.py`), so every word is spelled right and
stays readable at ~300 px, and the picture of interceptors climbing
over a Gulf port at night is an AI-made illustration (`hero.png`).
`main.ts` (Node 22, stdlib only) puts the finished picture at
`/output/entry.png` for the grader.

## What's on the page

- Masthead "THE WORLD TODAY" + "SUNDAY, 22 NOVEMBER 2026 • 27 STORIES • 6 SECTIONS"
- Lead: Iran strikes two US military sites in Bahrain on Saturday night —
  Sheikh Isa Air Base and the Fifth Fleet HQ at Juffair — the fourth
  Iranian attack on Bahrain in nine days; sirens, a civilian facility
  ablaze, CENTCOM says the barrage was intercepted.
- 3 secondary stories: drones set the sanctioned Russian cargo ship
  Sparta II ablaze in the Gulf of Finland; a Russian 'triple-tap' strike
  kills a 7-year-old boy and a paramedic in Kryvyi Rih; COP31 spills into
  overtime in Antalya with fossil fuels stripped from the draft.
- "BY THE NUMBERS" strip: 4 attacks on Bahrain in 9 days, 6.9 Peru quake,
  723 Hong Kong seats, 98.5% tariffs scrapped by the EU-Indonesia deal.
- 6 sections × 3 stories each (18 stories).
- "ALSO TODAY" strip with 5 more briefs. Total: 27 stories.

## The 27 stories (all first reported on 21–22 Nov 2026)

### Lead
1. Iran strikes US bases in Bahrain — IRGC hits Sheikh Isa Air Base and the
   Fifth Fleet HQ at Juffair on Saturday night, the fourth attack in nine
   days; Bahrain sounds sirens, a civilian industrial facility burns;
   CENTCOM says defences intercepted the barrage, no US damage or
   casualties — Reuters / AP / Fars / CENTCOM

### Secondary
2. Drones hit the sanctioned Russian cargo ship Sparta II in the Gulf of
   Finland; the burning vessel drifts into Finnish waters, 16 crew take to
   lifeboats; Finland says Ukraine is likely behind it — Reuters / CNN
3. Russian ballistic missiles kill a 7-year-old boy and a 20-year-old
   paramedic and wound 60 in a 'triple-tap' strike on Kryvyi Rih,
   Zelenskyy's hometown — AP / CNN
4. COP31 spills into overtime in Antalya: "a good deal or no deal", the EU
   warns; fossil fuels stripped from the draft, a $120bn adaptation
   finance target dropped; Ethiopia to host COP32 — Reuters / AP

### Middle East
5. Trump seeks a permanent nuclear accord with Iran — Fox News
6. Two tankers hit by unidentified projectiles off Oman, in the Strait of
   Hormuz — UKMTO
7. Blast at a Basra power plant kills four, wounds 30 — reports

### Europe
8. Estonia to close its border with Russia; Moscow denounces a "new Iron
   Curtain" — reports
9. Germany rallies the Coalition of the Willing in Berlin — reports
10. Denmark says Russia plotted to kill a US-Ukrainian citizen — reports

### Americas
11. Mexico captures "El Chapo Isidro" in a bloody Sinaloa raid; 11 dead,
    gunfire empties a baseball stadium — CNN / Reuters / AP
12. Jailed ex-president Bolsonaro taken to intensive care in Brasilia,
    stable with an acute bowel obstruction — Reuters
13. Pentagon redraws US-Canada defence ties; Hegseth limits "social
    activities" with Canadian forces — reports

### Asia & Pacific
14. Hong Kong votes for its Election Committee: 856 candidates contest 723
    seats — Hong Kong government / reports
15. Trump, Xi and Putin hold their first-ever trilateral meeting in
    Shenzhen, on the APEC margins — reports
16. Modi opens the Nitish Setu bridge in Bihar, linking Patna and Vaishali
    — reports

### World
17. Magnitude 6.9 earthquake shakes Peru's Andes; felt in Lima, no damage
    or casualties reported — USGS / AP
18. UN peacekeepers begin handing south Lebanon to the Lebanese army —
    UNIFIL / reports
19. FBI investigates an apparent hack of its criminal database — BBC

### Sport & Culture
20. Arsenal go six points clear after a draw at Newcastle; Leeds beat
    Chelsea at Stamford Bridge for the first time since 1999 — BBC Sport
21. Ireland stun world champions South Africa in a thriller — BBC Sport
22. "Spitting Image" co-creator Peter Fluck dies aged 85 — BBC

### Also today
23. Crude oil futures slide more than 3% — reports
24. EU Council leader proposes an extended EU budget $224bn below the
    Commission's draft — reports
25. South Korea repeats a $75,000 bounty for reporting exam cheating —
    reports
26. French protests enter a sixth week; turnout falls to 82,500 — reports
27. Magnitude 6.8 earthquake strikes off Timor-Leste, north-east of
    Lospalos — USGS

## Reproduce

```sh
python3 draw.py        # renders entry.png (1024x1024, deterministic)
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts   # copies it to out/entry.png
```

No network is used anywhere. `draw.py` needs Pillow and the
Liberation fonts bundled with most Linux systems.
