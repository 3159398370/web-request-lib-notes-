import scrapy


class BaiduSpider(scrapy.Spider):
    # 爬虫的名字 一般用于爬虫的时候使用的值
    name = "baidu"
    # 允许的域名
    allowed_domains = ["www.baidu.com"]
    # 起使的URL 一般指的是起始的URL
    start_urls = ["https://www.baidu.com"]

    def parse(self, response):
        pass
