# coding: utf-8

# URL管理器思路：
# 第一步：判断是否有待取的URL,方法定义为has_new_url
# 第二步：添加新的URL到未爬取的URL集合中，方法定义为add_new_url(url)和add_new_urls(urls)
# 第三步：获取一个未爬取新的URL，方法定义为get_new_url()
# 第四步：获取未爬取URL集合的大小，方法为new_url_size()
# 第五步：获取已爬取URL结合的大小，方法为old_url_size()

class UrlManager(object):
    def __init__(self):
        self.new_urls = set() # 未爬取的URL集合,set()函数生成一个无序不重复的集合
        self.old_urls = set() # 已爬取过的URL集合

    def has_new_url(self):
        '''判断是否有未爬取的URL'''
        return self.new_url_size() != 0

    def get_new_url(self):
        '''获取一个未爬取的URL'''
        new_url = self.new_urls.pop() # 删除列表中最后一个URL
        self.old_urls.add(new_url) # 将上面删除的URL加入到已爬的URL中
        return new_url

    def add_new_url(self, url):
        '''将新的URL添加到未爬取的URL集合中, 参数是一个URL'''
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url) # 将新的的url添加未爬取的URL集合中

    def add_new_urls(self, urls):
        '''将新的URL添加到未爬取的URL集合中,参数是一个URL集合或者列表之类'''
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url) # 将url传给add_new_url方法，调用add_new_url方法

    def new_url_size(self):
        '''获取未爬取的URL集合的大小'''
        return len(self.new_urls)

    def old_url_size(self):
        '''获取已经爬取过URL集合的大小'''
        return len(self.old_urls)


