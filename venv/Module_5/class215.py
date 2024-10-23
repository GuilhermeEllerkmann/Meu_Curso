class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta
    
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta




class Ferramenta_De_Escrever:
    def __init__(self, nome):
        self.nome = nome

    def escrever(self):
        return f'{self.nome} esta escrevendo'
    


escritor = Escritor('Luiz')
caneta = Ferramenta_De_Escrever('caneta azul')
maquina_de_escrever = Ferramenta_De_Escrever('Maquina de escrever')
escritor.ferramenta = caneta
escritor.ferramenta = maquina_de_escrever