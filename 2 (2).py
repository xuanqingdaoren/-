while True:
    from math import sqrt
    a=input('请输入一个整数：')
    def isprime(a):
        try:
            n=eval(a)
            if type(n)!=type(1):
                print('请输入整数！')
            else:
                if n==1:
                    return False
                for i in range(2,int(sqrt(n))+1):
                    if n%i==0:
                        return False
                    return True
        except:
            print('请输入数字')
    print(isprime(a))
    m=input('是否退出？<y/n>:')
    if m=='y':
        break
    elif m=='n':
        continue
        
