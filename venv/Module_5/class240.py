# with open('class240.txt', 'w') as arquivo:
#     ...

class MyOpen:
    def __init__(self, caminho_arquivo, modo):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None
    
    def __enter__(self):
        print('Abrindo arquivo')
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf8')
        return self._arquivo

    def __exit__(self, class_excepetion, excepetion_, traceback_):
        print('Fechando arquivo')
        self._arquivo.close()

        # raise class_excepetion('minha mensagem')

        # print(class_excepetion)
        # print(excepetion_)
        # print(traceback_ )
        # excepetion_.add_note('Minha nota')
        
        return True


with MyOpen('class240.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n', 123)
    arquivo.write('Linha 3\n')
    print('WITH', arquivo)