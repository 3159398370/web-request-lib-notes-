import urllib.request

url='https://www.starbucks.com.cn/menu/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}
response = urllib.request.urlopen(url)

content = response.read().decode('utf-8')
print(content)

from bs4 import BeautifulSoup

soup = BeautifulSoup(content, 'lxml')