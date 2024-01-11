import os
import re
import random

def assign_score(content):
    if "Editor's Choice" in content or "Cute" in content or "Dynamic" in content:
        return random.uniform(9, 95)
    elif "Minimalistic" in content:
        return random.uniform(65, 70)
    elif "Innovative" in content or "Anime" in content or "Game" in content or "Github Actions" in content:
        return random.uniform(84, 90)
    elif "Stats and Metrics" in content or "animation" in content:
        return random.uniform(80, 86)
    elif "GIF" in content:
        return random.uniform(77, 83)
    else:
        return random.uniform(70, 80)

def process_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if re.match(r'\s*score:', line):
            return  # Score already present, do nothing

        if "archetype:" in line:
            archetype_index = i
            break

    archetype_content = ' '.join(lines[archetype_index + 1:])

    score = assign_score(archetype_content)

    lines.insert(archetype_index, f'score: {score:.1f}\n')

    with open(file_path, 'w') as file:
        file.writelines(lines)

def process_files_in_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                process_file(file_path)

# Replace 'path/to/theme/copy' with the actual path to your 'theme copy' folder
folder_path = 'theme'
process_files_in_folder(folder_path)
