counts = {}
names = open('renming.txt','r',encoding='utf-8').read().split('、')
#print(names)
for word in names:
    counts[word]=counts.get(word,0)+1
#print(counts)
lists=list(counts.items())
for i in lists:
    print(i)