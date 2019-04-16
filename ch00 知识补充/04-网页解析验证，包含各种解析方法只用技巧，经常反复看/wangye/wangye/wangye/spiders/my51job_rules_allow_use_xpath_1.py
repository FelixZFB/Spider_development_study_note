# -*- coding:utf-8 -*-
# date: 2019.04.13

# 提取第一层页面中下一页的连接，下一页就是每个搜索分页面的连接地址
# LinkExtractor传入XPATH参数查找下一页的连接
# 爬虫会自动从response中不断查找下一页连接，该处支只传入了起始网址，只能找到一个下一页


# 找到下一页连接XPATH的规律，发现只有li标签的位置不一样，但是分析源码发现
# 其实都是ul标签下最后一个li标签，地址a标签的href中
'''
/html/body/div[2]/div[4]/div[55]/div/div/div/ul/li[13]/a
/html/body/div[2]/div[4]/div[55]/div/div/div/ul/li[8]/a
/html/body/div[2]/div[4]/div[55]/div/div/div/ul/li[13]/a
'''

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


class My51jobtestSpider(scrapy.Spider):

    name = 'my51job_test3'
    allowed_domains = ['51job.com']
    # 提取第1页和第10页的下一页连接
    start_urls = [
        'https://search.51job.com/list/090200,000000,0000,00,9,99,python,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=',
        'https://search.51job.com/list/090200,000000,0000,00,9,99,python,2,10.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=',
    ]

    def parse(self, response):
        # 注意extract()结果是一个列表，extract_first()提取列表中第一个元素
        # 提取li标签中最后一个元素使用li[last()]，倒数第二个li[last()-1]
        # 使用XPATH提取连接，只需要写到连接所在的标签即可
        link = LinkExtractor(restrict_xpaths='/html/body/div[2]/div[4]/div[55]/div/div/div/ul/li[last()]/a')
        links = link.extract_links(response)
        # 提取结果是一个列表，提取里面的属性的值
        print(type(links))
        for link in links:
            print(link)
            print(link.url)
            print(link.text)



if __name__ == '__main__':
    process = CrawlerProcess(get_project_settings())
    process.crawl('my51job_test3')
    process.start()

