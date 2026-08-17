lista = []
vogais = []

while True:
    compras = input()
    if compras.lower() == "fim":
        break
    lista.append(compras)
    if compras[0].lower() in "aeiou":
        vogais.append(compras)

if len(vogais) == 0:
    print('não ha vogais')
else:
    for i in vogais:
        print(i)
