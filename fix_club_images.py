import os

path = r"d:\Projects\olive oil\Oil of the Month Club.html"

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (
        ".vip-hero-img { flex: 1; min-height: 400px; background: url('images/club_hero.png') center/cover; position: relative; }\n    .vip-hero-img::after { content: ''; position: absolute; top:0; left:0; width:100%; height:100%; background: linear-gradient(to right, transparent, var(--bg-main)); }",
        ".vip-hero-img { flex: 1; min-height: 400px; position: relative; display: flex; overflow: hidden; }\n    .vip-hero-img img { width: 100%; height: 100%; object-fit: cover; position: absolute; inset: 0; z-index: 0; }\n    .vip-hero-img::after { content: ''; position: absolute; top:0; left:0; width:100%; height:100%; background: linear-gradient(to right, transparent, var(--bg-main)); z-index: 1; }"
    ),
    (
        ".selection-img { height: 250px; background-size: cover; background-position: center; position: relative; }\n    .selection-month { position: absolute; top: 20px; right: 20px; background: rgba(255,255,255,0.9); color: #2c2418; padding: 0.5rem 1.5rem; border-radius: 50px; font-weight: bold; text-transform: uppercase; letter-spacing: 1px; font-size: 0.85rem; }",
        ".selection-img { height: 250px; position: relative; overflow: hidden; display: flex; }\n    .selection-img img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.8s ease; }\n    .selection-card:hover .selection-img img { transform: scale(1.05); }\n    .selection-month { position: absolute; top: 20px; right: 20px; background: rgba(255,255,255,0.9); color: #2c2418; padding: 0.5rem 1.5rem; border-radius: 50px; font-weight: bold; text-transform: uppercase; letter-spacing: 1px; font-size: 0.85rem; z-index: 2; }"
    ),
    (
        "/* 6. The Reserve Collection (Showcase) */\n    .vip-reserve { position: relative; padding: 10rem 2rem; text-align: center; background: url('images/club_reserve.png') center/cover; background-attachment: fixed; color: #ffffff; }\n    .vip-reserve::before { content: ''; position: absolute; top:0; left:0; width:100%; height:100%; background: rgba(26,22,18,0.8); }\n    .reserve-content { position: relative; z-index: 1; max-width: 800px; margin: 0 auto; }",
        "/* 6. The Reserve Collection (Showcase) */\n    .vip-reserve { position: relative; padding: 10rem 2rem; text-align: center; color: #ffffff; overflow: hidden; }\n    .reserve-bg { position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; z-index: 0; }\n    .vip-reserve::before { content: ''; position: absolute; top:0; left:0; width:100%; height:100%; background: rgba(26,22,18,0.8); z-index: 1; }\n    .reserve-content { position: relative; z-index: 2; max-width: 800px; margin: 0 auto; }"
    ),
    (
        "<section class=\"vip-hero\">\n    <div class=\"vip-hero-img reveal-on-scroll\"></div>",
        "<section class=\"vip-hero\">\n    <div class=\"vip-hero-img reveal-on-scroll\">\n      <img src=\"images/tasting_experience.png\" alt=\"Exclusive Tasting Experience\">\n    </div>"
    ),
    (
        "<div class=\"selection-card\">\n        <div class=\"selection-img\" style=\"background-image: url('images/club_month1.png');\">\n          <div class=\"selection-month\">October</div>\n        </div>",
        "<div class=\"selection-card\">\n        <div class=\"selection-img\">\n          <img src=\"images/robust_peppery.png\" alt=\"October Selection\">\n          <div class=\"selection-month\">October</div>\n        </div>"
    ),
    (
        "<div class=\"selection-card\">\n        <div class=\"selection-img\" style=\"background-image: url('images/club_month2.png');\">\n          <div class=\"selection-month\">November</div>\n        </div>",
        "<div class=\"selection-card\">\n        <div class=\"selection-img\">\n          <img src=\"images/bundle_truffle.png\" alt=\"November Selection\">\n          <div class=\"selection-month\">November</div>\n        </div>"
    ),
    (
        "<div class=\"selection-card\">\n        <div class=\"selection-img\" style=\"background-image: url('images/club_month3.png');\">\n          <div class=\"selection-month\">December</div>\n        </div>",
        "<div class=\"selection-card\">\n        <div class=\"selection-img\">\n          <img src=\"images/bal_traditional.png\" alt=\"December Selection\">\n          <div class=\"selection-month\">December</div>\n        </div>"
    ),
    (
        "<!-- 6. The Reserve Collection -->\n  <section class=\"vip-reserve reveal-on-scroll\">\n    <div class=\"reserve-content\">",
        "<!-- 6. The Reserve Collection -->\n  <section class=\"vip-reserve reveal-on-scroll\">\n    <img class=\"reserve-bg\" src=\"images/premium_reserve.png\" alt=\"Reserve Collection\">\n    <div class=\"reserve-content\">"
    )
]

new_content = content
for old, new in replacements:
    if old in new_content:
        new_content = new_content.replace(old, new)
    else:
        print(f"COULD NOT FIND:\n{old}\n")

with open(path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done updating Oil of the Month Club.html")
