import itchat
from itchat.content import *
from weatherfiler import weatherfiler
from currencyfilter import currencyfilter
from translatefilter import translatefilter

@itchat.msg_register(TEXT, isGroupChat=True)
def group_reply(msg):
    if msg.isAt:
        filterlist = [weatherfiler()]
        for f in filterlist:
            value = f.reply(msg.text)
            if value is not None:
                msg.user.send('[机器人]'+'\n'+value)
    else:
        filterlist = [translatefilter(),currencyfilter()]
        for f in filterlist:
            value = f.reply(msg.text)
            if value is not None:
                msg.user.send('[机器人]'+'\n'+value)

@itchat.msg_register(TEXT)
def person_reply(msg):
    filterlist = [translatefilter(),weatherfiler(),currencyfilter()]
    for f in filterlist:
        value = f.reply(msg.text)
        if value is not None:
            msg.user.send('[机器人]'+'\n'+value)

itchat.auto_login()
itchat.run()
