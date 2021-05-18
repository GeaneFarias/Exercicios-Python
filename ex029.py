km = float(input('Velocidade: '))
if km >= 80:
    print('Você foi multado!! ')
    multa = (km- 80)*7
    print('sua multa é de é de R${}'.format(multa))
else:
    print('Boa viagem!!! Dirija com seguraça. ')