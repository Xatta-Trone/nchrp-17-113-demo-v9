import pandas as pd
import json
import numpy as np

# Load the Excel file
excel_path = "list09.xlsx"
df = pd.read_excel(excel_path)

# Define the mapping between DataFrame columns and desired JSON keys
column_mapping = {
    "id": "id",
    "Emphasis Area": "Emphasis Area",
    "Target Crash": "Target Crash Type",
    "Area Type": "Land Use Type",
    "CountermeasureID": "CountermeasureID",
    "Countermeasure": "Countermeasure",
    "Countermeasure Staus": "Countermeasure Type",
    "CMF": "CMF",
    "Crash Severity": "Crash Severity",
    "Road Type": "Road Type",
    "Star Quality": "Star Quality",
    "Min AADT": "Min AADT",
    "Max AADT": "Max AADT",
    "Min Num Lanes": "Min Num Lanes",
    "Max Num Lane": "Max Num Lane",
    "Cost": "Cost",
    "Service Life": "Service Life",
    "Implementation Time": "Implementation Time",
    "Contributing Factors": "Contributing Factors",
    "SSA Pillars": "SSA Element",
    "SSA Hierarchy": "SSA Hierarchy",
    "AASHTO": "AASHTO",
    "Countermeasure Link": "Countermeasure Link",
    "Knowledge Base": "Knowledge Base",
    "Countermeasure Factsheet": "Countermeasure Factsheet",
    "Other Countermeasures": "Other Countermeasures",
    "NCHRP 500 Series Objective": "NCHRP 500 Series Objective",
    # "CountermeasureID": "img"
}

# Helper function to handle NaN values
def clean_value(value):
    if pd.isna(value):
        return ""  # or return "" if you prefer empty strings
    if isinstance(value, np.integer):
        return int(value)
    if isinstance(value, np.floating):
        return float(value)
    return value

# Apply the mapping with NaN handling
json_list = []
for _, row in df.iterrows():
    entry = {}
    for old_key, new_key in column_mapping.items():
        value = row.get(old_key)
        # Special handling for "img"
        if new_key == "img":
            value = f"{value}.PNG" if not pd.isna(value) else None
        else:
            value = clean_value(value)
        entry[new_key] = value
    json_list.append(entry)

# Save the JSON list to a file
json_path = "data-v9-updated-april-2025.json"
with open(json_path, "w") as f:
    json.dump(json_list, f, indent=4)

print(f"JSON file saved to: {json_path}")
