from datetime import date
hoje = date.today().year
from time import sleep
ano = int(input('Qual seu ano de nascimento? '))
alistamento = ano - 2003
if alistamento <= -1:
    print('Seu alistamento esta atrasado em {} anos!!'.format(alistamento))
elif alistamento == 0:
    print('Chegou sua hora...')
    sleep(3)
    print('HORA DE SE ALISTAR!!!')
else:
    print('Ainda falta {} anos para seu alistamento!!'.format(alistamento))
