km = float(input('Quantos quilometros de viagem serão? '))
if km <= 200:
    valor = km * 0.50
    print('O VALOR DA SUA VIAJEM FICA EM {} R$'.format(valor))
else:
    valor1 = km * 0.45
    print('O VALOR DA SUA VIGEM É {} R$'. format(valor1))