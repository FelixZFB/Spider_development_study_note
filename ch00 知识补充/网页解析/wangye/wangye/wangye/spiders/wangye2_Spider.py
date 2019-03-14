# Scrapy爬虫中也可以采用BS4解析
# BS4和正则配合使用，解析网页快很准
# 该案例用于解析福利网站，sht国产原创，典型的博文结构，两层结构
# 第一层解析：找出该页面所有的文章的URL和标题
# 第二层解析：打开一个第一层解析得到的URL地址，得到里面的图片地址和magnet的值

import scrapy
import re
import requests
from urllib.parse import urljoin
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from bs4 import BeautifulSoup

class Wangye2Spider(scrapy.Spider):
    name = 'wangye2'
    allowed_domains = ['dsndsht23.com']
    start_urls = ['https://www.dsndsht23.com/forum-2-1.html']

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser', from_encoding='utf-8')
        papers = soup.find_all('a', class_="s xst", href=re.compile(r'thread-.*'))
        for paper in papers:
            url = paper['href']
            # 解析出来的url和检查网页源代码看到的url有所变化，需要拼接上网站主域名
            # 可以用urljoin函数拼接，也直接可以用字符串相加拼接
            # full_url = 'https://www.dsndsht23.com/' + url
            page_url = 'https://www.dsndsht23.com/'
            full_url = urljoin(page_url, url)
            # full_url = 'https://www.dsndsht23.com/' + url
            title = paper.get_text()
            print(full_url, title)

        # 查找是否有下一页的标签，标签class属性唯一，很好找
        next_page = soup.find('a', class_="nxt")
        next_page_url = 'https://www.dsndsht23.com/' + next_page['href']
        print(next_page_url)


        # 解析一个具体的网址，找到图片的连接和里面种子的文字，查看网址的规律都是一样的，同一个后端规律基本都相同
        # 种子有个地址可以直接下载，但是找到的地址需要处理才能下载，所以直接提取magnet的值
        new_url = 'https://www.dsndsht23.com/thread-87158-1-10.html'
        response = requests.get(new_url)
        soup = BeautifulSoup(response.text, 'html.parser', from_encoding='utf-8')
        # 将网页打印出来，分析提取图片连接的地址，如果直接查看上面网页源代码，图片地址连接是另外一个地址
        # 并且那个地址还需要拼接域名才是完整的地址
        # 源代码里面有个class="zoom"，里面有个file的属性就是图片真实地址
        # 打印出来找到图片地址和种子的地址
        # print(soup)
        # 该处标签唯一，直接使用find查找即可，find_all查找结果虽然只有一个，但是是一个列表类型
        # 需要循环取出标签之后，才能使用类似字典取键对应值的操作
        image_url = soup.find('img', class_='zoom')
        magnet = soup.find('div', class_='blockcode').find('li')
        print(image_url['file'])
        print(magnet)
        # 提取li标签下的文字,下面两种方法都可以
        # magnet_url = magnet.get_text()
        magnet_url = magnet.string
        print(magnet_url)



if __name__ == '__main__':
    process = CrawlerProcess(get_project_settings())
    process.crawl('wangye2')
    process.start()

