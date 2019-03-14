# XPATH解析七夜博客文章

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class Wangye1Spider(scrapy.Spider):
      name = 'wangye1'
      allowed_domains = ['cnblogs.com']

      start_urls = ['https://www.cnblogs.com/qiyeboy/default.html?page=1']

      def parse(self, response):
          papers = response.xpath(".//*[@class='day']")
          print(papers)




if __name__ == '__main__':
    process = CrawlerProcess(get_project_settings())
    process.crawl('wangye1')
    process.start()
