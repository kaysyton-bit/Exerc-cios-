salarios = {}

while True:
    cpf_ = input('digite o cpf do funcionario')
    nome_ = input('digite o nome do funcionario: ')
    salario_ = float(input('digite o salario do funcionario: '))
    salarios[nome_] = {"cpf": cpf_, "salario": salario_}

    p = input("digite 'enter' para encerrar ou 'continue' para continuar cadastrando...:")
    if p == '':
        break
    if p.lower().strip() == 'continue':
        continue
    else:
        print('comando não reconhecido')
        continue

somas = []
for dados in salarios.values():
    somas.append(dados['salario'])
media = sum(somas) / len(somas)

print("Abaixo da média:")
for dados, valor in salarios.items():
    if valor['salario'] < media:
        print(dados)
        print(valor['cpf'])

print("Acima da média:")
for dados, valor in salarios.items():
    if valor['salario'] > media:
        print(dados)
        print(valor['cpf'])
