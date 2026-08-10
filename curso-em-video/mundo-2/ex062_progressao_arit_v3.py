# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

termo_atual = primeiro_termo
posicao_atual = 1

total_termos_mostrados = 0
qtd_termos_lote = 10

while qtd_termos_lote != 0:
    total_termos_mostrados += qtd_termos_lote 
    
    while posicao_atual <= total_termos_mostrados: 
        print(f'{termo_atual} → ', end='')
        termo_atual += razao
        posicao_atual += 1
        
    print('PAUSA')
    qtd_termos_lote = int(input('Quantos termos você quer mostrar a mais? '))

print(f'Progressão finalizada com {total_termos_mostrados} termos mostrados.')