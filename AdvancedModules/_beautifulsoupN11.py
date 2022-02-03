from bs4 import BeautifulSoup
import requests

url = 'https://www.n11.com/bilgisayar/dizustu-bilgisayar'
html = requests.get(url).content
soup = BeautifulSoup(html,'html.parser')
list = soup.find('section',{'class':'group listingGroup resultListGroup import-search-view'}).find_all('li',{'class':'column'},limit = 2)
for li in list:
    name = li.find('div',{'class':'pro'}).find('a',{'class':'plink'}).find('h3',{'class':'productName'}).text.strip('\n').strip()
    link = li.find('div',{'class':'pro'}).find('a',{'class':'plink'}).get('href')
    oldPrice = li.find('div',{'class':'proDetail'}).find('a',{'class':'oldPrice'}).find('del').text.strip().strip('TL')
    newPrice = li.find('div',{'class':'proDetail'}).find('a',{'class':'newPrice'}).find('ins').text.strip().strip('TL').strip()
    print(name)
    print(oldPrice)
    print(newPrice)
