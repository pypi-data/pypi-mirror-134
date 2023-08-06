"""
pybaidu.translate
百度搜索爬虫接口

作者: stripe-python
更新时间: 2022.1.13

实例：
>>> from pybaidu.search import *
>>> search = BaiduSearch('python', cookie='你在开发者工具中的cookie')
>>> print(search.get())
"""

import requests as _requests
from bs4 import BeautifulSoup as _soup

from pybaidu.locals import *

__all__ = ['BaiduSearch']


class BaiduSearch(object):
    def __init__(self, keyword: str, page: int = 1, cookie: str = '', encoding: str = 'utf-8',
                 parser: str = 'html.parser', proxy_ip: str = None, proxy_type: str = HTTPS):
        """
        百度搜索爬虫核心类。
        提供get函数获取搜索结果。
        
        :param keyword: 搜索关键词
        :param page: 搜索页面页码
        :param cookie: 你在开发者工具中的cookie
        :param encoding: 网页编码，建议UTF-8
        :param parser: BeautifulSoup4解析器，默认html.parser，支持html.parser、lxml、html5lib、xml、lxml-xml等
        :param proxy_ip: 代理IP
        :param proxy_type: 代理IP方式
        :type keyword: str
        :type page: int
        :type cookie: str
        :type encoding: str
        :type parser: str
        :type proxy_ip: str
        :type proxy_type: str
        """
        page = (page - 1) * 10 if page != 1 else 1  # 页码运算公式
        self.url = f'https://www.baidu.com/s?wd={keyword}&lm=1&pn={page}'  # 构造URL
        self.encoding = encoding
        self.headers = {
            'User-Agent': USER_AGENT,
            'Host': 'www.baidu.com',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Cookie': cookie
        }
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
        self.soup = _soup(self.response.text, self.parser)  # 创建BeautifulSoup4解析对象
        
    def get(self, progress_bar=False):
        """
        获取百度搜索结果。
        
        :param progress_bar: 是否显示进度条。
        :type progress_bar: bool
        :rtype: List[str]
        :return: 搜索结果
        """
        content_left = self.soup.find('div', id='content_left')
        div_list = content_left.find_all('div')
        result = []
        
        for div in div_list:
            if progress_bar:
                print(PROGRESS_BAR, end='', flush=True)
                
            a_content = div.find('a')
            if not a_content:
                continue
                
            try:
                url = a_content['href']
            except KeyError:
                continue
                
            try:
                response = _requests.get(url, headers=self.headers)
                url = response.url
            except (Exception, SystemExit):
                pass
            if url == 'javascript:;':  # 过滤js弹窗url
                continue
                
            result.append(url)
        return result
