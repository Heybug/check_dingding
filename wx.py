# coding=utf-8

# 导入模块
from wxpy import *
import os
import time

'''
机器人Start
'''
# 初始化机器人，扫码登陆
bot = Bot(console_qr=True, cache_path=True)

# 搜索
name = '你的hero'
myFriend = bot.friends().search(name)[0]

# 登录成功后发送报告
if myFriend:
    myFriend.send('Hello from wxpy!')
else:
    print('没有找到:{}'.format(name))


# 打印来自其他好友、群聊和公众号的消息
@bot.register()
def print_others(msg):
    print(msg)


# 使用图灵机器人自动与指定好友聊天
@bot.register(myFriend)
def reply_text(msg):
    control(msg.text)


'''
机器人End
'''

'''
钉钉Start
'''
init_x, init_y = 760, 1687

# 延迟
sleep = 5


def screenshot():
    os.system('adb shell screencap -p /sdcard/autojump.png')
    os.system('adb pull /sdcard/autojump.png ./img')
    print('准备发送截图...')
    myFriend.send('准备发送截图...')
    myFriend.send_image('img/autojump.png')
    print('发送截图完成...')


def onClick(x, y):
    os.system('adb shell input tap %d %d' % (x, y))


def inputInfo(info):
    '''
    输入信息
    :param info:
    :return:
    '''
    os.system('adb shell input keyevent %s' % info)


def inputText(txt):
    '''
    输入字符串
    :param txt:
    :return:
    '''
    os.system('adb shell input text %s' % txt)


def open():
    '''
    打开应用
    :return:
    '''
    # 解屏
    # inputInfo(82)
    onClick(init_x, init_y)


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


def workspace():
    '''
    进入工作区
    :return:
    '''
    print('bbbb')
    onClick(538, 1714)
    time.sleep(sleep)
    # 翻页
    os.system('adb shell input swipe 600 1400 600 100 1000')
    time.sleep(sleep)
    # 进入打卡界面
    onClick(670, 800)


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
    myFriend.send('【系统消息】打卡成功!')


def control(code):
    myFriend.send('正在{}'.format(code))
    if code == '截图':
        screenshot()
    elif code == '打开钉钉':
        open()
    elif code == '登录':
        login()
    elif code == '工作区':
        workspace()
    elif code == '打卡':
        check()
    else:
        inputInfo(code)


'''
钉钉End
'''

# 进入 Python 命令行、让程序保持运行
embed()
