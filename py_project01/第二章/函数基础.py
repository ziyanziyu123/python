# ----------------------------
# Python 函数基础讲解与示例

# 1. 什么是函数？
# 函数是组织好的、可重复使用的代码，用来实现特定的功能。

# 2. 函数的定义
def say_hello():
    print("Hello, Python函数！")

# 3. 如何调用函数
say_hello()  # 调用函数

# 4. 带参数的函数
def add(a, b):
    """返回两个数的和"""
    result = a + b
    return result

print("add(5, 3) =", add(5, 3))  # 输出：add(5, 3) = 8

# 5. 参数的类型
def repeat(msg, times):
    """重复输出msg, 共times次"""
    for i in range(times):
        print(msg)

repeat("你好", 2)

# 6. 返回值
def get_sum_and_diff(x, y):
    """返回x+y和x-y，一次返回多个值"""
    return x + y, x - y

my_sum, my_diff = get_sum_and_diff(10, 3)
print("和:", my_sum, "差:", my_diff)

# 7. 位置参数、默认参数
def greet(name, msg="欢迎学习Python！"):
    print(f"{name}，{msg}")

greet("小明")
greet("小李", "早上好！")

# 8. 可变参数(*args, **kwargs)
def demo_args(*args):
    print("所有位置参数：", args)

demo_args(1, 2, 3, "abc")

def demo_kwargs(**kwargs):
    print("所有关键字参数：", kwargs)

demo_kwargs(a=10, b=20, c=30)

# 9. 文档字符串/函数说明
def square(n):
    """返回一个数的平方
    参数:
        n: 数值
    返回:
        n的平方
    """
    return n * n

print("square(4) =", square(4))
print("square函数说明：", square.__doc__)

# 10. 局部变量和全局变量
y = 100  # 全局变量

def func():
    x = 10  # 局部变量
    print("x=", x)
    print("y=", y)  # 可以读取全局变量

func()

# 11. lambda表达式（匿名函数）
f = lambda x, y: x * y
print("lambda函数 f(3,4) =", f(3, 4))

# 12. 小结
# - 函数用def关键词定义，可以有参数、返回值和说明文档；
# - 参数分为位置参数、默认参数、可变参数等；
# - 支持return返回结果（可多个），没有return默认返回None；
# - lambda用于简单匿名函数。

