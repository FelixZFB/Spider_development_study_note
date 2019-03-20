import requests
from bs4 import BeautifulSoup


headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    'Referer': 'https://www.zhihu.com/',
    'Cookie': '_zap=e8e301ad-bf31-45e6-bc90-00b0cfad880a; _xsrf=jHige81Z8z7qgA7JhpQJy6Qusg3641GZ; d_c0="AHDm-ApbJA-PTkEarHuC0T9f1L6YZnLFM8I=|1552917823"; tst=r; q_c1=33118b9596874d44beece30aa7646198|1552917848000|1552917848000; tgw_l7_route=7bacb9af7224ed68945ce419f4dea76d; capsion_ticket="2|1:0|10:1552985118|14:capsion_ticket|44:OWU4OWVkY2M3NTc4NDVkY2E4YTM1ZjVlNzc4NTE0Zjk=|1b9c627cefe5d21b26f9a64ec4f65959ff122c046642d1969dff58ad41292b33"; z_c0="2|1:0|10:1552985274|4:z_c0|92:Mi4xVVpVTURRQUFBQUFBY09iNENsc2tEeVlBQUFCZ0FsVk51dnA5WFFDY2pET3VJa3lZWURVWHMxSjB0WmVUYWNxSmdn|360fbf6d753f5554df31034f7af4c1efe122ad6a6ccb1ff48289f97122311590"',
}
res = requests.get("https://www.zhihu.com/search?type=content&q=python", headers=headers)
soup = BeautifulSoup(res.text, 'lxml', from_encoding='utf-8')
print(soup.title)
