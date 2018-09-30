from abc import ABCMeta, abstractmethod

class absfilter(metaclass=ABCMeta):
    def reply(self,msg):
        if isinstance(self, absfilter):
            return self.msgprocess(msg)

    @abstractmethod
    def msgprocess(self,msg):
            pass
