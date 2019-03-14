import requests
from bs4 import BeautifulSoup

url = 'https://www.cnblogs.com/qiyeboy/default.html?page=1'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0'
headers = {'User-Agent': user_agent}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser', from_encoding='utf-8')





