class Pessoa:
    year = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    @classmethod
    def metodo_de_classe(cls):
        return 

    @classmethod
    def create_50(cls, name):
        return cls(name, 50)
    
    @classmethod
    def anonymous(cls, idade):
        return cls('Anonymous', idade)
    


p1 = Pessoa.create_50('Guilherme')
p2 = Pessoa.anonymous(30)
print(p2.nome, p2.idade)



