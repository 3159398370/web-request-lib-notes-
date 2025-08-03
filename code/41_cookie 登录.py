# 通过登录 进入到主页面
#
# {
#     "source": "http://www.gushiwen.cn/user/collect.aspx",
#     "email": "19092419643@163.com",
#     "pwd": "933tu1212",
#     "code": "aekc",
#     "__VIEWSTATE": "/wEPDwUKLTU5OTg0MDIwNw8WAh4TVmFsaWRhdGVSZXF1ZXN0TW9kZQIBZGQGi0FCmPHMP+KelvQVsoBoqE2Axg==",
#     "__VIEWSTATEGENERATOR": "C93BE1AE"
# }

# 我们观察到，登录页面的请求头中，有__VIEWSTATE和__VIEWSTATEGENERATOR两个参数，这两个参数是动态的，所以我们需要获取这两个参数，

#难点：(1)_viewstate和_viewstategenerator参数的获取
#我们观察到这两个数据在页面的源码中，所以我们需要获取页面的源码，然后进行解析就可以了

# (2)验证码
import requests
url = "https://www.gushiwen.cn/user/login.aspx?from=http://www.gushiwen.cn/user/collect.aspx"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}
response = requests.get(url=url,headers=headers)
content = response.text
#解析页面源码 获取_viewstate和_viewstategenerator参数
from bs4 import BeautifulSoup
soup = BeautifulSoup(content,'lxml')
# 获取_viewstate
viewstate =  soup.select('#__VIEWSTATE')[0].attrs.get('value')

# 获取_viewstategenerator
viewstategenerator = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')
# print(viewstate)
# print(viewstategenerator)
#获取验证码图片
code = soup.select('#imgCode')[0].attrs.get('src')
# print( code)
code_url = 'https://www.gushiwen.cn' + code

# 获取到验证码的图片之后 下载到本地 观察验证码 手动输入
code_name = input('请输入验证码：')

#点击登录
url_post ='https://www.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fwww.gushiwen.cn%2fuser%2fcollect.aspx'
data_post= {

}