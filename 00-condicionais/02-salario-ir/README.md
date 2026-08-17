# Cálculo de salário e Imposto de Renda

## Problema

Fazer um programa que leia o valor da diária de um funcionário, a
quantidade de dias que este trabalhou no mês, e exiba o salário bruto,
o Imposto de Renda (IR) a ser pago e o salário líquido. O cálculo do IR
deve considerar os seguintes percentuais: salário até R$ 2.000,00 é
isento de IR; salário entre R$ 2.000,00 e R$ 5.000,00 paga 15% de IR;
salário superior a R$ 5.000,00 paga 27,5% de IR.

## Antes

15/10/2025

Primeira versão, resolvida inteiramente com condicionais em sequência,
calculando os dois valores possíveis de IR antecipadamente (ir1 e ir2)
mesmo que só um deles fosse usado em cada execução.

## Depois

24/05/2026

Separei o cálculo em duas funções: calcular_ir(), que decide o
percentual de acordo com a faixa salarial, e calcular_salario(), que usa
esse percentual para calcular bruto, IR e líquido de uma vez, retornando
os quatro valores. Isso evitou calcular os dois IRs possíveis sem
necessidade, como acontecia na primeira versão.
