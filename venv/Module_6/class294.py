import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'module_arc' / 'class294.csv'

lista_clientes = [
    {'Nome': 'Guilherme', 'Endereco': 'Marcolino machado, 201'},
    {'Nome': 'Giovana', 'Endereco': 'Maria esmeria, 314'},
    {'Nome': 'Leonardo', 'Endereco': 'N/A, N/A'},
]

with open(CAMINHO_CSV, 'w', newline='') as arquivo:
    nome_colunas = lista_clientes[0].keys()
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=nome_colunas
    )
    escritor.writeheader()

    for cliente in lista_clientes:
        escritor.writerow(cliente)


# with open(CAMINHO_CSV, 'w', newline='') as arquivo:
#     # nome_colunas = lista_clientes[0].keys()
#     nome_colunas = ['Nome', 'Endereco']
#     escritor = csv.writer(arquivo)

#     escritor.writerow(nome_colunas)

#     for cliente in lista_clientes:
#         escritor.writerow(cliente.values())
