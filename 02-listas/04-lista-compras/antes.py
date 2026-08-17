lista = []

while True:
    item = input()
    if item.lower() == "fim":
        break
    lista.append(item)

lista.sort()
for item in lista:
    print(item)
