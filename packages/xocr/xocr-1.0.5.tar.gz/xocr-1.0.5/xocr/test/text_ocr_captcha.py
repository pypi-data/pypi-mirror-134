# #!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022/1/9 22:09
# @Author : BruceLong
# @FileName: text_ocr_captcha.py
# @Email   : 18656170559@163.com
# @Software: PyCharm
# @Blog ：http://www.cnblogs.com/yunlongaimeng/
import time

from ocr_captcha import get_det_location

s = time.time()
# print(get_det_location(bg_file_path='../files/3.jpg', split_line_y=344, server_port=8892))
# print(get_det_location(bg_file_path='../files/3488a2e1778942dd9594e17a47610ef8.jpg', split_line_y=344, server_port=8892))
# print(get_det_location(bg_file_path='../files/9694b3bb54364775a468693365a20f60.jpg', split_line_y=344, server_port=8892))
print(get_det_location(bg_file_path='../files/f79a1cb84d2f46dfb3b69e293a55fc7e.jpg', split_line_y=344, server_port=8894))
print('用时：', time.time() - s)
