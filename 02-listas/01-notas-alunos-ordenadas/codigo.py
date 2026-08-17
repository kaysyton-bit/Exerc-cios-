nome = []
nota = []

while True:
    nomes = input('digite o nome do aluno: ')
    if nomes == "" or nomes.lower() == "fim":
        break
    elif nomes.isdigit():
        print('insira primeiro o nome do aluno:')
        continue
    nome.append(nomes)
    notas = float(input('digite a nota do aluno: ').replace(',', '.'))
    nota.append(notas)

juntos = list(zip(nome, nota))
for nomes, notas in sorted(juntos, key=lambda nota: nota[1], reverse=True):
    print(f"{nomes}: {notas:.2f}")
