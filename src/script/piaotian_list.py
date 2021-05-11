import requests
from bs4 import BeautifulSoup
from bs4.element import NavigableString
from src.config.config import linux_headers
from requests_html import HTMLSession
from hanziconv import HanziConv
from data.stopwords import stopwords
import pandas as pd
import urllib3
import time 
import opencc
converter = opencc.OpenCC('s2twp.json')

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
url = "https://www.ptwxz.com/booktopallvote/0/1.html"
base_url = "https://www.ptwxz.com/"
max_page = 5
max_rpage = 10

count_recommend_page = 1

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

while count_recommend_page < max_rpage:
    print("recommend page number", count_recommend_page)
    print("testing", f"https://www.ptwxz.com/booktopallvote/0/{count_recommend_page}.html")
    #get the recommended list
    html_file = requests.get(f"https://www.ptwxz.com/booktopallvote/0/{count_recommend_page}.html", verify = False, headers=linux_headers)

    # print(html_file)

    soup = BeautifulSoup(html_file.content, 'html.parser')

    # print(soup)

    #link of recommended list
    objhref = soup.find_all('td', class_="odd")

    # print(objhref)

    intro = []
    for i in objhref:
        try:
            # print(i.a['href'])
            intro.append(i.a['href'])        
        except:
            # print()
            pass



    print("=="*10+"intro"+"=="*10)
    #loop the book intro
    i = 0
    while i < len(intro):
        print(i+(count_recommend_page-1)*30)
        html_file = requests.get(base_url+intro[i], verify = False, headers=linux_headers)

        soup = BeautifulSoup(html_file.content, 'html.parser')
        
        #get in to the table of contents
        # print(soup)

        intro_href = soup.find_all('caption')

        #find 查看目錄
        print("查看目錄")
        tmp = intro_href[0].a['href']
        print(tmp)

        if "https" in tmp:
            table_url = tmp
        else:
            table_url = base_url+tmp

        #cut the index.html since there is two type of url 
        if "index.html" in table_url:
            table_url = table_url.split("index.html")[0]

        #get in to the table of novel
        html_file = requests.get(table_url, verify = False, headers=linux_headers)

        soup = BeautifulSoup(html_file.content, 'html.parser')

        
        # print(soup)

        table_soup = soup.find_all('li')
        
        name_soup = soup.find("div",class_="list")
        # print(name_soup.contents[0])
        try:
        #find author name
            atr = converter.convert(str(name_soup.contents[0][3:]))
        except:
            i -= 1
        #get the list of novel's chapter
        # print(table_soup)

        #chapter name
        cpt_list = []
        tmp_list = []

        count_page = 0
        for j in table_soup:
            count_page += 1
            if count_page > max_page:
                break

            #the novel content url
            try:
                tmp = j.a['href']
            except:
                count_page -= 1
                continue
            if tmp == "" or tmp == None:
                count_page -= 1
                continue
            
            # print(tmp)

            cpt_list.append(tmp)
            
            # title_list.append(HanziConv.toTraditional(str(i.string)))
            tmp_list.append(converter.convert(str(j.string)))

        #content of novel
        for j, k in zip(cpt_list, tmp_list):
            html_file = requests.get(table_url+j, verify = False, headers=linux_headers)
            print("novel content link")
            print(table_url+j)
            html_file.encoding = "gbk"
            html_traditional = converter.convert(html_file.text)
            soup = BeautifulSoup(html_traditional, 'html.parser')

            h1_name = soup.find("h1")
            print(h1_name)          
            name = str(h1_name.a.string)
            title = k
    
            cnt = soup.find_all('br')

            # tmp = str(cnt[1]).split("<br><br/>")

            # print(tmp)

            for l in cnt:
                if l.nextSibling in stopwords:
                    continue
                if type(l.nextSibling) != NavigableString:
                    continue
                # print("split line")
                # print(i.nextSibling)
                # print(str(i.nextSibling))
                cnt_list.append(str(l.nextSibling))
                atr_list.append(atr)
                title_list.append(title)
                name_list.append(name)
        
        i += 1
        print("end cnt index", len(cnt_list))

    count_recommend_page += 1

pd_novel = pd.DataFrame({"paragraphs": cnt_list, "name":name_list,
                 "author":atr_list, "title":title_list})
pd_novel.to_csv("novel_cc.csv")