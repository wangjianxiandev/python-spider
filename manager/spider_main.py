# -*- coding: utf-8 -*-
'''
spider_main.py 上面爬虫流程图中的[调度器]
面向对象写法，调度器负责循环从 UrlManager 获取爬取链接，然后交给 HtmlDownLoader 下载，然后把下载内容交给 HtmlParser 解析，然后把有价值数据输出给 HtmlOutput 进行应用。
'''
from Spider.manager import manager
from Spider.utils.choose_place import ChoosePlace
from Spider.utils.analysis import Analysis
from Spider.utils.url_manager import UrlManager
from Spider.utils.html_output import HtmlOutput
from Spider.utils.html_downloader import HtmlDownLoader
from Spider.utils.html_parser import HtmlParser


class SpiderMain(object):
    def __init__(self):
        self.urls = UrlManager()
        self.downloader = HtmlDownLoader()
        self.parser = HtmlParser()
        self.output = HtmlOutput()

    def craw(self, root_url, file_path):
        csvtext = self.downloader.download(root_url)
        # print(csvtext)
        house_list = self.parser._get_new_data(csvtext)
        print(house_list)
        self.output.output_csv(file_path, house_list)


if __name__ == '__main__':
    rootUrl ='https://bj.zu.anjuke.com'
    objSpider = SpiderMain()
    choose = ChoosePlace()
    city_name = input("请输入地名：")
    startpage = int(input("请输入爬取起始页："))
    endpage = int(input("请输入爬取结束页："))
    place_url = choose.choose_city(city_name,  rootUrl)
    file_path = 'D:\\JetBrains\\Projects\\kaiyuan\\Spider\\csvfile\\'+city_name+'.csv'
    for i in range(startpage, endpage+1):
        manager.run(place_url + '/p' + str(i) + '/', file_path)
    analysis = Analysis()
    analysis.jsonfenxi(city_name)