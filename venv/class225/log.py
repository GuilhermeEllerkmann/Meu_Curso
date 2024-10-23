from pathlib import Path
LOG_FILE = Path(__file__).parent / 'log.txt'

class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o metodo log')
    
    def _log_error(self, msg):
        return self._log(f'Error: {msg}')
    
    def _log_sucess(self, msg):
        return self._log(f'Sucess: {msg}')
    
class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        print('Salvando no log', msg_formatada)
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\n')


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')

if __name__ == "__main__":
    l = LogPrintMixin()
    l._log_error('Tudo errado cachorro')
    l._log_sucess('Que loko cachorro')
    lf = LogFileMixin()
    lf._log_error('asdasd')
    lf._log_sucess('que daora')
    print(LOG_FILE)