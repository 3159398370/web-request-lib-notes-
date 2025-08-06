# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# 如果想使用管道的话，那么必须在配置文件中配置管道
class ScrapyDangdang036Pipeline:
    def open_spider(self, spider):
        self.fp = open('book.json', 'w', encoding='utf-8')
    # item 就是yiejie后面的book对象
    def process_item(self, item, spider):
    #下面这种方法操作太频繁
    # # w 方法必须要写字符串
    #     with open('book.json', 'a', encoding='utf-8') as fp:
    #         fp.write(str(item))
        self.fp.write(str(item))
        return  item
    def close_spider(self, spider):
        self.fp.close()
#多条管道同时开启
import urllib.request
class DangDangDownloadPipeline:
    def process_item(self, item, spider):
        url = 'http:' + item.get('src')
        filename = './books/'+ item.get('name')+'.jpg'
        urllib.request.urlretrieve(url = url ,filename= filename)




        return item