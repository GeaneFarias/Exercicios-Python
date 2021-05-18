import random
aluno1 = str(input('Nome do aluno: '))
alu2 = str(input('Nome do aluno: '))
alu3 = str(input('Nome do aluno: '))
alu4 = str(input('Nome do aluno: '))
lista = [ aluno1, alu2, alu3,alu4]
random.shuffle(lista)
print('A ordem de apresentação será...')
print(lista)

