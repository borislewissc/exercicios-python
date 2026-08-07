# Crie um programa que faça o computador jogar Jokenpô com você.

from random import choice

print(('=' * 10), 'JOKENPÔ', ('=' * 10))
opcoes = ['PEDRA', 'PAPEL', 'TESOURA']
computador = choice(opcoes)
print('O computador já escolheu sua jogado, decida a sua.')
jogador = input('PEDRA, PAPEL ou TESOURA? ').upper().strip()

if jogador not in opcoes:
    print(f'Opção inválida! "{jogador}" não faz parte do Jokenpô.')
else:
    print(f'O computador escolheu {computador} e você escolheu {jogador}.')
    if computador == 'PEDRA' and jogador == 'TESOURA':
        print('Você perdeu!')
    elif computador == 'PAPEL' and jogador == 'PEDRA':
        print('Você perdeu!')
    elif computador == 'TESOURA' and jogador == 'PAPEL':
        print('Você perdeu!')
    elif computador == jogador:
        print('Empate! Jogue novamente.')
    else:
        print('Você ganhou!')