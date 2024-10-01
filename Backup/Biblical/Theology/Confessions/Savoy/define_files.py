import os
from bs4 import BeautifulSoup

# Path to the file that contains the HTML with div elements
input_file = 'D:\Repos\minininja0412.github.io\Biblical\Theology\Confessions\Savoy.html'  # Replace with your actual file name

# Load the content of the file
with open(input_file, 'r', encoding='utf-8') as file:
    file_content = file.read()

# Parse the file content using BeautifulSoup
soup = BeautifulSoup(file_content, 'html.parser')

# Get the directory where the Python script is located
script_directory = os.path.dirname(os.path.abspath(__file__))

# Find all div elements
div_elements = soup.find_all('div')

# Loop through each div element and create a file for it
for i, div in enumerate(div_elements, start=1):
    # Extract the id and the inner content of the div
    div_id = div.get('id', f'Div{i}')
    
    # Extract the contents of the div
    div_body = ''.join(str(content) for content in div.contents)
    
    # Remove the <section> and </section> tags but keep their content
    div_body = div_body.replace('<section>', '').replace('</section>', '')
    
    # Construct the HTML content for the file
    html_content = f"""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>eBibleCommentary</title>
    <link rel="stylesheet" href="../../../../Style.css" />
    <link rel="icon" href="cross_image.ico" />
  </head>

  <body>
    <section>
      <div class="back-button-container">
        <a href="../Savoy.html" class="back-button">Savoy</a>
      </div>
      <h1>Savoy Declaration of Faith</h1>
      {div_body}
    </section>
  </body>
</html>
"""

    # Define the filename, using the script's directory
    filename = os.path.join(script_directory, f"{i}.html")
    
    # Write the content to the file
    with open(filename, 'w', encoding='utf-8') as output_file:
        output_file.write(html_content)
    
    print(f"Created file: {filename}")
