import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os

def get_content():
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        book_text_div = soup.find(id=class_name)
        if book_text_div:
            content = str(book_text_div)
            
            return content
        else:
            print(f"Error: No <div class=\"{class_name}\"> element found in URL {url}")
            return ['','']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL {url}: {e}")

def write_content_to_file():
    filename = os.path.dirname(os.path.abspath(__file__)) + f'/' + file_name + f'.html'
    content = ''
    with open(filename, 'w', encoding='utf-8') as file:
        content += f'<!DOCTYPE html> <html> <head> <meta name="viewport" content="width=device-width, initial-scale=1.0" /> <link rel="stylesheet" type="text/css" href="../../../style.css" /   > <script rel="script" type="text/javascript" src="../../../functions.js"></script> </head> <body> <div class="container"> <header> <h1>{author}</h1> </header> <ul> <li> <a   href="../../../index.html">About</a> | <a href="../../../Theology.html"> Theology</a> | <a href="../../../OTIntro.html"> Old Testament</a> | <a href="../../../NTIntro.html">    New Testament</a> </li> </ul> <section> <p> <a href="{link_back_to}.html">{link_back_to}</a>: <b><a href="{url}" target="_blank">{title}</a></b> </p> </section> <section> <p> '
        content += get_content()
        content += f'</section> <footer> <p>&copy;    2023 ebiblecommentary. All rights reserved.</p> </footer> </div> </body> </html>'
        content = content.replace('FILE_NAME', link_back_to)
        content = content.replace(' align="JUSTIFY"', '')
        content = content.replace('<div id="txt_5" style="position:absolute;left:31px;top:287px;width:715px;height:1692px;overflow:hidden;">', '')
        content = content.replace('</div></section> <footer>', '</section> <footer>')
        content = content.replace('<p class="Normal-P-P0"><span class="Normal-C-C3"><br/></span></p>', '')
        content = content.replace('<p class="Normal-P-P1"><span class="Normal-C-C3"><br/></span></p>', '')
        content = content.replace('<p class="Wp-Normal-P"><span class="Normal-C-C6"><br/></span></p>', '')
        content = content.replace('<p class="Normal-P-P0"><span class="Normal-C-C6"><br/></span></p>', '')
        content = content.replace('<div id="txt_5" style="position:absolute;left:30px;top:298px;width:718px;height:7163px;overflow:hidden;">', '')
        content = content.replace('<p class="List-Paragraph-P"><span class="List-Paragraph-C"><br/></span></p>', '')
        content = content.replace('<div id="txt_5" style="position:absolute;left:33px;top:364px;width:715px;height:4690px;overflow:hidden;">', '')
        file.write(content)

url = 'https://www.baptistpillar.us/article_967d.html'
link_back_to = 'Baptism'
file_name = 'no-right-to-change'
author = 'John Craps'
title = 'We Have No Right to Change the Ordinance of Baptism'
class_name = 'txt_5'

write_content_to_file()