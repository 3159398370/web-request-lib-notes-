from lxml import etree

#xpath 解释
#(本地文件) etree.paser
#(2)服务器响应文件 response.read().decode('utf-8') etree.HTML()

tree = etree.parse('17xml导入.html')

#tree.xpath('xpath路径')
# tree.xpath()
#查找ul下面的li
#text()获取标签中的内容
# li_list = tree.xpath('//ul/li')
# #判断列表的长度
# print(li_list)
# print(len(li_list))
#查找所有有id属性的li标签
# li_list = tree.xpath('//li[@id]/text()')
# print(li_list)
#查找所有有id属性为l1的li标签的属性值
# li_list = tree.xpath('//li[@id="l1"]/text()')
# print(li_list)
# print(len(li_list))
#查找id为l1的li标签的class属性值
li_list = tree.xpath('//li[@id="l1"]/@class/text()')
print(li_list)
print(len(li_list))