# 用于断言


class CommonUtil(object):
    # 判断一个字符串是否包含在另一个字符串中
    def is_contain(self, str1, str2):
        if str1 in str2:
            flag = True
        else:
            flag = False
        return flag