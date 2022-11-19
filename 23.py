while True:
    num=input("请输入随机的三个整数并用空格隔开：")
    num=num.split()
    num1=list(map(int,list(num)))
    num1.sort()
    print(num1)
