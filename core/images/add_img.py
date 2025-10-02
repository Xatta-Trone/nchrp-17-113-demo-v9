import json
import os

# Load JSON data
with open('data.json', 'r') as file:
    data = json.load(file)

# Define the path to the images folder
images_folder = 'countermeasures'  # Replace with your actual image folder path

# Get all image files in the images folder
image_files = os.listdir(images_folder)

# Loop through each item and update 'id' and 'img' if applicable
for idx, item in enumerate(data):
    # Set ID as index + 1
    item["id"] = idx + 1

    countermeasure_id = item.get("CountermeasureID")
    # Match image file that starts with CountermeasureID
    matching_image = next(
        (img for img in image_files if img.startswith(countermeasure_id)),
        None
    )
    # Add image if found
    if matching_image:
        item["img"] = matching_image

# Save the updated JSON data
with open('data-updated.json', 'w') as file:
    json.dump(data, file, indent=4)

print("Updated data saved to 'data-updated.json'")
