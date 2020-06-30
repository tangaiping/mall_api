# 操作Excel

import xlrd
from xlutils.copy import copy

class OperationExcel(object):

    def __init__(self, file_name=None, sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = r'C:\Users\Administrator\PycharmProjects\api\mall\config\case.xls'
            self.sheet_id = 0
            self.data = self.get_data

    # 获取sheet的内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables

    # 获取单元格行数
    def get_lines(self):
        table = self.data
        nrows = table.nrows
        return nrows

    # 获取单元格数据
    def get_cell_value(self, row, col):
        tables = self.data
        cell = tables.cell_value(row, col)
        return cell

    # 回写数据到Excel
    def write_value(self, row, col, value):
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row, col, value)
        write_data.save(self.file_name)

    # 根据对应的case_id获取对应行的内容
    def get_row_data(self, case_id):
        row_num = self.get_row_num(case_id)
        row_data = self.get_row_value(row_num)
        return row_data

    # 根据case_id获取对应行号
    def get_row_num(self, case_id):
        num = 0
        cols_data = self.get_cols_data()
        for col_data in cols_data:
            if case_id in col_data:
                return num
            num += 1

    # 根据行号，找到该行的内容
    def get_row_value(self, row):
         tables = self.data
         row_data = tables.row_values(row)
         return row_data

    # 获取某一列的内容
    def get_cols_data(self, col_id=None):
        if col_id != None:
            cols = self.data.col_values(col_id)
        else:
            cols = self.data.col_values(0)
        return cols

if __name__ == '__main__':
    opera =OperationExcel()

    print(opera.get_data())
    print(opera.get_lines())
    print(opera.get_cell_value(1, 2))












