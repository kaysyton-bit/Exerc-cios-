valores = []
pares = []
impares = []

while True:
    entrada = int(input('digite um numero: '))
    valores.append(entrada)
    if entrada % 2 == 0:
        pares.append(entrada)
    else:
        impares.append(entrada)
    confirmacao = input('deseja continuar? s/n: ').lower()
    if confirmacao == 'n':
        break

print(
    f'Quantidade de números digitados: {len(valores)} '
    f'Soma dos números pares: {sum(pares)} '
    f'Soma dos números ímpares: {sum(impares)}'
)
