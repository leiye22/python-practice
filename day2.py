#coding=utf-8
import random
n = random.randint(1,100)
flag = 0
while flag != n:
    flag = int(input("请输入1-100之间的数字"))
    if flag > n:
        print("你猜的数字大了")
    elif flag < n:
        print("你猜的数字小了")
    else:
        print("恭喜你猜对了")