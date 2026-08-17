# Quantos pares? Quantos ímpares?

## Problema

O usuário digita uma quantidade indeterminada de números inteiros. Ao
final, exibir a quantidade de números digitados, a soma dos pares e a
soma dos ímpares.

## Código

13/06/2026

Infelizmente perdi o acesso à versão antiga do código.

O mais fácil até agora. Me admira o professor tê-lo colocado como
dificuldade média. Não sei como esperava que fosse resolvido o código
anterior, que supostamente seria fácil, se havia uma maneira mais
simples de resolver este.

Para a quantidade de números, como o assunto se tratava de listas,
armazenei os números em uma lista ao invés de usar uma variável de
controle. Para a soma dos pares, usei uma condição que verifica se o
resto da divisão do número por dois é igual a 0; se for, o número é
adicionado à lista de pares com append. Os números que não satisfazem
essa condição são adicionados à lista de ímpares, o que me permitiu
economizar em número de variáveis e condicionais.
