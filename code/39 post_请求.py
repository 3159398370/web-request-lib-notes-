import requests

url = 'https://fanyi.baidu.com/sug'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}
data = {
    'kw': 'hello'
}
response = requests.post(url=url, data=data, headers=headers)

import json

obj = json.loads(response.text)
print(obj)