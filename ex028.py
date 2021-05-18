import random
from time import sleep
num = int(input('ESTOU PENSANDO EM UM NUMERO DE 0 a 5 ADIVINHE QUAL É : '))
adv = [0, 1, 2, 3, 4, 5]
nume = random.choice(adv)
print('loadind...')
sleep(3)
if num == nume:
    print('PARABÉNS! você conseguiu me vencer!!')
else:
    print('GANHEI!! O numero que eu estou pensando é {} e não {}'.format(nume, num))

