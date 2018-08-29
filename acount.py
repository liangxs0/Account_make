#-*- utf8 -*-
import time
import datetime
import os
import xlwt
from xlrd import open_workbook
from xlutils.copy import copy
from os.path import join
import xlrd


def set_style(font_name,font_height,bold=False):
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = font_name
    font.height = font_height
    font.bold = bold
    font.colour_index = 4
    #设置边框
    borders = xlwt.Borders()
    borders.left = 6
    borders.righ = 6
    borders.top = 6
    borders.bottom = 6

    # 设置居中
    alignment = xlwt.Alignment()
    alignment.horz = xlwt.Alignment.HORZ_CENTER  # 水平方向
    alignment.vert = xlwt.Alignment.VERT_TOP  # 垂直方向
    style.font = font
    style.borders = borders
    style.alignment = alignment

    return style
def creat_excel():
    new_workbook = xlwt.Workbook()
    new_sheet = new_workbook.add_sheet('account')
    style = set_style('Time New Roman',200,200)
    new_sheet.write(0,0,'dateTime',style)
    new_sheet.write(0,1,'money',style)
    new_sheet.write(0,2,'Total',style)
    new_sheet.write(0,3,'Remark',style)
    new_workbook.width = 300
    new_workbook.save(r'account.xls')
def index_data(line,row,nowTime,money,all_money,remark):

    style = set_style('Time New Roman',200,200)
    source = r"account.xls"
    rb = open_workbook("account.xls",formatting_info=True)
    w = copy(rb)
    w.get_sheet(0).write(line,row,nowTime,style)
    w.get_sheet(0).write(line,row+1,money,style)
    w.get_sheet(0).write(line,row+2,all_money,style)
    w.get_sheet(0).write(line,row+3,remark,style)
    w.width = 350
    w.save("account.xls")
def Add_money():
    all_money = 0
    excel = xlrd.open_workbook('account.xls',encoding_override='utf8')
    sheet1 = excel.sheets()[0] #打开第一张表格
    #获取第一张表格的所有数据的钱
    row = sheet1.nrows
    for data in range(1,row):
        #print("data = %d",data)
        all_money = all_money+int(sheet1.row_values(data)[1])
        #print(all_money)
    return all_money
def write_excel(money,remark):
    excel = xlrd.open_workbook('account.xls', encoding_override='utf8')
    print(excel)
    print(excel.sheet_names())

    print(len(excel.sheets()))
    sheet1 = excel.sheets()[0]

    # 获取当excel表格的行数
    row = sheet1.nrows
    print("row = ", row)
    nowTime = datetime.datetime.now().strftime('%m/%d')
    all_money = Add_money() + float(money)
    index_data(row, 0, nowTime, float(money), float(all_money), remark)


