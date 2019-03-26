# -*- coding: utf-8 -*-
import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r = redis.Redis(connection_pool=pool)

r.hset('student', 'name', 'qiye')
print(r.hget('student', 'name'))

r.hmset('student', {'name': 'qiye', 'age': 20})
print(r.hmget('student', 'name', 'age'))
