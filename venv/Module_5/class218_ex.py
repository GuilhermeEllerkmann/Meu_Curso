class Carro:
    def __init__(self, nome, motores):
        self.nome = nome
        self._motor = None
        self._motores = motores  

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, codigo_motor):
        motor = self._motores.obter_motor(codigo_motor)
        if motor:
            self._motor = motor
        else:
            raise ValueError("Código de motor não encontrado.")

class Motor:
    def __init__(self):
        self._lista_motores = {}

    def adicionar_motor(self, motor, codigo):
        self._lista_motores[codigo] = motor

    def obter_motor(self, codigo):
        return self._lista_motores.get(codigo, None)

class Fabricante:
    def __init__(self, nome):
        self.nome = nome
        self._carros = []

    def insere_carro(self, carro):
        self._carros.append(carro)

    def listar(self):
        for carro in self._carros:
            print(f'Carro {carro.nome} com motor {carro.motor} da Fabricante {self.nome}')

# Inicializa a lista de motores
motores = Motor()
motores.adicionar_motor('1.6 em V', '001')
motores.adicionar_motor('1.6 em linha', '002')

# Inicializa o carro com a referência dos motores
gol = Carro('Gol', motores)
fox = Carro('Fox', motores)

# Atribui o motor ao carro pelo código
gol.motor = '001'
fox.motor = '002'

# Inicializa o fabricante e insere o carro
wolks = Fabricante('Wolksvagen')
wolks.insere_carro(gol)
wolks.insere_carro(fox)

# Lista os carros e seus motores
wolks.listar()
