# -*- coding: utf-8 -*-

import redis

# 创建连接池管理redis连接，可以避免每次建立和释放连接的开销
# 指定主机和端口建立redis连接

pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r = redis.Redis(connection_pool=pool)

# 向redis中存入键值
# 注意，需要CMD启动本地的redis-server,并且CMD窗口处于打开状态
r.set('name', 'qiye')
print(r.get('name'))
