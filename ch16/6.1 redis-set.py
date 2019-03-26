# -*- coding: utf-8 -*-
import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r = redis.Redis(connection_pool=pool)

# 向集合中添加元素
r.sadd('num1', 33, 44, 55, 66)
r.sadd('num2', 66, 77)
# 获取集合中元素的个数
print(r.scard('num1'))
# 获取集合中所有的成员
print(r.smembers('num1'))

# 获取多个集合的差集,第一个集合减掉第二个集合中相同的，保留剩下的
print(r.sdiff('num1', 'num2'))
print(r.sdiff('num2', 'num1'))
print(r.sdiff('num1', 'num1'))

# 获取多个集合的交集
print(r.sinter('num1', 'num2'))

# 获取多个集合的并集
print(r.sunion('num1', 'num2'))


