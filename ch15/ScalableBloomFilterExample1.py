# -*- coding: utf-8 -*-

from pybloom import ScalableBloomFilter

# 动态容量的布隆过滤器
sbf = ScalableBloomFilter(mode=ScalableBloomFilter.SMALL_SET_GROWTH)
count = 10000
for i in range(0, count):
    sbf.add(i)

print(10001 in sbf)
print(555 in sbf)

