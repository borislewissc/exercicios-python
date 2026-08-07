# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o seu salário: R$'))
anos = int(input('Digite em quantos anos você irá pagar: '))

prestacao = valor_casa / (anos * 12)
minimo = salario * 0.30

print(f'Para pagar uma casa de R${valor_casa:.2f} em {anos} anos, a prestação será de R${prestacao:.2f}.')

if prestacao <= minimo:
    print('EMPRÉSTIMO CONCEDIDO')
else:
    print('EMPRÉSTIMO NEGADO')