#(1)获取网页的源码
#(2)解析 解析服务器的响应文件 etree,HTml
import urllib.request
from lxml import etree
url = 'https://www.baidu.com/'

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0'
}
request = urllib.request.Request(url=url,headers=headers)

#模拟浏览器访问服务器
response = urllib.request.urlopen(request)
#获取网页源码
content = response.read().decode('utf-8')
# print(content)

#解析网页源码
tree = etree.HTML(content)

#获取想要的数据
result = tree.xpath('//*[@id="chat-submit-button"]/text()')
print(result)