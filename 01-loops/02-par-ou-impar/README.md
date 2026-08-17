# Jogo par ou ímpar

## Problema

Jogo de par ou ímpar contra o computador: o usuário escolhe par ou
ímpar, digita um número, o computador sorteia outro, e o resultado da
soma decide quem ganhou. O jogo repete até o usuário decidir sair.

## Antes

04/01/2026

Primeira versão, funcional, mas com lógica duplicada quase idêntica
entre os blocos de "par" e "impar".

## Depois

29/05/2026

Além de criar funções, removi a lógica duplicada. Ao ser removida, não
interfere no resultado do jogo nem no funcionamento do programa. A
função obter_numero_valido() checa se um número é válido, inicialmente
como string: uso valor.lstrip("-") para checar se não se trata de um
número negativo e .isdigit() para checar se é um número, retornando o
valor com return, o que encerra a função sem a necessidade de um else
- caso o primeiro if não fosse satisfeito, cairia direto no print. No
código anterior eu usava só strip e lower para retornar a variável sem
espaços e minúscula, caindo direto em um else com print e um continue
para reiniciar o laço.

Sobre if __name__ == "__main__": main(): é convenção profissional, o
código só roda automaticamente se o arquivo for executado diretamente.
Se um dia eu importar esse arquivo em outro programa (ou em um teste
automatizado) pra reaproveitar jogar_rodada(), o jogo não vai disparar
sozinho.
