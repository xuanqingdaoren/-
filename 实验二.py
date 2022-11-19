name = input("请输入你的名字:")

id = input("请输入你的生日（如20000101）:")

year = id[0:4]

month = id[4:6]

day = id[6:]

print("%s你的生日：%s年是%s月%s日."%(name,year,month,day))
