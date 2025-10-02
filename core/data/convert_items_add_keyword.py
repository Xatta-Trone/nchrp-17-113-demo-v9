import json
import random

# Load both JSON files
with open('nchrp-17-113-countermeasure-v10-july-2025.json', 'r') as f:
    countermeasures = json.load(f)

with open('items_v2.json', 'r') as f:
    items = json.load(f)

# Step 1: Extract all unique keywords
all_keywords = set()
for cm in countermeasures:
    keyword_field = cm.get("Keyword_OnlyForTool", "")
    if keyword_field:
        keywords = [kw.strip() for kw in keyword_field.split(';') if kw.strip()]
        all_keywords.update(keywords)

all_keywords = list(all_keywords)

# Step 2: Assign random keywords to each item
def get_random_keywords(keyword_list, min_k=8, max_k=10):
    count = random.randint(min_k, max_k)
    return random.sample(keyword_list, min(count, len(keyword_list)))

for item in items:
    item["keywords"] = get_random_keywords(all_keywords)

# Step 3: Save updated items
with open('items_v2_with_keywords.json', 'w') as f:
    json.dump(items, f, indent=2)

print("✅ 'items_v2_with_keywords.json' created with randomly assigned keywords.")
