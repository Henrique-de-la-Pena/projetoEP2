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

def remover_dado(dados_rolados, dados_guardados, indice):
    dado = dados_guardados[indice]
    del dados_guardados[indice]
    dados_rolados.append(dado)
    return [dados_rolados, dados_guardados]

def calcula_pontos_regra_simples(dados_rolados):
    pontos_regra_simples = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for i in range(len(dados_rolados)):
        pontos_regra_simples[dados_rolados[i]] += dados_rolados[i]
    return pontos_regra_simples