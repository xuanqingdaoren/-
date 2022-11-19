import random
n=10000
st=0
ft=0
for i in range(n):
    c_t=random.randint(1,3)
    m_C=random.randint(1,3)
    if m_C==c_t:
        ft+=1
    else:
        st+=1
s=st/10000
f=ft/10000
print('转换后成功概率为：'+str(s))
print('转换后失败概率为：'+str(f))
