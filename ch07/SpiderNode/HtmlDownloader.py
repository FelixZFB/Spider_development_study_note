# coding: utf-8

# 网页下载器，下载获得网页的全部内容

import requests

class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None
        # 设置用户代理，伪装成浏览器访问
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0'
        headers = {'User-Agent': user_agent}
        # 请求获取网址
        r = requests.get(url, headers=headers)
        r.encoding = 'utf-8' # 解决中文乱码的问题
        if r.status_code == 200:
            r.encoding = 'utf-8'
            return r.text
        return None


