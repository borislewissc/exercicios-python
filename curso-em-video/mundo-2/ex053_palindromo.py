# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
# APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = input('Digite a frase: ').strip().upper().replace(' ', '')
frase_invertida = frase[::-1]

print(f'O inverso de {frase} é {frase_invertida}')

if frase_invertida == frase:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo.')

# Totalmente diferente da solução do Guanabara, sem 'for'.