import os
import json

# ✅ Set this to your root folder path
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# ✅ Optional base URL if you plan to host the files on a web server
BASE_URL = "/core/docs/About_links_pdfs"

pdf_map = {
    "FHWA_SSA_Flyer": {},
    "FHWA_SSA_Hierarchy": {},
    "NCHRP_500_Series": {}
}

# Function to process a folder and gather PDF information
def process_folder(base_folder, category):
    folder_data = {}
    folder_path = os.path.join(ROOT_DIR, base_folder)
    
    if not os.path.exists(folder_path):
        return folder_data
        
    for dirpath, dirnames, filenames in os.walk(folder_path):
        # Get the relative subfolder path from the base folder
        rel_folder = os.path.relpath(dirpath, folder_path)
        if rel_folder == '.':
            current_key = 'root'
        else:
            current_key = rel_folder.replace(os.sep, '/')
        
        # Initialize the current folder in our data structure
        if current_key not in folder_data:
            folder_data[current_key] = []
            
        # Process PDF files in the current directory
        for f in filenames:
            if f.lower().endswith('.pdf'):
                full_path = os.path.join(dirpath, f)
                rel_path = os.path.relpath(full_path, ROOT_DIR)
                web_path = f"{BASE_URL}/{rel_path.replace(os.sep, '/')}"
                folder_data[current_key].append({
                    'filename': f,
                    'path': web_path
                })
    
    return folder_data

# Process each main folder
pdf_map['FHWA_SSA_Flyer'] = process_folder('FHWA_SSA_Flyer', 'FHWA_SSA_Flyer')
pdf_map['FHWA_SSA_Hierarchy'] = process_folder('FHWA_SSA_Hierarchy', 'FHWA_SSA_Hierarchy')
pdf_map['NCHRP_500_Series'] = process_folder('NCHRP 500 Series', 'NCHRP_500_Series')

# Remove empty folders from the mapping
for category in pdf_map:
    pdf_map[category] = {k: v for k, v in pdf_map[category].items() if v}

# Save mapping to a JSON file
output_file = os.path.join(ROOT_DIR, "pdf_manifest.json")
with open(output_file, "w", encoding="utf-8") as out:
    json.dump(pdf_map, out, indent=2, ensure_ascii=False)

print(f"✅ PDF manifest created: {output_file}")
print("\nSummary of PDFs found:")
for category in pdf_map:
    pdf_count = sum(len(pdfs) for pdfs in pdf_map[category].values())
    print(f"{category}: {pdf_count} PDFs")
