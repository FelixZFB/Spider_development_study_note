# coding: utf-8

# URL管理器思路：
# 第一步：判断是否有待取的URL,方法定义为has_new_url
# 第二步：添加新的URL到未爬取的URL集合中，方法定义为add_new_url(url)和add_new_urls(urls)
# 第三步：获取一个未爬取新的URL，方法定义为get_new_url()
# 第四步：获取未爬取URL集合的大小，方法为new_url_size()
# 第五步：获取已爬取URL结合的大小，方法为old_url_size()

# 代码进行优化，对URL集合进行序列化操作，减少内存的消耗
# URL进行MD5处理，可以减少内存消耗
# Python2中交cPickle

import pickle as cPickle
import hashlib

class UrlManager(object):
    def __init__(self):
        self.new_urls = self.load_progress('new_urls.txt') # 未爬取的URL集合
        self.old_urls = self.load_progress('old_urls.txt') # 已爬取过的URL集合

    def has_new_url(self):
        '''判断是否有未爬取的URL'''
        return self.new_url_size() != 0

    def get_new_url(self):
        '''从new_urls集合中，获取一个未爬取的URL，用于爬取'''
        new_url = self.new_urls.pop() # 删除列表中最后一个URL
        m = hashlib.md5() # 创建一个MD5处理的实例
        m.update(new_url.encode('utf-8')) # 对new_url进行MD5处理，python处理后默认是256位，下面只取中间的128位
        self.old_urls.add(m.hexdigest()[8:-8]) # 将上面删除的URL加入到已爬的URL中
        return new_url

    def add_new_url(self, url):
        '''将HTML解析得到的新的URL添加到未爬取的URL集合中, 参数是一个url,来自下面的add_new_urls方法'''
        if url is None:
            return
        m = hashlib.md5()
        m.update(url.encode('utf-8'))
        url_md5 = m.hexdigest()[8:-8]
        if url not in self.new_urls and url_md5 not in self.old_urls:
            self.new_urls.add(url) # 将新的的url进行MD5处理后添加到未爬取的URL集合中

    def add_new_urls(self, urls):
        '''
        将新的URL添加到未爬取的URL集合中,参数是一个URL集合或者列表之类
        注意，页面解析时候，获取的新的URL是一个列表，里面有一个或者多个新URL
        所以先得到新的URL列表，然后调用上面的add_new_url方法,将URL一个一个添加到未爬取的URL集合中
        '''
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

    def save_progerss(self, path, data):
        '''
        保存进度,将数据序列化写入文件
        :param path: 文件路径
        :param data: 数据
        :return:
        '''
        with open(path, 'wb') as f:
            cPickle.dump(data, f) # 将data以二进制方式写入到f文件中

    def load_progress(self, path):
        '''
        从本地文件加载进度，读取文件，反序列化读取文件中的内容
        :param path: 文件路径
        :return:
        '''
        print("[+] 从文件加载进度：%s" % path)
        try:
            with open(path, 'rb') as f:
                tmp = cPickle.load(f)
                return tmp
        except:
            print("[!] 无进度文件，创建：%s" % path)
        return set()


