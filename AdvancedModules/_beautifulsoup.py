from bs4 import BeautifulSoup
import json
import requests

apiUrl = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
html = requests.get(apiUrl).content
soup = BeautifulSoup(html,'html.parser')

list = soup.find('tbody',{"class":'lister-list'}).find_all('tr',limit=10)
for tr in list:
    title = tr.find('td',{'class':'titleColumn'}).find('a').text
    print(title)
for tr in list:
    title = tr.find('td',{'class':'titleColumn'}).find('span').text
    print(title)
for tr in list:
    title = tr.find('td',{'class':'ratingColumn imdbRating'}).find('strong').text
    print(title)


