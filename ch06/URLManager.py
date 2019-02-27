# coding: utf-8
class UrlManager(object):
    def __init__(self):
        self.new_urls = set() # 未爬取的URL集合
        self.old_urls = set() # 已爬取过的URL集合

    def has_new_url(self):
        '''判断是否有未爬取的URL'''
        return self.new_url_size() != 0

    def get_new_url(self):
        '''获取一个未爬取的URL'''
        new_url = self.new_urls.pop() # 删除列表中最后一个URL
        self.old_urls.add(new_url) # 将上面删除的URL加入到已爬的URL中
        return new_url