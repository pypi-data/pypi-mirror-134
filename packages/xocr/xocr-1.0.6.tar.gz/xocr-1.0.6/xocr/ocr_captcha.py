# #!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022/1/9 19:45
# @Author : BruceLong
# @FileName: ocr_captcha.py
# @Email   : 18656170559@163.com
# @Software: PyCharm
# @Blog ：http://www.cnblogs.com/yunlongaimeng/
import hashlib
import os

import ddddocr
import cv2

from .until.tools import makedirs_file_path, static_src_temp_server

det = ddddocr.DdddOcr(det=True, show_ad=False)
ocr = ddddocr.DdddOcr(show_ad=False)
old_ocr = ddddocr.DdddOcr(old=True, show_ad=False)


def get_det_location(
        bg_file_path: str = None,
        split_line_y: int = None,
        target_text: list = None,
        http_type: bool = False,
        server_port: int = 8891) -> dict:
    msg = {'msg': '希望得到了你想要的结果^_^'}
    if not http_type:
        if not os.path.exists(bg_file_path):
            msg['bg_msg'] = '背景图片路径不存在'
        if not target_text:
            msg['tx_msg'] = '目标文本没有输入'
            target_text = []
    else:
        # 处理网络图片
        pass
    full_path = makedirs_file_path(dir_name='image/cut_pic_temp')
    with open(bg_file_path, 'rb') as f:
        image = f.read()

    poses = det.detection(image)

    im = cv2.imread(bg_file_path)
    det_result = []
    for _index, box in enumerate(poses):
        # 获取每一个目标的左上角点和右下角点
        temp_item = dict(zip(['x1', 'y1', 'x2', 'y2'], box))
        x1, y1, x2, y2 = box
        # 裁剪图
        cropped = im[y1:y2, x1:x2]  # 裁剪坐标为[y0:y1, x0:x1]
        # 构造成一个文件名
        file_name = '{}.jpg'.format('_'.join([str(i) for i in [_index, x1, y1, x2, y2]]))
        filepath = os.path.join(full_path, file_name)

        # temp_item['cut_pic_path'] = file_name
        cv2.imwrite(filepath, cropped)
        with open(filepath, 'rb') as f:
            image = f.read()
        res = ocr.classification(image)
        old_res = old_ocr.classification(image)
        # temp_item['word'] = res
        temp_item['old_word'] = old_res
        if split_line_y and y1 >= split_line_y:
            target_text.append(temp_item)
        else:
            det_result.append(temp_item)
    if split_line_y:
        target_text.sort(key=lambda _it: _it.get('x1'))
        target_text = [i.get('old_word') for i in target_text]
        msg['tx_msg'] = '目标文本已经包含在图片中'
    result = {'target_text': target_text, 'det_result': det_result}
    # 画个圈圈诅咒你
    [cv2.rectangle(im, tuple(box[:2]), tuple(box[2:]), color=(0, 0, 255), thickness=2) for box in poses]
    cv2.rectangle(im, (0, 344), (344, 344), color=(255, 0, 0), thickness=2)

    # 根据背景文件生成一个md5
    hash_data = hashlib.md5((str(bg_file_path)).encode('utf8')).hexdigest()
    # 构造成一个文件名
    out_file_name = f'{hash_data}.jpg'
    filepath = os.path.join(full_path + '/' + out_file_name)
    cv2.imwrite(filepath, im)  # 保存在本地
    server = static_src_temp_server(server_name='det_server', full_path=full_path, port=server_port)
    if not server.get('port_msg'):
        filepath = '/'.join([server.get('httpserver'), out_file_name])
    filepath = '/'.join([server.get('httpserver'), out_file_name])

    result = dict({'result': locals().get('result'), 'target_img_psth': locals().get('filepath')}, **msg)
    return result
