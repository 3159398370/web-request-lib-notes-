import urllib.request

url = 'https://www.baidu.com'

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0'
}
# url的组成
#http/https ss加密

#协议————主机————端口号————路径————参数————锚点

#http 80
#http 443
# 创建一个请求对象，使用指定的URL和头部信息进行定制
request = urllib.request.Request(url=url,headers=headers)

# 发送定制的请求并获取服务器的响应
response = urllib.request.urlopen(request)

# 读取响应内容并将其从字节码解码为UTF-8格式的字符串
content = response.read().decode('utf-8')

# 打印解码后的响应内容
print(content)
