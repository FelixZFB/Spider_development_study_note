# coding: utf-8

# 数据存储器，数据来源于爬虫调度器(SpiderMan)
# 生成的文件按照当前的时间进行命名，以避免重复，同时对文件进行缓存写入
# codecs一个编码转换模块

import codecs
import time

class DataOutput(object):

    def __init__(self):
        self.filepath = 'baike_%s.html' % (time.strftime("%Y_%m_%d_%H_%M_%S",
                                                         time.localtime()))
        self.output_head(self.filepath) # 调用store_data方法时候，需要初始化，初始化时最先向文件中写入头部信息
        self.datas = [] # 再向文件中写入data
    def store_data(self, data):
        if data is None:
            return
        self.datas.append(data) # data来自SpiderMan
        if len(self.datas) > 10:
            self.output_html(self.filepath)

    def output_head(self, path):
        '''
        将HTML头部信息写进去写进去
        '''
        fout = codecs.open(path, 'w', encoding='utf-8')
        fout.write('<html>')
        fout.write('<head>')
        # 进行格式设置，不然浏览器打开会出现乱码
        fout.write('<meta http-equiv="content-type" content="text/html; charset=utf-8">')
        fout.write('</head>')
        fout.write('<body>')
        fout.write('<table>')
        fout.close()


    def output_html(self, path):
        '''
        将数据写入到HTML文件中
        :param path: 文件路径，就是代码开始的文件名称，
        :return:
        '''
        fout = codecs.open(path, 'a', encoding='utf-8') # 追加方式写入正文数据
        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>' % data['url'])
            fout.write('<td>%s</td>' % data['title'])
            fout.write('<td>%s</td>' % data['summary'])
            fout.write('</tr>')
            self.datas.remove(data) # 写完了就删除数据
        fout.close()

    def output_end(self, path):
        '''
        写入HTML结尾信息
        :param path: 文件存储的路径
        :return:
        '''
        fout = codecs.open(path, 'a', encoding='utf-8')
        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')
        fout.close()