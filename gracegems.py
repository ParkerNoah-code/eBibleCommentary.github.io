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

url = 'https://www.gracegems.org/Spurgeon/Treasury%20of%20David.htm'
author = 'Charles Spurgeon'
title = 'Treasury of David'
file_name = 'treasury'

urls_titles = find_html_files(url)
print(urls_titles)

valid_urls_titles = [
  ["https://www.gracegems.org/Spurgeon/000.htm", "preface_to_volume_1.htm"],
  ["https://www.gracegems.org/Spurgeon/001.htm", "001.htm"],
  ["https://www.gracegems.org/Spurgeon/002.htm", "002.htm"],
  ["https://www.gracegems.org/Spurgeon/003.htm", "003.htm"],
  ["https://www.gracegems.org/Spurgeon/004.htm", "004.htm"],
  ["https://www.gracegems.org/Spurgeon/005.htm", "005.htm"],
  ["https://www.gracegems.org/Spurgeon/006.htm", "006.htm"],
  ["https://www.gracegems.org/Spurgeon/007.htm", "007.htm"],
  ["https://www.gracegems.org/Spurgeon/008.htm", "008.htm"],
  ["https://www.gracegems.org/Spurgeon/009.htm", "009.htm"],
  ["https://www.gracegems.org/Spurgeon/010.htm", "010.htm"],
  ["https://www.gracegems.org/Spurgeon/011.htm", "011.htm"],
  ["https://www.gracegems.org/Spurgeon/012.htm", "012.htm"],
  ["https://www.gracegems.org/Spurgeon/013.htm", "013.htm"],
  ["https://www.gracegems.org/Spurgeon/014.htm", "014.htm"],
  ["https://www.gracegems.org/Spurgeon/015.htm", "015.htm"],
  ["https://www.gracegems.org/Spurgeon/016.htm", "016.htm"],
  ["https://www.gracegems.org/Spurgeon/017.htm", "017.htm"],
  ["https://www.gracegems.org/Spurgeon/018.htm", "018.htm"],
  ["https://www.gracegems.org/Spurgeon/019.htm", "019.htm"],
  ["https://www.gracegems.org/Spurgeon/020.htm", "020.htm"],
  ["https://www.gracegems.org/Spurgeon/021.htm", "021.htm"],
  ["https://www.gracegems.org/Spurgeon/022.htm", "022.htm"],
  ["https://www.gracegems.org/Spurgeon/023.htm", "023.htm"],
  ["https://www.gracegems.org/Spurgeon/024.htm", "024.htm"],
  ["https://www.gracegems.org/Spurgeon/025.htm", "025.htm"],
  ["https://www.gracegems.org/Spurgeon/026.htm", "026.htm"],
  [
    "https://www.gracegems.org/Spurgeon/preface_to_volume_2.htm",
    "preface_to_volume_2.htm"
  ],
  ["https://www.gracegems.org/Spurgeon/027.htm", "027.htm"],
  ["https://www.gracegems.org/Spurgeon/028.htm", "028.htm"],
  ["https://www.gracegems.org/Spurgeon/029.htm", "029.htm"],
  ["https://www.gracegems.org/Spurgeon/030.htm", "030.htm"],
  ["https://www.gracegems.org/Spurgeon/031.htm", "031.htm"],
  ["https://www.gracegems.org/Spurgeon/032.htm", "032.htm"],
  ["https://www.gracegems.org/Spurgeon/033.htm", "033.htm"],
  ["https://www.gracegems.org/Spurgeon/034.htm", "034.htm"],
  ["https://www.gracegems.org/Spurgeon/035.htm", "035.htm"],
  ["https://www.gracegems.org/Spurgeon/036.htm", "036.htm"],
  ["https://www.gracegems.org/Spurgeon/037.htm", "037.htm"],
  ["https://www.gracegems.org/Spurgeon/038.htm", "038.htm"],
  ["https://www.gracegems.org/Spurgeon/039.htm", "039.htm"],
  ["https://www.gracegems.org/Spurgeon/040.htm", "040.htm"],
  ["https://www.gracegems.org/Spurgeon/041.htm", "041.htm"],
  ["https://www.gracegems.org/Spurgeon/042.htm", "042.htm"],
  ["https://www.gracegems.org/Spurgeon/043.htm", "043.htm"],
  ["https://www.gracegems.org/Spurgeon/044.htm", "044.htm"],
  ["https://www.gracegems.org/Spurgeon/045.htm", "045.htm"],
  ["https://www.gracegems.org/Spurgeon/046.htm", "046.htm"],
  ["https://www.gracegems.org/Spurgeon/047.htm", "047.htm"],
  ["https://www.gracegems.org/Spurgeon/048.htm", "048.htm"],
  ["https://www.gracegems.org/Spurgeon/049.htm", "049.htm"],
  ["https://www.gracegems.org/Spurgeon/050.htm", "050.htm"],
  ["https://www.gracegems.org/Spurgeon/051.htm", "051.htm"],
  ["https://www.gracegems.org/Spurgeon/052.htm", "052.htm"],
  [
    "https://www.gracegems.org/Spurgeon/preface_to_volume_3.htm",
    "preface_to_volume_3.htm"
  ],
  ["https://www.gracegems.org/Spurgeon/053.htm", "053.htm"],
  ["https://www.gracegems.org/Spurgeon/054.htm", "054.htm"],
  ["https://www.gracegems.org/Spurgeon/055.htm", "055.htm"],
  ["https://www.gracegems.org/Spurgeon/056.htm", "056.htm"],
  ["https://www.gracegems.org/Spurgeon/057.htm", "057.htm"],
  ["https://www.gracegems.org/Spurgeon/058.htm", "058.htm"],
  ["https://www.gracegems.org/Spurgeon/059.htm", "059.htm"],
  ["https://www.gracegems.org/Spurgeon/060.htm", "060.htm"],
  ["https://www.gracegems.org/Spurgeon/061.htm", "061.htm"],
  ["https://www.gracegems.org/Spurgeon/062.htm", "062.htm"],
  ["https://www.gracegems.org/Spurgeon/063.htm", "063.htm"],
  ["https://www.gracegems.org/Spurgeon/064.htm", "064.htm"],
  ["https://www.gracegems.org/Spurgeon/065.htm", "065.htm"],
  ["https://www.gracegems.org/Spurgeon/066.htm", "066.htm"],
  ["https://www.gracegems.org/Spurgeon/067.htm", "067.htm"],
  ["https://www.gracegems.org/Spurgeon/068.htm", "068.htm"],
  ["https://www.gracegems.org/Spurgeon/069.htm", "069.htm"],
  ["https://www.gracegems.org/Spurgeon/070.htm", "070.htm"],
  ["https://www.gracegems.org/Spurgeon/071.htm", "071.htm"],
  ["https://www.gracegems.org/Spurgeon/072.htm", "072.htm"],
  ["https://www.gracegems.org/Spurgeon/073.htm", "073.htm"],
  ["https://www.gracegems.org/Spurgeon/074.htm", "074.htm"],
  ["https://www.gracegems.org/Spurgeon/075.htm", "075.htm"],
  ["https://www.gracegems.org/Spurgeon/076.htm", "076.htm"],
  ["https://www.gracegems.org/Spurgeon/077.htm", "077.htm"],
  ["https://www.gracegems.org/Spurgeon/078.htm", "078.htm"],
  [
    "https://www.gracegems.org/Spurgeon/preface_to_volume_4.htm",
    "preface_to_volume_4.htm"
  ],
  ["https://www.gracegems.org/Spurgeon/079.htm", "079.htm"],
  ["https://www.gracegems.org/Spurgeon/080.htm", "080.htm"],
  ["https://www.gracegems.org/Spurgeon/081.htm", "081.htm"],
  ["https://www.gracegems.org/Spurgeon/082.htm", "082.htm"],
  ["https://www.gracegems.org/Spurgeon/083.htm", "083.htm"],
  ["https://www.gracegems.org/Spurgeon/084.htm", "084.htm"],
  ["https://www.gracegems.org/Spurgeon/085.htm", "085.htm"],
  ["https://www.gracegems.org/Spurgeon/086.htm", "086.htm"],
  ["https://www.gracegems.org/Spurgeon/087.htm", "087.htm"],
  ["https://www.gracegems.org/Spurgeon/088.htm", "088.htm"],
  ["https://www.gracegems.org/Spurgeon/089.htm", "089.htm"],
  ["https://www.gracegems.org/Spurgeon/090.htm", "090.htm"],
  ["https://www.gracegems.org/Spurgeon/091.htm", "091.htm"],
  ["https://www.gracegems.org/Spurgeon/092.htm", "092.htm"],
  ["https://www.gracegems.org/Spurgeon/093.htm", "093.htm"],
  ["https://www.gracegems.org/Spurgeon/094.htm", "094.htm"],
  ["https://www.gracegems.org/Spurgeon/095.htm", "095.htm"],
  ["https://www.gracegems.org/Spurgeon/096.htm", "096.htm"],
  ["https://www.gracegems.org/Spurgeon/097.htm", "097.htm"],
  ["https://www.gracegems.org/Spurgeon/098.htm", "098.htm"],
  ["https://www.gracegems.org/Spurgeon/099.htm", "099.htm"],
  ["https://www.gracegems.org/Spurgeon/100.htm", "100.htm"],
  ["https://www.gracegems.org/Spurgeon/101.htm", "101.htm"],
  ["https://www.gracegems.org/Spurgeon/102.htm", "102.htm"],
  ["https://www.gracegems.org/Spurgeon/103.htm", "103.htm"],
  [
    "https://www.gracegems.org/Spurgeon/preface_to_volume_5.htm",
    "preface_to_volume_5.htm"
  ],
  ["https://www.gracegems.org/Spurgeon/104.htm", "104.htm"],
  ["https://www.gracegems.org/Spurgeon/105.htm", "105.htm"],
  ["https://www.gracegems.org/Spurgeon/106.htm", "106.htm"],
  ["https://www.gracegems.org/Spurgeon/107.htm", "107.htm"],
  ["https://www.gracegems.org/Spurgeon/108.htm", "108.htm"],
  ["https://www.gracegems.org/Spurgeon/109.htm", "109.htm"],
  ["https://www.gracegems.org/Spurgeon/110.htm", "110.htm"],
  ["https://www.gracegems.org/Spurgeon/111.htm", "111.htm"],
  ["https://www.gracegems.org/Spurgeon/112.htm", "112.htm"],
  ["https://www.gracegems.org/Spurgeon/113.htm", "113.htm"],
  ["https://www.gracegems.org/Spurgeon/114.htm", "114.htm"],
  ["https://www.gracegems.org/Spurgeon/115.htm", "115.htm"],
  ["https://www.gracegems.org/Spurgeon/116.htm", "116.htm"],
  ["https://www.gracegems.org/Spurgeon/117.htm", "117.htm"],
  ["https://www.gracegems.org/Spurgeon/118.htm", "118.htm"],
  [
    "https://www.gracegems.org/Spurgeon/preface_to_volume_6.htm",
    "preface_to_volume_6.htm"
  ],
  ["https://www.gracegems.org/Spurgeon/119.htm", "119.htm"],
  ["https://www.gracegems.org/Spurgeon/120.htm", "120.htm"],
  ["https://www.gracegems.org/Spurgeon/121.htm", "121.htm"],
  ["https://www.gracegems.org/Spurgeon/122.htm", "122.htm"],
  ["https://www.gracegems.org/Spurgeon/123.htm", "123.htm"],
  ["https://www.gracegems.org/Spurgeon/124.htm", "124.htm"],
  [
    "https://www.gracegems.org/Spurgeon/preface_to_volume_7.htm",
    "preface_to_volume_7.htm"
  ],
  ["https://www.gracegems.org/Spurgeon/125.htm", "125.htm"],
  ["https://www.gracegems.org/Spurgeon/126.htm", "126.htm"],
  ["https://www.gracegems.org/Spurgeon/127.htm", "127.htm"],
  ["https://www.gracegems.org/Spurgeon/128.htm", "128.htm"],
  ["https://www.gracegems.org/Spurgeon/129.htm", "129.htm"],
  ["https://www.gracegems.org/Spurgeon/130.htm", "130.htm"],
  ["https://www.gracegems.org/Spurgeon/131.htm", "131.htm"],
  ["https://www.gracegems.org/Spurgeon/132.htm", "132.htm"],
  ["https://www.gracegems.org/Spurgeon/133.htm", "133.htm"],
  ["https://www.gracegems.org/Spurgeon/134.htm", "134.htm"],
  ["https://www.gracegems.org/Spurgeon/135.htm", "135.htm"],
  ["https://www.gracegems.org/Spurgeon/136.htm", "136.htm"],
  ["https://www.gracegems.org/Spurgeon/137.htm", "137.htm"],
  ["https://www.gracegems.org/Spurgeon/138.htm", "138.htm"],
  ["https://www.gracegems.org/Spurgeon/139.htm", "139.htm"],
  ["https://www.gracegems.org/Spurgeon/140.htm", "140.htm"],
  ["https://www.gracegems.org/Spurgeon/141.htm", "141.htm"],
  ["https://www.gracegems.org/Spurgeon/142.htm", "142.htm"],
  ["https://www.gracegems.org/Spurgeon/143.htm", "143.htm"],
  ["https://www.gracegems.org/Spurgeon/144.htm", "144.htm"],
  ["https://www.gracegems.org/Spurgeon/145.htm", "145.htm"],
  ["https://www.gracegems.org/Spurgeon/146.htm", "146.htm"],
  ["https://www.gracegems.org/Spurgeon/147.htm", "147.htm"],
  ["https://www.gracegems.org/Spurgeon/148.htm", "148.htm"],
  ["https://www.gracegems.org/Spurgeon/149.htm", "149.htm"],
  ["https://www.gracegems.org/Spurgeon/150.htm", "150.htm"]
]

create_files(file_name, author, title, valid_urls_titles)