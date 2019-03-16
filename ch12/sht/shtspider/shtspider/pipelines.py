# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline

class ShtspiderPipeline(object):

    def __init__(self):
        self.file = open('papers.json', 'w', encoding='utf-8')

    # 将ITEM里面的信息写入到一个json文件中
    def process_item(self, item, spider):
        # 判断item字典对象中title对应的是否还有值
        if item['title']:
            # 将item字典类型的数据转换成json格式的字符串,
            # 注意json.dumps 序列化时对中文默认使用的ascii编码，要想写入中文，加上ensure_ascii=False
            line = json.dumps(dict(item), ensure_ascii=False) + "\n"
            self.file.write(line)
            return item
        else:
            raise DropItem("Missing title in %s" % item)

class MyImagesPipeline(ImagesPipeline):

    # 获取图片的url,然后下载图片
    def get_media_requests(self, item, info):
        # for image_url in item['image_urls']:
        yield scrapy.Request(item['image_urls'], meta={'item': item})

    # 确认图片是否下载完成或者没有下载
    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        return item

    # 图片重命名
    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        filename = u'full/{}.jpg'.format(item['title'])
        return filename



