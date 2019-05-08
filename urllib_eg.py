import requests
from bs4 import BeautifulSoup

def trade(pages):
    page=1
    while page < pages:
        url = 'https://buckysroom.org/trade/search.php?page=' + str(page)
        source_code =requests.get(url)
        

