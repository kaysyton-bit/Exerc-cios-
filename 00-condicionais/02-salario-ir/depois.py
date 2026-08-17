def calcular_ir(salario):
    if salario <= 2000:
        return 0
    elif salario <= 5000:
        return 0.15
    else:
        return 0.275


def calcular_salario(valor_diaria, dias_trabalhados):
    salario_bruto = valor_diaria * dias_trabalhados
    percentual = calcular_ir(salario_bruto)
    ir = percentual * salario_bruto
    salario_liquido = salario_bruto - ir
    return salario_bruto, percentual, ir, salario_liquido


valor_diaria = float(input())
dias_trabalhados = int(input())
salario_bruto, percentual, ir, salario_liquido = calcular_salario(
    valor_diaria, dias_trabalhados
)

if percentual == 0:
    print(f'Você está isento do Imposto de Renda.\nSeu salário é: R$ {salario_bruto:.2f}')
else:
    print(
        f'Você não está isento do Imposto de Renda.\n'
        f'Seu salário bruto é de: R$ {salario_bruto:.2f}\n'
        f'Seu valor do IR é: R$ {ir:.2f}\n'
        f'Seu salário líquido é de: R$ {salario_liquido:.2f}'
    )
