# coding: utf-8
# XPATH解析七夜博客文章

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class YunqiSpider(scrapy.Spider):
    name = 'yunqishuyuan'
    allowed_domains = ['yunqi.qq.com']

    start_urls = ['http://yunqi.qq.com/bk/so2/n30p1']

    def parse(self, response):
        # 注意：搜索一本书的标题，发现有两个地方有
        # div id="bookListBox"里面是假的
        # div ic="detailedBookListPanel"中才是真元素
        # 查看ch17中的云起书院-书本清单解析1

        # 下面的两种方法选取的结果一样
        # .从根节点开始选取，//不管在什么位置，div的class属性为book的所有div标签
        books1 = response.xpath(".//div[@class='book']")
        print(len(books1))
        print(books1[10])

        # .从根节点开始选取，//不管在什么位置，*代表所有的class属性为book的所有标签
        books2 = response.xpath(".//*[@class='book']")
        print(len(books2))
        print(books2[10])


        for book in books2[0:1]:
            novelImageUrl = book.xpath("./a/img/@src").extract_first()
            novelId = book.xpath("./div[@class='book_info']/h3/a/@id").extract_first()
            novelName = book.xpath("./div[@class='book_info']/h3/a/text()").extract_first()
            novelLink = book.xpath("./div[@class='book_info']/h3/a/@href").extract_first()
            # 注意网页中是dl标签（不是d1）,注意区分l和1
            novelAuthor = book.xpath("./div[@class='book_info']/dl[1]/dd[1]/a/text()").extract_first()
            print(novelImageUrl, novelId, novelName, novelLink, novelAuthor)
            # 有些书籍的作者，状态信息等信息为空的，因此该处尝试使用if语句，信息都全的话，才提取信息
            # 下面两种方法的结果一样
            # novelInfos = book.xpath("./div[@class='book_info']/dl/dd[@class='w_auth']")
            novelInfos = book.xpath("./div[@class='book_info']//dl//dd[@class='w_auth']")
            # print(novelInfos)
            print(len(novelInfos))
            if len(novelInfos) > 4:
                novelAuthor = novelInfos[0].xpath("./a/text()").extract_first()
                novelType = novelInfos[1].xpath("./a/text()").extract_first()
                novelStatus = novelInfos[2].xpath("./text()").extract_first()
                novelUpdateTime = novelInfos[3].xpath("./text()").extract_first()
                novelWords = novelInfos[4].xpath("./text()").extract_first()
                print(novelAuthor, novelType, novelStatus, novelUpdateTime, novelWords)
            else:
                novelAuthor = ''
                novelType = ''
                novelStatus = ''
                novelUpdateTime = ''
                novelWords = 0

if __name__ == '__main__':
    process = CrawlerProcess(get_project_settings())
    process.crawl('yunqishuyuan')
    process.start()
