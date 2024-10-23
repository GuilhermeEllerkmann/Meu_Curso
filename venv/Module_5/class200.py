#methods in instances of classes in python
#hard coded - is something that was writen directly on the code

class Carro:
    def __init__(self,nome):
        self.nome = nome

    def acelerar(self):
        print(f'O carro {self.nome} esta acelerando')

fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()

celta   = Carro('Celta')
print(celta.nome)
celta.acelerar()