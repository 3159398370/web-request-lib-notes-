import urllib.request
import urllib.parse
import urllib.response

# urlencod的应用场景：多个参数的时候

# import urllib.parse
# date = {
#     'wd':'周杰伦',
#     'sex':'男',
#     'age':'18',
#     'hobby':'rap'
#
# }
#
# a = urllib.parse.urlencode(date)
#
# print(a)

#获取网页源码

base_url = 'https://www.baidu.com/s?'

data = {
    'wd':'周杰伦',
    'sex':'男',
    'location':'中国'
}
new_data = urllib.parse.urlencode(data)
url = base_url + new_data
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0'
}
# 创建一个请求对象，包含请求的URL和头部信息
request = urllib.request.Request(url=url,headers=headers)

# 发送请求并打开URL，返回一个HTTP响应对象
response = urllib.request.urlopen(request)

# 读取响应内容并解码为UTF-8格式的字符串
connect = response.read().decode('utf-8')

# 打印响应内容
print(connect)
