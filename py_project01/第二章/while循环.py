
i = 0

while i < 10:
    i += 1
    if i == 5:
        continue #中断本次循环进入下一次循环 
    print(f"python基础语法学习第{i}周")
    # break #跳出循环 ，else代码不执行
    
else:
    print("完成学习")