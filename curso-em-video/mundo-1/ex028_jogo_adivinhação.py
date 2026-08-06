# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
num = randint(0, 5)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
guess = int(input('Em que número eu pensei?'))
if guess == num:
    print('Parabéns, você acertou!')
else:
    print(f'Você errou, o número era {num}.')