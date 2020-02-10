
import requests
from bs4 import BeautifulSoup 
import logging
'''
url = "https://www.ptt.cc/bbs/Gossiping/index.html"
r = requests.get('https://www.ptt.cc/bbs/Gossiping/index.html', headers = { 
    "cookie" : "over18=1",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    })

#print(r.content.decode())

objsoup = BeautifulSoup(r.text, 'html.parser')
objhref = objsoup.find_all('div', class_="title")
for i in objhref:
    print(i.a.string)
#print(objsoup)
for i in range(5):
    objbefore = objsoup.find("a", string = "‹ 上頁")
    
    newurl = "https://www.ptt.cc" + objbefore['href']
    print(newurl)
    r = requests.get(newurl, headers = { 
    "cookie" : "over18=1",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    })
    objsoup = BeautifulSoup(r.text, 'html.parser')
    objhref = objsoup.find_all('div', class_="title")
    for i in objhref:
        try:
            print(i.a.string)
        except AttributeError:
            logging.debug("a isn't in the content")

'''
class Ptt():
    url = ""
    #objsoup = BeautifulSoup()
    
    def __init__(self, url):
        self.url = url
    
    def find_title(self, url):
        r = requests.get( url , headers = { 
            "cookie" : "over18=1",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
            })
        objsoup = BeautifulSoup(r.text, 'html.parser')
        objhref = objsoup.find_all('div', class_="title")
        for i in objhref:
            try:
                print(i.a.string)
            except AttributeError:
                logging.debug("a isn't in the content")

    def privious_page(self):
        objbefore = objsoup.find("a", string = "‹ 上頁")
        newurl = "https://www.ptt.cc/" + objbefore['href']
        #print(newurl)
        return newurl