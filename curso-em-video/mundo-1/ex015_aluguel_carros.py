dias = int(input('Quantos dias alugados?'))
km = float(input('Quantos km rodados?'))
pagar = (60 * dias) + (0.15 * km)
print('Você precisar pagar R${} pelo aluguel do carro.'.format(pagar))