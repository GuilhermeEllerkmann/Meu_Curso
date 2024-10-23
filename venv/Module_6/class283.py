import os

# C:\Users\guilh\OneDrive\Documentos\Curso\Module_6\class283_examples

caminho = os.path.join(
    '\\Users', 'guilh', 'OneDrive', 'Documentos', 'Curso',
    'Module_6', 'class283_examples'
    )


for pasta in os.listdir(caminho):
    caminho_completo = os.path.join(caminho, pasta)
    print(pasta)

    if not os.path.isdir(caminho_completo):
        continue

    for imagem in os.listdir(caminho_completo):
        print('  ', imagem)

  
def asd(asd):
    teste = asd
    return teste