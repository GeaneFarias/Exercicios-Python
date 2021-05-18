from math import hypot
cate = float(input('comprimento do cateto oposto: '))
opos = float(input('comprimento do cateto adjacente: '))
'''ipo = (cate ** 2 + opos ** 2)**(1/2)'''
hypo = hypot(cate, opos)
print('a ipotenusa vai medir {:.2f}'.format(hypo))