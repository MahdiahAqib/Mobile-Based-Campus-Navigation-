import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET

# Folder containing XML files
xml_folder = "annotations/"

# List to store data
data = []

# Loop through all XML files
for xml_file in glob.glob(os.path.join(xml_folder, "*.xml")):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    filename = root.find("filename").text
    width = int(root.find("size/width").text)
    height = int(root.find("size/height").text)

    for obj in root.findall("object"):
        label = obj.find("name").text
        xmin = int(obj.find("bndbox/xmin").text)
        ymin = int(obj.find("bndbox/ymin").text)
        xmax = int(obj.find("bndbox/xmax").text)
        ymax = int(obj.find("bndbox/ymax").text)

        data.append([filename, label, xmin, ymin, xmax, ymax, width, height])

# Convert to DataFrame
df = pd.DataFrame(data, columns=["filename", "label", "xmin", "ymin", "xmax", "ymax", "width", "height"])

# Save to CSV
df.to_csv("annotations/annotations.csv", index=False)

print("Annotations saved as annotations.csv!")
