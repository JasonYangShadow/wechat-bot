import unittest
from pprint import pprint
from weatherfiler import weatherfiler
from absfilter import absfilter

class Test(unittest.TestCase):

    @unittest.skip('skip')
    def testweather(self):
        w = weatherfiler()
        print(w.msgprocess('h'))

    #@unittest.skip('skip')
    def testabsfilter(self):
        msg = u'让我看看天气'
        filterlist = [weatherfiler()]
        for f in filterlist:
            print(f.reply(msg))
