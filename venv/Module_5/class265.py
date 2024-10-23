from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    idade: int


if __name__ == '__main__':
    p1 = Pessoa('Guilherme', 17)
    p2 = Pessoa('Guilherme', 17)

    print(p1, p2)
    print(p1 == p2)
