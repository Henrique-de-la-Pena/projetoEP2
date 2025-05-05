import random

def rolar_dados(n):
    lista = []
    for i in range(0, n):
        dado = random.randint(1, 6)
        lista.append(dado)
    return lista
