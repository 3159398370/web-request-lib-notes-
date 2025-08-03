import urllib.request
import urllib.parse

def create_request(page):
    base_url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'
    data = {'start': (page-1)*20, 'limit': 20}
    data = urllib.parse.urlencode(data)
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0'}
    url = base_url + data
    request = urllib.request.Request(url=url, headers=headers)
    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    return response.read().decode('utf-8')

def down_load(page, connect):
    with open(f'douban{page}.json', 'w', encoding='utf-8') as fp:
        fp.write(connect)

if __name__ == '__main__':
    start_page = int(input('请输入起始页码：'))  # 修正拼写
    end_page = int(input('请输入结束页码：'))

    for page in range(start_page, end_page+1):
        request = create_request(page)
        connect = get_content(request)
        down_load(page, connect)