# 操作json文件
import json

class OperrationJson(object):
    def __init__(self, file_path=None):
        if file_path == None:
            self.file_path = r'C:\Users\Administrator\PycharmProjects\api\mall\config\data.json'
        else:
            self.file_path = file_path
            self.data = self.read_data()

    # 读取json文件
    def read_data(self):
        with open(self.file_path) as fp:
            data = json.load(fp)
            return data

    # 根据关键字获取对应数据
    def get_data(self, id):
        return self.data[id]

    # 写入json
    def write_data(self, data):
        with open(r'C:\Users\Administrator\PycharmProjects\api\mall\config\data.json', 'w')as fp:
            fp.write(json.dumps(data))

if __name__ == '__main__':
    op_json = OperrationJson()
    print(op_json.read_data())
    print(op_json.get_data('filtrate'))