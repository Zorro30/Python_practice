import requests
from bs4 import BeautifulSoup

url="http://www.cricbuzz.com/cricket-stats/icc-rankings"
r = requests.get(url)
#print(r.content)

soap = BeautifulSoup(r.content, "html.parser")
#print (soap.prettify())

links = soap.find_all("div")

#print (links)

g_data = soap.find_all("div", {"class":"cb-col cb-col-20 cb-lst-itm-sm "})
print (g_data)

#for link in g_data:
#    print (link.contents[0].find_all("div", {"class":"cb-col cb-col-50 cb-lst-itm-sm text-left"}))
    #print (link.contents[0].find_all("div",{"class": ""}))
    #stopped here it was not printing, cz the tags are having whitespace between them.