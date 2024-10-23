'''
Você foi contratado para desenvolver um script em Python que organize os
arquivos de uma pasta de maneira eficiente.
Sua tarefa é criar um programa que, usando a biblioteca pathlib, faça o
seguinte:

Liste todos os arquivos e subdiretórios dentro de uma pasta específica.

Verifique a extensão dos arquivos e mova-os para subdiretórios baseados em
suas extensões
(por exemplo, todos os arquivos .txt devem ser movidos para uma pasta chamada
txt, arquivos .jpg para uma pasta jpg, e assim por diante).

Se o subdiretório para uma extensão específica não existir, crie-o.

Após mover os arquivos, exiba uma mensagem indicando quantos arquivos foram
movidos e para quais pastas.

'''

from pathlib import Path

TARGET_DICT = (Path.home() / 'OneDrive' / 'Documentos' / 'Curso' /
               'Module_6' / 'my_ideas' / 'arquivos')


for item in TARGET_DICT.rglob('*'):
    if item.is_file():
        extention = item.suffix
        extention_dict = TARGET_DICT / f'{extention}_files'
        extention_dict.mkdir(exist_ok=True)
        new_file_path = extention_dict / item.name
        item.rename(new_file_path)

        print(f'Arquivo movido para: {new_file_path}')
