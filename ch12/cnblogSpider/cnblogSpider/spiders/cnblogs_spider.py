# coding: utf-8
import scrapy

class CnblogsSpider(scrapy.Spider):
    # 爬虫的名称，唯一的，最好不要文件、文件夹名称重复，以免混淆
    name = 'cnblogs'
    # 允许的域名
    allowed_domains = ['cnblogs.com']
    # 入口URL列表，爬虫启动的接口
    start_urls = [
        'https://www.cnblogs.com/qiyeboy/default.html?page=1'
    ]

    def parse(self, response):
        # 实现网页的解析
        pass
