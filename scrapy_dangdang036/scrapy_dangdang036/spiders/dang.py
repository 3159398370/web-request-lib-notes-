import scrapy
from scrapy_dangdang036.items import ScrapyDangdang036Item

class DangSpider(scrapy.Spider):
    name = "dang"
    allowed_domains = ["category.dangdang.com"]
    start_urls = ["https://category.dangdang.com/pg100-cp01.01.01.00.00.00.html"]
    base_url = "https://category.dangdang.com/pg"
    page = 1

    def parse(self, response):

# src = //ul[@id="component_59"]/li//img/@src
# alt = //ul[@id="component_59"]/li//img/@alt
# price = //ul[@id="component_59"]/li//p[@class="price"]/span[1]/text()
# extract_first(): 这个方法仅提取匹配到的第一个元素，并以字符串形式返回。如果没有找到任何匹配项，则返回None。
# extract(): 这个方法将匹配到的所有元素提取出来，并以列表形式返回。如果没有找到任何匹配项，则返回一个空列表。
        #所有的selector的对象都能再次调用xpath方法
        li_list = response.xpath('//ul[@id="component_59"]/li')
        for li in li_list:
            src = li.xpath('.//img/@data-original').extract_first()
        # 第一张图片不是懒加载
            if src:
                src = src
            else:
                src = li.xpath('.//img/@src').extract_first()

            name = li.xpath('.//img/@alt').extract_first()
            price = li.xpath('.//p[@class="price"]/span[1]/text()').extract_first()
            print(src, name, price)
            book = ScrapyDangdang036Item(src= src, name= name, price= price)
            #yield 相当于retrun返回一个值
            yield book
            # 每一页的爬取数据都是一样的，所以我们可以使用scrapy提供的方法来获取下一页的url
            # http://category.dangdang.com/pg2-cp01.01.01.00.00.00.html
        if self.page < 100:
            self.page = self.page + 1
            url = self.base_url + str(self.page) + "-cp01.01.01.00.00.00.html"
            # scrapy.Request就是scrapy的get请求对象
            yield scrapy.Request(url=url, callback=self.parse)