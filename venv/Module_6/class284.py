# os.walk
# os.walk e uma funcao que permite percorrer uma estrutura de diretorios de
# maneira recursiva. Ela gera uma sequencia de tuplas, onde cada tupla possui
# tres elementos: o diretorio atual (root), uma lista de subdiretorios (dirs)
# e uma lista os arquivos do diretorio atual (files).
import os
from itertools import count

caminho = os.path.join(
    '\\Users', 'guilh', 'OneDrive', 'Documentos', 'Curso',
    'Module_6', 'class283_examples'
    )
counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter, 'Pasta atual', root)

    for dir_ in dirs:
        print('  ', the_counter, 'Dir: ', dir_)

    for file_ in files:
        caminho_completo = os.path.join(root, file_)
        print('  ', the_counter, 'File: ', caminho_completo)
        os.unlink(caminho_completo)
