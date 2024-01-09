import os

# Get the path to the directory containing the script
script_directory = os.path.dirname(__file__)

# Construct the path to the "thubmail" folder
folder_path = os.path.join(script_directory, "thumbnail")

# List all files in the "thubmail" folder
files = os.listdir(folder_path)

# Loop through each file and rename if needed
for file_name in files:
    original_path = os.path.join(folder_path, file_name)
    
    # Check if the file is a .webp file
    if file_name.lower().endswith(".webp"):
        # Rename the file with lowercase letters
        new_name = file_name.lower()
        new_path = os.path.join(folder_path, new_name)
        
        # Perform the rename operation
        os.rename(original_path, new_path)
