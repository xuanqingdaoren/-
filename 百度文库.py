import requests as _requests
from bs4 import BeautifulSoup as _soup

PROGRESS_BAR = ' '

HTTP = 'http'
HTTPS = 'https'
SOCKS = 'socks'

USER_AGENT = (
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/68.0.3440.106 Safari/537.36'
)

CP936 = CP_936 = 'cp936'
UTF_8 = UTF8 = 'utf-8'
UTF_16 = UTF16 = 'utf-16'
UTF_32 = UTF32 = 'utf-32'
USC_2 = USC2 = 'usc-2'
USC_4 = USC4 = 'usc-4'
UTF_16_BE = UTF16BE = 'uft-16-BE'
UTF_16_LE = UTF16LE = 'uft-16-LE'
ASCII = ANSI = 'ansi'
LATIN_1 = LATIN1 = 'Latin-1'
GBK = 'gbk'
GB2312 = GB_2312 = 'gb2312'
GB18030 = GB_18030 = 'gb18030'
ISO = ISO_8859_1 = 'ISO-8859-1'

HTML_PARSER = DEFAULT_PARSER = 'html.parser'
XML = XML_PARSER = 'xml'
LXML = LXML_PARSER = 'lxml'
LXML_XML = LXML_XML_PARSER = 'lxml-xml'
HTML5LIB = HTML5LIB_PARSER = 'html5lib'


class BaiduLibrary(object):
    def __init__(self, url: str, cookie: str = '', proxy_ip: str = None, proxy_type: str = HTTPS,
                 encoding: str = 'utf-8', parser=HTML_PARSER):
        self.encoding = encoding
        self.url = url
        self.headers = {
            'Cookie': cookie,
            'User-Agent': USER_AGENT
        }
        self.parser = parser
        self._use_proxy_ip = proxy_ip is not None
        self.proxies = {proxy_type: proxy_ip}
        self._request()

    def _request(self):
        if self._use_proxy_ip:
            self.response = _requests.get(self.url, headers=self.headers, proxies=self.proxies)
        else:
            self.response = _requests.get(self.url, headers=self.headers)
        self.response.encoding = self.encoding
        self.soup = _soup(self.response.text, self.parser)

    def get(self):
        texts = self.soup.find_all('p', attrs={'v-pre': '', 'class': 'reader-word-layer'})
        texts = [i.string for i in texts]
        result = ''.join(texts)
        result = result.replace('\u2002', ' ')
        return result


BaiduWenKu = BaiduLibrary

# 这里cookie换成你自己的
bl = BaiduLibrary(
    'https://wenku.baidu.com/view/693ba922aaea998fcc220ee2.html?fr=hp_Database&_wkts_=1667924731733&bdQuery=%E7%99%BE%E5%BA%A6%E6%96%87%E5%BA%93',
    cookie='BIDUPSID=101765CAE51AF93F923C469FA36DC67E; PSTM=1641645875; BAIDUID=101765CAE51AF93FBBEA329530B4A5D8:FG=1; __yjs_duid=1_019e1b4964d26594bf17d330ca32ddee1641645902504; _click_param_reader_query_ab=-1; Hm_lvt_f06186a102b11eb5f7bcfeeab8d86b34=1641732155; H_PS_PSSID=31660_26350; delPer=0; PSINO=2; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BAIDUID_BFESS=833FF08B2F4102A5366B271DFB85A202:FG=1; Hm_lvt_d8bfb560f8d03bbefc9bdecafc4a4bf6=1641721971,1641959376; ___wk_scode_token=kWcvdF0fOpgsQtg3wL9VNQYGNNoGkjxdSyXDSd9eaBw%3D; BDRCVFR[-HoWM-pHJEc]=mk3SLVN4HKm; BA_HECTOR=2h2401ah2k2l84244t1gtsm6j0q; Hm_lpvt_d8bfb560f8d03bbefc9bdecafc4a4bf6=1641961687; bcat=a52de9ab8a6fa82d18c85829d0c7ddea88bf722e947d919a0a3ada4b5f51ba1eb5293cf91932b5eb52b524d836ef94e95e99e01c60a3c6a5d5f04ceb19e67ec1f825880003872c4af4ce0d62b663eb072d73bddb263ddb8b5789207cd7064eaa0d37bb7291f1abe5df463082da7f5d6bc5d05c3c9de110158241757e2c981a8b; __yjs_st=2_Yzg2YzRmNDE0OGI5NzU2NWIzZmE3ODgwZjcyZWZkMDJmZjFkYmI2YmUzZjE0NGEzNTRjNGY5N2Y2ZTMyNDQ4MjE0ZjEwYjkyNmU0OGNiZjMzMWQxNjliYzg3MTFlM2U2ZjkyMzg5ZDc4M2MxMzI3Nzg2N2Q5Y2VkNDVhMzQ1YzRjNTI0NmY5ZmVkMWI2ODUyNDE1NjFmZDg5M2I0OTU3MDM2OTNjMDYyMTIwZmRlZmMxYzljNjJiZGU4ZDdhNmI1MDhhNDYwNDQxZGNmYjE0YjI4OWNkZTdjZTNlYTdkODE5YjBmMTM3YjhjN2U3OWU2MWM0NGMwNzE1Y2MyMThjN183XzkwZTAyZjVj; ab_sr=1.0.1_YzliZjhmNjAxM2QxMmY0Y2Y5YzI3N2RkYTllMjZiOTllZTkzODczM2Q4N2RmOGM4MzI2OWY2NjFmMjFhN2Q1OWQ2YjM5NDNmY2Y3NGNjMjExYWUxMGEzYjMwYTM4NTY0ODQ0NDBiMWQ3YmQ2ZjZlNzg3M2ViOTQ2OTMxOTY5MDA5NGNjMGU4NDc1NTYzZWU5OTczYjU1Zjc4NGVlZjE1NA==')
print(bl.get())
