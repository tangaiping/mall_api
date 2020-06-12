# 获取Excel中的数据

class global_val:
    id = '0'
    request_name = '1'
    url = '2'
    run = '3'
    request_way = '4'
    header = '5'
    case_depend = '6'
    data_depend = '7'
    field_depend = '8'
    data = '9'
    except_result = '10'
    result = '11'


# 获取case_id
def get_id():
    return global_val.id


# 获取请求名称
def get_request_name():
    return global_val.request_name


# 获取url
def get_url():
    return global_val.url


# 获取是否运行
def get_run():
    return global_val.run


# 获取请求方式
def get_request_way():
    return global_val.request_way


# 获取是否携带header
def get_header():
    return global_val.header


# 获取case依赖
def get_case_depend():
    return global_val.case_depend


# 获取依赖的返回数据
def get_data_depend():
    return global_val.data_depend


# 获取数据依赖字段
def get_field_depend():
    return global_val.field_depend


# 获取请求数据
def get_data():
    return global_val.data


# 获取预期结果
def get_except_result():
    return global_val.except_result


# 获取返回结果
def get_result():
    return global_val.result


