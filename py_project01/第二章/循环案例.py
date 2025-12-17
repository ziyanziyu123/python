import random

random_num = random.randint(1,100)#生成随机数



while True:
    num = int(input("请输入一个你猜测的数（1-100之间）："))
    if num > random_num:
        print("你输入的数字大了！")
    elif num < random_num:
        print("你输入的数小了！")
    else:
        print("恭喜你，猜对了！")
        break

