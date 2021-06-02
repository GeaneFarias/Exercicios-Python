import time
from random import randint

comp = ('PEDRA', 'PAPEL', 'TESOURA')
jogo = randint(0, 2)

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogada = int(input('Qual é a sua jogada? '))

print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('POOH!!')

print('-='*20)
print('O computador escolheu {}'.format(comp[jogo]))
print('O jogador escolheu {}'.format(comp[jogada]))
print('-='*20)

if jogo == 0:
    if jogada == 0:
        print('EMPATE!!')
    elif jogada == 1:
        print('Jogador GANHOU!!!')
    elif jogada == 2:
        print('Computador GANHOU!!')
    else:
        print('Operação invalida')

if jogo == 1:
    if jogada == 0:
        print('Computador GANHOU!!')
    elif jogada == 1:
        print('EMPATE!!')
    elif jogada == 2:
        print('Jogador GANHOU!!')
    else:
        print('operação invalida')

if jogo == 2:
    if jogada == 0:
        print('Jogador GANHOU!!')
    elif jogada == 1:
        print('Computador GANHOU!!')
    elif jogada == 2:
        print('EMPATE!!')
    else:
        print('operação invalida')
else:
    print('operação invalida')


