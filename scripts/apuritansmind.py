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
title = 'Sermons'
file_name = 'sermon'
titles = ['The Vain Self Flatteries of the Sinner – Psalm 36:2', 'The End of the Wicked Contemplated by the Righteous – Revelation 18:20', 'The Portion of the Wicked – Romans 2:8, 9', 'When the Wicked Shall Have Filled Up the Measure of Their Sin, Wrath Will Come Upon Them to the Uttermost – 1 Thess. 2:16', 'Wicked Men Inconsistent With Themselves – Matthew 11:16-19', 'The Eternity of Hells Torments – Matthew 25:46', 'Sinners in Zion Tenderly Warned – Isaiah 33:14', 'The Future Punishment of the Wicked Unavoidable and Intolerable – Ezekiel 22:14', 'Sinners in the Hands of an Angry God– Deuteronomy 32:35', 'Wicked Men Useful in Their Destruction Only – Ezekiel 15:2-4', 'Sinners Delay Concerns the Soul – Acts 24:25', 'Natural Men in a Dreadful Condition – Acts 16:29, 30', 'Christians A Chosen Generation, A Royal Priesthood, A Holy Nation, A Peculiar People – 1 Peter 2:9', 'Few There Be That Find It – Matthew 7:14', 'God Makes Men Sensible of Their Misery Before He Reveals His Mercy and Love – Hosea 5:15', 'God’s Sovereignty in the Salvation of Men – Romans 9:18', 'Pardon for the Greatest of Sinners – Psalm 25:11', 'The Warnings of Scripture Are in the Best Manner Adapted to the Awakening and Conversion Of Sinners – Luke 16:31', 'The Final Judgment – Acts 17:31', 'The Perpetuity And Change Of The Sabbath – 1 Corinthians 16:1, 2', 'God Glorified in Man’s Dependence – 1 Corinthians 1:29-31', 'The Wisdom of God, Displayed in the Way of Salvation – Ephesians 3:10', 'Justification by Faith Alone – Romans 4:5', 'Pressing into the Kingdom of God– Luke 26:16', 'Ruth’s Resolutions – Ruth 1:16', 'The Justice of God in the Damnation of Sinners – Romans 3:19', 'The Excellency of Jesus Christ – Revelation 5:5-6', 'The Folly Of Looking Back In Fleeing Out Of Sodom – Luke 17:32', 'The Sole Consideration, That God is God, Sufficient to Still All Objections to His Sovereignty – Psalm 46:10', 'Unbelievers Contemn The Glory And Excellency Of Christ – Acts 4:11', 'Men Naturally Are God’s Enemies – Romans 5:10', 'Jesus Christ The Same Yesterday, Today, And Forever – Hebrews 13:8', 'Christ Exalted – 1 Corinthians 15:25, 26', 'The Character Of Paul An Example To Christians – Philippians 3:17', 'Man’s Natural Blindness In Things Of Religion – Psalm 94:8-11', 'Christ’s Agony – Luke 22:44', 'Wicked Men of the Past are Still in Hell – 1 Peter 3:19, 20', 'The Scripture Is The Word Of God – 2 Timothy 3:16', 'A Divine and Supernatural Light – Matthew 16:17', 'The Most High a Prayer Hearing God – Psalm 65:2', 'Many Mansions – John 14:2', 'The Nature and End of Excommunication – 1 Corinthians 5:11', 'The Sorrows of the Bereaved Spread Before Jesus – Matthew 14:12', 'The True Excellency Of A Gospel Minister – John 5:35', 'The Church’s Marriage To Her Sons, And To Her God – Isaiah 62:4, 5', 'True Saints, When Absent From the Body, Are Present With the Lord – 2 Corinthians 5:8', 'God’s Awful Judgment In The Breaking And Withering Of The Strong Rods of a Community – Ezekiel 19:12', 'Christ the Example of Ministers – John 13:15, 16', 'True Grace Distinguished From the Experience of Devils – James 2:19', 'A Farewell Sermon – 2 Corinthians 1:14', 'Christian Knowledge – Hebrews 5:12', 'Procrastination – Proverbs 27:1', 'A Warning To Professors – Ezekiel 23:37, 38, 39', 'Christian Charity – Deuteronomy 15:7-11', 'The Christian Pilgrim – Hebrews 11:13, 14', 'Christian Cautions – Psalms 139:23, 24', 'Praise, One Of The Chief Employments Of Heaven – Revelation 14:2', 'The Preciousness Of Time And The Importance Of Redeeming It – Ephesians 5:16', 'The Unreasonableness Of Indetermination In Religion – 1 Kings 18:21', 'God The Best Portion Of The Christian – Psalm 73:25', 'Hope And Comfort Usually Follow Genuine Humiliation And Repentance – Hosea 2:15', 'Temptation and Deliverance – Genesis 39:12', 'The Portion of the Righteous – Romans 2:10', 'Hypocrites Deficient in the Duty of Prayer – Job 37:10', 'Dishonesty – Exodus 20:15', 'The Manner in Which the Salvation of the Soul is to be Sought – Genesis 6:22', 'Peace With God – Romans 5:1', 'The Peace Which Christ Gives His True Followers – John 14:27', 'Safety, Fullness, and Sweet Refreshment, to be Found in Christ – Isaiah 32:2', 'The Pure In Heart Blessed – Matthew 5:8']
urls = [
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/the-vain-self-flatteries-of-the-sinner/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/the-end-of-the-wicked-contemplated-by-the-righteous/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/the-portion-of-the-wicked/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/when-the-wicked-have-filled-up-the-measure-of-their-sin/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/wicked-men-inconsistent-with-themselves/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/the-eternity-of-hells-torments/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/sinners-in-zion-tenderly-warned/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/the-future-punishment-of-the-wicked-unavoidable-and-intolerable/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/sinners-in-the-hands-of-an-angry-god/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/wicked-men-useful-in-their-destruction-only/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/sinners-delay-concerns-the-soul/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/natural-men-in-a-dreadful-condition/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/christians-a-chosen-generation/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/few-there-be-that-find-it/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/men-sensible-of-their-misery/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/gods-sovereignty-in-the-salvation-of-men/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/pardon-for-the-greatest-sinners/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/the-warnings-of-scripture-are-in-the-best-manner-adapted-to-the-awakening-and-conversion-of-sinners/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/the-final-judgment/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/the-perpetuity-and-change-of-the-sabbath/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/god-glorified-in-mans-dependence/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/the-wisdom-of-god-displayed-in-the-way-of-salvation/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/justification-by-faith-alone/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/pressing-into-the-kingdom/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/ruths-resolution/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/the-justice-of-god-in-the-damnation-of-sinners/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/the-excellency-of-christ/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/the-folly-of-looking-back-in-fleeing-out-of-sodom/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/the-sole-consideration-that-god-is-god-sufficient-to-still-all-objections-to-his-sovereignty/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/unbelievers-contemn-the-glory-and-excellency-of-christ/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/men-naturally-are-god%E2%80%99s-enemies/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/jesus-christ-the-same-yesterday-today-and-forever/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/christ-exalted/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/the-character-of-paul-an-example-to-christians/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/man%E2%80%99s-natural-blindness-in-things-of-religion/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/christs-agony/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/wicked-men-of-the-past-are-still-in-hell/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/the-scripture-is-the-word-of-god/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/a-divine-and-supernatural-light/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/the-most-high-a-prayer-hearing-god/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/many-mansions/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/the-nature-and-end-of-excommunication/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/the-sorrows-of-the-bereaved-spread-before-jesus/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/the-true-excellency-of-a-gospel-minister/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/the-churchs-marriage-to-her-sons-and-to-her-god/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/true-saints-when-absent-from-the-body-are-present-with-the-lord/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/god%E2%80%99s-awful-judgment-in-the-breaking-and-withering-of-the-strong-rods-of-a-community/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/god%E2%80%99s-awful-judgment-in-the-breaking-and-withering-of-the-strong-rods-of-a-community/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/christ-the-example-of-ministers/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/true-grace-distinguished-from-the-experience-of-devils/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/a-farewell-sermon/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/christian-knowledge/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/procrastination/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/a-warning-to-professors/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/christian-charity/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/the-christian-pilgrim/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/christian-cautions/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/praise-one-of-the-chief-employments-of-heaven/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/the-preciousness-of-time-and-the-importance-of-redeeming-it/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/the-unreasonableness-of-indetermination-in-religion/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/god-the-best-portion-of-the-christian/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/hope-and-comfort/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/temptation-and-deliverance/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/the-portion-of-the-righteous/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/hypocrites-deficient-in-the-duty-of-prayer/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/dishonesty/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/the-manner-in-which-the-salvation-of-the-soul-is-to-be-sought/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/peace-with-god/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/safety-fullness-and-sweet-refreshment-to-be-found-in-christ/',
  'https://www.apuritansmind.com/puritan-favorites/jonathan-edwards/sermons/the-pure-in-heart-blessed/',
]

create_files(file_name, author, title, titles, urls)
create_table_of_contents(file_name, author, title, titles)