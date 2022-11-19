while True:
    a = input("输入一个五位自然数：")
    b = a[::-1]
    if a == b:
        print("此数是回文数列")
    else:
        print("此数不是回文数列")
    num = input("输入y退出")
    if num == "y":
        break
