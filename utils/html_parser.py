# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup


class HtmlParser(object):

    def _get_new_data(self, content):
        soup = BeautifulSoup(content, 'lxml')
        house_list = soup.find_all('div', class_="zu-itemmod")
        return house_list
