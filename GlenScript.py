# Notes go up here
# I like structuring python scripts like C

import requests
from bs4 import BeautifulSoup

def aznCrawl():
    page = requests.get('http://simple.wikipedia.org')
    soup = BeautifulSoup(page.content, "lxml")
    allTexts = soup.find_all('b')
    print(allTexts)

aznCrawl()