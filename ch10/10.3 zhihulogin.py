import requests
from requests_toolbelt import MultipartEncoder

url = "http://httpbin.org/post"
fields = {
    "client_id": "c3cef7c66a1843f8b3a9e6a1e3160e20",
    "grant_type": "password",
    "timestamp": "1527040472416",
    "source": "com.zhihu.web",
    "signature": "66a16483ab16e54c3bb4ef84bf683dd67cadc246",
    "username": "18200116656",
    "password": "zfb123456zfb"
}

m = MultipartEncoder(fields, boundary='----WebKitFormBoundaryH6BBAmaUzVUheiMp')
res = requests.post(url, headers={'Content-Type': m.content_type}, data=m.to_string())

print(res.request.body)
# # 查看请求头
print(res.request.headers)
print(res.text)
