import requests
from bs4 import BeautifulSoup
import logging
from hanziconv import HanziConv

logging.basicConfig(level=logging.DEBUG, format='')


url = input()
l = []
for i in range(10):
    logging.debug(url)
    
    html_file = requests.get(url)
    #logging.debug(html_file.encoding)

    html_file.encoding = "gb2312"

    if html_file.status_code == requests.codes.ok:
        logging.debug("success to get the web content")
    else:
        logging.debug("disable to access the web")
    html_traditional = HanziConv.toTraditional(html_file.text)

    soup = BeautifulSoup(html_traditional, 'html.parser')
    content = soup.find_all('br')

    with open("file_name.txt", "a") as file:
        for data in content:
            #logging.debug(data.text)
            file.write(data.text)
    file.close()
    
    l = url.split("/")
    num = l[6].split(".")
    tmp = str(int(num[0])+1) + '.' +  num[1]
    url = url.replace(num[0]+'.'+num[1], tmp)
    



