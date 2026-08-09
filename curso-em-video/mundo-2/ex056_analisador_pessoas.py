# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

# Nota de evolução/melhoria:
# A versão original do exercício assume que sempre haverá ao menos um homem
# no grupo. Esta versão inclui tratamentos de borda (como o caso de 
# não haver homens no grupo ou idades zeradas).

soma_idade = 0 
maioridade_homem = 0
nome_velho = ''
tot_homens = 0
mulher20 = 0

for p in range(1, 5):
    print(('-' * 10), f'{p}ª PESSOA', ('-' * 10))
    nome = input('Digite o nome: ').strip()
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo: ').strip()

    soma_idade += idade

    if sexo in 'Mm':
        tot_homens += 1
        if tot_homens == 1 or idade > maioridade_homem:
            maioridade_homem = idade
            nome_velho = nome

    if sexo in 'Ff' and idade < 20:
        mulher20 += 1

media_idade = soma_idade / 4
print(f'A média de idade do grupo é de {media_idade:.1f} anos.')

if tot_homens > 0:
    print(f'O homem mais velho tem {maioridade_homem} anos e se chama {nome_velho}.')
else:
    print('Não foi cadastrado nenhum homem no grupo.')

print(f'Ao todo são {mulher20} mulheres com menos de 20 anos.')