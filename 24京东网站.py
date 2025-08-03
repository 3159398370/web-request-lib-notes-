import urllib.request

url = 'https://www.jd.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}
request = urllib.request.urlopen(url)
content = request.read().decode('utf-8')
print(content)