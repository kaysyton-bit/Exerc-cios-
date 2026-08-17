telefonia = {}

while True:
    dados = input('digite o nome que deseja cadastrar ou "fim" para consultar:').lower()
    if dados.strip() == 'fim' or dados == '':
        break
    dados_numero = int(input('digite o numero telefonico: '))
    telefonia[dados] = dados_numero

consulta = input('digite o nome para realizar a consulta:').lower()
if consulta not in telefonia.keys():
    print(f'{consulta} não foi cadastrado')
else:
    else:
    print('O numero de', consulta, 'é:', telefonia[consulta])
