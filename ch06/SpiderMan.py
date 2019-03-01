# coding: utf-8

# 爬虫调度器，管理下载器、解析器、URL管理器、数据存储器

# 首先导入所有的模块
from ch06.DataOutput import DataOutput
from ch06.HtmlDownloader import HtmlDownloader
from ch06.HtmlParser import HtmlParser
from ch06.URLManager import UrlManager

class SpiderMan(object):

    # 初始化属性
    def __init__(self):
        self.manager = UrlManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = DataOutput()

    # 定义一个方法传入初始URL
    def crawl(self, root_url):
        # 添加入口的URL，让爬虫开始工作
        self.manager.add_new_url(root_url)
        # 判断url管理器中是否有新的url,同时判断抓取了多少个url
        while(self.manager.has_new_url() and self.manager.old_url_size()<50):
            try:
                # 从url管理器中获取新的url
                new_url = self.manager.get_new_url()
                # HTML下载器下载网页
                html = self.downloader.download(new_url)
                # HTML解析器提取网页数据，获取数据和新的url
                new_urls, data = self.parser.parser(new_url, html)
                # 将提取的新的url添加到URL管理器中
                self.manager.add_new_urls(new_urls)
                # 数据存储器存储文件
                self.output.store_data(data)
                print("已经抓取%s个链接" % self.manager.old_url_size())
            except Exception:
                print("crawl failed")

        # 数据存储器将文件输出成指定的格式
        self.output.output_html()

if __name__ == '__main__':
    # 创建一个爬虫实例
    spider_man = SpiderMan()
    # 创建初始url
    first_url = 'https://baike.baidu.com/item/网络爬虫/5162711'
    # 执行爬虫程序
    spider_man.crawl(first_url)
