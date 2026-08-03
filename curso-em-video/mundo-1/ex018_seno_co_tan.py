# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import cos, radians, sin, tan

angulo = float(input('Digite o ângulo: '))
rad = radians(angulo)
seno = sin(rad)
cosseno = cos(rad)
tangente = tan(rad)
print('O ângulo de {} tem:\nO valor do seno {:.2f}\nO valor do cosseno {:.2f}\nO valor da tangente {:.2f}.'.format(angulo, seno, cosseno, tangente))