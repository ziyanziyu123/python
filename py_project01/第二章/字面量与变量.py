# 字面量的写法
print(100) # 整数(int )
print(True)
print("hello")
print(None)
print(True + 1)

# 变量(python是动态类型语言，一个变量可以存储不同类型数据，但是项目开发中，推荐变量只存储一种类型数据)
num = 1114.1
print(num)

num = "OK"
print(num)

#案例
base = 20.7
incr = 50
print("未来一个月的播放量：", base + incr)
print("未来两个月的播放量：", base + incr + incr)

#一次定义多个变量
a,b,c = 100,200,300
d = a
e = b
a = c
b = d 
c = e
print(a,b,c)

