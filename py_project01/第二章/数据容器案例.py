#定义列表
num_list = []

#列表赋值
for  n in range(0,10):
    num_list.append(int(input(f"请输入列表中的第{n + 1}个元素(整数)：")))

print(f"打印列表：\n{num_list}")

num_list.sort()
print(f"对列表进行排序：\n{num_list}")

max = min = agv = num_list[0]
total = 0
#求最大值
for m in num_list:
    if m >= max:
        max = m
print(f"最大值是：{max},{max(num_list)}")        

#求最小值
for m in num_list:
    if m <= min:
        min = m
print(f"最小值是：{min}")        

#求平均值
for m in num_list:
    total += m

print(f"平均值是：{total / len(num_list)}")
