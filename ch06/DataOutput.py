# coding: utf-8

# 数据存储器，数据来源于爬虫调度器

import codecs

class DataOutput(object):

    def __init__(self):
        self.datas = []
    def store_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = codecs.open('baike.html', 'w', encoding='utf-8')
        fout.write('<html>')
        fout.write('<head>')
        # 进行格式设置，不然浏览器打开会出现乱码
        fout.write('<meta http-equiv="content-type" content="text/html; charset=utf-8">')
        fout.write('<body>')
        fout.write('<table>')
        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>' % data['url'])
            fout.write('<td>%s</td>' % data['title'])
            fout.write('<td>%s</td>' % data['summary'])
            fout.write('</tr>')
            self.datas.remove(data)
        fout.write('</table>')
        fout.write('</body>')
        fout.write('</head>')
        fout.write('</html>')
        fout.close()

