# -*- coding:utf-8 -*-
# date: 2019.04.13

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

    name = 'my51job_test2'
    allowed_domains = ['51job.com']
    start_urls = ['https://search.51job.com/list/090200,000000,0000,00,9,99,python,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=',
                  'https://search.51job.com/list/090200,000000,0000,00,9,99,python,2,2.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=',
                  ]

    # 起始网址传入第1页和第2页的连接，分别查找两个下一页，得到第2页和第3页的连接
    def parse(self, response):
        # 注意extract()结果是一个列表，extract_first()提取列表中第一个元素
        # 提取li标签中最后一个元素使用li[last()]，倒数第二个li[last()-1]
        url2 = response.xpath("/html/body/div[2]/div[4]/div[55]/div/div/div/ul/li[last()]/a/@href").extract()
        url3 = response.xpath("/html/body/div[2]/div[4]/div[55]/div/div/div/ul/li[last()]/a/@href").extract_first()
        print(type(url2))
        print(url2)
        print(type(url3))
        print(url3)
        name = response.xpath("/html/body/div[2]/div[4]/div[55]/div/div/div/ul/li[last()]/a/text()").extract_first()
        print(type(name))
        print(name)

        name2 = response.xpath("/html/body/div[2]/div[4]/div[55]/div/div/div/ul/li[last()-1]/a/text()").extract_first()
        print(name2)


if __name__ == '__main__':
    process = CrawlerProcess(get_project_settings())
    process.crawl('my51job_test2')
    process.start()

