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

def calcula_pontos_soma(dados_rolados):
    soma = 0
    for i in range(len(dados_rolados)):
        soma += dados_rolados[i]
    return soma

def calcula_pontos_sequencia_baixa(dados_rolados):
    for i in range(len(dados_rolados)):
        if dados_rolados[i] + 1 in dados_rolados:
            if dados_rolados[i] + 2 in dados_rolados:
                if dados_rolados[i] + 3 in dados_rolados:
                    return 15
    return 0

def calcula_pontos_sequencia_alta(dados_rolados):
    for i in range(len(dados_rolados)):
        if dados_rolados[i] + 1 in dados_rolados:
            if dados_rolados[i] + 2 in dados_rolados:
                if dados_rolados[i] + 3 in dados_rolados:
                    if dados_rolados[i] + 4 in dados_rolados:
                        return 30
    return 0

def calcula_pontos_full_house(dados_rolados):
    dados = {}
    soma = 0
    for i in range(len(dados_rolados)):
        if dados_rolados[i] not in dados:
            dados[dados_rolados[i]] = 1
        else:
            dados[dados_rolados[i]] += 1
    if len(dados) == 2:
        for qtd in dados.values():
            if qtd == 2:
                for valor, vezes in dados.items():
                    soma += valor * vezes
    return soma

def calcula_pontos_quadra(dados_rolados):
    dados = {}
    soma = 0
    for i in range(len(dados_rolados)):
        if dados_rolados[i] not in dados:
            dados[dados_rolados[i]] = 1
        else:
            dados[dados_rolados[i]] += 1
    for qtd in dados.values():
        if qtd >= 4 and soma == 0:
            for valor, vezes in dados.items():
                soma += valor * vezes
    return soma