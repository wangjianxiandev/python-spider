# -*- coding: utf-8 -*-
'''
url_manager.py 上面爬虫流程图中的[URL 管理器]
负责管理深度 URL 链接和去重等机制。
'''
class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.used_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    def new_url_size(self):
        return len(self.new_urls)

    def old_url_size(self):
        return len(self.used_urls)