from requests_html import HTMLSession

session = HTMLSession

# 进入首页
url_list_page = session.get(' https://2p.17wo.cn:47203/share-center-changtaobao/changtaobaoproduct/queryproductlist')
a = url_list_page.html.links
print(a)
