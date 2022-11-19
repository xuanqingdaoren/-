symple=input('随便输入')
num=le=sp=ot=0
i=0
for i in range(len(symple)):
    if'a'<=symple[i]<='z' or 'A'<=symple<='Z':
        le+=1
    elif'0'<=symple[i]<='9':
        num+=1
    elif symple[i]==' ':
        sp+=1
    else:
        ot+=1
print('英文字母：'+str(le)+'数字：'+str(num)+'空格'+str(sp)+'标点'+str(ot))
