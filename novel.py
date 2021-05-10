import requests
from bs4 import BeautifulSoup
import logging
from hanziconv import HanziConv
from module.ptt import Ptt
from module.wenku8 import wenku8
#from module.ptt import good
from module.piaotian import piaotian
import warnings
from urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)


import ssl
ssl._create_default_https_context = ssl._create_unverified_context

logging.basicConfig(level=logging.CRITICAL, format='')


'''
test = Ptt("https://www.ptt.cc/bbs/Gossiping/index.html")
test.find_title("https://www.ptt.cc/bbs/Gossiping/index.html")

for i in range(5):
    newurl = test.privious_page()
    test.find_title(newurl)

'''

test2 = piaotian()
test2.read("https://www.wenku8.net/modules/article/reader.php?aid=2111&cid=76180")


# test3 = wenku8()
# test3.read("https://www.wenku8.net/novel/2/2111/76180.htm")

# for i in range(3):
    
#     newurl = test3.nextpage("https://www.wenku8.net/novel/2/2111")
#     #print(newurl)
#     test3.read(newurl)