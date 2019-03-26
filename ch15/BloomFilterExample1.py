# -*- coding: utf-8 -*-

from pybloom import BloomFilter

# 创建一个一个容量为1000，漏失率为0.001的布隆过滤器
f = BloomFilter(capacity=1000, error_rate=0.001)
for x in range(10):
    f.add(x)
print(f)
# 判断数字是否在容器(数据库)中
print(11 in f)
print(2 in f)
