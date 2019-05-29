# -*- coding: utf-8 -*- 

__author__ = "Road36"
__date__ = "19-5-29"

"""
Describe:
写入excel数据
"""
import xlwt


def generate_excel(wb_name, ws_name, url, data):
    """二维数组类型类数据写入"""
    wb = xlwt.Workbook()
    ws = wb.add_sheet(ws_name)

    for i in range(len(data)):
        for j in range(len(data[i])):
            ws.write(i, j, data[i][j])
    wb.save(url + wb_name + r".xls")
