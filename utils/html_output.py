# -*- coding: utf-8 -*-
'''
html_output.py 上面爬虫流程图中的[应用器]
负责对解析后的数据应用，这里简单用一个 WEB 页面把爬取的所有存在在 datas 列表的数据以 Table 输出。
'''
import csv


class HtmlOutput(object):

    def output_csv(self, file_path, house_list):
        with open(file_path, 'a+', encoding='UTF-8', newline='') as f:
            w = csv.writer(f)
            for house in house_list:
                temp = []
                name = house.find('div', class_="zu-info").a['title']
                price = house.find('div', class_='zu-side').text.strip()
                address = house.find('address', class_='details-item').a.text.strip()
                house_url = house.find('div', class_="zu-info").a['href']
                temp = [name, address, price, house_url]
                # print(temp)
                # 写入表格（test.csv）
                w.writerow(temp)

