# coding: utf-8
import scrapy
from scrapy import Selector
from cnblogSpider.items import CnblogspiderItem
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class CnblogsSpider(scrapy.Spider):
    # 爬虫的名称，唯一的，最好不要文件、文件夹名称重复，以免混淆
    name = 'cnblogs'
    # 允许的域名
    allowed_domains = ['cnblogs.com']
    # 入口URL列表，爬虫启动的接口
    start_urls = [
        'https://www.cnblogs.com/qiyeboy/default.html?page=1'
    ]

    # 首先定义parse方法，属于第一层爬取，
    # 然后定义一格parse_body方法，属于第二层爬取（需要使用第一层爬取的url）

    # parse方法，有一个response参数，该参数就是请求初始URL得到的内容
    # 通过该response开始爬虫后面的各个工作
    def parse(self, response):
        # 实现网页的解析
        # 首先抽取所有的文章，response中选择所有class='day'对应的节点元素
        # 分析原文可以发现，每一篇文章都是放在，<div class="day"> </div>标签里面
        # 选取的结果就是一个列表，就是多篇文章
        papers = response.xpath(".//*[@class='day']")

        # 加入调试查看命令,可以分布查看每一次爬行的结果
        # from scrapy.shell import inspect_response
        # inspect_response(response, self)

        # 从每篇文章中抽取数据
        for paper in papers:
            # 提取出一篇文章的地址，标题，时间，和内容（就是标题）
            # .从paper下面开始选，//不管在什么位置，*所有的,class='postTitle'属性下a标签下href属性的第一个值
            # .extract()[0]提取文字
            url = paper.xpath(".//*[@class='postTitle']/a/@href").extract()[0]
            # .从paper下面开始选，//不管在什么位置，*所有的,class='postTitle'属性下a标签下的第一个文字内容
            title = paper.xpath(".//*[@class='postTitle']/a/text()").extract()[0]
            time = paper.xpath(".//*[@class='dayTitle']/a/text()").extract()[0]
            # 提取文章的摘要
            content = paper.xpath(".//*[@class='c_b_p_desc']/text()").extract()[0]

            # 将提取到的数据封装成一个Item对象，封装之后类似一个字典，url为键，提取到的url地址就是值
            item = CnblogspiderItem(url=url, title=title, time=time, content=content)

            # 上面已经提取到了具体的一篇文章的地址，然后通过改地址，创建一个新的请求
            # 通过Request类请求，传入上面解析到的文章的URL，传入一个回调方法进行网页的解析
            # Request中有个meta参数，用来传递信息，传递信息的格式必须是一个字典类型，
            # 通过Request传进去，通过Request的请求结果response取出来，取出方法与字典一样
            request = scrapy.Request(url=url, meta={'item': item}, callback=self.parse_body)

            # 将parse打造成一个生成器,生成item，经过循环之后会生成很多item字典对象
            # 函数生成器，相当于return返回request请求对象的值，上面的request执行了parse_body方法，
            # 最终得到的就是一个item字典对象，实际返回的就是一个容器，里面存储着分析网页得到的各种数据
            yield request

        next_page = Selector(response).re(u'<a href="(\S*)">下一页</a>')
        if next_page:
            # url为请求的对象，callback为回调方法，指定由谁来解析请求的响应
            yield scrapy.Request(url=next_page[0], callback=self.parse)

    def parse_body(self, response):
        # 取出前面已经封装好的Item对象，里面已经包含了URL、标题、时间和摘要
        # 这里爬取图片的URL后，继续封装到Item里面去
        item = response.meta['item']
        # .意思选择匹配的当前节点，//选择文档中所有匹配当前节点的节点，不考虑他们的位置，
        # *匹文档中所有的元素，[@class='postBody'],匹配属性为class值为postBody的元素
        # 整个表达式含义，从response元素开始匹配文档中所有属性class='postBody'的元素，实际就是匹配的文章的正文内容
        body = response.xpath(".//*[@class='postBody']")
        # 找出了文章正文，然后匹配里面所有的图片链接
        # 下面表达式含义，从body元素节点开始匹配，找出所有的img元素下所有的src图片链接属性的值
        # extract()提取所有的内容，提取所有src的属性，就是图片的连接地址，extract_first()和extract()[0]用来提取第一个内容，有时候一个标签下面有很多文字内容
        item['image_urls'] = body.xpath(".//img//@src").extract()
        yield item # 函数生成器，相当于返回item对象（该处也可写成return item）


# 命令行可以启动爬虫，我们也可以添加爬虫启动程序
if __name__ == '__main__':
    process = CrawlerProcess(get_project_settings())
    process.crawl('cnblogs')
    process.start()
