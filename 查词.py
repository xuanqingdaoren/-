import jieba
txt = open('1.txt','r',encoding='utf-8').read()
words = jieba.lcut(txt)
#print(words)
counts = {}
names = open('renming.txt','r',encoding='utf-8').read().split('、')
#print(names)
for name in names:
    #print(name)
    for i in words:
        if i==name:
            counts[i]=counts.get(i,0)+1
#print(counts)
lists=list(counts.items())
for df in lists:
    print(df)


