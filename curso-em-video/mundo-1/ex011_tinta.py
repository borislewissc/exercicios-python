largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
qtd_tinta = area / 2
print('Sua parede possui uma área de {}m² e irá precisar de {} litros de tinta.'.format(area, qtd_tinta))