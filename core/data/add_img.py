import json
import os

# Load JSON data
with open('data-v8.json', 'r') as file:
    data = json.load(file)

# Define the path to the images folder
# Replace with the actual path to your images folder
images_folder = 'countermeasures'

# Get all image files in the images folder
image_files = os.listdir(images_folder)

# Loop through each item in the JSON data
for item in data:
    countermeasure_id = item.get("CountermeasureID")
    # Find the matching image file by CountermeasureID (regardless of extension)
    matching_image = next(
        (img for img in image_files if img.startswith(countermeasure_id)),
        None
    )
    # Add img key if a matching image is found
    if matching_image:
        item["img"] = matching_image

# Save the updated JSON data
with open('data-v8-updated.json', 'w') as file:
    json.dump(data, file, indent=4)

print("Updated data saved to 'data-v8-updated.json'")
