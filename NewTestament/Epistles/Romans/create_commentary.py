import os

def create_files_in_current_directory(num_files):
    script_directory = os.path.dirname(os.path.abspath(__file__))

    with open(r"D:\WritingProject\\minininja0412.github.io\\NewTestament\\Epistles\\Romans\\content.txt", 'r') as content_file:
        content = content_file.read()

    for i in range(1, num_files + 1):
        file_name = os.path.join(script_directory, f'Commentary1-{i}.html')
        with open(file_name, 'w') as file:
            file.write(content)
        print(f'Created {file_name}.')

if __name__ == "__main__":
    num_files_to_create = 7  # Change this to the desired number of files
    create_files_in_current_directory(num_files_to_create)