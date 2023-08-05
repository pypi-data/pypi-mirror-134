# #!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022/1/9 22:09
# @Author : BruceLong
# @FileName: text_ocr_captcha.py
# @Email   : 18656170559@163.com
# @Software: PyCharm
# @Blog ：http://www.cnblogs.com/yunlongaimeng/
from slide_captcha import get_slide_location

print(get_slide_location(bg_file_path='../files/bgPic.jpg', fg_file_path='../files/cutPic.png'))
