# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# pipelines.py用于下载Item对象中的数据到本地
# pipelines.py中代码定制完成后，需要在settings.py中进行激活

import json
import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline


class CnblogspiderPipeline(object):
    def __init__(self):
        self.file = open('papers.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        # 判断item字典对象中title对应的是否还有值
        if item['title']:
            # 将item字典类型的数据转换成json格式的字符串
            line = json.dumps(dict(item)) + "\n"
            self.file.write(line)
            return item
        else:
            raise DropItem("Missing title in %s" % item)

# 定制图片下载组件
class MyImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        # 循环每一张图片地址下载，若传过来的不是集合则无需循环直接yield
        for image_url in item['cimage_urls']:
            # meta里面的数据是从spider获取，然后通过meta参数传递给下面方法：file_path
            yield scrapy.Request(image_url, meta={'item': item})

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        return item

    def file_path(self, request, response=None, info=None):
        # 提取上面的item对象
        item = request.meta['item']
        image_guid = item['title']+'.'+request.url.split('/')[-1].split('.')[-1]
        filename = u'full/{0}'.format(image_guid)
        return filename