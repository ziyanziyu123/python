# -*- coding: utf-8 -*-
"""
Python 算术运算符演示
"""

# 定义两个变量
a = 10
b = 3

# 加法 +
print(f"{a} + {b} = {a + b}")      # 结果: 13

# 减法 -
print(f"{a} - {b} = {a - b}")      # 结果: 7

# 乘法 *
print(f"{a} * {b} = {a * b}")      # 结果: 30

# 除法 / (结果为浮点数)
print(f"{a} / {b} = {a / b}")      # 结果: 3.3333...

# 整除 // (只取整数部分)
print(f"{a} // {b} = {a // b}")    # 结果: 3

# 取余 % (获取余数)
print(f"{a} % {b} = {a % b}")      # 结果: 1

# 幂运算 ** (求次方)
print(f"{a} ** {b} = {a ** b}")    # 结果: 1000 (10的3次方)


# ========================================
# 赋值运算符演示
# ========================================
print("\n--- 赋值运算符 ---")

# 基本赋值 =
num = 10
print(f"num = 10, num的值: {num}")

# 加法赋值 +=
num += 5   # 等同于 num = num + 5
print(f"num += 5, num的值: {num}")    # 结果: 15

# 减法赋值 -=
num -= 3   # 等同于 num = num - 3
print(f"num -= 3, num的值: {num}")    # 结果: 12

# 乘法赋值 *=
num *= 2   # 等同于 num = num * 2
print(f"num *= 2, num的值: {num}")    # 结果: 24

# 除法赋值 /=
num /= 4   # 等同于 num = num / 4
print(f"num /= 4, num的值: {num}")    # 结果: 6.0

# 整除赋值 //=
num = 17
num //= 3  # 等同于 num = num // 3
print(f"num = 17, num //= 3, num的值: {num}")  # 结果: 5

# 取余赋值 %=
num = 17
num %= 5   # 等同于 num = num % 5
print(f"num = 17, num %= 5, num的值: {num}")   # 结果: 2

# 幂赋值 **=
num = 2
num **= 3  # 等同于 num = num ** 3
print(f"num = 2, num **= 3, num的值: {num}")   # 结果: 8

# 比较运算符演示
print("\n--- 比较运算符 ---")

x = 10
y = 5

print(f"x = {x}, y = {y}")

# 等于 ==
print(f"x == y: {x == y}")   # False

# 不等于 !=
print(f"x != y: {x != y}")   # True

# 大于 >
print(f"x > y: {x > y}")     # True

# 小于 <
print(f"x < y: {x < y}")     # False

# 大于等于 >=
print(f"x >= y: {x >= y}")   # True

# 小于等于 <=
print(f"x <= y: {x <= y}")   # False
