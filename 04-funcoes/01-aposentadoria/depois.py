from scr import aposentadoriaa 


aposentadoria = {}
aposentadoria['Nome'] = input('Digite seu nome: ')
yrbirth = int(input('Digite seu ano de nascimento: '))
aposentadoria['Ano de nascimento'] = yrbirth
aposentadoria['Idade'] = aposentadoriaa.calculateyr(yrbirth)
workcard = int(input('Digite o numero da sua carteira de trabalho (ou 0 caso não tenha): '))

if workcard > 0:
    hiredate = int(input('Digite seu ano de contratação: '))
    aposentadoria['Salario'] = float(input('Digite seu salario: $').replace(',', '').strip())
    aposentadoria['Ano de aposentadoria'] = aposentadoriaa.retirementageBR(hiredate, yrbirth)
    aposentadoria['CTPS'] = workcard

for chave, dado in aposentadoria.items():
    print('- ', chave, ':', dado)
