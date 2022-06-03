
#菱形
n=0
while n<=3:
    print(" "*(5-n)+'*'*(2*n+1))
    n+=1
n-=1
while n>0:
    print(" "*(6-n)+"*"*(2*n-1))
    n-=1
