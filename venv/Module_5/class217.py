class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []
    

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

cliente1 = Cliente('Guilherme')
cliente1.inserir_endereco('Maiocon lino Machado', 201)
cliente1.inserir_endereco('Rua Maria Esmeria', 314)

cliente1.listar_enderecos()