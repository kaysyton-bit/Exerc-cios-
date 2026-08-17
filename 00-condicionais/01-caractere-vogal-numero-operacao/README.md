# Caractere: vogal, número ou operação

## Problema

Escrever um programa para ler um único caractere e depois informar se
este é uma vogal, um número ou uma operação matemática (+, -, * ou /).

## Antes

11/10/2025

Aqui solicitei ao programa que pegasse uma entrada e checasse se esta
estava em uma das opções dentro de "AEIOU" ou "aeiou". Um ponto forte do
raciocínio foi prever que o usuário poderia digitar uma vogal em
maiúsculo ou minúsculo, utilizei o mesmo método na checagem de operação
matemática, e a função do Python caractere.isnumeric() foi utilizada
para verificar um número.

## Depois

23/05/2026

Aqui mudei algumas poucas coisas, determinei que o input seria uma
string para facilitar na hora de manipular os dados e resolvi um ponto
cego do código anterior, que era a possibilidade do usuário digitar mais
de um caractere, sendo que a questão determina que seja apenas um,
portanto usei a função len() que conta caracteres dentro da string; caso
fosse diferente de 1, o código não continuaria e seria mostrado na tela
"será aceito apenas um caractere".

Ao invés de fazer uma dupla checagem com "AEIOU" ou "aeiou", utilizei a
função .lower(), que transforma qualquer caractere maiúsculo em
minúsculo.

Outro ponto cego resolvido foi a possibilidade do usuário digitar uma
consoante ou outro caractere que não é operação, como "@", portanto fiz
com que o programa exibisse "ERRO! o caractere não é numero, vogal ou
operação matemática" caso o caractere não fosse nenhuma das categorias
verificadas anteriormente.
