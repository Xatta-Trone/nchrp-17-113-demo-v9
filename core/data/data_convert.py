import csv
import json
import os
from datetime import datetime
from pathlib import Path
# -------------------------------
# 1️⃣ Step 1: Convert CSV → JSON
# -------------------------------

# Input and output file paths
csv_file = "Factsheet_Spreadsheet_V08a_Mi_Tools_v01.csv"
intermediate_json = "output.json"
final_json = "data.json"

# Read CSV and convert to JSON
data = []
with open(csv_file, mode="r", encoding="latin1") as f:
    reader = csv.DictReader(f)
    for row in reader:
        data.append(row)

# Write initial JSON
with open(intermediate_json, mode="w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print(f"✅ CSV converted to JSON: {intermediate_json}")

# -------------------------------
# 2️⃣ Step 2: Add image paths
# -------------------------------

# Define the path: go up one folder, then into images/countermeasures
images_folder = os.path.join('..', 'images', 'countermeasures')

# Convert to absolute path
images_folder = os.path.abspath(images_folder)

# Check if the folder exists
if not os.path.isdir(images_folder):
    raise FileNotFoundError(f"❌ Image folder not found: {images_folder}")

# List all image files inside countermeasures folder
image_files = os.listdir(images_folder)

# -------------------------------
# 3️⃣ Step 3: Update JSON items
# -------------------------------

for idx, item in enumerate(data):
    # Add an 'id' field (1-based index)
    item["id"] = idx + 1

    # Get CountermeasureID to match image files
    countermeasure_id = item.get("CountermeasureID")
    if countermeasure_id:
        matching_image = next(
            (img for img in image_files if img.startswith(countermeasure_id)),
            None
        )
        if matching_image:
            item["img"] = matching_image

# -------------------------------
# 4️⃣ Step 4: Save Final JSON
# -------------------------------

with open(final_json, 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

print(f"✅ Final updated JSON saved to: {final_json}")

final_js = Path("data.js")

# 5) Write JS (window.CM_DATA = ...)
body = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</script>", "<\\/script>")
js_content = (
    "/* Auto-generated on " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
    f" * Source: {csv_file}\n"
    " */\n"
    "window.CM_DATA = " + body + ";\n"
)
final_js.write_text(js_content, encoding="utf-8")
print(f"✅ Wrote JS: {final_js.resolve()}")