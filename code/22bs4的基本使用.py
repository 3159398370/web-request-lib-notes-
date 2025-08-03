from  bs4 import BeautifulSoup
from matplotlib.pyplot import title

#默认打开的是gbk 编码
soup = BeautifulSoup(open('075_尚硅谷_爬虫_解析_bs4的基本使用.html',encoding='utf-8'), 'lxml')
#获取第一个a标签
print(soup.a)
#获取标签的属性和属性值
print(soup.a.attrs)

#bs4的一些函数
#（1）find
#返回的是第一个匹配的标签
# print(soup.find('a'))
# print(soup.find('a',title='a2'))
#根据class属性来找对对应的标签对象，注意class属性的值不能用class来获取
# print(soup.find('a',class_='a1'))
# (2)find_all
# print(soup.find_all(['a','span']))
# (3)select
#select方法返回的是一个列表，并且会返回多个数据
print(soup.select('a1'))