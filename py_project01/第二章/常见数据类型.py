# 常见数据类型
from tokenize import String


print("hello1")
print(type("hello"))
print(isinstance("hellp",str))
print(isinstance("hellp", int))


# 字符串
s1 = "hello"
s2 = 'python'
s3  = """
我单位承诺上述内容属实，并知悉
《非经营性互联网信息服务备案管理办法》
“第二十二条第二款，超出备案的项目提供服务的，
由住所所在地省通信管理局责令限期改正，
并处五千元以上一万元以下罚款；拒不改正的，
关闭网站并注销备案。”、“第二十三条，填报虚假备案信息
的，由住所所在地省通信管理局关闭网站并注销备案”
等规定。
"""
print(s3)

msg = 'It\'s very good'
age = 18
print("她说" + msg + str(age))
print(f"她说, {msg}  {age}")