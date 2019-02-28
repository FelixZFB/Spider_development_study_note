# coding: utf-8

# HTML解析器，提取网页中需要的URL和需要的数据
# 网页图片及原始代码，以及网页解析提取参考67_7_1

import re
from urllib.parse import urljoin
from bs4 import BeautifulSoup

class HtmlParser(object):

    def parser(self, page_url, html_cont):
        '''
        用于解析网页内容，抽取URL和数据
        参数page_url:下载下面的URL
        参数html_cont: 下载的网页内容
        return: 返回URL和数据
        '''
        if page_url is None or html_cont is None:
            return
        # 创建一个BS的实例
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8') # 采用html.parser解析
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        '''
        获取新的URL集合
        参数page_url:下载页面的URL
        参数soup：上面的BS创建的BS实例
        返回新的URL集合
        '''
        new_urls = set()
        # 提取符合要求的a标记,提取的是a标签全部内容的一个列表
        # 提取词条概要中相关的部分词条，挑取其中几个，选定一个规则
        links = soup.find_all('a', href=re.compile(r'/item/%E8%9'))
        for link in links:
            # 提取href的属性，既URL地址
            new_url = link['href']
            # 拼接成完整的网址，目前的页面URL和提取得到的新的URL进行合并
            new_full_url = urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        '''
        抽取有效数据
        :param page_url: 下载页面的URL
        :param soup: 上面创建的BS实例
        :return: 返回有效的数据
        '''
        data = {}
        data['url'] = page_url
        title = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        data['title'] = title.get_text() # 获取标签中的内容
        summary = soup.find('div', class_='lemma-summary')
        data['summary'] = summary.get_text()

        return data















