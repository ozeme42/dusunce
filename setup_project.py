import os
import shutil
import re
import json

SOURCE_DIR = r"C:\Users\mahmut\.gemini\antigravity\brain\85280c2a-ce7f-4049-a067-53c69ba36624"
PROJECT_DIR = r"C:\Users\mahmut\.gemini\antigravity\scratch\dusunce-ve-hayat-rehberi"
EPISODES_DIR = os.path.join(PROJECT_DIR, "episodes")
DATA_DIR = os.path.join(PROJECT_DIR, "data")

print("Copying and indexing episodes 1-31...")

episodes_meta = []

for i in range(1, 32):
    # Determine source file name
    src_variants = [
        os.path.join(SOURCE_DIR, f"dusunce_ve_hayat_bolum{i}.html"),
        os.path.join(SOURCE_DIR, f"dusunce_ve_hayat_bolum{i:02d}.html")
    ]
    src_path = None
    for p in src_variants:
        if os.path.exists(p):
            src_path = p
            break
            
    if not src_path:
        print(f"Warning: Episode {i} not found!")
        continue

    dest_file = f"bolum{i:02d}.html"
    dest_path = os.path.join(EPISODES_DIR, dest_file)
    
    with open(src_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract title
    title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
    title = title_match.group(1).strip() if title_match else f"Düşünce ve Hayat {i}. Bölüm"

    # Extract subtitle or main heading if available
    h2_match = re.search(r'<h2[^>]*>(.*?)</h2>', content, re.IGNORECASE)
    h2 = h2_match.group(1).strip() if h2_match else ""

    p_match = re.search(r'<p[^>]*class="[^"]*text-amber-800[^"]*"[^>]*>(.*?)</p>', content, re.IGNORECASE)
    sub = p_match.group(1).strip() if p_match else ""

    episodes_meta.append({
        "id": i,
        "filename": dest_file,
        "title": title,
        "heading": re.sub('<[^<]+?>', '', h2),
        "subtitle": re.sub('<[^<]+?>', '', sub),
    })

    # Ensure tailwind script uses the guaranteed gstatic url or fallback
    # If it has cdn.tailwindcss.com, replace or ensure gstatic is present
    content = content.replace("https://cdn.tailwindcss.com", "https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js")
    
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Copied {len(episodes_meta)} episodes.")

with open(os.path.join(DATA_DIR, "episodes_index.json"), "w", encoding="utf-8") as f:
    json.dump(episodes_meta, f, ensure_ascii=False, indent=2)

print("Indexing complete.")
