nome = str(input('Qual seu nome completo? ')).strip()
print('Nome maiúsculo {}'.format([nome.upper()]))
print('Nome minúsculo {}'.format([nome.lower()]))
print('Seu nome completo tem {} letras '.format(len(nome) - nome.count(' ')))##Para eliminar os espaços exedentes
##print('Seu primeiro nome tem {} lestras'.format(nome.find(' ')))##uma forma de fazer a contagem de letras do priemiro nome
separa = nome.split()
print('Seu primero nome tem {} letras'.format(len(separa[0]))) ##outra mod de fazer a contagem do primero nome 