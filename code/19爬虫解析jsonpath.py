import json
import jsonpath

obj = json.load(open('073_尚硅谷_爬虫_解析_jsonpath.json',encoding='utf-8'))

print(obj)

# # 使用jsonpath从对象中提取所有书籍的作者列表
# author_list = jsonpath.jsonpath(obj,'$.store.book[*].author')
# print(author_list)
#所有的作者
# author_list = jsonpath.jsonpath(obj,'$..author')
# print(author_list)
# store下的所有元素
store_list = jsonpath.jsonpath(obj,'$.store.*')
print(store_list)