print("项目  1、十转二、八、十六进制；2、二转十、八、十六进制；3、八转十、二、十六进制；4、十六转二、八、十进制。")
m = int(input("请输入所需项目编号（如1）：")) 
if m == 1:
    print("2,8,16")
    n = int(input("请选择转换后进制"))
    o = int(input("请输入："))
    if n == 2:
        o = bin(o)
        print('该进制转为二进制为：',format(o))
    elif n == 8:
        o = oct(o)
        print('该进制转为八进制为：',format(o))
    elif n == 16:
        o = hex(o)
        print('该进制转为十六进制为：',format(o))
elif m == 2:
    print("8,10,16")
    n1 = int(input("请选择转换后进制"))
    p = input("请输入：")
    if n1 == 8:
        p = int(p,2)
        p1 = oct(p)
        print('该进制转为八进制为：',format(p1))
    elif n1 == 10:
        p = int(p,2)
        print('该进制转为十进制为：',format(p))
    elif n1 == 16:
        p = int(p,2)
        p1 = hex(p)
        print('该进制转为十六进制为：',format(p1))
elif m == 3:
    print("2,10,16")
    n2 = int(input("请选择转换后进制"))
    q = input("请输入：")
    if n2 == 2:
        q = int(q,8)
        q1 = bin(q)
        print('该进制转为二进制为：',format(q1))
    elif n2 == 10:
        q = int(q,8)
        print('该进制转为十进制为：',format(q))
    elif n2 == 16:
        q = int(q,8)
        q1 = hex(q)
        print('该进制转为十六进制为：',format(q1))
elif m == 4:
    print("2,8,10")
    n3 = int(input("请选择转换后进制"))
    r = input("请输入：")
    if n3 == 2:
        r = int(r,16)
        r1 = bin(r)
        print('该进制转为二进制为：',format(r1))
    elif n3 == 8:
        r = int(r,16)
        r1 = oct(r)
        print('该进制转为八进制为：',format(r1))
    elif n3 == 10:
        r = int(r,16)
        print('该进制转为十进制为：',format(r))


    
        
           
