import requests
from bs4 import BeautifulSoup
from bs4.element import NavigableString
from src.config.config import mingying_headers, proxies_list, time_sleep
from requests_html import HTMLSession
from hanziconv import HanziConv
from data.stopwords import stopwords
import pandas as pd
import urllib3
import random
import opencc
converter = opencc.OpenCC('s2twp.json')

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)




max_books = 5
max_r_pages = 5
max_pages = 1

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
count_recommend_page = 0
while count_recommend_page <= max_r_pages:
        
    url = f"https://www.mingyantong.com/allarticle/zhaichao?page={count_recommend_page}"
    # url = "http://www.mingyantong.com/allarticle/zhaichao"
    base_url = "https://www.mingyantong.com"

    #freeze time 
    time_sleep()
    # html_file = requests.get(url, verify = False, headers=mingying_headers, proxies={"https":proxy})
    html_file = requests.get(url, verify = False, headers=mingying_headers())

    # print(html_file)

    soup = BeautifulSoup(html_file.content, 'html.parser')

    # print(soup)

    book_list = soup.find_all(class_="xqallarticletilelink")
    # print(book_list)  

    i = 0
    while i < len(book_list):
        # if i > max_books:
        #     break

        book_url = book_list[i]['href']
        print("look in to book")
        book_url = base_url+book_url
        print(book_url)

        j = 0
        max_pages = 1
        while j < max_pages:
            print("books pages", j)
            if j > max_pages:
                break
            print("=="*10+"waiting time"+"=="*10)
            time_sleep()    
            html_file = requests.get(book_url+f"?page={j}", verify = False, headers=mingying_headers())

            soup = BeautifulSoup(html_file.content, 'html.parser')
            
            # print(soup)
            try:
                page_last = soup.find(class_="pager-last").string
                # print("books max web's page")
                # print(page_last)
                max_pages = int(page_last)
            except:
                print("did not found maximun web's pages")
            # print(mingyan_list)
            #store author 
            tmp_list = soup.find_all(attrs = {"class":"views-field-field-oriwriter-value", "rel":"tag"})
            #store novel name
            tmp2_list = soup.find_all(attrs={"class":"active", "rel":"tag"})
            # store mingyan
            mingyan_list = soup.find_all(class_="xlistju")


            tmp3_list = soup.find_all(class_="views-field-phpcode-1")
            for k in tmp3_list:
                try:
                    atr = k.nextSibling.find(attrs = {"class":"views-field-field-oriwriter-value", "rel":"tag"}).string
                    name = k.nextSibling.find(attrs = {"class":"active", "rel":"tag"}).string
                    cnt = k.find(class_="xlistju").string
                    atr = converter.convert(str(atr))
                    name = converter.convert(str(name))
                    cnt = converter.convert(str(cnt))
                    print("atr:", atr)
                    print("name: ", name)
                    print("paragraphs:", cnt)
                    if atr == "None":
                        print("atr is None")
                        atr = None
                    if name == "None":
                        print("name is None")
                        name = None
                    if cnt == "None":
                        print("cnt is None")
                        continue
                        cnt = None
                    cnt_list.append(cnt)
                    atr_list.append(atr)
                    name_list.append(name)
                    
                except Exception:
                    continue

            # print(len(mingyan_list))
            # print(len(tmp_list))
            # print(len(tmp2_list))
            # print(tmp_list)

            # for k in range(len(mingyan_list)):
            #     if str(mingyan_list[k].string) == "None":
            #         continue
                
            #     cnt_list.append(HanziConv.toTraditional(str(mingyan_list[k].string)))
            #     atr_list.append(HanziConv.toTraditional(str(tmp_list[k].string)))
            #     name_list.append(HanziConv.toTraditional(str(tmp2_list[k].string)))
    
            j += 1
            #save the checkpoint
            pd_minyan = pd.DataFrame({"paragraphs": cnt_list, "name":name_list,
                            "author":atr_list})
            pd_minyan.to_csv("mingyan_cc.csv")
        #next book
        i += 1
    count_recommend_page += 1

# for i in range(len(cnt_list)):
#     print(cnt_list[i])
#     print(atr_list[i])
#     print(name_list[i])


