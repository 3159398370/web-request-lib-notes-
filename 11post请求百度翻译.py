import urllib.request
import urllib.parse


url = 'https://fanyi.baidu.com/sug'

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0'
}

data = {
    'kw':'spider'
}

#post请求的参数必须进行编码
data = urllib.parse.urlencode(data).encode('utf-8')
#post请求，是不会拼接在yrl后面的，而是在请求报文中进行编码的
#post请求，data参数的数据类型必须进行编码
request = urllib.request.Request(url=url,data=data,headers=headers)

print( request)

#模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)
#获取响应数据
content = response.read().decode('utf-8')
#字符串变成jison对象
import json
obj = json.loads(content)
print(obj)