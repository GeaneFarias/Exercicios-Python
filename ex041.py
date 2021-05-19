from datetime import date
ano = date.today().year
nasc = int(input('Qual seu anos de nascimento ? '))
idade = ano - nasc
if idade <= 9:
    print('Com {} anos você é um nadador MIRIM!!'.format(idade))
elif idade <= 14:
    print('Com {} anos você é um nadador INFANTIL!! '.format(idade))
elif idade <= 19:
    print('Com {} anos você é um nadador JÚNIOR!!'.format(idade))
elif idade <= 25:
    print('Com {} anos você é um nandador SÊNIOR!!'.format(idade))
else:
    idade >= 25
    print('Com {} anos você é um nadador MASTER!!'.format(idade))