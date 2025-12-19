# 列表操作
# 小白学习python，列表语法演示

# 创建一个列表
fruits = ["apple", "banana", "orange",12,13,14,34]#列表中可以有不同类型的元素


# 访问元素
print(f"第一个水果: {fruits[0]}")  # apple

# 修改元素
fruits[1] = "pear"
print(f"修改后的列表: {fruits}")

# 添加元素
fruits.append("watermelon")
print(f"添加新元素后: {fruits}")

# 插入元素
fruits.insert(1, "grape")
print(f"插入元素后: {fruits}")

# 删除元素
del fruits[2]
print(f"删除第3个元素后: {fruits}")

# 弹出元素
last_fruit = fruits.pop()
print(f"弹出最后一个元素: {last_fruit}, 剩下的: {fruits}")

# 移除指定元素
fruits.remove("grape")
print(f"移除grape后: {fruits}")

# 获取列表长度
print(f"水果数量: {len(fruits)}")

# 遍历列表
print("遍历水果列表：")
for fruit in fruits:
    print(fruit)

# 列表切片演示
# 语法: list[起始索引:结束索引:步长]
# 从起始索引开始(包含), 到结束索引(不包含)，步长可选
slice_fruits = fruits[0:2]  # 取第0和第1个元素
print(f"切片fruits[0:2]: {slice_fruits}")

slice_to_end = fruits[1:]  # 从第1个元素到结尾
print(f"切片fruits[1:]: {slice_to_end}")

slice_from_start = fruits[:2]  # 从开头到第2个元素(不含)
print(f"切片fruits[:2]: {slice_from_start}")

slice_with_step = fruits[::2]  # 每隔一个取一个
print(f"切片fruits[::2]: {slice_with_step}")

reversed_fruits = fruits[::-2]  # 反转列表
print(f"切片fruits[::-1] (反转): {reversed_fruits}")

