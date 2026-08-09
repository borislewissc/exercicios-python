# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

num = randint(0, 10)
print(f'Vou pensar em um número entre 0 e 10. Tente adivinhar...')
guess = int(input('Em que número eu pensei? '))
tentativas = 1

while guess != num:
    if guess > num:
        print('Menos... Tente mais uma vez.')
    else:
        print('Mais... Tente mais uma vez.')
    guess = int(input('Em que número eu pensei? '))
    tentativas += 1
print(f'Você acertou após {tentativas} tentativas! O número era {num}.')

# while guess > num:
    # print('Menos... Tente mais uma vez.')
    # guess = int(input('Em que número eu pensei? '))
    # tentativas += 1
# while guess < num:
    # print('Mais... Tente mais uma vez.')
    # guess = int(input('Em que número eu pensei? '))
    # tentativas += 1
# if guess == num: 
    # print(f'Você acertou após {tentativas} tentativas! O número era {num}')