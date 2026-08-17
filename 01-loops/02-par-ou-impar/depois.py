import random


def obter_numero_valido(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor.lstrip("-").isdigit():
            return int(valor)
        print("Digite um número inteiro válido.")


def obter_escolha_par_impar():
    while True:
        escolha = input("Escolha entre 'par' ou 'impar': ").strip().lower()
        if escolha in ("par", "impar"):
            return escolha
        print('Escolha inválida. Digite "par" ou "impar".')


def jogar_rodada():
    escolha = obter_escolha_par_impar()
    jogada_usuario = obter_numero_valido("Digite seu número: ")
    jogada_computador = random.randint(1, 100)
    soma = jogada_usuario + jogada_computador
    soma_e_par = soma % 2 == 0
    usuario_venceu = soma_e_par if escolha == "par" else not soma_e_par

    print(f"Minha jogada foi: {jogada_computador} e a sua: {jogada_usuario}")
    print("Parabéns, você ganhou!" if usuario_venceu else "Infelizmente você perdeu.")


def main():
    input("Pressione um botão para iniciar: ")
    while True:
        continuar = input("Vamos jogar par ou ímpar? (S/N) ").strip().lower()
        if continuar == "n":
            break
        elif continuar == "s":
            jogar_rodada()
        else:
            print('Escolha entre "S" ou "N".')
    print("Obrigado por jogar, até uma próxima! ;)")


if __name__ == "__main__":
    main()
