import urllib.request
import urllib.error
url = 'https://blog.csdn.net/2301_79263365/article/details/139783074?'
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0'
}

try:
    request =urllib.request.Request(url=url,headers=headers)

    response = urllib.request.urlopen(request)

    connect = response.read().decode('utf-8')

    print(connect)
except urllib.error.HTTPError:
    print('系统错误')

except urllib.error.URLError:
    print('系统升级')
