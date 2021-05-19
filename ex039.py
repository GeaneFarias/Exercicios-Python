from datetime import date
hoje = date.today().year
from time import sleep
ano = int(input('Qual seu ano de nascimento? '))
alist = hoje - ano
print('Você nasceu em {}, e esta com {} anos agora em {}'.format(ano, alist, hoje))
if alist > 18:
    saldo = alist - 18
    print('Seu alistamento esta atrasado em {} anos!!'.format(saldo))
elif alist == 18:
    print('Chegou sua hora...')
    sleep(3)
    print('A HORA DE SE ALISTAR!!!')
else:
    saldo = 18 - alist
    print('Ainda falta {} anos para seu alistamento!!'.format(saldo))
