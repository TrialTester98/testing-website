import os
import random
import re

folder_path = 'theme copy'  # Replace with the actual path to your 'theme copy' folder

def update_score(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Extract the current score
    score_match = re.search(r'score: (\d+(\.\d+)?)', content)
    if score_match:
        current_score = float(score_match.group(1))

        # Check if the score is 86 or below
        if current_score <= 86:
            # Set it to a random number between 30 and 50
            new_score = round(random.uniform(30, 50), 1)

            # Update the content with the new score
            updated_content = re.sub(r'score: (\d+(\.\d+)?)', f'score: {new_score}', content)

            # Write the updated content back to the file
            with open(file_path, 'w') as updated_file:
                updated_file.write(updated_content)

# Iterate through each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.md'):
        file_path = os.path.join(folder_path, filename)
        update_score(file_path)
