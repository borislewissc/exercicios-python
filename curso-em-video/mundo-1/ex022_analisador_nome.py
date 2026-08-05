# Crie um proograma que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maisúculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

nome_completo = str(input('Digite seu nome completo: '))
print(f'Seu nome em maiúscula é {(nome_completo.upper())}')
print(f'Seu nome em minúscula é {(nome_completo.lower())}')
print(f'Seu nome completo possui {(len(nome_completo.replace(' ', '')))} letras')
nome_separado = nome_completo.split()
print(f'Seu primeiro nome é {(nome_separado[0])} e possui {len(nome_separado[0])} letras')