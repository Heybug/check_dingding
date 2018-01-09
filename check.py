#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6

import os
import time

init_x, init_y = 760, 1687

# 延迟
sleep = 5


def screenshot():
    os.system('/usr/local/bin/adb shell screencap -p /sdcard/autojump.png')
    os.system('/usr/local/bin/adb pull /sdcard/autojump.png /Users/o2o2/github/check_dingding/img')


def onClick(x, y):
    os.system('/usr/local/bin/adb shell input tap %d %d' % (x, y))


def inputInfo(info):
    '''
    输入信息
    :param info:
    :return:
    '''
    os.system('/usr/local/bin/adb shell input keyevent %s' % info)


def inputText(txt):
    '''
    输入字符串
    :param txt:
    :return:
    '''
    os.system('/usr/local/bin/adb shell input text %s' % txt)


def open():
    '''
    打开应用
    :return:
    '''
    # 解屏
    inputInfo(82)
    time.sleep(sleep)
    onClick(init_x, init_y)
    time.sleep(sleep)


def login():
    '''
    开始登录
    :return:
    '''
    # 点击输入框
    onClick(700, 700)
    # 点击清空账号
    onClick(955, 682)
    # 输入账号
    inputText('18589245630')

    # 跳到输入密码
    inputInfo(61)
    # 点击清空密码
    onClick(955, 908)

    # 输入密码
    inputText('123456')

    # 关闭键盘
    inputInfo(4)
    # 点击登录
    onClick(530, 1090)
    time.sleep(sleep)


def workspace():
    '''
    进入工作区
    :return:
    '''
    onClick(538, 1714)
    time.sleep(sleep)
    # 翻页
    # inputInfo(93)
    os.system('/usr/local/bin/adb shell input swipe 600 1400 600 100 1000')
    time.sleep(sleep)
    # 进入打卡界面
    onClick(670, 800)
    time.sleep(sleep)


def check():
    # 上班打卡
    time.sleep(sleep)
    onClick(540, 700)
    # 下班打卡
    # onClick(540, 1245)
    time.sleep(sleep)
    # 退出进程
    onClick(780, 1870)
    onClick(544, 1690)
    inputInfo(4)
    # 锁屏
    inputInfo(26)


# 截屏
# screenshot()

# 打开应用
open()

# 登录
login()

# 进入工作去
workspace()

# 打卡
check()

os.system('echo 打卡成功:`date` >> ~/Desktop/text.txt')
