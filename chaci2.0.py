word = open('1.txt','r',encoding='utf-8').readlines()
lt=[]
ls=[]
counts={}
for line in word:
    for i in line:
        #print(i)
        lt.append(i)
        #print(lt)
for i1 in lt:
    if i1=='行':
        ls.append(lt.index(i1))
        if lt[(lt.index(i1))+1]=='者':
            counts['行者']=counts.get('行者',0)+1
            lt[lt.index(i1)]='1'
            continue
        elif lt[(lt.index(i1))+1]!='者':
            lt[lt.index(i1)] = '1'
            continue
        continue
    elif i1=='八':
        ls.append(lt.index(i1))
        if lt[(lt.index(i1)) + 1] == '戒':
            counts['八戒']=counts.get('八戒',0)+1
            lt[lt.index(i1)] = '2'
            continue
        elif lt[(lt.index(i1)) + 1] != '戒':
            lt[lt.index(i1)] = '2'
            continue
        continue
    elif i1=='沙':
        ls.append(lt.index(i1))
        if lt[(lt.index(i1)) + 1] == '僧':
            counts['沙僧'] = counts.get('沙僧', 0) + 1
            lt[lt.index(i1)] = '3'
            continue
        elif lt[(lt.index(i1)) + 1] != '僧':
            lt[lt.index(i1)] = '3'
            continue
        continue
    elif i1=='三':
        ls.append(lt.index(i1))
        if lt[(lt.index(i1)) + 1] == '藏':
            counts['三藏'] = counts.get('三藏', 0) + 1
            lt[lt.index(i1)] = '4'
            continue
        elif lt[(lt.index(i1)) + 1] != '藏':
            lt[lt.index(i1)] = '4'
            continue
        continue
    continue
#print(counts)
#print(ls)
lists=list(counts.items())
for df in lists:
    print(df)


