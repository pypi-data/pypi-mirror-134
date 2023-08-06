"""
pybaidu.translate
百度翻译爬虫接口

作者: stripe-python
更新时间: 2022.1.13

实例：
>>> from pybaidu.translate import *
>>> translate = BaiduTranslate('百度翻译接口', cookie='你在开发者工具中的cookie')
>>> print(translate.get())
>>> from pprint import pprint
>>> pprint(translate.data)
"""

import os as _os
import re as _re

import requests as _requests
import execjs as _execjs  # JS逆向要用到

try:
    import simplejson as _json  # simplejson比json好用
except (ModuleNotFoundError, ImportError):
    import json as _json

from pybaidu.locals import *
    
__all__ = ['LANGUAGE_DICT', 'get_language', 'BaiduTranslate']

# 语言字典
LANGUAGE_DICT = {'zh': '中文', 'jp': '日语', 'jpka': '日语假名', 'th': '泰语', 'fra': '法语', 'en': '英语', 'spa': '西班牙语',
                 'kor': '韩语', 'tr': '土耳其语', 'vie': '越南语', 'ms': '马来语', 'de': '德语', 'ru': '俄语', 'ir': '伊朗语',
                 'ara': '阿拉伯语', 'est': '爱沙尼亚语', 'be': '白俄罗斯语', 'bul': '保加利亚语', 'hi': '印地语', 'is': '冰岛语', 'pl': '波兰语',
                 'fa': '波斯语', 'dan': '丹麦语', 'tl': '菲律宾语', 'fin': '芬兰语', 'nl': '荷兰语', 'ca': '加泰罗尼亚语', 'cs': '捷克语',
                 'hr': '克罗地亚语', 'lv': '拉脱维亚语', 'lt': '立陶宛语', 'rom': '罗马尼亚语', 'af': '南非语', 'no': '挪威语', 'pt_BR': '巴西语',
                 'pt': '葡萄牙语', 'swe': '瑞典语', 'sr': '塞尔维亚语', 'eo': '世界语', 'sk': '斯洛伐克语', 'slo': '斯洛文尼亚语', 'sw': '斯瓦希里语',
                 'uk': '乌克兰语', 'iw': '希伯来语', 'el': '希腊语', 'hu': '匈牙利语', 'hy': '亚美尼亚语', 'it': '意大利语', 'id': '印尼语',
                 'sq': '阿尔巴尼亚语', 'am': '阿姆哈拉语', 'as': '阿萨姆语', 'az': '阿塞拜疆语', 'eu': '巴斯克语', 'bn': '孟加拉语', 'bs': '波斯尼亚语',
                 'gl': '加利西亚语', 'ka': '格鲁吉亚语', 'gu': '古吉拉特语', 'ha': '豪萨语', 'ig': '伊博语', 'iu': '因纽特语', 'ga': '爱尔兰语',
                 'zu': '祖鲁语', 'kn': '卡纳达语', 'kk': '哈萨克语', 'ky': '吉尔吉斯语', 'lb': '卢森堡语', 'mk': '马其顿语', 'mt': '马耳他语',
                 'mi': '毛利语', 'mr': '马拉提语', 'ne': '尼泊尔语', 'or': '奥利亚语', 'pa': '旁遮普语', 'qu': '凯楚亚语', 'tn': '塞茨瓦纳语',
                 'si': '僧加罗语', 'ta': '泰米尔语', 'tt': '塔塔尔语', 'te': '泰卢固语', 'ur': '乌尔都语', 'uz': '乌兹别克语', 'cy': '威尔士语',
                 'yo': '约鲁巴语', 'yue': '粤语', 'wyw': '文言文', 'cht': '中文繁体'}
# 语言字典逆序
LANGUAGE_DICT = {value: key for key, value in LANGUAGE_DICT.items()}


def get_language(language: str, default='zh'):
    return LANGUAGE_DICT.get(language, default)


def _get_gtk():
    """
    获得窗口GTK值，常量
    
    :rtype: str
    :return: 窗口GTK值
    """
    return '320305.131321201'


def _get_sign(word: str):
    """
    JS逆向获得sign值。
    JS来源自百度翻译的javascript代码中。
    
    :param word: 要翻译的文字
    :type word: str
    :rtype: str
    :return: sign值
    """
    gtk = _get_gtk()  # GTK值
    # 定义JS代码
    js = r'''
var t = "{{word}}"
var i = "{{gtk}}"
function a(r) {
    if (Array.isArray(r)) {
        for (var o = 0, t = Array(r.length); o < r.length; o++) t[o] = r[o];
        return t
    }
    return Array.from(r)
}
function n(r, o) {
    for (var t = 0; t < o.length - 2; t += 3) {
        var a = o.charAt(t + 2);
        a = a >= "a" ? a.charCodeAt(0) - 87 : Number(a), a = "+" === o.charAt(t + 1) ? r >>> a : r << a, r = "+" === o.charAt(t) ? r + a & 4294967295 : r ^ a
    }
    return r
}
function e(r) {
    var o = r.match(/[\uD800-\uDBFF][\uDC00-\uDFFF]/g);
    if (null === o) {
        var t = r.length;
        t > 30 && (r = "" + r.substr(0, 10) + r.substr(Math.floor(t / 2) - 5, 10) + r.substr(-10, 10))
    } else {
        for (var e = r.split(/[\uD800-\uDBFF][\uDC00-\uDFFF]/), C = 0, h = e.length, f = []; h > C; C++) "" !== e[C] && f.push.apply(f, a(e[C].split(""))), C !== h - 1 && f.push(o[C]);
        var g = f.length;
        g > 30 && (r = f.slice(0, 10).join("") + f.slice(Math.floor(g / 2) - 5, Math.floor(g / 2) + 5).join("") + f.slice(-10).join(""))
    }
    var u = void 0;
    var l = "gtk";
    var u = null !== i ? i : (i = {{gtk}} || "") || "";
    for (var d = u.split("."), m = Number(d[0]) || 0, s = Number(d[1]) || 0, S = [], c = 0, v = 0; v < r.length; v++) {
        var A = r.charCodeAt(v);
        128 > A ? S[c++] = A : (2048 > A ? S[c++] = A >> 6 | 192 : (55296 === (64512 & A) && v + 1 < r.length && 56320 === (64512 & r.charCodeAt(v + 1)) ? (A = 65536 + ((1023 & A) << 10) + (1023 & r.charCodeAt(++v)), S[c++] = A >> 18 | 240, S[c++] = A >> 12 & 63 | 128) : S[c++] = A >> 12 | 224, S[c++] = A >> 6 & 63 | 128), S[c++] = 63 & A | 128)
    }
    for (var p = m, F = "" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(97) + ("" + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(54)), D = "" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(51) + ("" + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(98)) + ("" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(102)), b = 0; b < S.length; b++) p += S[b], p = n(p, F);
    return p = n(p, D), p ^= s, 0 > p && (p = (2147483647 & p) + 2147483648), p %= 1e6, p.toString() + "." + (p ^ m)
}
    '''
    
    js = js.replace('{{word}}', word)  # 替换变量
    js = js.replace('{{gtk}}', gtk)
    
    python = _execjs.compile(js)
    sign = python.call('e', word)
    return sign


def _get_token(headers=None, encoding='utf-8', proxies=None, use=False):
    """
    从百度翻译网站获取窗口token值。
    
    :param headers: 请求头
    :param encoding: 网页编码
    :param proxies: 代理字典
    :param use: 是否使用代理IP
    :type headers: dict
    :type encoding: str
    :type proxies: dict
    :type use: bool
    :rtype: str
    :return: 窗口token值
    """
    url = 'https://fanyi.baidu.com/?aldtype=16047'
    if use:
        response = _requests.get(url, headers=headers, proxies=proxies)
    else:
        response = _requests.get(url, headers=headers)
    response.encoding = encoding
    
    html = response.text
    token = _re.findall("token: '(.*)'", html)
    if not token:
        raise _requests.exceptions.RequestException('not found token')
    token = token[0]
    return token


class BaiduTranslate(object):
    def __init__(self, text: str, input_language: str = 'zh',
                 output_language: str = 'en', cookie: str = '', js_engine: str = NODE_JS,
                 encoding: str = 'utf-8', proxy_ip: str = None, proxy_type: str = HTTPS):
        """
        百度翻译爬虫核心类。
        提供get函数获取结果和data属性。
        由于使用JS逆向，请先配置好至少一种本地Javascript环境。
        
        :param text: 要翻译的文字
        :param input_language: 输入语言简写，可以使用get_language函数获得
        :param output_language: 输出语言简写，可以使用get_language函数获得
        :param cookie: 你在开发者工具中的cookie
        :param js_engine: JS逆向所用引擎，推荐Node.JS，Windows下可以使用JScript。支持Node.JS、JScript、PyV8、JavaScriptCore、SpiderMonkey、JScript、PhantomJS、SlimerJS、Nashorn
        :param encoding: 网页编码，建议UTF-8
        :param proxy_ip: 代理IP
        :param proxy_type: 代理IP方式
        :type text: str
        :type input_language: str
        :type output_language: str
        :type cookie: str
        :type js_engine: str
        :type proxy_ip: str
        :type proxy_type: str
        """
        _os.environ['EXECJS_RUNTIME'] = js_engine  # 设置PyExecJs运行环境
        self.url = 'https://fanyi.baidu.com/v2transapi'  # 在XHR页找到的接口URL
        
        self.headers = {
            'User-Agent': USER_AGENT,
            'Cookie': cookie
        }
        self.proxies = {proxy_type: proxy_ip}
        self._use_proxy_ip = proxy_ip is not None
        self.form = {
            'from': input_language,
            'to': output_language,
            'query': text,
            'transtype': 'translang',
            'simple_means_flag': '3',
            'domain': 'common',
            'sign': _get_sign(text),
            'token': _get_token(self.headers, encoding, self.proxies, self._use_proxy_ip)
        }  # 构造form表单
        self.encoding = encoding
        self._request()
    
    def _request(self):
        if self._use_proxy_ip:
            self.response = _requests.post(self.url, data=self.form, headers=self.headers, proxies=self.proxies)
        else:
            self.response = _requests.post(self.url, data=self.form, headers=self.headers)
        self.response.encoding = self.encoding
        self.data = _json.loads(self.response.text)  # json解码
    
    def get(self):
        """
        获取翻译结果，若翻译失败，报KeyError
        
        :raises: KeyError
        :rtype: str
        :return: 翻译结果
        """
        return self.data['trans_result']['data'][0]['dst']  # 翻译结果
    
    @property
    def json(self):
        """
        获取翻译json数据
        
        :rtype: dict
        :return: 翻译json数据
        """
        return self.data
