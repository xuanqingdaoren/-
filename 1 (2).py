a = input("")
def isnum(a):
    try:
        n=eval(a)
        if type(n)==float or type(n)==int or type(n)==complex:
            print('True')
        else:
            print('False')
    except:
        print('False')
isnum(a)
