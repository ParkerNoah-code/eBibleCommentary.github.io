import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
import time

def get_content(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        book_text_div = soup.find_all('div', class_='et_pb_text_inner')
        if book_text_div:
            content = str(book_text_div)
            
            return content
        else:
            print(f"Error: No <div class=\"bookText\"> element found in URL {url}")
            return ['','']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
    
def create_table_of_contents(file_name, author, title, titles):
    content = ''
    filename = os.path.dirname(os.path.abspath(__file__)) + f'/' + file_name +'.html'
    with open(filename, 'w', encoding='utf-8') as file:
        content += f'<!DOCTYPE html> <html> <head> <meta name="viewport" content="width=device-width, initial-scale=1.0" /> <link rel="stylesheet" type="text/css" href="../../../style.css" /> <script rel="script" type="text/javascript" src="../../../functions.js"></script> </head> <body> <div class="container"> <header> <h1>AUTHOR_NAME</h1> </header> <ul> <li> <a href="../../../index.html">About</a> | <a href="../../../Theology.html"> Theology</a> | <a href="../../../OTIntro.html"> Old Testament</a> | <a href="../../../NTIntro.html"> New Testament</a> </li> </ul> <section> <p><a href="../theologians.html">AUTHOR_NAME</a>: </p> <p> <b>TITLE_OF_BOOK</b> </p> </section> <section> <p>TABLE_OF_CONTENTS</p> </section> <footer> <p>&copy; 2023 ebiblecommentary. All rights reserved.</p> </footer> </div> </body> </html>'
        for i in range(0, len(titles)):
            content = content.replace('TABLE_OF_CONTENTS', '<a href="' + file_name + '-' + str(i) + '.html">' + titles[i] + '</a><br> TABLE_OF_CONTENTS')
        content = content.replace('AUTHOR_NAME', author)
        content = content.replace('TITLE_OF_BOOK', title)
        content = content.replace('FILE_NAME', file_name)
        content = content. replace('<br> TABLE_OF_CONTENTS', '')
        file.write(content)

def create_files(file_name, author, title, titles, urls):
    for u in range(0,len(titles)):
        filename = os.path.dirname(os.path.abspath(__file__)) + f'/' + file_name + f'-'+str(u)+'.html'
        content = ''
        with open(filename, 'w', encoding='utf-8') as file:
            content += f'<!DOCTYPE html> <html> <head> <meta name="viewport" content="width=device-width, initial-scale=1.0" /> <link rel="stylesheet" type="text/css" href="../../../style.css" /   > <script rel="script" type="text/javascript" src="../../../functions.js"></script> </head> <body> <div class="container"> <header> <h1>AUTHOR_NAME</h1> </header> <ul> <li> <a   href="../../../index.html">About</a> | <a href="../../../Theology.html"> Theology</a> | <a href="../../../OTIntro.html"> Old Testament</a> | <a href="../../../NTIntro.html">    New Testament</a> </li> </ul> <section> <p> <a href="FILE_NAME.html"><span>TITLE_OF_BOOK</span></a> </p> </section> <section> <p> '
            content += get_content(urls[u])
            content += f'</section> <footer> <p>&copy;    2023 ebiblecommentary. All rights reserved.</p> </footer> </div> </body> </html>'
            content = content.replace('AUTHOR_NAME', author)
            content = content.replace('TITLE_OF_BOOK', title)
            content = content.replace('FILE_NAME', file_name)
            content = content.replace(' align="JUSTIFY"', '')
            content = content.replace('<blockquote>', '')
            content = content.replace('</blockquote>', '')
            file.write(content)
        
    print("Task completed successfully.")

author = 'Jonathan Edwards'
title = 'The Idol of Free-Will'
file_name = 'idol-of-free-will'
titles = ['The Idol of Free-Will']
urls = ['https://www.apuritansmind.com/puritan-favorites/john-owen/the-idol-of-free-will/']

create_files(file_name, author, title, titles, urls)
#create_table_of_contents(file_name, author, title, titles)