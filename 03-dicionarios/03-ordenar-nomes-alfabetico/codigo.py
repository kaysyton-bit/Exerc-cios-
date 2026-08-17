nomez = {}

while True:
    entrada = input('digite o nome que deseja cadastrar ou "fim" para consultar:').lower()
    if entrada == 'fim':
        break
    letra = entrada[0].upper()
    nomez[letra] = entrada

for letra, o in sorted(nomez.items()):
    print(letra, o)
