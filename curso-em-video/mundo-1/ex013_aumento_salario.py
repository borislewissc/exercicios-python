salario_atual = float(input('Digite seu salário: R$'))
salario_novo = salario_atual + (salario_atual * 15 / 100)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento passa a receber R${:.2f}'.format(salario_atual, salario_novo))