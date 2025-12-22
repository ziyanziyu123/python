# 字典（dict）的语法及示例

# 1. 字典的定义（key: value 对，key必须唯一且可哈希）
d1 = {"name": "Tom", "age": 20, "city": "Beijing"}
d2 = dict(a=1, b=2, c=3)  # 另一种定义方式
d3 = {}  # 空字典

print("d1:", d1)
print("d2:", d2)
print("d3:", d3)

# 2. 访问字典的元素
print("d1的name:", d1["name"])
# print(d1["gender"])  # 若key不存在会报错
print("使用get访问不存在的key:", d1.get("gender"))  # 推荐，返回None不报错

# 3. 增加和修改元素
d1["gender"] = "男"  # 新增
d1["age"] = 21      # 修改
print("新增/修改后d1:", d1)

# 4. 删除元素
del d1["city"]    # 按key删除
print("删除city后:", d1)
d1.pop("gender")  # pop并返回被删除的值
print("删除gender后:", d1)

# 5. 遍历字典
print("遍历key：")
for k in d1:
    print(k)
print("遍历value：")
for v in d1.values():
    print(v)
print("遍历key,value：")
for k, v in d1.items():
    print(k, v)

# 6. 常用方法
print("d2中是否含a这个key？", "a" in d2)
d2.clear()       # 清空字典
print("d2清空后：", d2)

# 7. 字典的嵌套和综合示例
student = {
    "name": "Alice",
    "age": 18,
    "scores": {"math": 90, "english": 85}
}
print("嵌套字典student:", student)

# 8. 字典合并（Python 3.5+）
d4 = {"x": 1, "y": 2}
d5 = {"y": 100, "z": 200}
merged = {**d4, **d5}  # y会被d5覆盖
print("合并后的字典:", merged)

