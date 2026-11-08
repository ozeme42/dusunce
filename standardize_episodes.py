import os
import re

EPISODES_DIR = r"C:\Users\mahmut\.gemini\antigravity\scratch\dusunce-ve-hayat-rehberi\episodes"

for i in range(1, 32):
    filename = f"bolum{i:02d}.html"
    filepath = os.path.join(EPISODES_DIR, filename)
    if not os.path.exists(filepath):
        continue

    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    # Ensure worksheet.css link is included
    if "worksheet.css" not in html:
        html = html.replace("</head>", '  <link rel="stylesheet" href="../assets/css/worksheet.css">\n</head>')

    # Ensure gstatic tailwind is used
    html = html.replace("https://cdn.tailwindcss.com", "https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js")

    # Ensure home button is in header if not already present
    if '../index.html' not in html:
        # Match <header class="no-print... <div class="flex items-center gap-2">
        # and insert the home icon
        html = re.sub(
            r'(<header[^>]*>.*?<div class="flex items-center gap-2">)',
            r'\1\n      <a href="../index.html" class="text-2xl hover:scale-110 transition p-1 bg-amber-100 rounded-lg border border-amber-300" title="Kütüphaneye Dön">🏠</a>',
            html,
            count=1,
            flags=re.DOTALL
        )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("All 31 episodes standardized with worksheet.css and home navigation.")
