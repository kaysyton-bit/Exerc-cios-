import datetime
from datetime import date


def calculateyr(yearbirth):
    hoje = datetime.date.today()
    age = hoje.year - yearbirth
    return age


def retirementageBR(workcardid, hireyr, yearbirt, retirement):
    retirement['CTPS'] = workcardid
    min_ageBR = 65
    min_contribution = 20
    agein_hireyr = hireyr - yearbirt
    agef_time = agein_hireyr + min_contribution
    retirement['Ano de aposentadoria'] = max(min_ageBR, agef_time)


aposentadoria = {}
aposentadoria['Nome'] = input('Digite seu nome: ')
yrbirth = int(input('Digite seu ano de nascimento: '))
aposentadoria['Ano de nascimento'] = yrbirth
aposentadoria['Idade'] = calculateyr(yrbirth)
workcard = int(input('Digite o numero da sua carteira de trabalho (ou 0 caso não tenha): '))

if workcard > 0:
    hiredate = int(input('Digite seu ano de contratação: '))
    aposentadoria['Salario'] = float(input('Digite seu salario: $').replace(',', '').strip())
    retirementageBR(workcard, hiredate, yrbirth, aposentadoria)

for chave, dado in aposentadoria.items():
    print('- ', chave, ':', dado)
