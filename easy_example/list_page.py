import requests
from urllib import parse


# 进入首页
url_list_page = ' https://2p.17wo.cn:47203/share-center-changtaobao/changtaobaoproduct/queryproductlist'
header1 = {
    'Connection': 'keep-alive',
    'Content-Type': "application/json;charset=UTF-8",
    'Referer': 'https:////2p.17wo.cn:47203/mall/',
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Mobile Safari/537.36",
    'token': '030e79d87cc24245af3e1e615e3cec4dvQNoYE'
    }
payload1 = {"data": {"pageNum": 1, "pageSize": 10, "type": 1}}
# parse转码成utf-8
postdata = parse.urlencode(payload1)
response1 = requests.post(url_list_page, headers=header1, data=postdata)
# 查看响应内容，response.text 返回的是Unicode格式的数据
html = response1.text
# # 创建 Beautiful Soup 对象
# soup = bs4.BeautifulSoup(html, "lxml")
# # 获取“颜色”文本
# info = soup.find_all('h4').get_text()
# try:
#     assert info == '颜色'
#     print('------pass------')
# except ValueError:
#     print('------fail------')



print(postdata)
print(html)
print(response1.status_code)
print(response1.url)



