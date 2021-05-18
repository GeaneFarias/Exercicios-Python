num  = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opçao = int(input('Sua opção: '))
if opçao == 1:
    print('{} convertido para BINARIO é igual a {}'.format(num, bin(num)[2 :]))
elif opçao == 2:
    print('{} Convertido para OCTAL é igual a {}'.format(num, oct(num)))
elif opçao == 3:
    print('{} Convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)))
else:
    print('Opção invalida!! Tente novamente