
import urllib.request
url = "https://ip.900cha.com/"

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
    'Content-Type': 'application/json'
}

request = urllib.request.Request(url=url, headers=headers)

proxies = {
    'https': '116.208.196.37:21755'
}
# response = urllib.request.urlopen(request)
#handler build_opener   open
handler = urllib.request.ProxyHandler(proxies = proxies)
opener = urllib.request.build_opener(handler)
response = opener.open(request)
content = response.read().decode('utf-8')

with open('ip.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
