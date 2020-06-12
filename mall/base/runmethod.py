import json
import requests
requests.packages.urllib3.disable_warnings()


# 对不同的请求方式进行封装
class RunMethod(object):
    def post_method(self, url, data, header=None):
        res = None
        if header != None:
            res = requests.post(url=url, data=data, headers=header, verify=False)
        else:
            res = requests.post(url=url, data=data, verify=False)
        return res.json()

    def get_method(self, url, data=None, header=None):
        res = None
        if header != None:
            res = requests.post(url=url, params=data, headers=header, verify=False)
        else:
            res = requests.post(url=url, params=data, verify=False)
        return res.json()

    def run_method(self, method, url, data=None, header=None):
        res = None
        if method == 'post':
            res = self.post_method(url, data, header)
        else:
            res = self.get_method(url, data, header)
        return json.dumps(res, indent=2, sort_keys=True, ensure_ascii=False)

if __name__ == '__main__':
    url = 'https://2p.17wo.cn:47203/share-center-changtaobao/changtaobaoproduct/queryproductlist'
    data = {"pageNum": 1, "pageSize": 10, "type": 1}
    run = RunMethod()
    run_test = run.run_method(method="Post", url=url, data=data)
    print(run_test)