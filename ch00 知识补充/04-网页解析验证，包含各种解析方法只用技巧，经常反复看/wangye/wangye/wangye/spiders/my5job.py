# coding: utf-8
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class CnblogsSpider(scrapy.Spider):
    # 爬虫的名称，唯一的，最好不要文件、文件夹名称重复，以免混淆
    name = 'my51jobtest'
    # 允许的域名
    allowed_domains = ['51job.com']
    # 入口URL列表，爬虫启动的接口
    start_urls = [
        'https://search.51job.com/list/090200,000000,0000,00,9,99,python,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=',
    ]

    def parse(self, response):
        jobs = response.xpath(".//div[@id='resultList']//div[@class='el']")
        print(jobs)
        print(len(jobs))
        print(type(jobs))

        # 每一个工作标签中提取工作相关的信息
        for job in jobs:
            # 匹配结果仍然是一个列表类型,列表中只有一个元素，
            # P02中已经提取过，发现里面有很多空格，提取第一个元素的值并去掉里面的空格
            # 注意TZKT_Study_Note中的P02项目使用的是etree.HTML解析HTML源码，提取元素可以使用列表语法，该处selector不可以
            jobName = job.xpath("./p/span/a/text()").extract_first().strip()
            jobLink = job.xpath("./p/span/a/@href").extract_first().strip()
            jobCompany = job.xpath("./span[1]/a/text()").extract_first().strip()
            jobAddress = job.xpath("./span[2]/text()").extract_first().strip()
            jobDate = job.xpath("./span[4]/text()").extract_first().strip()
            # 发现有些工作缺少工资信息，会导致代码终止，加入try语句
            global jobSalary
            try:
                jobSalary = job.xpath("./span[3]/text()").extract_first().strip()
            except:
                pass

            print(jobName, jobLink, jobCompany, jobAddress, jobDate, jobSalary)



# 命令行可以启动爬虫，我们也可以添加爬虫启动程序
if __name__ == '__main__':
    process = CrawlerProcess(get_project_settings())
    process.crawl('my51jobtest')
    process.start()
