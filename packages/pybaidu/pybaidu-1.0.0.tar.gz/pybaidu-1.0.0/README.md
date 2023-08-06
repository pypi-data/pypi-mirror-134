# 简介
`pybaidu`是一个通过python爬虫请求百度来获取百度信息的python第三方库。

# 安装
使用`pip`:
```shell
pip install pybaidu
```
使用`git`:
```shell
git clone https://gitcode.net/weixin_38805653/pybaidu
cd pybaidu
python setup.py install
```

# 终端
使用终端查看pybaidu信息。
```shell
python -m pybaidu
```

# 使用
```python
from pybaidu import *
BaiduImage  # 百度图片爬虫核心类
BaiduSearch  # 百度搜索爬虫核心类
BaiduKnew   # 百度知道爬虫核心类
BaiduKnewSearch  # 百度知道搜索爬虫核心类
BaiduVideo  # 百度视频搜索爬虫核心类
BaiduTranslate   # 百度翻译爬虫核心类
BaiduLibrary   # 百度文库爬虫核心类
```
具体文档请见源码中的doc-string。
