# -*- coding: utf-8 -*-
import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r = redis.Redis(connection_pool=pool)

# 获取字符串，起始结束为字节位置
r.set('name', 'qiye安全博客')
print(r.getrange('name', 4, 9))

# 从指定字符串开始向后修改字符串的内容
r.setrange('name', 1, 'pyt')
print(r.get('name'))
bytes1 = r.get('name')

str1 = str(bytes1, encoding='utf-8')
print(str1)

str2 = bytes.decode(bytes1)
print(str2)
