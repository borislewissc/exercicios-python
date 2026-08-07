# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço normal 
# – 3x ou mais no cartão: 20% de juros

print(('=' * 10), 'LOJAS GUANABARA', ('=' * 10))

preco_normal = float(input('Preço das compras: R$'))
total = 0

print("""FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão""")
forma = int(input('Qual é a opção? '))

if forma == 1:
    total = preco_normal - (preco_normal * 0.10)
elif forma == 2:
    total = preco_normal - (preco_normal * 0.05)
elif forma == 3:
    total = preco_normal
    parcela2x = preco_normal / 2
    print(f'Sua compra será parcelada em 2x de R${parcela2x:.2f}')
elif forma == 4:
    total = preco_normal + (preco_normal * 0.20)
    parcela = int(input('Quantas parcelas? '))
    totparc = total / parcela
    print(f'Sua compra será parcelada em {parcela}x de R${totparc:.2f}')
else:
    print('Opção inválida de pagamento. Tente novamente!')

if total > 0:
    print(f'Sua compra de R${preco_normal:.2f} vai custar R${total:.2f} no final.')


