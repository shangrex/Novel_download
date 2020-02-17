import requests
from bs4 import BeautifulSoup
import logging

class wenku8():
    
    def read(self, url):
        self.url = url
        html = requests.get(url)
    
        objsoup = BeautifulSoup(html.content, 'html.parser')
        logging.debug("find br")
        
        objdiv = objsoup.find_all("div", id = "content")
        newobjsoup = BeautifulSoup(objdiv[0].encode())
        for i in newobjsoup.find_all('br'):
            print(i.nextSibling)
        
    def nextpage(self, url):
        logging.debug("next page")
        html = requests.get(self.url)
        objsoup = BeautifulSoup(html.content, 'html.parser')
        print(objsoup)
        for i in objsoup.find_all('a', string = "上一页"):
            return url + '/' + i.find_next_sibling('a').get('href')
