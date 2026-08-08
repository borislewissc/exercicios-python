# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número inteiro: '))

if num <= 1:
    eh_primo = False
else:
    eh_primo = True

    for c in range(2, num):
        if num % c == 0:
            eh_primo = False
            break

if eh_primo:
    print('É primo')
else:
    print('Não é primo')