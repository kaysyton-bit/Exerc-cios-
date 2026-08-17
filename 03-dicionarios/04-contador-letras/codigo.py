alpha = {}
mensagem = input('digite a frase: ').replace(" ", "").upper()

for letra in mensagem:
    if letra.isalpha():
        if letra in alpha.keys():
            alpha[letra] += 1
        else:
            alpha[letra] = 1

for chave, quantidade in sorted(alpha.items()):
    print(chave, ': ', quantidade)
