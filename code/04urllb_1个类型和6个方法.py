import urllib.request
url = 'https://www.baidu.com/'
#模拟浏览器向服务器发送数据
resopse = urllib.request.urlopen(url)
#resopse是HTTPResponse的类型
print(type(resopse))
# content = resopse.read()
# print(content)
# content = resopse.readline()
# print(content)
# content = resopse.readlines()
# print(content)
#返回状态码
# print(resopse.getcode())
#返回url地址
# print(resopse.geturl)
#获取状态信息
print(resopse.getheaders())