while True:
    try:
        n = int(input("输入年份(如2000)"))
    except:
        print("请重新输入")
        continue
    if n % 4 == 0 and n % 400 == 0:
        print("该年为闰年")
    else:
        print("概念不是闰年")

