import urllib.request
import urllib.parse
url = 'https://baike.baidu.com/item/'

#定制请求头
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0'
}

name = urllib.parse.quote('周杰伦')

url = url + name

# print(name)

request = urllib.request.Request(url = url ,headers= headers)

response = urllib.request.urlopen(request)

connect = response.read().decode('utf-8')

print(connect)