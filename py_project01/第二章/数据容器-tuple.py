# ----------------------------
# 元组（tuple）的语法及示例

# 1. 元组的定义（用小括号()，元素间用逗号,隔开,不加小括号也可以，建议加上）
t1 = 1, 2, 3, 4
t2 = ("python", 123, True)
t3 = (2,)  # 注意：只有一个元素的元组，必须加逗号
t4 = ()    # 空元组

print("t1:", t1)
print("t2:", t2)
print("t3:", t3)
print("t4:", t4)

# 2. 元组的下标和切片（和列表类似）
print("t1[0]:", t1[0])
print("t2[-1]:", t2[-1])
print("t1[1:3]:", t1[1:3])

# 3. 遍历元组
print("遍历t1：")
for item in t1:
    print(item)

# 4. 元组的不可变性
# t1[0] = 10  # 会报错，元组不能修改元素

# 5. 元组的常用操作
print("t1的长度：", len(t1))
print("最大值：", max(t1))
print("最小值：", min(t1))
print("3在t1中吗？", 3 in t1)
print("4不在t1中？", 4 not in t1)
print("t1重复两次：", t1 * 2)
print("t1和t3拼接：", t1 + t3)

# 6. 元组可以用于多个变量一次赋值（解包）
x, y, z, w = t1
print(f"x={x}, y={y}, z={z}, w={w}")

# 7. 嵌套元组
t5 = (1, (2, 3), 4)
print("嵌套元组t5:", t5)
print("访问嵌套元素：", t5[1][1])

# 8. 元组和列表的互相转换
lst = [5, 6, 7]
t6 = tuple(lst)
print("列表转元组：", t6)
lst2 = list(t1)
print("元组转列表：", lst2)

# 9. 元组的count和index方法使用说明

# (1) count方法：统计某个元素在元组中出现的次数
t7 = (1, 2, 3, 2, 4, 2, 5)
print("元组t7:", t7)
print("2在t7中出现的次数：", t7.count(2))
print("6在t7中出现的次数：", t7.count(6))

# (2) index方法：查找某个元素在元组中第一次出现的下标
print("2在t7中第一次出现的位置：", t7.index(2))
# print("6在t7中的位置：", t7.index(6))  # 如果元素不存在会报错

# 10. 组包与解包
# 组包：把多个值“打包”成一个元组
a = 10
b = 20
c = 30
packed = a, b, c  # 这其实就是组包形成元组
print("组包后的元组：", packed)

# 解包：将元组中的元素依次赋值给多个变量
d, e, f = packed
print("解包后的变量：d={}, e={}, f={}".format(d, e, f))

# 组包和解包也可以和函数配合使用
def get_point():
    x = 3
    y = 7
    return x, y  # 返回一个元组，自动组包

point = get_point()
print("函数返回的元组：", point)

px, py = get_point()  # 自动解包
print("解包后的坐标：px={}, py={}".format(px, py))

# 还可以使用星号(*)进行扩展解包
t8 = (1, 2, 3, 4, 5)
first, *middle, last = t8
print("first:", first)
print("middle:", middle)
print("last:", last)
