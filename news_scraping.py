from bs4 import BeautifulSoup
import requests

r =requests.get("http://indiatoday.in")
soup = BeautifulSoup(r.text,'lxml')

news_box = soup.find('ul')
all_news = news_box.find_all('a')

for news in all_news:
    print(news.text)

