a='hello world'
b='abcdefg'
print(type(a))
print(type(b))

#一对引号字符串
name1='Tom'
name2='Rose'

#三引号字符串
name3='''Tom'''
name4="""Rose"""
a='''i am Tom,
     nice to meet you！'''
b="""i am Rose,
     nice to meet you!"""
c="I'm Tom"
d='I\'m Tom'

#字符串输出
print('hello world')
name='Tom'
print('我的名字是%s'%name)
print(f'我的名字是{name}')

#字符串输入
name=input('请输入您的名字：')
print(f'您输入的名字是{name}')
print(type(name))

password=input('请输入您的密码：')
print(f'您输入的密码是{password}')
print(type(password))

# 需求：字符串 name = "abcdef" ，取到不同下标对应的数据。
name='abcdef'
print(name[1])
print(name[0])
print(name[2])

#切片
name='abcdefg'
#cde
print(name[2:5:1])
#cde
print(name[2:5])
#abcde
print(name[:5])
#bcdef
print(name[1:])
#abcdefg
print(name[:])
#aceg
print(name[::2])
#abcdef
print(name[:-1])
#def
print(name[-4:-1])
#gfedcba
print(name[::-1])

#查找
mystr = "hello world and superctest and chaoge and Python"
print(mystr.find('and'))
print(mystr.find('and',15,30))
print(mystr.find('ands'))

print(mystr.index('and'))
print(mystr.index('and',15,30))
print(mystr.index('ands'))

print(mystr.count('and'))
print(mystr.count('ands'))
print(mystr.count('and',0,20))

#修改
print(mystr.replace('and','he'))
print(mystr.replace('and','he',10))
print(mystr)

print(mystr.split('and'))
print(mystr.split('and',2))
print(mystr.split(''))
print(mystr.split('',2))

list1=['chao', 'ge', 'test', 'promotion']
t1= ('aa', 'b', 'cc', 'ddd')
print('_'.join(list1))
print('...'.join(t1))

print(mystr.capitalize())
print(mystr.title())
print(mystr.lower())
print(mystr.upper())

#删除
print(mystr.lstrip())
print(mystr.rstrip())
print(mystr.strip())

print(mystr.ljust(10,'.'))
print(mystr.ljust(10))
print(mystr.center(10))
print(mystr.center(10,'.'))

#判断
print(mystr.startswith('hello'))
print(mystr.startswith('hello',5,20))
print(mystr.endswith('Python'))
print(mystr.endswith('python'))
print(mystr.endswith('Python',2,20))

mystr1='hello'
mystr2='hello12345'
mystr3='12345'
mystr4='12345-'
mystr5='1 2 3 4 5'
mystr6='          '

print(mystr1.isalpha())
print(mystr2.isalpha())
print(mystr1.isdigit())
print(mystr3.isdigit())
print(mystr2.isalnum())
print(mystr4.isalnum())
print(mystr5.isspace())
print(mystr6.isspace())