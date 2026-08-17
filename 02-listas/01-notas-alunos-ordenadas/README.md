# Alunos ordenados por nota

## Problema

Cadastrar nomes e notas de alunos e exibir a lista ordenada da maior
para a menor nota.

## Código

06/06/2026

Não resolvi problemas de listas da primeira vez, portanto esta é minha
primeira e atual versão de um código de listas (talvez desenvolva
melhor em outro momento com funções).

Esta atividade me deu um pouco mais de trabalho devido a alguns
descuidos na hora de usar o laço for. No entanto, foi excelente para
praticar diversos métodos de manipulação de listas.

Funções anônimas (lambda): Pratiquei o uso de métodos mais sofisticados,
como a função anônima key=lambda, muito comum para manipular listas.
Neste programa utilizei-a para dizer ao Python qual parâmetro (e de qual
posição da lista) ele deveria levar em consideração na hora de ordenar.

Estrutura dos dados com zip(): o parâmetro que apelidei de "nota" (poderia ter qualquer outro nome)
representa a segunda posição das
listas que foram unidas pelo método zip(). A estrutura criada contém
primeiro o nome e depois a nota, sendo posição [0] o nome e posição [1]
a nota, que é o critério de ordenação.

Diferença na ordenação (decrescente vs inversão): para ordenar do maior
para o menor, utilizei o argumento reverse=True. Ele ordena os elementos
com base em seus valores de forma decrescente. Isso é diferente da
função reverse(), que apenas inverte a ordem atual da lista, sem levar
em conta o valor dos dados (O exercício durou mais que o esperado porque confundi as duas coisas).
