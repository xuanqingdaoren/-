def t(filename):
    datenames,date=[],[]
    w=open(filename,'r',encoding='utf-8')
    for i in w:
        c=i.strip('\n').split(',')
        if '指标' in c[0]:
            years=[int(x[:-1]) for x in c[1:]]
        else:
            datenames.append('{:10}'.format(c[0]))
            date.append([float(x) for x in c[1:]])
    w.close()
    return years,datenames,date
def u(date):
    return sum(date)/len(date)
def o(xlist,ylist):
    xmeans,ymeans=u(xlist),u(ylist)
    bnumerator=-len(xlist)*xmeans*ymeans
    bdenominator=-len(xlist)*xmeans**2
    for x,y in zip(xlist,ylist):
        bnumerator+=x*y
        bdenominator+=x**2
    b=bnumerator/bdenominator
    a=ymeans-b*xmeans
    return a,b
def p(newyears,a,b):
    return [(a+b*x) for x in newyears]
def q(years,datenames,newdate):
    print('{:^60}'.format("国家财政收支线性估计"))
    header='指标    '
    for d in years:
        header+='{:10}'.format(d)
    print(header)
    for name,linedate in zip(datenames,newdate):
        line=name
        for date in linedate:
            line+='{:>10.1f}'.format(date)
        print(line)
def main():
    newyears=[x+2024 for x in range(7)]
    newdate=[]
    years,datenames,dates=t('1.csv')
    for date in dates:
        a,b=o(years,date)
        newdate.append(p(newyears,a,b))
    q(newyears,datenames,newdate)
main()

    
