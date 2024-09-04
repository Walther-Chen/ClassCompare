import json
import os

#chdir to the parent directory of the script
parent_dir=os.path.dirname(os.path.dirname(__file__))

# Construct the path to the classlist.json file
json_file_path = os.path.join(parent_dir, 'classlist.json')

# Read the JSON file
with open(json_file_path, 'r', encoding="utf-8") as json_file:
    class_list = json.load(json_file)

# Output the content of the classlist.json file
print(class_list)
