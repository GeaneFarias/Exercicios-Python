l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
area = l * a
print('Altura de {} mais largura de {} da {}'.format(a, l, area))
tinta = area / 2
print('Para pintar a área de {} metros quadrados é nescessario {}l de tinta '.format(area, tinta))