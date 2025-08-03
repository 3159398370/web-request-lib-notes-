import requests

url = 'https://www.baidu.com'

response = requests.get(url=url)
#一个属性和六个属性
# print(type(response))
#设置的编码格式
response.encoding = 'utf-8'
#以字符串的形式来返回网页的源码
print(response.text)
print(response.url)

print(response.status_code)

print(response.cookies)