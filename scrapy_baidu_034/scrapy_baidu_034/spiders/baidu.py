import scrapy


class BaiduSpider(scrapy.Spider):
    # 爬虫的名字 一般用于爬虫的时候使用的值
    name = "baidu"
    # 允许的域名
    allowed_domains = ["www.baidu.com"]
    # 起使的URL 一般指的是起始的URL
    start_urls = ["https://www.baidu.com"]

    # 是执行了start_urls之后的方法  response就是返回的那个对象
    # 相当于 response = urllib.request.urlopen(url)
    # 相当于 response = requests.get(url)
    def parse(self, response):
        print('苍茫的宇宙')
