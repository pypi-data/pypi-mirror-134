from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pybaidu',
    version='1.0.0',
    packages=['pybaidu'],
    author='stripe-python',
    author_email='13513519246@139.com',
    maintainer='stripe-python',
    maintainer_email='13513519246@139.com',
    description='pybaidu是一个通过python爬虫请求百度来获取百度信息的python第三方库。',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://gitcode.net/weixin_38805653/pybaidu',
    install_requires=['requests', 'beautifulsoup4', 'python-pptx', 'PyExecJS'],
    download_url='https://gitcode.net/weixin_38805653/pybaidu'
)
