import random

# Funcoes:
# seed
#  -> Inicializa o gerador de random (por isso "Numeros pseudoaleatorios")
random.seed(0)


# random.randrange(inicio, fim, passo)
#   -> gera um numero inteiro aleatorio dentro de um intervalo especifico
r_range = random.randrange(10, 20, 2)
# print(r_range)

# random.randint(inicio, fim)
#   -> gera um numero inteiro aleatorio dentro de um intervaldo "sem passo"
r_int = random.randint(10, 20)
# print(r_int)

# random.uniform(inicio, fim)
#   -> gera um numero flutuante aleatorio dentro de um intervalo 'sem passo'
r_uni = round(random.uniform(10, 20), 2)
# print(r_uni)

# random.shuffle(SequenciaMutavel) -> Embaralha a lista original
nomes = ['Luiz', 'Guilherme', 'Giovana', 'Lucas']
# random.shuffle(nomes)
# print(nomes)

# random.sample(iteravel, k=N)
#   -> escolhe elementos do iteravel e retorna outro iteravel (nao repete)
novos_nomes = random.sample(nomes, k=2)
# print(novos_nomes)

# random.choices(Iteravel, k=N)
#   -> Escolhe elementos do iteravel e retorna outro iteravel (repete)
novos_nomes = random.choices(nomes, k=3)
# print(nomes)
# print(novos_nomes)

# random.choice(Iteravel) -> escolhe um item do iteravel
print(random.choice(nomes))
