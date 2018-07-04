# Notes go up here
# I like structuring python scripts like C

import requests

def main():
    page = requests.get('https://dougvace.github.io')
    print(page.content)
    
main()
