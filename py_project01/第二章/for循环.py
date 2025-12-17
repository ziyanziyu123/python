# msg = input("请输入需要遍历的字符串：")

# for s in msg:
#     print(f"遍历的元素：{s}")
# else:
#     print("遍历完成！")


# total = 0
# for i in range(101): #range(0,101,2)
#     if i % 2  == 1:
#         total += i


# print(f"1到100之间的奇数和为：{total}")


# m = int(input("请输入长方形的长度："))
# n = int(input("请输入长方形的宽度："))

# for i in  range(n):
#     for j in range(m):
#       print("*",end="  ")  
#     print()

for i in range(1,10):
    for j in range(1,i + 1):
        print(f"{j} x {i} = {j * i}",end="\t")
    print()