# 集合（set）的语法及示例

# 1. 集合的定义（使用大括号{}，元素唯一，不重复）
s1 = {1, 2, 3, 4}
s2 = {"apple", "banana", "orange"}
s3 = set()  # 创建一个空集合，不能用 s3 = {}（那是空字典）

print("s1:", s1)
print("s2:", s2)
print("s3:", s3)

# 2. 集合自动去重
s4 = {1, 2, 2, 3, 4, 4, 5}
print("集合自动去重：", s4)

# 3. 集合的常用操作
# 添加元素
s1.add(5)
print("添加5后：", s1)

# 移除元素（如果不存在会报错）
s1.remove(2)
print("移除2后：", s1)

# 安全移除（不存在不会报错）
s1.discard(100)
print("安全移除100后：", s1)

# 随机删除一个元素
removed = s1.pop()
print("随机删除一个元素：", removed, "剩下：", s1)

# 清空集合
s2.clear()
print("s2清空后：", s2)

# 4. 集合的遍历
print("遍历s4：")
for item in s4:
    print(item)

# 5. 集合之间的运算
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# 并集
print("a | b（并集）：", a | b)
print("a.union(b)：", a.union(b))

# 交集
print("a & b（交集）：", a & b)
print("a.intersection(b)：", a.intersection(b))

# 差集
print("a - b（a独有）：", a - b)
print("a.difference(b)：", a.difference(b))

# 对称差集
print("a ^ b（对称差集）：", a ^ b)
print("a.symmetric_difference(b)：", a.symmetric_difference(b))

# 6. 集合的关系判断
print("a是否是b的子集：", a.issubset(b))
print("{3,4}.issubset(a):", {3, 4}.issubset(a))
print("a是否是b的超集：", a.issuperset(b))
print("a和b是否没有交集：", a.isdisjoint(b))

# 7. 集合的其它用法
# 集合可用于去除列表中的重复元素
lst = [1, 2, 2, 3, 4, 4, 5]
no_repeat = list(set(lst))
print("去除列表重复后的结果：", no_repeat)

# 集合不支持下标和切片（因为无序）
# s1[0]  # 会报错

