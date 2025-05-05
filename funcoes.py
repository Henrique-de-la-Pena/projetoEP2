import random

def rolar_dados(n):
    lista = []
    for i in range(0, n):
        dado = random.randint(1, 6)
        lista.append(dado)
    return lista

def guardar_dado(dados_rolados, dados_guardados, indice):
    dado = dados_rolados[indice]
    del dados_rolados[indice]
    dados_guardados.append(dado)
    return [dados_rolados, dados_guardados]