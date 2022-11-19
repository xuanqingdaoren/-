a=eval(input("请输入一个数："))
b=eval(input("请输入另一个数："))
d=a*b
if a>b:
    while a%b!=0:
        c=a%b
        a=b
        b=c
    e=int(d/b)
    print('两个数的最大公约数为:'+str(b)+'\n两个数的最小公倍数为:'+str(e))
elif a<b:
    while b%a!=0:
        c=a%b
        b=a
        a=c
    e=int(d/a)
    print('两个数的最大公约数为:'+str(a)+'\n两个数的最小公倍数为:'+str(e))
else:
    print('最大公约数和最大公倍数都是:'+str(a))

    
        
