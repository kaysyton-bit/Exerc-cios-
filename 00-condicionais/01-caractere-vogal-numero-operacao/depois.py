caractere = str(input())
if len(caractere) != 1:
    print("será aceito apenas um caractere.")
elif caractere.lower() in "aeiou":
    print("O caractere é uma vogal")
elif caractere.isdigit():
    print("O caractere é um número")
elif caractere in "+-*/":
    print("O caractere é uma operação matemática")
else:
    print("ERRO! o caractere não é numero, vogal ou operação matemática")
