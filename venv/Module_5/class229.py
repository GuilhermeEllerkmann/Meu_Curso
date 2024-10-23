from abc import ABC, abstractmethod

class Log(ABC):

    @abstractmethod
    def _log(self, msg):...
    
    def _log_error(self, msg):
        return self._log(f'Error: {msg}')
    
    def _log_sucess(self, msg):
        return self._log(f'Sucess: {msg}')
    

class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')

l = LogPrintMixin()
l._log_error('oi')