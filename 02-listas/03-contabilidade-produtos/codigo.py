produto = []
preco_de_compra = []
lucros_desejados = []

for i in range(5):
    produto.append(input('digite o nome do produto para a contabilidade: '))
    preco_de_compra.append(float(input('digite o valor da compra: ')))
    lucros_desejados.append(float(input('digite o percentual de lucro desejado: ')))

for i in range(5):
    lucro = preco_de_compra[i] * (1 + (lucros_desejados[i]) / 100)
    print(f'{produto[i]}: Compra = R${preco_de_compra[i]}, Venda = R${lucro}')
