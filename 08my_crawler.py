import urllib.request
# 1.(定义一个url) 就是要访问的地址
url = 'https://www.baidu.com/'

# 2.模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)
# 需要解码 decode('编码的格式')
# 3.获取响应中的源码
content = response.read().decode('utf-8')

print(content)