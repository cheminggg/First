from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import time



baseUrl = 'https://www.instagram.com/'
plusUrl = input ('qidirish : ')
url = baseUrl + quote_plus(plusUrl)

driver = webdriver.Chrome()
driver.get(url)

time.sleep(3)

html = driver.page_source
soup = BeautifulSoup(html)

rasm = soup.select('.v1Nh3.kIKUG._bz0w')

n = 1

for i in rasm:
     print('https://www.instagram.com' + i.a['href'])
     imgUrl = i.select_one('.KL4Bh').img['src']
     with urlopen(imgUrl) as f:
         with open('./img/' + plusUrl + str(n) + '.jpg', 'wb') as h:
            img = f.read()
            h.write(img)
     n += 1
     print(imgUrl)
     print() 

driver.close()

