import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.yellowpages.com/search?search_terms=coffee&geo_location_terms=Los+Angeles%2C+CA")
#print (r.content)

soup= BeautifulSoup(r.content)
print (soup.prettify())

links= soup.find_all("a")

for link in links:
    "<a href='%s'>%s</a>" %(link.get("href"),link.text)

g_data= soup.find_all("div", {"class":"info"})

for item in g_data:
    print (item.contents[0].find_all("a", {"class": "business-name"})[0].text)
    try:
        print (item.contents[1].find_all("p", {"class": "adr"})[0].text)
        print (item.contents[1].find_all("div",{"class": "phones phone primary"})[0].text)
    except:
        pass