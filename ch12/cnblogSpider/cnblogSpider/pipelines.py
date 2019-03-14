# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# pipelines.py用于下载Item对象中的数据到本地
# pipelines.py中代码定制完成后，需要在settings.py中进行激活

import json
from scrapy.exceptions import DropItem

class CnblogspiderPipeline(object):
    def __init__(self):
        self.file = open('papers.json', 'w')

    def process_item(self, item, spider):
        # 判断item字典对象中title对应的是否还有值
        if item['title']:
            # 将item字典类型的数据转换成json格式的字符串
            line = json.dumps(dict(item)) + "\n"
            self.file.write(line)
            return item
        else:
            raise DropItem("Missing title in %s" % item)
