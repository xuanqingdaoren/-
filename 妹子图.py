import requests
from bs4 import BeautifulSoup
import urllib.request
import os
#注释
#获取图片
#http请求头
while True:
    os.mkdir('./image2')
    url = "https://www.mmonly.cc/mmtp/list_9_1.html"
    Hostreferer = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42',
               }
    start_html = requests.get(url=url, headers=Hostreferer)
    def getGrilsImg():
        response = requests.get(url)
        html = response.text
        #创建对象解析网页
        soup = BeautifulSoup(html,'html.parser')
        #找到img标签
        gril = soup.find_all('img')
        x = 0
   #获取img路径
        for i in gril:
            imgsrc = i.get('src')
            urllib.request.urlretrieve(imgsrc,'./image/%s.jpg'%x)
            x += 1
            print('正在下载第%d张'%x)
    getGrilsImg()
    num =input('是否退出？<y/n>')
    if num == 'y':
        break
    elif num == 'n':
        print('没有了！注意尺度！')