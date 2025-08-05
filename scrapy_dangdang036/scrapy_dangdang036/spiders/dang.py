import scrapy


class DangSpider(scrapy.Spider):
    name = "dang"
    allowed_domains = ["category.dangdang.com"]
    start_urls = ["https://category.dangdang.com/pg100-cp01.01.01.00.00.00.html"]

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
            name = li.xpath('.//img/@alt').extract_first()
            price = li.xpath('.//p[@class="price"]/span[1]/text()').extract_first()
            print(src, name, price)

