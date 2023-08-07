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
        content += f'<!DOCTYPE html> <html> <head> <meta name="viewport" content="width=device-width, initial-scale=1.0" /> <link rel="stylesheet" type="text/css" href="../../../style.css" /> <script rel="script" type="text/javascript" src="../../../functions.js"></script> </head> <body> <div class="container"> <header> <h1>AUTHOR_NAME</h1> </header> <ul> <li> <a href="../../../index.html">About</a> | <a href="../../../Theology.html"> Theology</a> | <a href="../../../OTIntro.html"> Old Testament</a> | <a href="../../../NTIntro.html"> New Testament</a> </li> </ul> <section> <p> <b>TITLE_OF_BOOK</b> </p> </section> <section> <p>TABLE_OF_CONTENTS</p> </section> <footer> <p>&copy; 2023 ebiblecommentary. All rights reserved.</p> </footer> </div> </body> </html>'
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

url = 'https://www.gracegems.org/Watson/Sermons.htm'
author = 'Thomas Watson'
title = 'Sermons'
file_name = 'watson'

urls_titles = find_html_files(url)
# print(urls_titles)

valid_urls_titles = [
  ["https://www.gracegems.org/Watson/worst_things.htm", "worst_things.htm"],
  [
    "https://www.gracegems.org/Watson/christian_on_the_mount.htm",
    "christian_on_the_mount.htm"
  ],
  [
    "https://www.gracegems.org/Watson/duty_of_self_denial.htm",
    "duty_of_self_denial.htm"
  ],
  [
    "https://www.gracegems.org/Watson/god_is_his_people.htm",
    "god_is_his_people.htm"
  ],
  [
    "https://www.gracegems.org/Watson/consolation_in_affliction.htm",
    "consolation_in_affliction.htm"
  ],
  [
    "https://www.gracegems.org/Watson/attributes_of_God.htm",
    "attributes_of_God.htm"
  ],
  [
    "https://www.gracegems.org/Watson/spiritual_watch.htm",
    "spiritual_watch.htm"
  ],
  ["https://www.gracegems.org/Watson/Lords%20Supper.htm", "Lords%20Supper.htm"],
  ["https://www.gracegems.org/Watson/heart_purity.htm", "heart_purity.htm"],
  [
    "https://www.gracegems.org/Watson/death_of_the_righteous.htm",
    "death_of_the_righteous.htm"
  ],
  ["https://www.gracegems.org/Watson/good_shepherd.htm", "good_shepherd.htm"],
  ["https://www.gracegems.org/Watson/comforting_rod.htm", "comforting_rod.htm"],
  ["https://www.gracegems.org/Watson/sanctification.htm", "sanctification.htm"],
  ["https://www.gracegems.org/Watson/christian_joy.htm", "christian_joy.htm"],
  [
    "https://www.gracegems.org/Watson/righteous_mans_weal.htm",
    "righteous_mans_weal.htm"
  ],
  ["https://www.gracegems.org/Watson/mystical_union.htm", "mystical_union.htm"],
  ["https://www.gracegems.org/Watson/saints_desire.htm", "saints_desire.htm"],
  [
    "https://www.gracegems.org/Watson/good_practitioner.htm",
    "good_practitioner.htm"
  ],
  [
    "https://www.gracegems.org/Watson/fight_of_faith_crowned.htm",
    "fight_of_faith_crowned.htm"
  ],
  [
    "https://www.gracegems.org/Watson/godly_mans_picture8.htm",
    "godly_mans_picture8.htm"
  ],
  [
    "http://www.gracegems.org/Watson/godly_mans_picture9.htm",
    "godly_mans_picture9.htm"
  ],
  [
    "https://www.gracegems.org/Watson/Christian_on_earth.htm",
    "Christian_on_earth.htm"
  ],
  [
    "https://www.gracegems.org/Watson/beauty_of_grace.htm",
    "beauty_of_grace.htm"
  ],
  ["https://www.gracegems.org/Watson/evil_tongue.htm", "evil_tongue.htm"],
  [
    "https://www.gracegems.org/Watson/upright_mans_character.htm",
    "upright_mans_character.htm"
  ],
  [
    "https://www.gracegems.org/Watson/souls_malady_and_cure.htm",
    "souls_malady_and_cure.htm"
  ],
  [
    "https://www.gracegems.org/Watson/wise_as_serpents.htm",
    "wise_as_serpents.htm"
  ],
  [
    "https://www.gracegems.org/Watson/substantial_excellency.htm",
    "substantial_excellency.htm"
  ],
  ["https://www.gracegems.org/Watson/new_creature.htm", "new_creature.htm"],
  ["https://www.gracegems.org/Watson/heavenly_race.htm", "heavenly_race.htm"],
  ["https://www.gracegems.org/Watson/fiery_serpents.htm", "fiery_serpents.htm"],
  ["https://www.gracegems.org/Watson/spiritual_vine.htm", "spiritual_vine.htm"],
  [
    "https://www.gracegems.org/Watson/times_shortness.htm",
    "times_shortness.htm"
  ],
  [
    "https://www.gracegems.org/Watson/christ_all_in_all.htm",
    "christ_all_in_all.htm"
  ],
  [
    "https://www.gracegems.org/Watson/mystical_temple.htm",
    "mystical_temple.htm"
  ],
  [
    "https://www.gracegems.org/Watson/roman_catholicism.htm",
    "roman_catholicism.htm"
  ],
  ["https://www.gracegems.org/Watson/plea_for_alms.htm", "plea_for_alms.htm"],
  [
    "https://www.gracegems.org/Watson/farewell_prayer.htm",
    "farewell_prayer.htm"
  ],
  [
    "https://www.gracegems.org/Watson/crown_of_righteousness.htm",
    "crown_of_righteousness.htm"
  ],
  [
    "https://www.gracegems.org/Watson/reading_the_scriptures.htm",
    "reading_the_scriptures.htm"
  ],
  [
    "https://www.gracegems.org/Watson/perfume_of_love.htm",
    "perfume_of_love.htm"
  ],
  [
    "https://www.gracegems.org/Watson/trees_of_righteousness.htm",
    "trees_of_righteousness.htm"
  ],
  [
    "https://www.gracegems.org/Watson/plea_for_the_godly.htm",
    "plea_for_the_godly.htm"
  ],
  [
    "https://www.gracegems.org/Watson/happiness_of_drawing_near_to_god.htm",
    "happiness_of_drawing_near_to_god.htm"
  ],
  [
    "https://www.gracegems.org/Watson/loveliness_of_christ.htm",
    "loveliness_of_christ.htm"
  ],
  [
    "https://www.gracegems.org/Watson/lover_of_the_word.htm",
    "lover_of_the_word.htm"
  ],
  [
    "https://www.gracegems.org/Watson/light_in_darkness.htm",
    "light_in_darkness.htm"
  ],
  [
    "https://www.gracegems.org/Watson/his_heart_is_fixed.htm",
    "his_heart_is_fixed.htm"
  ],
  [
    "https://www.gracegems.org/Watson/one_thing_necessary.htm",
    "one_thing_necessary.htm"
  ],
  [
    "https://www.gracegems.org/Watson/christians_charter.htm",
    "christians_charter.htm"
  ],
  [
    "https://www.gracegems.org/Watson/day_of_judgment.htm",
    "day_of_judgment.htm"
  ],
  ["https://www.gracegems.org/Watson/assurance.htm", "assurance.htm"],
  [
    "https://www.gracegems.org/Watson/saints_spiritual_delight.htm",
    "saints_spiritual_delight.htm"
  ],
  ["https://www.gracegems.org/Watson/kiss_the_son.htm", "kiss_the_son.htm"],
  [
    "https://www.gracegems.org/Watson/until_my_change_comes.htm",
    "until_my_change_comes.htm"
  ],
  ["https://www.gracegems.org/Watson/true_religion.htm", "true_religion.htm"],
  [
    "https://www.gracegems.org/Watson/peace_of_christ.htm",
    "peace_of_christ.htm"
  ],
  ["https://www.gracegems.org/Watson/Scripture.htm", "Scripture.htm"],
  [
    "https://www.gracegems.org/Watson/gods_anatomy_upon_mans_heart.htm",
    "gods_anatomy_upon_mans_heart.htm"
  ],
  [
    "https://www.gracegems.org/Watson/preciousness_of_the_soul.htm",
    "preciousness_of_the_soul.htm"
  ],
  [
    "https://www.gracegems.org/Watson/comfort_for_the_church.htm",
    "comfort_for_the_church.htm"
  ],
  [
    "https://www.gracegems.org/Watson/knowing_and_doing_good.htm",
    "knowing_and_doing_good.htm"
  ],
  ["https://www.gracegems.org/Watson/sacred_anchor.htm", "sacred_anchor.htm"],
  [
    "https://www.gracegems.org/Watson/let_us_not_grow_weary.htm",
    "let_us_not_grow_weary.htm"
  ],
  ["https://www.gracegems.org/Watson/dearly_beloved.htm", "dearly_beloved.htm"],
  [
    "https://www.gracegems.org/Watson/love_one_another.htm",
    "love_one_another.htm"
  ],
  [
    "https://www.gracegems.org/Watson/farewell_sermon.htm",
    "farewell_sermon.htm"
  ],
  ["https://www.gracegems.org/Watson/original_sin.htm", "original_sin.htm"]
]

create_files(file_name, author, title, valid_urls_titles)