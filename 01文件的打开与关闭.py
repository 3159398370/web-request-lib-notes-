# fp=open('test.txt', 'w')
# fp.write(('hello world'))
#
# fp= open('demo/text.txt', 'w')
# fp.write(("hello shanguigu"))
#
# fp.close()
# fp=open('a.text','a')
# fp.write('jiwd,i am here\n'*5)
# fp.close()
fp=open('a.text','r')
# content=fp.read()
# print(content)

content=fp.readlines()
print(content)