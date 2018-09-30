import itchat
from itchat.content import *
from weatherfiler import weatherfiler

def text_reply(msg):
    filterlist = [weatherfiler()]
    for f in filterlist:
        msg = f.reply(msg)
        if msg is not None:
            return '[机器人]\n'+msg
    return None

@itchat.msg_register(TEXT, isGroupChat=True)
def group_reply(msg):
    if msg.isAt:
        value = text_reply(msg.text)
        if value is not None:
            msg.user.send(value)

@itchat.msg_register(TEXT)
def person_reply(msg):
    value = text_reply(msg.text)
    if value is not None:
        msg.user.send(value)

itchat.auto_login()
itchat.run(True)
