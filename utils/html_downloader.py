# -*- coding: utf-8 -*-
'''
html_downloader.py 上面爬虫流程图中的[下载器]
负责对指定的 URL 网页内容进行下载获取，这里只是简单处理了 HTTP CODE 200，实质应该依据 400、500 等分情况进行重试等机制处理。
'''
import requests


class HtmlDownLoader(object):
    def download(self,url):
        if url is None:
            return None
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0',
        }
        response = requests.get(url, headers=headers, timeout=100)
        if response.status_code == 200:
            response.encoding='utf-8'
            return response.text
        else:
            return None