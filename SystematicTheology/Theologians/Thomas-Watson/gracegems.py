import re
import requests
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def find_html_files(url):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to fetch {url}. Status code: {response.status_code}")
            return

        soup = BeautifulSoup(response.text, 'html.parser')
        html_links = soup.find_all('a', href=re.compile(r'\.htm$'))
        base_url = response.url

        html_files = [[urljoin(base_url,link['href']), link['href']] for link in html_links]
        return html_files

    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return []
    
def get_content(url_link):
    try:
        # Fetch the content of the URL
        response = requests.get(url_link)
        response.raise_for_status()  # Check for HTTP errors

        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the div element with class="bookText"
        book_text_div = soup.find('blockquote')

        if book_text_div:
            return str(book_text_div)
        else:
            print(f"Error: No <div class=\"bookText\"> element found in URL {url_link}")
            return ''

    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL {url_link}: {e}")
        return ''
    
def create_table_of_contents(file_name, author, title, urls, titles):
    content = ''
    filename = os.path.dirname(os.path.abspath(__file__)) + f'/' + file_name +'.html'
    with open(filename, 'w', encoding='utf-8') as file:
        content += f'<!DOCTYPE html> <html> <head> <meta name="viewport" content="width=device-width, initial-scale=1.0" /> <link rel="stylesheet" type="text/css" href="../../../style.css" /> <script rel="script" type="text/javascript" src="../../../functions.js"></script> </head> <body> <div class="container"> <header> <h1>AUTHOR_NAME</h1> </header> <ul> <li> <a href="../../../index.html">About</a> | <a href="../../../Theology.html"> Theology</a> | <a href="../../../OTIntro.html"> Old Testament</a> | <a href="../../../NTIntro.html"> New Testament</a> </li> </ul> <section> <p><a href="../theologians.html">AUTHOR_NAME</a>: </p> <p> <b>TITLE_OF_BOOK</b> </p> </section> <section> <p>TABLE_OF_CONTENTS</p> </section> <footer> <p>&copy; 2023 ebiblecommentary. All rights reserved.</p> </footer> </div> </body> </html>'
        for i in range(0, len(titles)):
            content = content.replace('TABLE_OF_CONTENTS', '<a href="' + file_name + '-' + str(i) + '.html">' + titles[i] + '</a><br> TABLE_OF_CONTENTS')
        content = content.replace('<br> TABLE_OF_CONTENTS', '')
        content = content.replace('AUTHOR_NAME', author)
        content = content.replace('TITLE_OF_BOOK', title)
        content = content.replace('FILE_NAME', file_name)
        file.write(content)

def create_files(file_name, author, title, valid_urls_titles):
    urls = []
    titles = []
    for i in valid_urls_titles:
        urls.append(i[0])
        titles.append(i[1].replace('_',' ').replace('%', ' ').replace('.htm','').upper())
    create_table_of_contents(file_name, author, title, urls, titles)

    for u in range(0,len(urls)):
        print(urls[u]+' + '+titles[u])
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

url = 'http://gracegems.org/Watson/religion_our_true_interest.htm'
author = 'Thomas Watson'
title = 'The Great Gain of Godliness'
file_name = 'gain-of-godliness'

urls_titles = find_html_files(url)
print(urls_titles)

valid_urls_titles = [['https://gracegems.org/Watson/religion_our_true_interest1.htm', 'Part 1.htm'], ['https://gracegems.org/Watson/religion_our_true_interest2.htm', 'Part 2.htm'], ['https://gracegems.org/Watson/religion_our_true_interest3.htm', 'Part 3.htm']]

create_files(file_name, author, title, valid_urls_titles)