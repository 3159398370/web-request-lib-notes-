#get请求
#获取豆瓣电影的第一页数据，并保存起来

import urllib.request


url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0'
}

#请求对象的定制

request = urllib.request.Request(url=url,headers=headers)

response = urllib.request.urlopen(request)

connect = response.read().decode('utf-8')

# (3) 数据下载到本地
# fp = open('douban.json', 'w', encoding='utf-8')
# fp.write(connect)

with open('douban1.json', 'w', encoding='utf-8') as fp:
    fp.write(connect)