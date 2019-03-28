# -*- coding: utf-8 -*-
import pymongo

# 建立数据库连接
# 注意，脚本不能命名为pymongo.py，不然会报错找不到MongoClient属性
client = pymongo.MongoClient()
# 获取数据库,没有就直接创建
db = client.papers
# 获取一个集合
collection = db.books
# 插入文档
# 注意，脚本没运行一次，就像数据库中插入一次文档，所以，下面查询文档，结果会越来越多
book = {"author": "Mike",
        "text": "My first book!",
        "tags": ["爬虫", "python", "网络"]
        }
book_id = collection.insert(book)
# 查询文档
book_result = collection.find_one({"author": "Mike"})
print(book_result)

# 查看所有符合条件的文档数量
print(collection.find({"author": "Mike"}).count())
# 查询所有符合条件的文档
book_results = collection.find({"author": "Mike"})
for result in book_results:
        print(result)

# 删除文档
collection.delete_many({"author": "Mike"})


