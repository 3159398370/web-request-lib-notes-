# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyDangdang036Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 数据结构 要下载的数据都有什么
    src = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
