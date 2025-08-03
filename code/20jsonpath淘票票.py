import urllib.request
url = 'https://www.taopiaopiao.com/cityAction.json?activityId&_ksTS=1753363149927_104&jsoncallback=jsonp105&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'

headers={
    # "authority": "www.taopiaopiao.com",
    # "method": "GET",
    # "path": "/cityAction.json?activityId&_ksTS=1753363149927_104&jsoncallback=jsonp105&action=cityAction&n_s=new&event_submit_doGetAllRegion=true",
    # "scheme": "https",
    "accept": "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
    # "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "bx-v": "2.5.31",
    "cache-control": "no-cache",
    "cookie": "tb_city=310100; tb_cityName=\"yc+6ow==\"; isg=BPLyKGnAzo9qOvKw5cyITx2HQzjUg_YdSRE5IbzLAKWQT5JJpRFiLamhP-tzP261",
    "dnt": "1",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.taopiaopiao.com/?spm=a1z21.3046609.city.2.10c7112aWg2pfV&tbpm=3&city=310100",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Microsoft Edge\";v=\"138\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0",
    "x-requested-with": "XMLHttpRequest",
}

request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
content = content.split('(')[1].split(')')[0]

with open('21jsonpath淘票票.json','w',encoding='utf-8')as fp:
    fp.write(content)

import json
import jsonpath
obj = json.load(open('21jsonpath淘票票.json','r',encoding='utf-8'))
city_list =jsonpath.jsonpath(obj,'$..regionName')
print(city_list)