# -*- coding: utf-8 -*-
# 解析xlsx
import openpyxl
from config.index import Config
import os
def removeOldFile(_path):
    if os.path.exists(_path):
        os.remove(_path)
    else:
        print('file is not exist')
# import numpy as np
def parseXlsx():
    parseUrl = Config.__downloadPath__
    workbook = openpyxl.load_workbook(parseUrl)    #找到需要xlsx文件的位置
    booksheet = workbook.active                 #获取当前活跃的sheet,默认是第一个sheet
    removeOldFile(parseUrl) # 先删除文件
    # 如果想获取别的sheet页采取下面这种方式，先获取所有sheet页名，在通过指定那一页。
    # sheets = workbook.get_sheet_names()  # 从名称获取sheet
    # booksheet = workbook.get_sheet_by_name(sheets[0])

    #获取sheet页的行数据
    rows = booksheet.rows
    #获取sheet页的列数据
    columns = booksheet.columns
    i = 0
    # 迭代所有的行
    print('rows', rows)
    data = []
    validColumnLen = 4 # 有效的列数
    for row in rows:
        i = i + 1
        line = [col.value for col in row]
        # print('line', line)
        lineLen = len(line)
        noneLen = line.count(None)
        if lineLen == noneLen: # 全空数据的行忽略
            continue
        else:
            realColLen = lineLen - noneLen # 有效列数
            if i == 1: # 列头第一行忽略
                continue
            elif validColumnLen > realColLen: # 行数据中列数据不完整的忽略
                continue
            row_data = []
            for col in range(1, validColumnLen + 1):
                row_data.append(booksheet.cell(row=i, column=col).value)
            data.append(row_data)
            pass
    # print (cell_data_1, cell_data_2, cell_data_3, cell_data_4)
    print('解析结果', data)
    return data

