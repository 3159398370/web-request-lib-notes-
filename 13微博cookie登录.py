# 使用的场景：数据采集的时候，需要登录，然后进到某个界面
#个人信息界面是utf-8 但是报错了编码错误
#
import urllib.request
import urllib.response

url ='https://weibo.com/u/7439225996'
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
        "cookie": "SCF=AiuVLx6bUNnJduXUbQFTuo4iBGZ3mMtO_Rqm44XYMS_D88z7qwS-jIyIPrdpBGkx2JzlaM6AiYBETZ6EAGt0J2Q.; SINAGLOBAL=5754809308725.555.1749301671368; ULV=1749301671725:1:1:1:5754809308725.555.1749301671368:; SUB=_2A25FfAcFDeRhGeFK6FsT8ivFwjqIHXVm8AbNrDV8PUNbmtAYLUf2kW9NQ3diWkqSWuQ_PghmvoQLf6SWDeJzip34; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhQwTnTPaJDEpllDrA7Y--h5NHD95QNShe4eozf1K.cWs4DqcjVi--ciKn4iKn7i--Ri-z7iK.0i--NiKnRi-zpi--Xi-iWi-iWTCH8SC-4SEHWeBtt; ALF=02_1755317333; XSRF-TOKEN=3mNRJNhYKPYKr8aSbWdSPYeN; WBPSESS=1nU5vWVmxLJv-HSLrjsvrr7aNnxee62HKEuDJzvCrVtG-y_-ySK81Tx4PAV1VJD7qKr-K6zZ8EoKh-tmCvEJIpA0H8skc0T0C9F2yFWHdQhECgtCf1nkcaq8Pk8_mwsZad_o9_U9NJ3Q61WO8zxA-w==",
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

with open('weibo.html','w',encoding='utf-8') as fp:
    fp.write(content)