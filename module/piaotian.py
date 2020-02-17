import requests
from bs4 import BeautifulSoup
import logging



'''
from urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)
'''
'''
url = input()
n = int(input())
l = []
for i in range(n):
    logging.debug(url)
    
    html_file = requests.get(url)
    logging.debug(html_file.encoding)

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
            logging.debug(data.text)
            file.write(data.text)
    file.close()
    
    l = url.split("/")
    num = l[6].split(".")
    tmp = str(int(num[0])+1) + '.' +  num[1]
    url = url.replace(num[0]+'.'+num[1], tmp)
'''

class piaotian():
    def read(self, url):
        
        html_file = requests.get(url, verify = False, headers = {
            "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
        })
        
        #html_file = requests.get(url)
        logging.debug(html_file.encoding)

        #html_file.encoding = "gb2312"

        if html_file.status_code == requests.codes.ok:
            logging.debug("success to get the web content")
        else:
            logging.debug("disable to access the web")

        #html_traditional = HanziConv.toTraditional(html_file.text)

        soup = BeautifulSoup(html_file, 'html.parser')
        content = soup.find_all('br')

        print(content)
        
    
        #write file
        '''
        with open("file_name.txt", "a") as file:
            for data in content:
                logging.debug(data.text)
                file.write(data.text)
        file.close()
        '''