# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CnblogspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    time = scrapy.Field()
    content = scrapy.Field()
    pass

# Item对象相当于一个容器，将爬取到数据包装成结构化的数据
# 数据包装后类似于字典

# 1.Field类简介
# ①Field对象指明了每个字段的元数据（任何元数据），Field对象接受的值没有任何限制
# ②设置Field对象的主要目就是在一个地方定义好所有的元数据
# ③注意，声明item的Field对象，并没有被赋值成class属性。（可通过item.fields进行访问）
# ④Field类仅是内置字典类（dict）的一个别名，并没有提供额外的方法和属性。被用来基于类属性的方法来支持item生命语法。
# 【Field类源码】
# class Field(dict):
#     Container of field metadata

# 创建一个CnblogspiderItem类的实例item
# title="Python爬虫", content='爬虫开发'作为参数传递给Item类
# 放进这个容器，进行结构化出力，并用Field对象声明，
# 存储在一个容器中，用于之后的访问,存储之后的格式为一个字典

item = CnblogspiderItem(title="Python爬虫", content="爬虫开发")
print(item)

# 获取字段的值，item就是一个字典，然后访问键title的值，以下两种方法
print(item['title'])
print(item.get('title'))

# 设置字段的值，将title的值修改为爬虫
item['title'] = '爬虫'

# 获取所有的键和值
print(item.keys())
print(item.values())
print(item.items())

# item的复制,字典传入Item类之后，还是可以结构化数据
item2 = CnblogspiderItem(item)
print(item2)
print(type(item2))

# dict和item的转换,上面的item2是一个Item类，现在转化后是一个字典
dict_item = dict(item)
print(dict_item)
print(type(dict_item))



