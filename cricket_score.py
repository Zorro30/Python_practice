import bs4 as bs
from urllib import request


url = "http://www.cricbuzz.com/cricket-match/live-scores"

sauce = request.urlopen(url).read()
soup = bs.BeautifulSoup(sauce,"lxml")

score = []
results = []
live = []

for div_tags in soup.find_all('div', attrs={"class": "cb-lv-scrs-col text-black"}):
        score.append(div_tags.text)
for div_detail in soup.find_all('div', attrs={"class":  "cb-lv-scrs-col cb-text-live"}):
        live.append(div_detail.text)
for result in soup.find_all('div', attrs={"class": "cb-lv-scrs-col cb-text-complete"}):
        results.append(result.text)

print(score[0],live[0], " | ", results[0])