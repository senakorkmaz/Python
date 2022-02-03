from bs4 import BeautifulSoup
import requests
import time

url = 'http://www.mersin.edu.tr/haberler/366314/erasmus-sinav-duyurulari'
while (1):
    html = requests.get(url).content
    soup = BeautifulSoup(html,'html.parser')
    link = soup.find('div',{'class':'col-md-8 text-left'}).find_all('li',limit=2)
    for li in link:
        print(li.text.strip())
    time.sleep(1)


