import requests
import json
from bs4 import BeautifulSoup

# 使用requests请求得到网页
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'
headers = {'User_Agent': user_agent}
r = requests.get('http://seputu.com', headers=headers)
# print(r.text)


# 将网页内容生成一个BS4实例
soup = BeautifulSoup(r.text, 'html.parser', from_encoding='utf-8')
content = []
for mulu in soup.find_all(class_='mulu'):
    h2 = mulu.find('h2')
    if h2 != None:
        # 获取标题
        h2_title = h2.string # 获取每部分的标题
        # print(h2_title)
        list = []
        for a in mulu.find(class_='box').find_all('a'):
            href = a.get('href') # 获取章节的连接
            box_title = a.string # 获取章节的内容即章节的标题
            # print(href, box_title)
            list.append({'href': href, 'box_title': box_title})
        content.append({'title': h2_title, 'content': list})

print(content)

# 存储为JSON格式，
with open('qiye.json', 'w') as fp:
    # 把内容写入到文件中
    json.dump(content, fp=fp, indent=4)




