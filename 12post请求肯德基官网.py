#1页
#https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
#pageIndex:1

#https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
#post
#cname :北京
# pid:
# pageIndex:2
# pageSize :10
import urllib.request
import urllib.parse

def create_request(page):
    base_url = 'https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    data = {
        "cname": "北京",
        "pid": "",
        "pageIndex":page,
        "pageSize": 10

    }
    data = urllib.parse.urlencode(data).encode('utf-8')
    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0'
    }
    request = urllib.request.Request(url=base_url,data=data,headers=headers)
    return request
def get_content(request):
    response = urllib.request.urlopen(request)
    connect = response.read().decode('utf-8')
    return connect

def down_load(page, connect):
    with open('kfc'+str(page)+'.json', 'w', encoding='utf-8') as fp:
        fp.write(connect)

base_url= 'https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

if __name__ == '__main__':
    staret_page = int(input('请输入起始页码：'))
    end_page = int(input('请输入结束页码：'))
    for page in range(staret_page, end_page+1):
       request=create_request(page)
       #获取响应数据
       content = get_content(request)
       #下载
       down_load(page,content)
