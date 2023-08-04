with open("content.txt", "r") as content_file:
    content = content_file.read()

for i in range(1, 151):
    filename = f"OldTestament\PoeticWisdom\Psalms\SermonicCommentary{i}.html"
    with open(filename, "w") as file:
        file.write(content)