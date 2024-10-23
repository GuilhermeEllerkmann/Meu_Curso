from dataclasses import dataclass


@dataclass()
class Pessoa:
    nome: str
    sobrenome: str


if __name__ == '__main__':
    lista = [Pessoa('A', 'Z'), Pessoa('B', 'Y'), Pessoa('C', 'X'), ]
    ordenadas = sorted(lista, reverse=False, key=lambda p: p.sobrenome)
    print(ordenadas)
