# #!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022/1/7 18:10
# @Author : BruceLong
# @FileName: tools.py
# @Email   : 18656170559@163.com
# @Software: PyCharm
# @Blog ：http://www.cnblogs.com/yunlongaimeng/
import os
import shutil
import socket


def get_host_info():
    '''
    获取主机相关信息
    :return:
    '''
    # 获取本机计算机名称
    hostname = socket.gethostname()
    # 获取本机ip
    ip = socket.gethostbyname(hostname)
    result = {
        'ip': ip,
        'hostname': hostname,  # 主机名
        'sys_type': os.name,  # 当前只注册了3个值：分别是posix , nt , java， 对应linux/windows/java虚拟机
    }
    return result


def kill_linux_process(port: int = None, pid: int = None, keyword: str = None):
    '''
    杀死linux进程
    :param port:根据端口号杀死
    :param pid: 根据pid号杀死
    :param keyword: 根据关键词杀死
    :return:
    '''
    if port:
        os.popen(f"kill $(lsof -Pti :{port})")
    if pid:
        os.popen(f"sudo kill -9 {pid}")
    if keyword:
        os.popen("ps auxww | grep {keyword} | awk '{p}' | xargs kill -9".format(keyword=keyword, p='{print $2}'))


def makedirs_file_path(base_path: str = None, dir_name: str = '') -> str:
    '''
    根据给定的文件夹名，在当路径中创建相应的文件夹
    :param base_path: 基础文件夹路径
    :param dir_name: 需要创建的文件夹名
    :return: 创建完成后的文件夹路径
    '''
    path = os.path.dirname(__file__).replace('until', '')
    if base_path:
        path = base_path
    file_path = os.path.join(path, dir_name).replace('\\', '/')

    if not os.path.exists(file_path):
        os.makedirs(file_path)
    return file_path


def static_src_temp_server(server_name: str, full_path: str = None, port: int = 8888) -> dict:
    '''
    静态资源临时访问服务
    :param full_path:绝对路径
    :param port: 端口号
    :return: 结果信息
    '''
    sys_type = get_host_info().get('sys_type')

    # 1. 判断目录是否存在
    msg = {'msg': '一切ok'}
    if not os.path.exists(full_path):
        msg['path_msg'] = '路径不存在，请传入正确的路径'
    # 3. 获取当前ip地址
    ip = get_host_info().get('ip')
    # 系统类型为windows操作系统做以下操作
    if sys_type == 'nt':
        # 4. cmd进入文件目录
        # 2. 判断对应端口是否存在
        port_status = os.popen(f'netstat -ano|findstr "{port}"').read().split('\n')
        if port_status[0]:
            msg['port_msg'] = '抱歉端口已经被占用'
        # 5. 启动对应的服务
        server_path = makedirs_file_path(dir_name='cmd')
        run_str = f'''@echo off
    if "%1" == "h" goto begin
    mshta vbscript:createobject("wscript.shell").run("%~nx0 h",0)(window.close)&&exit
    :begin
    cd "{full_path}" && python -m http.server {port}'''
        filename = f'{server_name}_start.bat'
        save_file_path = os.path.join(server_path, filename)
        with open(save_file_path, 'w') as f:
            f.write(run_str)
        os.popen(f'''cd {server_path} && {filename}''').read().split('\n')
    # 系统类型为linux操作系统做以下操作
    if sys_type == 'posix':
        port_status = os.popen(f'netstat -an|grep "{port}"').read().split('\n')
        if port_status[0]:
            msg['port_msg'] = '抱歉端口已经被占用'
            # 慎用
            # kill_linux_process(port=port)
        os.popen(f'''cd "{full_path}" && python -m http.server {port} > /dev/null 2>&1 &''').read().split('\n')
    return dict(
        {
            'ip': ip,
            'port': port,
            'httpserver': f'http://{ip}:{port}'
        }
        , **msg
    )


def rm_files(basedir: str = None, filenames: list = None):
    '''
    删除文件列表
    :param basedir:基础文件路径
    :param filenames: 文件列表
    :return:
    '''
    if basedir:
        filenames = [os.path.join(basedir, i) for i in filenames]
    # 判断是文件还是文件夹, 若是文件夹 全部删除  若是文件 跳过
    for _ in filenames:
        if os.path.isdir(_):  # 判断是否为文件夹
            # **注：该命令可递归删除文件夹,慎用!!该文件夹和文件夹里面所有内容会被删除.
            shutil.rmtree(_)
            print("%s目录 已删除" % _)
        else:  # 如果不是文件夹,则为文件
            os.remove(_)  # 该命令删除文件
            print("%s文件 已删除" % _)


def get_mtime_files(basedir: str = None, limit: int = 1000, is_rm: bool = False):
    '''
    根据创建时间倒序，并确定是否需要删除文件
    :param basedir: 基础文件路径
    :param limit: 注注注：需要保留的文件数
    :param is_rm: 是否需要删除
    :return:
    '''
    lists = os.listdir(basedir)
    # 按文件创建时间正序排列
    lists.sort(key=lambda fn: os.path.getmtime(basedir + '\\' + fn))
    if is_rm:
        print(lists[:-limit])
        x = input('确定是否删除【0/1】：')
        if x == '1':
            # print('所有文件已经删除完毕')
            rm_files(basedir=basedir, filenames=lists)
    # print(lists[:limit])
