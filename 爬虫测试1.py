# python爬虫第一个案例
# 作者：玄青道人（暗夜）
# 作用：某壁纸网站的爬虫分析测试
import urllib.request
import requests
from bs4 import BeautifulSoup
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47'
}
url = 'https://www.mmonly.cc/mmtp/list_9_1.html'
request = urllib.request.Request(url=url,headers=header)
# 发送url请求到服务器
def getimg():
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html,'html.parser')
    gril = soup.find_all('img')
    print(gril)

