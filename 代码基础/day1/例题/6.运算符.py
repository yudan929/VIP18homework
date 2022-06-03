#单个变量赋值
num=1
print(num)

#多个变量赋值
num1,float1,str1=10,0.5,'hello world'
print(num1)
print(float1)
print(str1)

#多变量赋相同值
a=b=10
print(a)
print(b)

a=100
a+=1
print(a)

b=2
b*=3
print(b)

c=10
c+=1+2
print(c)

#比较运算符
a=7
b=5
print(a==b)
print(a!=b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)

#逻辑运算符
a=1
b=2
c=3
print((a<b)and (b<c))
print((a>b)and (b<c))
print((a>b)or(b<c))
print(not (a>b))

#数字之间的逻辑运算
# and运算符，只要有⼀个值为0，则结果为0，否则结果为最后⼀个⾮0数字
a=0
b=1
c=2
print(a and b )
print(b and a)
print(a and c)
print(c and a)
print(b and c)
print(c and b)

# or运算符，只有所有值为0结果才为0，否则结果为第⼀个⾮0数字
print(a or b)
print(a or c)
print(b or c)