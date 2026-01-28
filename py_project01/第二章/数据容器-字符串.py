# ----------------------------
# 字符串基础语法说明与示例

# 1. 定义字符串
s1 = "Hello, World!"
s2 = '你好，Python！'
s3 = """这是一个
多行字符串"""
print(s1)
print(s2)
print(s3)

# 2. 字符串作为数据容器的语法与示例

# (1) 下标索引：可以通过下标访问每个字符
print("第一个字符：", s1[0])
print("最后一个字符：", s1[-1])

# (2) 切片：可以切出子字符串（和列表类似）
print("前5个字符：", s1[:5])
print("下标1到4的字符：", s1[1:5])

# (3) 遍历：for循环遍历字符串的每个字符
print("逐字符遍历：")
for ch in s2:
    print(ch, end=" ")
print()

# (4) in/not in 判断成员是否存在
print("'H' 是否在 s1 中？", 'H' in s1)
print("'z' 是否不在 s1 中？", 'z' not in s1)

# (5) len()函数可统计字符串的字符个数
print("s1的长度：", len(s1))

# (6) max() 和 min()
print("s2中的最大字符(按编码):", max(s2))
print("s2中的最小字符(按编码):", min(s2))

# (7) 字符串是不可变的数据容器
# s1[0] = 'h'  # 错误：字符串不能直接修改(会抛出TypeError)

# (8) 转换成列表进行修改
s1_list = list(s1)
s1_list[0] = 'h'
s1_new = ''.join(s1_list)
print("将首字母小写的新字符串：", s1_new)

# 3. 字符串的常用操作

# (1) 拼接
s4 = s1 + " " + s2
print("拼接结果：", s4)

# (2) 重复
s5 = s2 * 3
print("重复字符串：", s5)

# (3) 查找与替换
print("查找World的位置：", s1.find("World"))
print("将Hello替换为Hi：", s1.replace("Hello", "Hi"))

# (4) 大小写转换
print("转为大写：", s1.upper())
print("转为小写：", s1.lower())

# (5) 去除空格
s6 = "   Python学习   "
print("去除左右空格：", s6.strip())

# (6) 分割与连接
s7 = "Python,Java,C++"
splitted = s7.split(",")  # 以,分割为列表
print("分割结果：", splitted)
joined = "-".join(splitted)
print("用-连接：", joined)

# (7) 判断内容
print("是否全是字母：", "abcXYZ".isalpha())
print("是否全是数字：", "12345".isdigit())
print("是否全是空格：", "   ".isspace())

# 4. 字符串格式化
name = "张三"
age = 20
score = 95.5

# (1) 百分号方式
print("姓名：%s，年龄：%d，成绩：%.1f" % (name, age, score))
# (2) format方法
print("姓名：{}，年龄：{}，成绩：{}".format(name, age, score))
# (3) f-string (Python3.6+)
print(f"姓名：{name}，年龄：{age}，成绩：{score}")

# 常见注意：字符串是不可变类型，不能像列表那样通过下标直接修改字符
