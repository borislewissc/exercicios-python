# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    print("""[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa""")
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        print(f'{num1} + {num2} = {num1 + num2}')
    elif opcao == 2:
        print(f'{num1} * {num2} = {num1 * num2}')
    elif opcao == 3:
        if num1 > num2:
            print(f'{num1} > {num2}')
        elif num2 > num1:
            print(f'{num2} > {num1}')
        else:
            print(f'{num1} = {num2}')
    elif opcao == 4:
        print('Informe os números novamente:')
        num1 = int(input('Digite o primeiro valor: '))
        num2 = int(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    print('=' * 10)
print('Fim do programa! Volte sempre!')