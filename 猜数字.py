import random
target=random.randint(1,100)
count=0
while True:
    try:
        num=eval(input("请输入数字(0~100整数)"))
    except:
        print("请输入数字！")
        continue
    count=count+1
    if num>target:
        print("猜大了！")
    elif num<target:
        print("猜小了！")
    else:
        print("猜对了！")
        break
print("此轮猜测次数是：",count)
