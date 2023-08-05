# #!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022/1/9 20:18
# @Author : BruceLong
# @FileName: test_rm_files.py
# @Email   : 18656170559@163.com
# @Software: PyCharm
# @Blog ：http://www.cnblogs.com/yunlongaimeng/
import os

from until.tools import rm_files, get_mtime_files

rm_files(basedir=r'C:\Users\hbsxw\Desktop\PypiProjects\xocr\xocr\image',
         filenames=['cut_pic_temp']
         )

# import os
#
# url = r'C:\Users\hbsxw\Downloads'
# lists = os.listdir(url)
# # print(lists)
# lists.sort(key=lambda fn: os.path.getmtime(url + '\\' + fn))
# print(lists[:-10])
# print(lists[-10:])
# filepath = os.path.join(url, lists[-1])
# print(filepath)

# print(get_mtime_files(basedir=url, limit=10, is_rm=True))
