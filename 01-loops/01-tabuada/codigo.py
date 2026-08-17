while True:
    numero = int(input('digite um numero inteiro ou um numero negativo para parar:'))
    if numero < 0:
        break
    for i in range(11):
        print(f"{numero} x {i} = {numero * i}")

print('você optou por encerrar o programa')
