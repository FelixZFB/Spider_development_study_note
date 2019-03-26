# -*- coding: utf-8 -*-

# 使用布隆过滤器对URL进行去重

import hashlib
from pybloom import ScalableBloomFilter
from scrapy.dupefilters import RFPDupeFilter
from  scrapy.utils.url import canonicalize_url

class URLBloomFilter(RFPDupeFilter):
    # 根据urlhash_bloom过滤
    def __init__(self, path=None):
        self.urls_sbf = ScalableBloomFilter(mode=ScalableBloomFilter.SMALL_SET_GROWTH)
        RFPDupeFilter.__init__(self, path)

    def request_seen(self, request):
        # 生成一个哈希sha1处理实例
        fp = hashlib.sha1()
        # 更新传入的参数为格式化统一后的函数（有时候同一个网址，可能请求网址的格式不一样）
        fp.update(canonicalize_url(request.url))
        # sha1处理后的url
        url_sha1 = fp.hexdigest()
        if url_sha1 in self.urls_sbf:
            return True
        else:
            self.urls_sbf.add(url_sha1)
