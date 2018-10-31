# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


class ChoosePlace(object):
    def choose_city(self, cname, url):
        if url is None:
            return None
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0',
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            response.encoding='utf-8'
            content = response.text
        soup = BeautifulSoup(content, 'lxml')
        city_list = soup.find_all('dd')
        names = []
        urls = []
        for city in city_list:
            for k in city.find_all('a'):
                url = k['href']
                name = k.string
                urls.append(url)
                names.append(name)
        # print(urls)
        # print(names)
        if cname in names:
            cindex = names.index(cname)
        return urls[cindex]

    def choose_province(self, url):
        if url is None:
            return None
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0',
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            response.encoding='utf-8'
            content = response.text
        soup = BeautifulSoup(content, 'lxml')
        text = soup.find('label', id="province")
        return text
