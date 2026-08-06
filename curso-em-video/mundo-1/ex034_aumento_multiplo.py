# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

from rich import print

salario = float(input('Digite o seu salário: '))
if salario <= 1250.00:
    aumento = salario * 0.15
else:
    aumento = salario * 0.10
print(f'Você ganha [red]R${salario:.2f}[/red], mas você receberá um aumento de [yellow]R${aumento:.2f}[/yellow] e seu novo salário será [green]R${salario + aumento:.2f}[/green]')