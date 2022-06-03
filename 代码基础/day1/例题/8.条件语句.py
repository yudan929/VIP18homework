# # 需求分析：如果⽤户年龄⼤于等于18岁，即成年，输出"已经成年，可以上⽹"。
# age=input('请输入您的年龄：')
# if int(age)>=18:
#     print('已经成年，可以上网')
# else:
#     print('未成年')
#
# # 思考：中国合法⼯作年龄为18-60岁，即如果年龄⼩于18的情况为童⼯，不合法；
# # 如果年龄在18-60岁之间为合法⼯龄；⼤于60岁为法定退休年龄。
# age=input('请输入您的年龄：')
# age=int(age)
# if age<18:
#     print('童工，不合法')
# elif age>60:
#     print('已退休')
# elif age>=18 and age<=60:
#     print('合法')
# else:
#     print('输入错误！')
#
# #思考：坐公交：如果有钱可以上⻋，没钱不能上⻋；上⻋后如果有空座，则可以坐下；如果没空座，就要站着。怎么书写程序？
# mo=input('是否有钱？y/n')
# if mo=='y':
#     print('请上车')
#     s=input('是否有空位？y/n')
#     if s=='y':
#         print('请坐')
#     else:
#         print('站着')
# else:
#     print('没有钱不能上车')

#猜拳游戏
import  random
player=input('请出拳：石头-0，剪刀-1，布-2：')
player=int(player)
computer=random.randint(0,2)
if player==computer:
    print('平局')
elif (player==0 and computer==2)or(player==1 and computer==0)or(player==2 and computer==1):
    print('计算机胜出')
else:
    print('玩家赢')
