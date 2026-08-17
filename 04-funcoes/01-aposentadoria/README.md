# Cálculo de aposentadoria

## Problema

Calcular a idade de aposentadoria de uma pessoa com base no ano de
nascimento e no ano de contratação, considerando idade mínima e tempo
mínimo de contribuição. (Decidi escrever a lógica do código em inglês para exercitar boas práticas.)

## Antes

17/07/2026

Preciso corrigir as funções que não funcionam independentemente.
retirementageBR() recebia o dicionário aposentadoria inteiro e alterava
ele diretamente por dentro da função, ao invés de calcular e devolver um
valor com return, funciona, mas prende a função a esse dicionário
específico ela não funciona sozinha fora desse contexto.

## Depois

19/07/2026

Corrigi retirementageBR() para que ela não dependa mais do dicionário:
agora recebe só os dados que precisa (hireyr, yearbirt) e devolve o
resultado com return, deixando a responsabilidade de montar o dicionário
fora da função. 

11/08/2026

Criei um pacote para as funções.
