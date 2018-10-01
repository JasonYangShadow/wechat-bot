from absfilter import absfilter
from forex_python.converter import CurrencyRates
import re

class currencyfilter(absfilter):
    def __init__(self):
        self.__currency = CurrencyRates()

    def msgprocess(self,msg):
        text = ''
        allmatched = re.findall(u'(\d+日元)',msg)
        if len(allmatched) >0:
            for matched in allmatched:
                jpy = matched[:-2]
                cny = self.__currency.convert('JPY','CNY',int(jpy))
                text += matched +' => ' + str(cny) + u'人民币' + '\n'
            return text
        else:
            return None
