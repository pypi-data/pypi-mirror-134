"""
pybaidu
百度系列产品爬虫接口

作者: stripe-python
更新时间: 2022.1.13
注释: 中文

>>> import pybaidu
"""

from pybaidu.library import BaiduLibrary, BaiduWenKu
from pybaidu.translate import BaiduTranslate, get_language, LANGUAGE_DICT as languages
from pybaidu.video import BaiduVideo
from pybaidu.search import BaiduSearch
from pybaidu.image import BaiduImage
from pybaidu.knew import BaiduKnew, BaiduKnewSearch

name = 'pybaidu'

__version__ = '1.0.0'  # 版本
__all__ = ['BaiduLibrary', 'BaiduWenKu', 'BaiduTranslate', 'get_language', 'languages',
           'BaiduVideo', 'BaiduSearch', 'BaiduImage', 'BaiduKnew', 'BaiduKnewSearch',
           'name', '__version__']
