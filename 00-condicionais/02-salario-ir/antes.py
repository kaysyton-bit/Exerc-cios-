valor_diaria = float(input())
trabalhados_mes = int(input())
valor_bruto = valor_diaria * trabalhados_mes
ir1 = valor_diaria * trabalhados_mes * 15 / 100
ir2 = valor_diaria * trabalhados_mes * 27.5 / 100

if valor_bruto <= 2000.00:
    print("Você está isento do Imposto de Renda.")
    print(f"Seu salário é: R$ {valor_bruto:.2f}")
elif valor_bruto > 2000.00 and valor_bruto <= 5000.00:
    print("Você não está isento do Imposto de Renda.")
    print(f"Seu salário bruto é de: R$ {valor_bruto:.2f}")
    print(f"Seu valor do IR é: R$ {ir1:.2f}")
    print(f"Seu salário líquido é de: R$ {valor_bruto - ir1:.2f}")
elif valor_bruto > 5000.00:
    print("Você não está isento do Imposto de Renda.")
    print(f"Seu salário bruto é de: R$ {valor_bruto:.2f}")
    print(f"Seu valor do IR é: R$ {ir2:.2f}")
    print(f"Seu salário líquido é de: R$ {valor_bruto - ir2:.2f}")
