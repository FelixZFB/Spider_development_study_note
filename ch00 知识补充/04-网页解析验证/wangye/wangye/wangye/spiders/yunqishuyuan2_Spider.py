# coding: utf-8
# 解析一本书的信息
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class YunqiSpider(scrapy.Spider):
    name = 'yunqishuyuan_book'
    allowed_domains = ['yunqi.qq.com']
    start_urls = ['http://yunqi.qq.com/bk/gdyq/24114533.html']

    def parse(self, response):
        # .选取当前节点，//不管在什么位置，div的class属性为book的所有div标签
        novelLabel = response.xpath(".//div[@class='tags']/text()").extract_first()
        # 总人气选择，可以使用以下两种选取方法
        # *代表选取文档中的所有元素，*[@id='novelInfo']选取文档所有id属性为novelInfo的元素
        # novelAllClick = response.xpath(".//*[@id='novelInfo']/table/tr[2]/td[1]/text()").extract_first()
        # 选取所有拥有id为novelInfo的属性的 div 元素
        novelAllClick = response.xpath(".//div[@id='novelInfo']/table/tr[2]/td[1]/text()").extract_first()
        novelAllPopular = response.xpath(".//div[@id='novelInfo']/table/tr[2]/td[2]/text()").extract_first()
        novelAllComm = response.xpath(".//div[@id='novelInfo']/table/tr[2]/td[3]/text()").extract_first()
        print(novelLabel, '   ', novelAllClick, '   ', novelAllPopular, '   ', novelAllComm)

        novelMonthClick = response.xpath(".//div[@id='novelInfo']/table/tr[3]/td[1]/text()").extract_first()
        novelMonthPopular = response.xpath(".//div[@id='novelInfo']/table/tr[3]/td[2]/text()").extract_first()
        novelMonthComm = response.xpath(".//div[@id='novelInfo']/table/tr[3]/td[3]/text()").extract_first()
        print(novelMonthClick, '   ', novelMonthPopular, '   ', novelMonthComm)

        novelWeekClick = response.xpath(".//div[@id='novelInfo']/table/tr[4]/td[1]/text()").extract_first()
        novelWeekPopular = response.xpath(".//div[@id='novelInfo']/table/tr[4]/td[2]/text()").extract_first()
        novelWeekComm = response.xpath(".//div[@id='novelInfo']/table/tr[4]/td[3]/text()").extract_first()
        print(novelWeekClick, '   ', novelWeekPopular, '   ', novelWeekComm)

        novelCommentNum1 = response.xpath(".//div[@id='novelInfo']/table/tr[5]/td[2]/span[1]/text()").extract()[0]
        print(novelCommentNum1)
        novelCommentNum = response.xpath(".//*[@id='novelInfo_commentCount']/text()").extract_first()
        print(novelCommentNum)




if __name__ == '__main__':
    process = CrawlerProcess(get_project_settings())
    process.crawl('yunqishuyuan_book')
    process.start()
