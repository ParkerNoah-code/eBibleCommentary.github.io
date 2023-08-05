import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os

def get_links_from_div_class(url, class_name):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        div_elements = soup.find_all('div', class_=class_name)

        base_url = response.url  # Get the base URL

        links = []
        for div in div_elements:
            # Find all 'a' tags within the 'div' and extract the 'href' attribute.
            for a in div.find_all('a', href=True):
                if 'class' not in a.attrs:
                    absolute_link = urljoin(base_url, a['href'])
                    links.append(absolute_link)

        return links
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return []
    
def get_titles(url, class_name):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        div_elements = soup.find_all('div', class_=class_name)

        base_url = response.url  # Get the base URL

        titles = []
        for div in div_elements:
            # Find all 'a' tags within the 'div' and extract the 'href' attribute.
            for a in div.find_all('a', href=True):
                if 'class' not in a.attrs:
                    absolute_link = urljoin(base_url, a['href'])
                    titles.append(a.get_text())

        return titles
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return []

# Replace 'your_url_here' with the actual URL you want to parse.
def write_content_to_file(url, content, index, total):
    filename = os.path.dirname(os.path.abspath(__file__)) + f'/' + file_name + f'-{index}.html'
    with open(filename, 'w', encoding='utf-8') as file:
        content = content.replace("</p>", "")
        content = content.replace("<p>", "</p><p>")
        content = content.replace('<div class="bookText">', '<!DOCTYPE html> <html> <head> <meta name="viewport" content="width=device-width, initial-scale=1.0" /> <link rel="stylesheet" type="text/css" href="../../../style.css" /> <script rel="script" type="text/javascript" src="../../../functions.js"></script> </head> <body> <div class="container"> <header> <h1>AUTHOR_NAME</h1> </header> REPLACEME')
        content = content.replace('REPLACEME','<ul> <li> <a href="../../../index.html">About</a> ??? <a href="../../../Theology.html"> Theology</a> ??? <a href="../../../OTIntro.html"> Old Testament</a> ??? <a href="../../../NTIntro.html"> New Testament</a> </li> </ul> <section> <p> <a href="FILE_NAME.html"><span>TITLE_OF_BOOK</span></a> </p> </section> <section> <p>')
        content = content.replace('</div>', '</p> </section> <footer> <p>&copy; 2023 ebiblecommentary. All rights reserved.</p> </footer> </div> </body> </html>')
        content = content.replace('AUTHOR_NAME', author)
        content = content.replace('TITLE_OF_BOOK', title)
        content = content.replace('FILE_NAME', file_name)
        content = content.replace('|', '"')
        content = content.replace('???', '|')
        file.write(content)
        total += 1
    return total

    print(f"Successfully saved content from URL {url} to file {filename}")
total = 0
url = 'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/'
file_name = 'sermon'
author = 'Jonathan Edwards'
title = 'Sermons'
class_name = 'et_pb_text_inner'
links = get_links_from_div_class(url, class_name)
list_title = get_titles(url, class_name)

print(links)

# Loop through each URL and process the content
t = 0
for i, url in enumerate(links):
    try:
        # Fetch the content of the URL
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors

        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the div element with class="bookText"
        book_text_div = soup.find('div', class_='bookText')

        if book_text_div:
            # Get the contents of the div as a string
            content = str(book_text_div)

            # Write the contents to the HTML file
            
            t = write_content_to_file(url, content, i, t)
        else:
            print(f"Error: No <div class=\"bookText\"> element found in URL {url}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL {url}: {e}")

filename = os.path.dirname(os.path.abspath(__file__)) + f'/' + file_name + f'.html'
with open(filename, 'w', encoding='utf-8') as file:
    contents = ''
    contents += f'<!DOCTYPE html> <html> <head> <meta name="viewport" content="width=device-width, initial-scale=1.0" /> <link rel="stylesheet" type="text/css" href="../../../style.css" /> <script rel="script" type="text/javascript" src="../../../functions.js"></script> </head> <body> <div class="container"> <header> <h1>AUTHOR_NAME</h1> </header> '
    contents += f'<ul> <li> <a href="../../../index.html">About</a> ??? <a href="../../../Theology.html"> Theology</a> ??? <a href="../../../OTIntro.html"> Old Testament</a> ??? <a href="../../../NTIntro.html"> New Testament</a> </li> </ul> <section> <p> <a href="FILE_NAME.html"><span>TITLE_OF_BOOK</span></a> </p> </section> <section> <p> TABLE_OF_CONTENTS '
    contents += f'</p> </section> <footer> <p>&copy; 2023 ebiblecommentary. All rights reserved.</p> </footer> </div> </body> </html>'
    contents = contents.replace('AUTHOR_NAME', author)
    contents = contents.replace('TITLE_OF_BOOK', title)
    contents = contents.replace('FILE_NAME', file_name)
    for i in range(1, t):
        contents = contents.replace('TABLE_OF_CONTENTS', '<a href="' + file_name + '-' + str(i) + '.html">' + list_title[i] + '</a><br> TABLE_OF_CONTENTS')
    contents = contents.replace('<br> TABLE_OF_CONTENTS', '')
    contents = contents.replace('|', '"')
    contents = contents.replace('???', '|')
    file.write(contents)
    print(t)

print("Task completed successfully.")