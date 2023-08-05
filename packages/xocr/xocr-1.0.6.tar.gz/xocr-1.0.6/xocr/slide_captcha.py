# #!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022/1/7 19:04
# @Author : BruceLong
# @FileName: slide_captcha.py
# @Email   : 18656170559@163.com
# @Software: PyCharm
# @Blog ：http://www.cnblogs.com/yunlongaimeng/
import hashlib
import os

import cv2

from .until.tools import makedirs_file_path, static_src_temp_server


def get_slide_location(bg_file_path: str = None,
                       fg_file_path: str = None,
                       http_type: bool = False,
                       server_port: int = 8890) -> dict:
    '''
    获取滑块验证码目标位置
    :param bg_file_path:背景文件路径/网络地址
    :param fg_file_path:滑块缺口文件路径/网络地址
    :param http_type:是否使用http网络请求，默认不使用
    :return:
    '''
    msg = {'msg': '希望得到了你想要的结果^_^'}
    if not http_type:
        if not os.path.exists(bg_file_path):
            msg['bg_msg'] = '背景图片路径不存在'
        if not os.path.exists(fg_file_path):
            msg['fg_msg'] = '滑块图片路径不存在'
    else:
        # 处理网络图片
        pass
    try:
        # 读取背景图片和缺口图片
        bg_img = cv2.imread(bg_file_path)  # 背景图片
        tp_img = cv2.imread(fg_file_path)  # 缺口图片
        # 识别图片边缘
        bg_edge = cv2.Canny(bg_img, 100, 200)
        tp_edge = cv2.Canny(tp_img, 100, 200)
        # 转换图片格式
        bg_pic = cv2.cvtColor(bg_edge, cv2.COLOR_GRAY2RGB)
        tp_pic = cv2.cvtColor(tp_edge, cv2.COLOR_GRAY2RGB)
        # 缺口匹配
        res = cv2.matchTemplate(bg_pic, tp_pic, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)  # 寻找最优匹配
        # 绘制方框
        th, tw = tp_pic.shape[:2]
        tl = max_loc  # 左上角点的坐标
        br = (tl[0] + tw, tl[1] + th)  # 右下角点的坐标
        cv2.rectangle(bg_img, tl, br, (0, 0, 255), 2)  # 绘制矩形
        # 构造生成目标文件标注结果
        # 根据背景文件生成一个md5
        hash_data = hashlib.md5((str(bg_file_path)).encode('utf8')).hexdigest()
        # 构造成一个文件名
        file_name = f'{hash_data}.jpg'
        full_path = makedirs_file_path(dir_name='image/slide_temp')
        filepath = os.path.join(full_path + '/' + file_name)
        cv2.imwrite(filepath, bg_img)  # 保存在本地
        server = static_src_temp_server(server_name='slide_server', full_path=full_path, port=server_port)
        if not server.get('port_msg'):
            filepath = '/'.join([server.get('httpserver'), file_name])
        filepath = '/'.join([server.get('httpserver'), file_name])
    except Exception as e:
        msg['msg'] = str(e)
        pass
    result = dict({'location': locals().get('max_loc'), 'target_img_psth': locals().get('filepath')}, **msg)
    return result
