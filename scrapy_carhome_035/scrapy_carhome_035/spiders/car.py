import scrapy

class CarSpider(scrapy.Spider):
    name = "car"
    allowed_domains = ["www.autohome.com.cn"]
    start_urls = ["https://www.autohome.com.cn/price/brandid_15?pvareaid=104399"]

    def parse(self, response):
        name_list = response.xpath('//div[@class="tw-mb-2 tw-flex tw-flex-wrap tw-items-center"]/a/text()')
        name_price = response.xpath('//div[contains(@class, "tw-mb-2.5") and contains(@class, "tw-text-[#828CA0]")]/a/text()')
        with open('car.txt', 'w', encoding='utf-8') as f:
           for i in range(len(name_list)):
               name= name_list[i].extract()
               price= name_price[i].extract()
               f.write(name+' '+price+'\n')
               print(name+' '+price)
