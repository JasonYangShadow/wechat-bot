from absfilter import absfilter
from urllib.request import Request,quote,urlopen,unquote
import json

class translatefilter(absfilter):
    def __init__(self):
        self.__api = 'https://translate.googleapis.com/translate_a/single?client=gtx&dt=t&sl='

    def msgprocess(self,msg):
        if u'翻译 ' in msg:
            target = msg[msg.find(u'翻译 ')+3:]
            req_url = self.__api + 'zh' +'&tl=ja&q='+quote(target)
            req = Request(req_url, headers={'User-Agent': 'Mozilla/5.0'})
            webpage = urlopen(req).read()
            webpage = webpage.decode('utf-8')
            jsonvalue = json.loads(webpage)
            if jsonvalue is not None:
                return jsonvalue[0][0][0]
        elif u'翻訳 ' in msg:
            target = msg[msg.find(u'翻訳 ')+3:]
            req_url = self.__api + 'ja' +'&tl=zh&q='+quote(target)
            req = Request(req_url, headers={'User-Agent': 'Mozilla/5.0'})
            webpage = urlopen(req).read()
            webpage = webpage.decode('utf-8')
            jsonvalue = json.loads(webpage)
            if jsonvalue is not None:
                return jsonvalue[0][0][0]
        else:
            return None
