# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

reta1 = float(input('Digite o comprimento da primeira reta: '))
reta2 = float(input('Digite o comprimento da segunda reta: '))
reta3 = float(input('Digite o comprimento da terceira reta: '))

cond1 = (reta1 + reta2) > reta3
cond2 = (reta1 + reta3) > reta2
cond3 = (reta2 + reta3) > reta1

if cond1 and cond2 and cond3:
    print('As retas acima podem formar um triângulo.')
    if reta1 == reta2 == reta3:
        print('Especificamente um triângulo EQUILÁTERO')
    elif reta1 != reta2 != reta3:
        print('Especificamente um triângulo ESCALENO')
    else:
        print('Especificamente um triângulo ISÓSCELES')
else:
    print('As retas acima não podem formar um triângulo.')