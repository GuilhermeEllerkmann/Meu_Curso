class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, nome):
        print(f'Chamando {nome}', self.phone)

call1 = CallMe(14988094431)
call1('Guilherme')     