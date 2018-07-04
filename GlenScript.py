# Notes go up here
# I like structuring python scripts like C

import requests

def main():
    page = requests.get('https://simple.wikipedia.org/wiki/Main_Page')
    print(page.content)
    
main()
