import urllib.request

proxies_pool = [
    {'http':'114.232.125.106:15018'},
]

import random

proxies = random.choice(proxies_pool)

url = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=68018901_58_oem_dg&wd=ip'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}

request = urllib.request.Request(url = url,headers=headers)

handler = urllib.request.ProxyHandler(proxies=proxies)

opener = urllib.request.build_opener(handler)

response = opener.open(request)

content = response.read().decode('utf-8')

with open('test.html','w',encoding='utf-8')as fp:
    fp.write(content)