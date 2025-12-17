import csv
from math import ceil


day = input("请输入星期几（1-7）：")

match day:
    case "1":
        print("周一，噩梦的开始！")
    case "2":
        print("周二，噩梦的延续！")
    case "3":
        print("周三，检查就能看到希望！")
    case "4":
        print("周四，噩梦就要醒了！")
    case "5":
        print("周五，就要胜利了！")
    case "6"|"7":
        print("周末，属于自己的欢乐时间！")
    case _:#匹配其他所有请
        print("不是打工人，滚出去！")

