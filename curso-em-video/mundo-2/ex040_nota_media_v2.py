# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2

print(f'Com as notas {nota1:.1f} e {nota2:.1f}, a média do aluno é {media:.1f}')

if media >= 7:
    print('APROVADO')
elif 7 > media >= 5:
    print('RECUPERAÇÃO')
else:
    print('REPROVADO')