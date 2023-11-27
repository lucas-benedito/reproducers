import json
import os
import glob

# Read the path where the json reside
artifact_discovery = input("Path for the artifacts: ")
path_to_search = os.path.abspath(artifact_discovery)
# search all json files
search_dir = os.path.join(path_to_search, "*.json")

json_files = glob.glob(search_dir, recursive=False)

if json_files:
    # Create an empty list to store the Python objects.
    python_objects = []

    # Load each JSON file into a Python object.
    for json_file in json_files:
        with open(json_file, "r") as f:
            python_objects.append(json.load(f))

    lines = sorted(python_objects, key=lambda k: k['created'], reverse=False)

    # Dump all the Python objects into a single JSON file.
    with open("/tmp/combined.json", "w") as f:
        json.dump(lines, f, indent=4)

    print("Files combined into /tmp/combined.json")
else:
    print("No JSON files found to process.")