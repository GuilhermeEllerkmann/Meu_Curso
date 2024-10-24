# os + shutil - Apagando, copiando, movendo e renomeando pastas com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
# Copiar Árvore recursivamente -> shutil.copytree
# Apagar Árvore recursivamente -> shutil.rmtree
# Apagar arquivos -> os.unlink
# Renomear/Mover -> shutil.move ou os.rename

import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'OneDrive', 'Desktop')
PASTA_ORIGINAL = os.path.join(DESKTOP, 'class286_photos')
NOVA_PASTA = os.path.join(DESKTOP, 'NOVA_PASTA')

if os.path.exists(NOVA_PASTA):
    print('Pasta ja existe, impossivel criar pasta existente')
else:
    shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA)
