"""
pybaidu.translate
百度视频搜索爬虫接口

作者: stripe-python
更新时间: 2022.1.13

实例：
>>> from pybaidu.video import *
>>> video = BaiduVideo('百度翻译接口', cookie='你在开发者工具中的cookie')
>>> print(video.get())
"""

import requests as _requests
from bs4 import BeautifulSoup as _soup

from pybaidu.locals import *

__all__ = ['BaiduVideo']


class BaiduVideo(object):
    def __init__(self, keyword: str, cookie: str = '', encoding: str = UTF_8, parser=HTML_PARSER,
                 proxy_ip: str = None, proxy_type: str = HTTPS):
        """
        百度视频搜索爬虫核心类。
        提供get函数获取搜索结果。
        
        :param keyword: 搜索关键词
        :param cookie: 你在开发者工具中的cookie
        :param encoding: 网页编码，建议UTF-8
        :param parser: BeautifulSoup4解析器，默认html.parser，支持html.parser、lxml、html5lib、xml、lxml-xml等
        :param proxy_ip: 代理IP
        :param proxy_type: 代理IP方式
        :type keyword: str
        :type cookie: str
        :type encoding: str
        :type parser: str
        :type proxy_ip: str
        :type proxy_type: str
        """
        self.url = f'https://www.baidu.com/sf/vsearch?pd=video&tn=vsearch&ie=utf-8&wd={keyword}'
        self.headers = {
            'User-Agent': USER_AGENT,
            'Cookie': cookie
        }
        self.encoding = encoding
        self.parser = parser
        self.proxies = {proxy_type: proxy_ip}
        self._use_proxy_ip = proxy_ip is not None
        self._request()
    
    def _request(self):
        if self._use_proxy_ip:
            self.response = _requests.get(self.url, headers=self.headers, proxies=self.proxies)
        else:
            self.response = _requests.get(self.url, headers=self.headers)
        self.response.encoding = self.encoding
        self.soup = _soup(self.response.text, self.parser)
    
    def get(self):
        """
        获取视频搜索结果。

        :rtype: Dict[str, str]
        :return: 搜索结果
        """
        a_list = self.soup.find_all('a', attrs={'class': 'video-title c-link'})
        result = {}
        for a in a_list:
            url = a['href']
            title = a.get_text()
            title = title.replace('\n', '').replace('\t', '')
            title = title.strip()
            result[title] = url
        return result
