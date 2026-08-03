reais = float(input('Quantos reais você possui? R$'))
qtd_dolar = reais / 5.08
print('Se você possui R${:.2f}, você consegue comprar ${:.2f}!'.format(reais, qtd_dolar))