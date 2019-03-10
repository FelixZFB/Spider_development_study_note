# coding: utf-8
# 下载一个网址中的图片，该网址中的图片都是小图，必须点击图片后，才能弹出放大后的图片
# 因此，考虑将图片全部下载下来后再看
# 由于网站是国外服务器，在线查看图片都要慢慢下载展开，所以该代码下载图片也很慢

import requests
import re
import time
import threading
from bs4 import BeautifulSoup

root_urls = [
    'https://www.porngals4.com/in-need-of-assistance-all-girl-massage-79425/',
    'https://www.porngals4.com/lesbian-adventures-strap-on-specialists-07-78456/',
]

def downpicture():

    # 下载获取网页内容
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0'
    headers = {'User-Agent': user_agent}
    for root_url in root_urls:
        r = requests.get(root_url, headers=headers)
        r.encoding = 'utf-8' # 解决中文编码乱码的问题

        # 解析网页内容，提取所需的图片网址
        soup = BeautifulSoup(r.text, 'html.parser', from_encoding='utf-8')
        # 检查原网址，发现网页可以打开的大图片，网址前面部分都是统一的命名规则，找出所有的含有匹配图片链接的标签
        links = soup.find_all('a', href=re.compile(r'https://b.porngals4.com/media/galleries/.*'))
        urls = []
        for link in links:
            # 提取href的属性，既URL地址
            new_url = link['href']
            urls.append(new_url)

        # 以二进制方式写入图片并存储图片
        for url in urls:
            pic= requests.get(url,headers=headers)
            # 取网址末10位作为图片名称
            # filename = ''.join(list(url)[-10:])
            # 取图片下载时间戳的前十位，第十位刚刚好是秒计数
            t = time.time()
            t1 = list(str(t))
            filename = ''.join(t1[0:10]) + '.jpg'
            with open(filename, 'wb') as f:
                f.write(pic.content)
            print(filename + "下载完成")


if __name__ == '__main__':
    downpicture()






