while True:
    def tongji():
        str1=input('随便输')
        zimu=shuzi=kongge=qita=0
        for i in str1:
            if 'a'<=i<='z' or 'A'<=i<='Z':
                zimu += 1
            elif '0'<=i<='9':
                shuzi += 1
            elif i==' ' :
                kongge += 1
            elif:
                qita += 1
        print('字母{}数字{}空格{}其他{}'.format(zimu,shuzi,kongge,qita))
    tongji()
    m=input('是否退出？<y/n>:')
    if m=='y':
        break
    elif m=='n':
        continue
