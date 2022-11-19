# 1.来到美女图片网页，然后查看网页源代码确认是服务器渲染，然后获取源代码，批量提取高清大图页面链接地址
# 2.通过对两个高清大图链接地址定位比较，找到了共有的定位条件，然后获取链接下载

import requests
import re
from bs4 import BeautifulSoup
import time
import os

url = 'https://www.mn52.com/meihuoxiezhen/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

resp = requests.get(url,headers=headers)

# 把源码交给bs
main_page = BeautifulSoup(resp.text,'html.parser')
h4List = main_page.find_all("h4")
for i in range(-1,1):
    h4List.pop(i)
# print(h4List)  # 测试用的
p = re.compile(r'"(?P<href>.*?)"')
for item in h4List:
    child_href = 'https://www.mn52.com' + ''.join(p.findall(str(item))) # 将bs4.element.Tag对象转为string对象
    # 拿到子页面的源代码
    child_page_resp = requests.get(child_href,headers=headers)
    # 文件夹命名
    p_name = re.compile(r'<div class="w740">.*?<h1>(?P<img_name>.*?)</h1>',re.S)
    img_name = p_name.findall(child_page_resp.text)
    img_name_f = ''.join(img_name)
    dirs = 'D:/python_img/' + img_name_f
    # 如果不存在这个文件夹就创建这个文件夹
    if not os.path.exists(dirs):
        os.makedirs(dirs)

    # print(img_name) # 测试用的
    # print(child_page_resp.text) # 测试用的
    # break
    # 把源代码交给bs
    child_page = BeautifulSoup(child_page_resp.text,'html.parser')
    imgList = child_page.find('div',id='piclist').find_all('img')
    # print(imgList)  # 测试用的
    num = 1
    for item in imgList:
        src = 'https://www.mn52.com' + item.get('src')
        # 下载图片
        img_resp = requests.get(src)
        # img_resp.content # 这里拿到的是字节
        with open(f'{dirs}/{num}.jpg','wb') as f:
            f.write(img_resp.content)
            num += 1
    print('over!!!')
    time.sleep(1) # 缓一秒爬取
print('Game Over!!!')
resp.close()