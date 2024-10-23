class Pessoa:
    ANO_ATUAL = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def ano_de_nascimento(self):
        ano = Pessoa.ANO_ATUAL - self.idade
        return ano
    

p1 = Pessoa('Guilherme', 24)

print(p1.ano_de_nascimento())