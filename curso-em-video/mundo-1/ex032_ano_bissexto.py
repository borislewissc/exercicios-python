# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date

ano = int(input('Qual ano você quer analisar? Digite 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
div4 = ano % 4 == 0
div100 = ano % 100 != 0
div400 = ano % 400 == 0
if (div4 and div100) or div400:
    print(f'O ano de {ano} é bissexto')
else:
    print(f'O ano de {ano} não é bissexto')