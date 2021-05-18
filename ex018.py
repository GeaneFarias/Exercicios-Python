from math import radians, sin, cos, tan
angulo = float(input('digite o angulo: '))
seno = sin(radians(angulo))
cosse = cos(radians(angulo))
tang = tan(radians(angulo))
print('O ângulo de {} tem o seno de {:.2f}'.format(angulo, seno))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(angulo, cosse))
print('O ângulo de {} tem a Tangente de {:.2f}'.format(angulo, tang))