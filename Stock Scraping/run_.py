import requests
from bs4 import BeautifulSoup
from time import sleep
import os
import json

class Stock:
    def __init__(self,url):
        self.url    = url

    def priceTrack(self):
        url = self.url
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        #print(soup.prettify())
        price = soup.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span')
    
   #def 
if __name__ == '__main__':

    stock = Stock('https://finance.yahoo.com/quote/TSLA?p=TSLA&.tsrc=fin-srch')
    i = 0
    p = stock.priceTrack()
    D = []
    while i < 100:
        data ={}
        data['price'] = p.text
        D.append(data)
        i += 1
    with open('out.json', "w") as writeJ:
        json.dump(D,writeJ)
