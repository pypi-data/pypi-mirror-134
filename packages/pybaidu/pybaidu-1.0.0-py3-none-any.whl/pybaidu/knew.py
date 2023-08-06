"""
pybaidu.knew
百度知道爬虫接口

作者: stripe-python
更新时间: 2022.1.13
测试中发现有BUG，请谨慎使用。

实例1(百度知道搜索)：
>>> from pybaidu.knew import *
>>> search = BaiduKnewSearch('python', cookie='你在开发者工具中的cookie')
>>> print(search.get())

实例2(百度知道文字信息):
>>> from pybaidu.knew import *
>>> # URL来源于网络
>>> know = BaiduKnew('https://zhidao.baidu.com/question/1967252270711756540.html?fr=iks&word=python&ie=gbk&dyTabStr=MCw2LDQsNSwzLDEsNyw4LDIsOQ==', cookie='你在开发者工具中的cookie')
>>> print(know.get())
"""
from warnings import warn as _warn  # 警告用户本库有BUG

import requests as _requests
from bs4 import BeautifulSoup as _soup

from pybaidu.locals import *

__all__ = ['BaiduKnew', 'BaiduKnewSearch']


def _warn_bug():
    msg = 'A bug is found during the test, please use it with caution.'
    _warn(msg)


class BaiduKnewSearch(object):
    def __init__(self, keyword: str, page: int = 1, cookie: str = '', encoding: str = GBK,
                 parser: str = HTML_PARSER, proxy_ip: str = None, proxy_type: str = HTTPS):
        """
        百度知道搜索爬虫核心类。
        提供get函数获取结果和answers函数获取每个页面的答案。
        不会有广告的URL。
        
        :param keyword: 搜索关键字
        :param page: 搜索页面页码
        :param cookie: 你在开发者工具中的cookie
        :param encoding: 网页编码，建议GBK
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
        _warn_bug()
        page = (page - 1) * 10 if page != 1 else 1
        self.url = f'https://zhidao.baidu.com/search?lm=0&pn={page}&word={keyword}'
        self.encoding = encoding
        self.parser = parser
        self.headers = {
            'User-Agent': USER_AGENT,
            'Cookie': cookie
        }
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
        获取百度知道搜索结果。
        
        :rtype: Dict[str, str]
        :return: 搜索结果
        """
        section = self.soup.find('section', id='page-main')
        div = section.find('div', attrs={'class': 'list-wraper'})
        dl_list = div.find_all('dl', attrs={'class': 'dl'})
        result = {}
        for dl in dl_list:
            a = dl.find('dt').find('a')
            url = a.get('href', a.get('data-href'))
            title = a.get_text()
            result[title] = url
        return result
    
    def answers(self, progress_bar=False, ignore_errors=True):
        """
        通过BaiduKnew类获取每个页面的答案。
        测试中发现有BUG，请谨慎使用。
        
        :param progress_bar: 显示进度条
        :param ignore_errors: 是否忽略错误
        :type progress_bar: bool
        :type ignore_errors: bool
        :rtype: List[str]
        :return: 每个页面的答案
        """
        result = []
        for url in self.get().values():
            if progress_bar:
                print(PROGRESS_BAR, end='', flush=True)
            bk = BaiduKnew(url, cookie=self.headers['Cookie'], encoding=self.encoding,
                           parser=self.parser, proxy_ip=list(self.proxies.values())[0],
                           proxy_type=list(self.proxies.keys())[0])
            try:
                text = bk.get()
            except (Exception, SystemExit) as error:
                if not ignore_errors:
                    raise error
                continue
            result.append(text)
        return result
    
    
class BaiduKnew(object):
    def __init__(self, url: str, cookie: str = '', encoding: str = GBK,
                 parser: str = HTML_PARSER, proxy_ip: str = None, proxy_type: str = HTTPS):
        """
        百度知道爬虫核心类。
        提供get函数获取最好回答。
        测试中发现有BUG，请谨慎使用。
        
        :param url: 网页URL
        :param cookie: 你在开发者工具中的cookie
        :param encoding: 网页编码，建议GBK
        :param parser:
        :param proxy_ip:
        :param proxy_type:
        """
        _warn_bug()
        self.url = url
        self.encoding = encoding
        self.parser = parser
        self.headers = {
            'User-Agent': USER_AGENT,
            'Cookie': cookie
        }
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
        article = self.soup.find('article')
        best = article.find('div', id='wgt-best')
        
        div = best.find('div', attrs={'class': 'bd answer'})
        div = div.find('div', attrs={'class': 'line content'}).find('div')
        result = div.get_text().replace('\u5c55\u5f00\u5168\u90e8', '')\
            .replace('\n\n\n\n\n\n', '').replace('\ufffc', '')
        
        return result
