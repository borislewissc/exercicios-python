# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

maioridade = 0
menoridade = 0
atual = date.today().year


for c in range(1,8):
    nasc = int(input(f'Qual o ano de nascimento da {c}ª pessoa? '))
    idade = atual - nasc
    if idade >= 21:
        maioridade += 1
    else:
        menoridade +=1
print(f'Tem {maioridade} maiores de idade e {menoridade} menores de idade')