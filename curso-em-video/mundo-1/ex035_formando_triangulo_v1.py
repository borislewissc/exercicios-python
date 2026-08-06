# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

from rich import print

reta1 = float(input('Digite o comprimento da primeira reta: '))
reta2 = float(input('Digite o comprimento da segunda reta: '))
reta3 = float(input('Digite o comprimento da terceira reta: '))

cond1 = (reta1 + reta2) > reta3
cond2 = (reta1 + reta3) > reta2
cond3 = (reta2 + reta3) > reta1

if cond1 and cond2 and cond3:
    print('[green]As retas acima podem formar um triângulo.[/green]')
else:
    print('[red]As retas acima não podem formar um triângulo.[/red]')