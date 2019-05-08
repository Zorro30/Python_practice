from urllib.request import urlopen
from bs4 import BeautifulSoup
import lxml

page = urlopen("https://www.bbc.com/news")
read = page.read()


soup_page = BeautifulSoup(read,'lxml')
news = soup_page.findAll('a')
#print(news)

for i in news:
    print (i)
#news = soup_page.findAll("class" ,attrs = "gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor")
'''
for tags in soup_page.findall('div', attrs={'class' :'gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor'}):

    print (tags.text)'''
