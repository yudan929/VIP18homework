#---输出内容给用户---
print('hello Python')
age=18
print(age)

#---格式化输出---
name='TOM'
weight=75.5
student_id=1
# 我的名字是TOM
print('我的名字是%s' %name)
# 我的学号是0001
print('我的学号是%04d'% student_id)
# 我的体重是75.50公⽄
print('我的体重是%.2f公斤'%weight)
# 我的名字是TOM，今年18岁了
print('我的名字是%s,今年%d岁了'%(name,age))
# 我的名字是TOM，明年19岁了
print('我的名字是%s,我明年%d岁了'%(name,age+1))
# 我的名字是TOM，明年19岁了
print(f'我的名字是{name},我明年{age+1}岁了')

#---转义字符---
print('输出的内容',end='\n')