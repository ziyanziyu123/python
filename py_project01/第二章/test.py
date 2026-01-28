# 字符串是不可变的，不能通过索引赋值修改
s = "python"
# s[1] = 'h'  # 错误：字符串不支持项赋值

# replace() 并没有修改原字符串，而是返回一个【新字符串】
print("--- 演示 replace 不会修改原字符串 ---")
s1 = "hello"
print(f"原字符串 s1: {s1}, 内存地址: {id(s1)}")

s2 = s1.replace('e', 'a')  # replace 返回新字符串
print(f"新字符串 s2: {s2}, 内存地址: {id(s2)}")
print(f"原字符串 s1: {s1}, 内存地址: {id(s1)}")  # s1 没有变！

print("\n--- 对比 ---")
result = s1 is s2
print(f"s1 和 s2 是同一个对象吗？ {result}")  # False，是两个不同的对象