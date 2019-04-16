# -*- coding:utf-8 -*-
# date: 2019.04.13

# 提取第一层页面的所有连接，就是该搜索结果页面的连接
# 搜索结果可以添加附加条件，同时可以爬取
# 第二层页面就是每个职位信息的连接
# LinkExtractor传入正则查找连接

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


class My51jobtestSpider(scrapy.Spider):

    name = 'my51job_test1'
    allowed_domains = ['51job.com']
    start_urls = ['https://search.51job.com/list/090200,000000,0000,00,9,99,python,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=']

    def parse(self, response):
        # 该正则方法提取连接，welfare=之后还可以添加搜索的附加条件，比如年终奖，体检之类，
        # 但是提取的到链接地址还是第一层页面，并且包含在没有附加条件的网址之中
        # scrapy爬取时候，不同的第一层页面会包含相同的工作岗位，爬取时候会自动过滤第二层已爬取过的页面
        # welfare=可以添加结束符号，只匹配到这里结束
        pattern = r'https://search.51job.com/list/090200,000000,0000,00,9,99,python,2,\d+.html\?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
        link = LinkExtractor(allow=pattern)
        links = link.extract_links(response)
        print(type(links))

        for link in links:
            print(link)


if __name__ == '__main__':
    process = CrawlerProcess(get_project_settings())
    process.crawl('my51job_test1')
    process.start()

# 运行结果，起始网址的1-6的6个分页面都提取出来了
# 同时还提取出来了添加附加搜索条件的第1个页面
