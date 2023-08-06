"""
pybaidu.image
百度图片爬虫接口

作者: stripe-python
更新时间: 2022.1.13

实例：
>>> from pybaidu.image import *
>>> images = BaiduImage('python', cookie='你在开发者工具中的cookie')
>>> print(images.get(10))  # 获取前10张图片
>>> images.download(10)  # 下载前10张图片
"""

import re as _re
import os as _os

import requests as _requests
from bs4 import BeautifulSoup as _soup

from pybaidu.locals import *


class BaiduImage(object):
    def __init__(self, keyword: str, cookie: str = '', encoding: str = UTF_8,
                 proxy_ip: str = None, proxy_type: str = HTTPS, parser: str = HTML_PARSER):
        """
        百度图片爬虫核心类。
        提供get函数获取图片搜索结果和download函数下载图片。
        
        :param keyword: 图片搜索关键词。
        :param cookie: 你在开发者工具中的cookie
        :param encoding: 网页编码，建议UTF-8
        :param proxy_ip: 代理IP
        :param proxy_type: 代理IP方式
        :param parser: BeautifulSoup4解析器，默认html.parser，支持html.parser、lxml、html5lib、xml、lxml-xml等
        :type keyword: str
        :type cookie: str
        :type encoding: str
        :type proxy_ip: str
        :type proxy_type: str
        :type parser: str
        """
        self.url = f'https://image.baidu.com/search/index?word={keyword}&tn=baiduimage'
        self.proxies = {proxy_type: proxy_ip}
        self.encoding = encoding
        self.parser = parser
        self._use_proxy_ip = proxy_ip is not None
        
        self.headers = {
            'User-Agent': USER_AGENT,
            'Cookie': cookie
        }
        self._request()
        
    def _request(self):
        if self._use_proxy_ip:
            self.response = _requests.get(self.url, headers=self.headers, proxies=self.proxies)
        else:
            self.response = _requests.get(self.url, headers=self.headers)
        self.response.encoding = self.encoding
        self.soup = _soup(self.response.text, self.parser)
        
    def get(self, index: int = 10):
        """
        获取图片URL列表。
        
        :param index: 获取前多少张图片
        :type index: int
        :rtype: List[str]
        :return: 图片的URL列表
        """
        url_list = _re.findall('"objURL":"(.*?)",', self.response.text, _re.I)  # 正则获取图片URL
        url_list = [i.replace('\\', '') for i in url_list]
        result = url_list[:index]
        return result
    
    def download(self, index: int = 10, save_path: str = 'images', progress_bar=False):
        """
        下载图片至本地。
        图片保存至文件夹(图片集)中。
        文件名示例:
        1.jpg
        2.jpeg
        3.png
        ...
        10.gif
        
        :param index: 下载前多少张图片
        :param save_path: 保存到的图片集路径
        :param progress_bar: 是否显示进度条
        :type index: int
        :type save_path: str
        :type progress_bar: bool
        :rtype: str
        :return: 图片集路径
        """
        if not _os.path.exists(save_path):
            _os.mkdir(save_path)
        urls = self.get(index)
        n = 1
        for src in urls:
            if progress_bar:
                print(PROGRESS_BAR, flush=True, end='')
            if self._use_proxy_ip:
                response = _requests.get(src, headers=self.headers, proxies=self.proxies)
            else:
                response = _requests.get(src, headers=self.headers)
            file_format = _re.findall('fmt=(.*)', src)[0].split('?')[0]
            file_name = _os.path.join(save_path, f'{n}.{file_format}')
            with open(file_name, 'wb') as f:
                f.write(response.content)
            n += 1
        return save_path
