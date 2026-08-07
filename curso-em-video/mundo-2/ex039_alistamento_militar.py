# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

atual = date.today().year
nasc = int(input('Digite seu ano de nascimento: '))
idade = atual - nasc

if idade == 18:
    print('Você deve se alistar IMEDIATAMENTE!')
elif idade > 18:
    passou = idade - 18
    ano_alistamento = atual - passou
    print(f"""Você deveria ter se alistado há {passou} anos.
Seu alistamento foi em {ano_alistamento}""")
else:
    faltam = 18 - idade
    ano_alistamento = atual + faltam
    print(f"""Ainda faltam {faltam} anos para o alistamento.
Seu alistamento será em {ano_alistamento}""")