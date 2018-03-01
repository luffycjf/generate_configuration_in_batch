#! /usr/bin/python
# -*- coding:utf-8 -*-
import multiprocessing,xlrd


def file_replace(filedata,replacedata,filename):
    for key in replacedata:
        try:
            filedata = filedata.replace(key,replacedata[key])
        except:
            pass
    with open(filename, 'w') as file:
        file.write(filedata)
    return None

def readexcel(excelname):
    workbook = xlrd.open_workbook(excelname)
    sheet1 = workbook.sheet_by_index(0)
    replacedata = []
    key_list = sheet1.row_values(0)
    for j in range(1,sheet1.nrows):
        replacedata_dict = {}
        for i in range(len(key_list)):
            replacedata_dict[key_list[i]] = str(sheet1.cell(j,i).value)
        replacedata.append(replacedata_dict)
    return replacedata

if __name__== '__main__':
# vars.xlsx是参数的表格路径名称
    replacedata_list  = readexcel('vars.xlsx')
# template.txt是模版的路径名称
    with open('template.txt', 'r') as file :  
        filedata = file.read()
#4代表多进程的数量
    pool = multiprocessing.Pool(processes=4)
    for replacedata in replacedata_list:
#filename对应参数表里面的生成文件的名称
        filename = replacedata['filename']
        del replacedata['filename']
        pool.apply_async(file_replace, (filedata,replacedata,filename, ))
    pool.close()
    pool.join()
