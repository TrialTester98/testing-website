category_file_path = 'category.txt'

with open(category_file_path, 'r') as infile:
    lines = infile.readlines()

# Remove empty lines
non_empty_lines = [line.strip() for line in lines if line.strip()]

with open(category_file_path, 'w') as outfile:
    outfile.write('\n'.join(non_empty_lines))
    
with open('category.txt', 'r') as file:
    lines = file.readlines()

# Check if the number of lines is even
if len(lines) % 2 != 0:
    print("Error: The number of lines in the file is not even.")
else:
    # Swap line pairs
    swapped_lines = [lines[i + 1].strip() + '\n' + lines[i].strip() for i in range(0, len(lines), 2)]

    # Write the swapped lines back to the file
    with open('category.txt', 'w') as file:
        file.write('\n'.join(swapped_lines))

    print("Lines swapped successfully.")

import os
import re

def update_markdown(file_path, archetype):
    with open(file_path, 'r') as file:
        content = file.read()

    # Find the position of 'archetype:' in the content
    archetype_index = content.find('archetype:')

    # Insert the array elements under 'archetype'
    new_content = content[:archetype_index + len('archetype:\n')] + '\n  - ' + '\n  - '.join(archetype) + content[archetype_index + len('archetype:'):]

    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.write(new_content)

    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Remove empty lines
    non_empty_lines = [line.strip() for line in lines if line.strip()]

    with open(file_path, 'w') as file:
        file.write('\n'.join(non_empty_lines))


def remove_archetypes(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Use regular expression to remove the archetype section
    content = re.sub(r'archetype:[\s\S]+?---', 'archetype:\n---', content)

    with open(file_path, 'w') as file:
        file.write(content)

def process_category_file(category_path):
    with open(category_path, 'r') as file:
        lines = file.readlines()

    for i in range(0, len(lines), 2):
        username = lines[i].strip().split('/')[-1].lower()
        archetype = [item.strip() for item in lines[i + 1].strip().split(',')]

        
        # Check if the markdown file exists
        markdown_file_path = f'theme/{username}.md'
        print(markdown_file_path)
        remove_archetypes(markdown_file_path)
        if os.path.exists(markdown_file_path):
            update_markdown(markdown_file_path, archetype)


if __name__ == "__main__":
    category_file_path = "category.txt"
    process_category_file(category_file_path)
