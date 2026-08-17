lista = {}
n = int(input('digite a quantidade de linhas: '))

for i in range(1, n + 1):
    pares = input('digite os valores: ').split()
    chave = pares[0]
    valor = int(pares[1])
    if chave in lista:
        soma = valor + lista[chave]
        lista[chave] = soma
        continue
    lista[chave] = valor

for categoria, valor in lista.items():
    print(*{categoria}, sep=': ', *{valor})
