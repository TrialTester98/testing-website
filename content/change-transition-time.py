import os

folder_path = 'theme'

def update_transition(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if line.startswith('transition: 3s'):
            lines[i] = 'transition: 1s\n'

    with open(file_path, 'w') as file:
        file.writelines(lines)

def main():
    for filename in os.listdir(folder_path):
        if filename.endswith('.md'):
            file_path = os.path.join(folder_path, filename)
            update_transition(file_path)

if __name__ == "__main__":
    main()
