num=input("请输入成绩并用空格隔开：")
num=num.split()
for i in range(len(num)):
    y = l = j = b = 0
    if num[i]>='85':
        y+=1
    elif '75'<=num[i]<='84':
        l=l+1
    elif '60'<=num[i]<='74':
        j+=1
    elif num[i]<='59':
        b+=1
print("优有 "+str(y)'个，良有'+str(l)'个，及格有'+str(j)'个，不及格有'+str(b)'个')
