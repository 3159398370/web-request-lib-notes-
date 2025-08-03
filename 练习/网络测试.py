# 使用的场景：数据采集的时候，需要登录，然后进到某个界面
#个人信息界面是utf-8 但是报错了编码错误

import urllib.request
import urllib.response

url ='http://10.64.250.153/task3d/index'
headers = {
    # ":authority": "weibo.com",
    # ":method": "GET",
    # ":path": "/ajax/profile/info?uid=7439225996",
    # ":scheme": "https",
    # "accept": "application/json, text/plain, */*",
    # "accept-encoding": "gzip, deflate, br, zstd",
    # "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    # "cache-control": "no-cache",
    # "client-version": "v2.47.89",
    "cookie": "JSESSIONID=929909413716699BF57632AF656A411B",
    # "dnt": "1",
    # "pragma": "no-cache",
    # "priority": "u=1, i",
    #referer 判断当前路径是不发上一个页面进来的
    "referer": "https://weibo.com/u/7439225996",
    # "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Microsoft Edge\";v=\"138\"",
    # "sec-ch-ua-mobile": "?0",
    # "sec-ch-ua-platform": "\"Windows\"",
    # "sec-fetch-dest": "empty",
    # "sec-fetch-mode": "cors",
    # "sec-fetch-site": "same-origin",
    # "server-version": "v2025.07.16.1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0",
    "x-requested-with": "XMLHttpRequest"
}

#请求对象的定制
request = urllib.request.Request(url=url,headers=headers)

response = urllib.request.urlopen(request)
#获取响应的数据
content = response.read().decode('utf-8')
print(content)

with open('300标注.html','w',encoding='utf-8') as fp:
    fp.write(content)