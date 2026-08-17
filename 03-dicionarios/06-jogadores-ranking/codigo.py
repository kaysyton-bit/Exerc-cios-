import random

jogadores = {}

for i in range(1, 5):
    jogadores[f'jogador {i}'] = input(
        f'pessione enter para fazer sua jogada jogador n{i}: '
    ), random.randint(1, 10)

print('Valores sorteados:')
for jogador, numero in jogadores.items():
    print('O', jogador, 'recebeu: ', *numero)

print("Ranking dos jogadores:")
for posicao, (d, v) in enumerate(
    sorted(jogadores.items(), key=lambda x: x[1], reverse=True), start=1
):
    print(posicao, 'lugar:', d, 'com: ', *v)
