import requests
from bs4 import BeautifulSoup
from bs4.element import NavigableString
from src.config.config import mingying_headers
from requests_html import HTMLSession
from hanziconv import HanziConv
from data.stopwords import stopwords
import pandas as pd
import urllib3
import time 
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

max_books = 1
max_pages = 10

#author name
atr = ""
atr_list = []
#paragraphs 
cnt_list = []
#title of chapter
title = ""
title_list = []
#novel name
name = ""
name_list = []

url = "https://www.mingyantong.com/allarticle/zhaichao"
base_url = "https://www.mingyantong.com"


html_file = requests.get(url, verify = False, headers=mingying_headers)

# print(html_file)

soup = BeautifulSoup(html_file.content, 'html.parser')

# print(soup)

book_list = soup.find_all(class_="xqallarticletilelink")
# print(book_list)

i = 0
while i < len(book_list):
    if i > max_books:
        break

    book_url = book_list[i]['href']
    print("look in to book")
    book_url = base_url+book_url
    print(book_url)

    j = 0
    while j < max_pages:
        print(j)
        if j > max_pages:
            break
        html_file = requests.get(book_url+f"?page={j}", verify = False, headers=mingying_headers)

        soup = BeautifulSoup(html_file.content, 'html.parser')
        
        print(soup)

        mingyan_list = soup.find_all(class_="xlistju")
        # print(mingyan_list)
        #store author 
        tmp_list = soup.find_all(attrs = {"class":"views-field-field-oriwriter-value", "rel":"tag"})
        tmp2_list = soup.find_all(attrs={"class":"active", "rel":"tag"})
        # print(tmp2_list)

  

        print(len(mingyan_list))
        print(len(tmp_list))
        print(len(tmp2_list))
        print(tmp_list)

        for k in range(len(mingyan_list)):
            if str(mingyan_list[k].string) == "None":
                continue
            
            cnt_list.append(HanziConv.toTraditional(str(mingyan_list[k].string)))
            atr_list.append(HanziConv.toTraditional(str(tmp_list[k].string)))
            name_list.append(HanziConv.toTraditional(str(tmp2_list[k].string)))
   
        j += 1

    i += 1
    break

for i in range(len(cnt_list)):
    print(cnt_list[i])
    print(atr_list[i])
    print(name_list[i])