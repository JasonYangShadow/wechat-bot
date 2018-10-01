import unittest
from pprint import pprint
from weatherfiler import weatherfiler
from absfilter import absfilter
from currencyfilter import currencyfilter
from translatefilter import translatefilter

class Test(unittest.TestCase):

    @unittest.skip('skip')
    def testweather(self):
        w = weatherfiler()
        print(w.msgprocess('h'))

    @unittest.skip('skip')
    def testabsfilter(self):
        msg = u'让我看看天气'
        filterlist = [weatherfiler()]
        for f in filterlist:
            print(f.reply(msg))

    @unittest.skip('skip')
    def testcurrency(self):
        msg = u'今天花了10000日元啊,还有3000日元的消费啊'
        filterlist = [(currencyfilter())]
        for f in filterlist:
            print(f.reply(msg))

    #@unittest.skip('skip')
    def testtranslate(self):
        msg = u'翻译 今天花了10000日元啊,还有3000日元的消费啊'
        filterlist = [(translatefilter())]
        for f in filterlist:
            print(f.reply(msg))
        msg2 = u'翻訳 私わヨウキョクです'
        filterlist2 = [(translatefilter())]
        for f in filterlist2:
            print(f.reply(msg2))
