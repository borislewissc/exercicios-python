from rich import print

salario_atual = float(input('Digite seu salário: R$'))
salario_novo = salario_atual + (salario_atual * 15 / 100)
print('Um funcionário que ganhava [red]R${:.2f}[/red], com 15% de aumento passa a receber [green]R${:.2f}[/green]'.format(salario_atual, salario_novo))