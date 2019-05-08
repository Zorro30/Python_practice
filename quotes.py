
from bs4 import BeautifulSoup
import requests

res = requests.get('http://quotes.toscrape.com/')
soup = BeautifulSoup(res.text, 'lxml')

Image_quote = soup.find('img', {'class' : ' p-qotd bqPhotoDefault bqPhotoDefaultFw img-responsive'})
print(Image_quote['alt'])

