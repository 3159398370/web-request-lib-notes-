import urllib.request
url = 'https://active.starbucks.com.cn/sortable/f152ccf3-b71c-495c-b1ff-f1594d453165.jpg'
# 发送请求
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
content = response.read()
with open('1.jpg', 'wb') as f:
    f.write(content)
    print('下载完成')
#下载图片

url = 'https://active.starbucks.com.cn/sortable/f152ccf3-b71c-495c-b1ff-f1594d453165.jpg'
# 使用 urlretrieve 直接下载图片
urllib.request.urlretrieve(url, '1.jpg')
print('下载完成')