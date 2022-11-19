# 1.拿到主页面的源代码，然后提取到子页面的链接地址(这里可以先在网页打开子页面获取链接，然后反向定位在网页源码具体处)
# 2.正常情况下请求子页面源代码，然后获取下载链接下载，但这个有些不一样，该网站已经分好类了，所以不从首页爬起反而更高效
import os.path
import requests
from bs4 import BeautifulSoup
import time

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
num = 1

# 爬取 清纯少女 前10页图片
while num <11:
    url = f'https://www.vmgirls.com/pure/page/{num}'

    resp = requests.get(url,headers=headers)
    # print(resp.text) #测试用的

    # 把源码交给bs
    main_page = BeautifulSoup(resp.text,'html.parser')
    aList = main_page.find_all('a',class_='list-title h-2x')
    # print(len(aList)) # 测试用的
    for a in aList:
        a_href = a.get('href')
        # print(a_href) # 测试用的
        child_page_resp = requests.get(a_href,headers=headers)
        # print(child_page_resp.text) # 测试用的

        # 把源码交给bs
        child_page = BeautifulSoup(child_page_resp.text,'html.parser')

        img_name_f = child_page.find('title').string # 获取title标签下的文本
        # print(img_name_f) # 测试用的
        #文件夹命名
        dirs = 'D:/Python_image/'+img_name_f
        # 如果不存在该路径，那就创建一个
        if not os.path.exists(dirs):
            os.makedirs(dirs)

        imgList = child_page.find('div',class_='nc-light-gallery').find_all('a')
        imgList.pop(0)
        count = 1
        for item in imgList:
            src = item.get('href')
            # print(src) # 测试用的
            # 下载图片
            img_resp = requests.get(src)
            with open(f'{dirs}/{count}.jpg','wb') as f:
                f.write(img_resp.content)
                count += 1
        print('over!!!')
        time.sleep(1)  # 缓一秒爬取
        # break # 用于测试
    num += 1
    break # 用于测试
print('======Game Over!!!======')
resp.close()
