import os
import random
import numpy as np

# Function to parse markdown files
def parse_markdown(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

# Function to update score in markdown file
def update_score(file_path, new_score):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if line.startswith("score:"):
            lines[i] = f"score: {new_score}\n"
            break

    with open(file_path, 'w') as file:
        file.writelines(lines)

# Get list of markdown files in the 'theme copy' folder
folder_path = 'theme'
markdown_files = [file for file in os.listdir(folder_path) if file.endswith('.md')]

# Initialize lists
dark_list = []
light_list = []

# Populate dark and light lists based on mode and score
for file_name in markdown_files:
    file_path = os.path.join(folder_path, file_name)
    content = parse_markdown(file_path)
    score = float(content.split("score:")[1].split()[0])
    mode = content.split("mode:")[1].split()[0].strip()

    if score < 80.5:
        if mode == 'dark':
            dark_list.append(file_name)
        elif mode == 'light':
            light_list.append(file_name)


# Function to sort the file lists based on the number of archetypes and specified order
def sort_file_list(file_list):
    return sorted(file_list, key=lambda file_name: (len(parse_markdown(os.path.join(folder_path, file_name)).split("archetype:")[1].splitlines()[0].strip().split('|')), file_name))

# Sort dark and light lists
dark_list = sort_file_list(dark_list)
light_list = sort_file_list(light_list)

# Function to sort single archetype files based on specified order
def sort_single_archetype(file_list):
    order = {'Innovative': 0, 'Little Bit of Everything': 1, 'Github Actions': 2,  'Game': 3, 'Stats and Metrics': 4, 'Minimalistic': 5}

    return sorted(file_list, key=lambda file_name: order.get(parse_markdown(os.path.join(folder_path, file_name)).split("archetype:")[1].splitlines()[0].strip().split('|')[0].strip(), 5))

# Sort dark and light lists with single archetype
dark_list = sort_single_archetype(dark_list)
light_list = sort_single_archetype(light_list)
prev_light = None
prev_arr = []
prev_index = 0

def update_scores(dark_file_list, light_file_list, starting_score, choose_light, use_prev):
    global prev_index;
    global prev_light;
    chosen_dark_files = []
    for i in range(3 - choose_light):
        dark_weights = np.arange(len(dark_file_list), 0, -1)
        random_file = random.choices(dark_file_list, weights= dark_weights, k= 1)[0]
        chosen_dark_files.append(random_file)
        dark_file_list.remove(random_file)

    light_weights = np.arange(len(light_file_list), 0, -1)
    chosen_light_files = random.choices(light_file_list, weights= light_weights, k = choose_light)
    print(chosen_dark_files)
    print(chosen_light_files)
    chosen_files = chosen_light_files + chosen_dark_files
    scores = [starting_score, starting_score - 0.1, starting_score - 0.2]
    scores = [round(element, 1) for element in scores]
    print(scores)
    
    for file_name in chosen_files:
        file_path = os.path.join(folder_path, file_name)
        file_score = round(random.choice(scores), 1)
        if file_name in light_file_list:
            if use_prev:
                prev_index = scores.index(file_score) + 1
                print(prev_index)
            else:
                if prev_index == 1:
                    file_score = round(random.choice([prev_light-0.4, prev_light-0.5]), 1)
                elif prev_index == 2:
                    file_score = round(random.choice([prev_light-0.2, prev_light-0.4]), 1)
                else:
                    file_score = round(random.choice([prev_light-0.1, prev_light-0.2]), 1)
            
            print(file_score)
            prev_light = file_score
        
        # prev_light = file_score
        update_score(file_path, file_score)
        scores.remove(file_score)
        if file_name in light_file_list:
            light_file_list.remove(file_name)
            

    return dark_file_list, light_file_list, starting_score-0.3


# Update scores following the specified pattern
start_score = 80
while len(dark_list) >= 3:
    dark_list, light_list, start_score = update_scores(dark_list, light_list, start_score, 1, True)

    if len(dark_list) >= 3:
        dark_list, light_list, start_score = update_scores(dark_list, light_list, start_score, 1, False)
    else:
        break
    if len(dark_list) >= 3:

        dark_list, light_list, start_score = update_scores(dark_list, light_list, start_score, 0, True)
    else:
        break

# Print remaining elements in the lists
print("Remaining files in dark_list:", dark_list)
print("Remaining files in light_list:", light_list)
