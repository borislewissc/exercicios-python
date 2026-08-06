from rich import print

dias = int(input('Quantos dias alugados?'))
km = float(input('Quantos km rodados?'))
pagar = (60 * dias) + (0.15 * km)
print('Você precisar pagar [red]R${}[/red] pelo aluguel do carro.'.format(pagar))