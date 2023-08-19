import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os

def write_content_to_file():
    for i in range(0, len(titles)):
        filename = os.path.dirname(os.path.abspath(__file__)) + f'/' + file_name + f'-{i}.html'
        content = ''
        with open(filename, 'w', encoding='utf-8') as file:
            content += f'<!DOCTYPE html> <html> <head> <meta name="viewport" content="width=device-width, initial-scale=1.0" /> <link rel="stylesheet" type="text/css" href="../../../style.css" /      > <script rel="script" type="text/javascript" src="../../../functions.js"></script> </head> <body> <div class="container"> <header> <h1>{author}</h1> </header> <ul> <li> <a      href="../../../index.html">About</a> | <a href="../../../Theology.html"> Theology</a> | <a href="../../../OTIntro.html"> Old Testament</a> | <a href="../../../NTIntro.html">    New   Testament</a> </li> </ul> <section> <p> <a href="{link_back_to}.html">{title}</a>: </p> </section> <section> <p> '
            content += lines[i]
            content += f'</section> <footer> <p>&copy;    2023 ebiblecommentary. All rights reserved.</p> </footer> </div> </body> </html>'
            file.write(content)

link_back_to = 'systematic-theology'
file_name = 'systematic-theology'
author = 'Louis Berkhof'
title = 'Systematic Theology'

titles = [ "I. The Existence of God ","II. The Knowability of God ","III. Relation of the Being and Attributes of God ","IV. The Names of God ","V. The Attributes of God in General ","VI.The Incommunicable Attributes ","VII. The Communicable ","VIII. The Holy Trinity ","I. The Divine Decrees in General ","II. Predestination ","III. Creation in General ","IV. Creation of the Spiritual World ","V. Creation of the World ","VI. Providence ","I. The Origin of Man ","II. The Constitutional Nature of Man ","III. Man as the Image of God ","IV. Man in the Covenant of Works ","I. The Origin of Sin ","II. The Essential Character of Sin ","III. The Transmission of Sin ","IV. Sin in the Life of the Human Race ","V. The Punishment of Sin ","I. Name and Concept of the Covenant ","II The Covenant of Redemption ","III. Nature of the Covenant of Grace ","IV. The Dual Aspect of the Covenant ","V. The Different Dispensations of the Covenant ","I. The Doctrine of Christ in History ","II The Names and Natures of Christ ","III. The Unipersonality of Christ ","I. The State of Humiliation ","II. The State of Exaltation ","I. Introduction; The Prophetic Office ","II. The Priestly Office ","III. The Cause and Necessity of the Atonement ","IV. The Nature of the Atonement ","V. Divergent Theories of the Atonement ","VI.The Purpose and the Extent of the Atonement ","VII. The Intercessory Work of Christ ","VIII. The Kingly Office ","I. Soteriology in General ","II. The Operations of the Holy Spirit in General ","III. Common Grace ","IV. The Mystical Union ","V. Calling in General and External Calling ","VI. Regeneration and Effectual Calling ","VII. Conversion ","VIII. Faith ","IX. Justification ","X. Sanctification ","XI. Perseverance of the Saints ","Introduction ","I. Scriptural Names of the Church and the Doctrine of the Church in History ","II. Nature of the Church ","III. The Government of the Church ","IV. The Power of the Church ","I. The Means of Grace in General ","II. The Word as a Means of Grace ","III. The Sacraments in General ","IV. Christian Baptism ","V. The Lord's Supper ","Introductory Chapter ","I. Physical Death ","II. The Immortality of the Soul ","III. The Intermediate State ","I. The Second Coming of Christ ","II. Millenial Views ","III. The Resurrection of the Dead ","IV. The Final Judgement. ","V. The Final State ","Bibliography" ]

text_file = open("D:\WritingProject\minininja0412.github.io\SystematicTheology\Theologians\Louis-Berkhof\sys-theo-text.txt", "r")
lines = text_file.read().split('REPLACE_TITLE')
print(len(lines))
print(len(titles))

write_content_to_file()