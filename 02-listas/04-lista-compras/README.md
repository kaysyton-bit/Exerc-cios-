# Lista de compras

## Problema

Simular uma lista de compras. O usuário deve poder digitar itens
livremente, um por vez, e o programa deve armazená-los em uma lista. A
entrada termina quando o usuário digitar "fim" (caso-insensitivo). Ao
final, exibir todos os itens em ordem alfabética crescente. Depois o
problema foi expandido: exibir apenas os itens que começam com vogal.

## Antes

06/12/2025

Honestamente nem sei como isso foi aceito, o código faz tudo menos o
que precisava fazer. Apenas criei a possibilidade do usuário digitar
itens na lista e organizei em ordem alfabética, usando um for para
mostrar um item de cada vez - mas não filtra por vogal, que era o
pedido.

## Depois (ainda não terminado, mas funcional)

21/06/2026

Criei duas listas vazias, como pedido pela questão. Um laço infinito que
é quebrado somente quando o usuário digita "fim", independente de ser
maiúsculo ou minúsculo, antes de ser adicionado à lista, garantindo que
"fim" não vá parar lá dentro. Depois checo se a primeira letra da
entrada é uma vogal (independentemente de ser maiúscula ou não)
verificando se está dentro da string "aeiou", já que Python não tem uma
função nativa que identifique vogais. Se for uma vogal, a palavra é
adicionada à última posição de uma lista separada. Depois que o
primeiro laço é quebrado, o programa checa se a lista de vogais está
vazia; se estiver, uma mensagem é exibida informando ao usuário, senão
o programa exibe somente os itens que começam com vogal, um por vez.

Ainda falta a ordenação alfabética pedida no enunciado original, que
ficou de fora nessa versão.
