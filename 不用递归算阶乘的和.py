num = int(input("please input a number:"))

sum = 0
for i in range(1,num+1):
    x = 1
    for j in range(1,i+1):
        x = x * j
    sum = sum+ x
print("1!+...+{}!的阶乘结果是{}".format(num,sum))
