class Caneta:
    def __init__(self, cor):
        self._cor_tampa = None
        self._cor = cor

    @property
    def cor(self):
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        if valor == 'Rosa':
            raise ValueError('Nao aceito essa cor')
        
        print('estou no setter', valor)
        self._cor = valor
    
    @property
    def cor_tampa(self):
        return self._cor_tampa
    
    @cor_tampa.setter
    def cor_tampa(self, cor):
        self._cor_tampa = cor

        


caneta = Caneta('Azul')
caneta.cor = 'Preta'
caneta.cor_tampa = 'Roxo'


print(caneta.cor, caneta.cor_tampa)
