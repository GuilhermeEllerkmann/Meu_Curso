'''Crie um script em Python que:

Leia um arquivo CSV que contenha informações de alunos. O arquivo terá as
seguintes colunas: Nome, Idade, Nota1, Nota2, Nota3.

Calcule a média de cada aluno com base nas três notas e escreva um novo
arquivo CSV com os mesmos dados, mas com a coluna Média incluída.

Regras:
Você deve usar a biblioteca csv para ler e escrever os arquivos.
O arquivo CSV original será fornecido no seguinte formato:

Nome,Idade,Nota1,Nota2,Nota3
Ana,17,8.5,9.0,7.5
Bruno,18,6.0,5.5,7.0
Carla,17,9.5,8.0,9.0

O novo arquivo CSV deve ser salvo com o nome alunos_media.csv.

'''

import csv
from pathlib import Path
from typing import Dict, List, Union

CSV_PATH = (Path.home()
            / 'OneDrive' / 'Documentos' / 'Curso' /
            'Module_6' / 'my_ideas' / 'arquivos' / 'alunos_notas.csv'
            )

NEW_FILE_CSV = (Path.home()
                / 'Onedrive' / 'Documentos' / 'Curso' / 'Module_6' /
                'my_ideas' / 'arquivos' / 'alunos_media.csv'
                )

with open(CSV_PATH, 'r', newline='') as inputfile:
    reader = csv.DictReader(inputfile)
    fieldnames = (list(reader.fieldnames) if
                  reader.fieldnames is not None else [])

    linhas: List[Dict[str, Union[float, str]]] = []
    app_repr_line: List[Dict[str, float]] = []

    for linha in reader:
        try:
            nome: str = linha['Nome']
            idade: float = float(linha['Idade'])
            nota1: float = float(linha['Nota1'])
            nota2: float = float(linha['Nota2'])
            nota3: float = float(linha['Nota3'])
            media: float = (nota1 + nota2 + nota3) / 3

            dados_aluno: Dict[str, Union[float, str]] = {
                'Nome': nome,
                'Idade': idade,
                'Nota1': nota1,
                'Nota2': nota2,
                'Nota3': nota3,
                'Media': media,
            }

            if media < 5:
                dados_aluno['Aproved?'] = 'Reproved'
            else:
                dados_aluno['Aproved?'] = 'Aproved'

            linhas.append(dados_aluno)

        except ValueError as e:
            print(f"Erro ao converter valores na linha: {linha}. Erro: {e}")
        except KeyError as e:
            print(f"Coluna não encontrada: {e}")

    with open(NEW_FILE_CSV, 'w', newline='') as outfile:
        if 'Media' not in fieldnames:
            fieldnames.append('Media')
        if 'Aproved?' not in fieldnames:
            fieldnames.append('Aproved?')
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(linhas)
