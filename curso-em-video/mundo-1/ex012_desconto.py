from rich import print

preco_base = float(input('Digite o preço do produto: '))
preco_final = preco_base - (preco_base * 5 / 100)
print('O produto que custava [red]R${}[/red], na promoção com desconto de 5% vai custar [green]R${}[/green]!'.format(preco_base, preco_final))