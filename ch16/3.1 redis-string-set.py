# -*- coding: utf-8 -*-

import redis
import time

pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r = redis.Redis(connection_pool=pool)
# ex参数为过期时间，单位是秒
# 先存入，然后等待4秒，取出值为None
r.set('name', 'qiye', ex=3)

time.sleep(4)
print(r.get('name'))

# name不存在时，才进行操作,上面的qiye已经过期了
r.setnx('name', 'haha')
print(r.get('name'))

# getset设置新值并获取原来的值,获取的是原来的值haha
print(r.getset('name','hello'))
