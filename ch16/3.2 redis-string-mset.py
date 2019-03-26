# -*- coding: utf-8 -*-
# 一次存入多个键值,以字典的方式存入
import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r = redis.Redis(connection_pool=pool)
keydict = {'age': 20, 'country': 'china'}
r.mset(keydict)
list = ['age', 'country']

print(r.mget(list))
print(r.mget('age', 'country'))