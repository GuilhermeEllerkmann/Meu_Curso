from dataclasses import dataclass, asdict, astuple


@dataclass()
class Pessoa:
    nome: str
    sobrenome: str


if __name__ == '__main__':
    p1 = Pessoa('Guilherme', 'Ellerkmann')
    print(asdict(p1).keys())
    print(asdict(p1).values())
    print(asdict(p1).items())
    print(astuple(p1))
