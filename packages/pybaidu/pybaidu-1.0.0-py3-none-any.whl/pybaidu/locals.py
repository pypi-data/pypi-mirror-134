"""
pybaidu.locals
百度爬虫常用常量收集

作者: stripe-python
更新时间: 2022.1.13
"""

PROGRESS_BAR = '█'  # 进度条文字

# 各种代理IP类型
HTTP = 'http'
HTTPS = 'https'
SOCKS = 'socks'

USER_AGENT = (
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/68.0.3440.106 Safari/537.36'
)  # User-Agent，默认Chrome

# 各种JS逆向引擎
NODE = NODE_JS = 'Node'
PYV8 = 'PyV8'
JAVA_SCRIPT_CORE = 'JavaScriptCore'
SPIDERMONKEY = SPIDER_MONKEY = 'SpiderMonkey'
JSCRIPT = 'JScript'
PHANTOM_JS = PHANTOMJS = 'PhantomJS'
SLIMERJS = 'SlimerJS'
NASHORN = 'Nashorn'

# 各种编码
CP936 = CP_936 = 'cp936'
UTF_8 = UTF8 = 'utf-8'
UTF_16 = UTF16 = 'utf-16'
UTF_32 = UTF32 = 'utf-32'
USC_2 = USC2 = 'usc-2'
USC_4 = USC4 = 'usc-4'
UTF_16_BE = UTF16BE = 'uft-16-BE'
UTF_16_LE = UTF16LE = 'uft-16-LE'
ASCII = ANSI = 'ansi'
LATIN_1 = LATIN1 = 'Latin-1'
GBK = 'gbk'
GB2312 = GB_2312 = 'gb2312'
GB18030 = GB_18030 = 'gb18030'
ISO = ISO_8859_1 = 'ISO-8859-1'

# 各种BeautifulSoup4解析器
HTML_PARSER = DEFAULT_PARSER = 'html.parser'
XML = XML_PARSER = 'xml'
LXML = LXML_PARSER = 'lxml'
LXML_XML = LXML_XML_PARSER = 'lxml-xml'
HTML5LIB = HTML5LIB_PARSER = 'html5lib'

# 默认PPT图片尺寸(单位：厘米)
PPT_WIDTH = 25.4
PPT_HEIGHT = 19.05

# 各种文本文件写入方式
W = W_MODE = 'w'
A = A_MODE = 'a'
W_NEW = W_NEW_MODE = 'w+'
