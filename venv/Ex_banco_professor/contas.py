from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia: int, conta: int, saldo: float = 0):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abstractmethod
    def sacar(self, valor: float) -> float:
        ...

    def depositar(self, valor: float) -> float:
        self.saldo += valor
        self.detalhes(f'(DEPOSITO {valor})')
        return self.saldo

    def detalhes(self, msg: str = '') -> None:
        print(f'O seu saldo e {self.saldo:.2f} {msg}')

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'{self.agencia!r}, {self.conta!r}, {self.saldo!r}'
        return f'{class_name}({attrs})'


class ContaPoupanca(Conta):
    def sacar(self, valor):

        if self.saldo < valor:
            self.detalhes(f'Saque negado {valor}')
            return self.saldo
        else:
            self.saldo -= valor
            self.detalhes(f'SAQUE REALIZADO {valor}')
            return self.saldo


class ContaCorrente(Conta):
    def __init__(
            self, agencia: int, conta: int, saldo: float = 0, limite: float = 0
    ):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor: float) -> float:
        limite_maximo = -self.limite

        if self.saldo <= limite_maximo:
            self.detalhes(f'Saque negado {valor}')
            return self.saldo
        else:
            self.saldo -= valor
            self.detalhes(f'SAQUE REALIZADO {valor}')
            return self.saldo

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r}, '\
            f'{self.limite!r})'
        return f'{class_name}{attrs}'


if __name__ == '__main__':
    cp1 = ContaPoupanca(111, 222)
    cp1.sacar(1)
    cp1.depositar(1)
    cp1.sacar(1)
    cp1.sacar(1)
    print('##')

    cc1 = ContaCorrente(111, 222, 0, 100)
    cc1.sacar(1)
    cc1.depositar(1)
    cc1.sacar(1)
    cc1.sacar(1)
    cc1.sacar(98)
    cc1.sacar(1)
    print('##')
