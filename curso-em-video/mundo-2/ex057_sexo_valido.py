# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Digite o seu sexo (M/F): ')).strip().upper()

while sexo not in ['M', 'F']: # Usar lista ao invés de 'MF' para evitar que valide o input MF.
    sexo = str(input('Dados Inválidos. Digite o seu sexo (M/F): ')).strip().upper()
print(f'Sexo {sexo} registrado com sucesso!')