#urllib

# (1)一个类型和六个方法
# (2)get 请求
#(3)post 请求
#(4)ajax的get 请求
#(5)ajax的post
# (6)cookies
# (7)代理

# requests
#(1)一个请求和六个属性
#(2)get 请求
#(3)post
#(4)ajax
#(5)cookies 验证码
#(6)代理

import requests

url = 'https://www.baidu.com/s?'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}
data = {
    'wd': '北京'
}
# kwargs 字典
response = requests.get(url=url,params=data,headers=headers)

content = response.text
print(content)

