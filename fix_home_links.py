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

    if '../index.html' not in html:
        # Search for flex items-center gap-2 inside no-print
        # and insert the home icon
        m = re.search(r'(<div[^>]*class="[^"]*no-print[^"]*"[^>]*>.*?<div class="flex items-center gap-2">)', html, re.DOTALL)
        if m:
            target = m.group(1)
            replacement = target + '\n      <a href="../index.html" class="text-2xl hover:scale-110 transition p-1 bg-amber-100 rounded-lg border border-amber-300" title="Kütüphaneye Dön">🏠</a>'
            html = html.replace(target, replacement, 1)
        else:
            # Fallback: add right after body tag or in first flex container
            html = re.sub(
                r'(<body[^>]*>.*?<div class="[^"]*flex[^"]*items-center[^"]*gap-2[^"]*">)',
                r'\1\n      <a href="../index.html" class="text-2xl hover:scale-110 transition p-1 bg-amber-100 rounded-lg border border-amber-300" title="Kütüphaneye Dön">🏠</a>',
                html,
                count=1,
                flags=re.DOTALL
            )

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)

print("Home link verification complete.")
