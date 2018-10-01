from absfilter import absfilter
from urllib.request import urlopen,quote
from config import Config
import json

class weatherfiler(absfilter):
    def __init__(self):
        self.__config = Config()
        self.__key = self.__config.getValue("weather","key")
        self.__api = "https://free-api.heweather.com/s6/weather/forecast"
        self.__cities = self.__config.getValue("weather","city")

    def msgprocess(self,msg):
        if u'问天气' in msg:
            cities = self.__cities.split(',')
            text = ''
            for city in cities:
                city_quote = quote(city)
                url = self.__api+"?location="+city_quote+"&key="+self.__key
                with urlopen(url) as resp:
                    jsonvalue = json.loads(resp.read().decode('utf-8'))
                    if jsonvalue is not None:
                        if jsonvalue['HeWeather6'][0]['status'] == 'ok':
                            text += city+'\n' 
                        for item in jsonvalue['HeWeather6'][0]['daily_forecast']:
                            text += u'日期:'+item.get('date','') + ' ' + u'白天天气:'+ item.get('cond_txt_d','')+ ' ' + u'晚间天气:'+ item.get('cond_txt_n','')+' '+ u'最高温度:' + item.get('tmp_max','') +'度 '+ u'最低温度:'+ item.get('tmp_min','') +'度 ' + u'降水概率:' + item.get('pop','未知') +' ' + u'风向:' + item.get('wind_dir','') + ' ' + u'风力:' + item.get('wind_sc','') +'级 ' + '\n'
                        text += '\n'
            return text
        else:
            return None
