# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

url = 'https://bj.zu.anjuke.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0',
}
response = requests.get(url, headers=headers)
if response.status_code == 200:
    response.encoding = 'utf-8'
    content = response.text
soup = BeautifulSoup(content, 'lxml')
city_list = soup.find_all('dd')
names = []
urls = []
for city in city_list:
    for k in city.find_all('a'):
        url = k['href']
        name = k.string
        i =2
        urls.append(url+'/p'+str(i)+'/')
        names.append(name)
print(urls)
print(names)