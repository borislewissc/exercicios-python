from rich import print

numero = int(input('Digite um número:'))
sucessor = numero + 1
antecessor = numero - 1
print(f'O número {numero} possui o sucessor [green]{sucessor}[/green] e o antecessor [red]{antecessor}[/red]')