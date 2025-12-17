# if 条件判断的示例

# ---- 语法解释 ----
# if 语句用于根据条件判断来执行不同的代码块。
# 基本语法：
# if 条件:
#     语句块1
# elif 条件2:
#     语句块2
# else:
#     语句块3
# 
# 多个条件可以用 elif 增加分支，用 else 定义所有条件都不成立时执行的代码。
# 条件表达式的结果为 True 时，对应的语句块会被执行。
# ------------------

# 示例1：判断一个数是否为正数
num = 5
# 这里判断 num 是否大于0
if num > 0:
    print("num是正数")
    print("num不是负数")

# 示例2：if-else 判断奇偶
number = 4
# 判断 number 是否能被2整除
if number % 2 == 0:
    print(f"{number}是偶数")
else:   # 上面条件不成立时执行
    print(f"{number}是奇数")

# 示例3：if-elif-else 多条件判断
score = 85
# 先判断分数是否优秀，再判断及格与否
if score >= 90:
    print("成绩优秀")
elif score >= 60:   # 上述条件不成立，再判断这个条件
    print("成绩及格")
else:               # 都不成立则执行此分支
    print("成绩不及格")

# 示例4：嵌套if
age = 20
# 先判断是否成年人，再在内部判断是否为老年人
if age >= 18:
    print("成年人")
    if age > 60:
        print("老年人")
else:
    print("未成年")

# account = "17855368219"
# secret = "lcy123"

# Iaccount = input("请输入您的账号：")
# Isecret = input("请输入您的密码：")

# if account != Iaccount:
#     print("您输入的账号错误！") 
# if secret != Isecret:
#     print("您输入的密码错误！")
# else:
#     print("尊敬的业主，欢迎您回家！")

# # 判断闰年
year = int(input("请输入年份："))

if  year % 100 == 0:
    if year % 400 == 0:
        print(f"{year}是闰年！")
    else:
        print(f"{year}不是闰年！")
else:
    if  year % 4 == 0:
        pass # 语法占位的作用
        print(f"{year}是闰年！")
    else:
        print(f"{year}不是闰年！")

