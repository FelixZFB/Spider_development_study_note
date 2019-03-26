# -*- coding: utf-8 -*-
import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r = redis.Redis(connection_pool=pool)

dict = {'num1': 11, 'num2': 22, 'num3': 33}
r.zadd('z_num', dict)

# 获取有序集合元素的个数
print(r.zcard('z_num'))
# 按照索引范围获取集合中的元素
print(r.zrange('z_num', 0, 1))

# 获取值对应的分数
print(r.zscore('z_num', 'num2'))