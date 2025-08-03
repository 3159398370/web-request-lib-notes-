import urllib.request

url = 'http://wulanack.biaozhu.cc/anno/2DCommon?taskId=21229&batchId=502714&taskType=0'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}
request = urllib.request.urlopen(url)
content = request.read().decode('utf-8')
print(content)
with open('25.html', 'w', encoding='utf-8') as f:
    f.write(content)