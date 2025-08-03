# fp = open('test.txt','w')

# fp.write('hello word')
#
# fp.close()

# fp= open('test.txt','w')
# name_list=['zhangsan','lisi']
#
# fp.write(name_list)


# # 序列化的两种方式
# fp= open('test.txt','w')
# name_list=['zhangsan','lisi']
#
# import json
# names=json.dumps(name_list)
#
# print(names)
#
# fp.write(names)

fp = open('test.txt','r')

content = fp.read()
print(content)

import json
result = json.loads(content)
print(result)
print(type(result))

fp.close()