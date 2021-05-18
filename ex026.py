name = str(input('Digite seu nome: ')).strip().upper()
letra = name.count('A')
print('A letra A aparece {} vezes'.format(letra))
print('A primeira letra A aparece na posição {} '.format(name.find('A')+1))
print('A ultima letra A apareceu na posição {}'.format(name.rfind('A'))) ## usar.rfind para começar a contagem do ultimo para o primeiro