#Escopo da classe e de metodos de classe

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def acao(self, alimento):
        print(f'{self.nome} esta comendo {alimento}')

    def executar(self, *args, **kwargs):
        return self.acao(*args, **kwargs)

leao = Animal('Leao')
print(leao.nome)
leao.executar('zebra')