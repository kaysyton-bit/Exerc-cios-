import random

input('pressione um botão para iniciar')

while True:
    user_sentinel = input('vamos jogar par ou impar?: ) S/N? ').strip().lower()
    if user_sentinel == 'n':
        break
    elif user_sentinel == 's':
        user = input('escolha entre par ou impar: ').strip().lower()
        if user == "par":
            user_plays = int(input('digite seu numero: '))
            computer = random.randint(1, 100)
            resultado = user_plays + computer
            if resultado % 2 == 0:
                print(f'minha jogada foi: {computer} e a sua: {user_plays} \nParabens voce ganhou! ')
                continue
            elif resultado % 2 != 0:
                print(f'minha jogada foi: {computer} e a sua: {user_plays} \nInfelizmente você perdeu. ')
                break
        elif user == "impar":
            user_plays = int(input('digite seu numero: '))
            computer = random.randint(1, 100)
            resultado = user_plays + computer
            if resultado % 2 != 0:
                print(f'minha jogada foi: {computer} e a sua: {user_plays} \nParabens voce ganhou! ')
                continue
            elif resultado % 2 == 0:
                print(f'minha jogada foi: {computer} e a sua: {user_plays} \nInfelizmente você perdeu. ')
                break
        else:
            print('escolha entre "par" ou "impar" para jogar ')
            continue
    else:
        print('escolha entre "S/N" ')
        continue

print('obrigado por jogar, ate uma proxima! ;)')
