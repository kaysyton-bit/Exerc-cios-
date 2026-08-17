caractere = input()
if caractere in "aeiou" or caractere in "AEIOU":
    print("O caractere é uma vogal")
elif caractere.isnumeric():
    print("O caractere é um número")
elif caractere in "+-*/":
    print("O caractere é uma operação matemática")
