# coding=utf-8
import time
import random
from wxpy import *

# 初始化机器人，扫码登陆
bot = Bot(cache_path=True, console_qr=True)

# 搜索
nameS = ['::']
myFriend = bot.friends().search('::')
print(myFriend)


# myFriend.send('Hello WeChat!')


# 打印来自其他好友、群聊和公众号的消息
@bot.register()
def print_others(msg):
    print(msg)


tuLing = Tuling(api_key='db23cb873b61435888b149522272d092')


# 使用图灵机器人自动与指定好友聊天
@bot.register(myFriend)
def reply_my_friend(msg):
    chatTime = random.randint(5, 20)
    myFriend = bot.friends().search('::')
    print(chatTime, myFriend)
    time.sleep(chatTime)
    tuLing.do_reply(msg)


# 进入 Python 命令行、让程序保持运行
embed()
