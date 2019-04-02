# coding: utf-8
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class CnblogsSpider(scrapy.Spider):
    # 爬虫的名称，唯一的，最好不要文件、文件夹名称重复，以免混淆
    name = 'cnblogss'
    # 允许的域名
    allowed_domains = ['cnblogs.com']
    # 入口URL列表，爬虫启动的接口
    start_urls = [
        'https://www.cnblogs.com/qiyeboy/default.html?page=1'
    ]

    def parse(self, response):
        papers = response.xpath(".//*[@class='day']")
        print(papers)


# 命令行可以启动爬虫，我们也可以添加爬虫启动程序
if __name__ == '__main__':
    process = CrawlerProcess(get_project_settings())
    process.crawl('cnblogss')
    process.start()
