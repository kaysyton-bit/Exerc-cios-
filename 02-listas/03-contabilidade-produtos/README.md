# Contabilidade de produtos

## Problema

Ler os nomes, os preços de compra e os percentuais de lucro de 5
produtos. Exibir para cada um o nome, o preço de compra e o preço de
venda calculado.

## Código

19/06/2026

Esse exercício poderia ter sido melhor resolvido criando dicionários,
porém o foco da disciplina na época era trabalhar as listas, então
foquei em usar somente os métodos ensinados no curso até então. Em breve
vou revisitar esse código e tabalha-lo melhor.

Criei três listas independentes vazias pois pretendia usar repetição,
tendo um melhor controle na manipulação dos dados. Criei um laço que se
repete 5 vezes ao invés de um looping, já que a questão tratava de 5
produtos. Fiz o append ao fim de cada lista a partir da entrada do
usuário, não vi necessidade de criar variáveis temporárias.

Ao fim do primeiro laço inicio outro que se repetirá 5x, pois já sabia
que se tratavam de 5 objetos em cada lista a serem percorridos, sem
necessidade de usar len. Para cada objeto, o lucro se dá pelo resultado
do objeto em preco_de_compra multiplicado pelo objeto em
lucros_desejados sobre 100, mais 1. Por fim, printo o produto, o preço
de compra e o cálculo do lucro de cada objeto dentro das listas.
