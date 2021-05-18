from random import choice
aluno1 = str(input('Nome do aluno: '))
alu2 = str(input('Nome do aluno: '))
alu3 = str(input('Nome do aluno: '))
alu4 = str(input('Nome do aluno: '))
lista = [ aluno1, alu2, alu3,alu4]
sort = choice(lista)
print('O aluno sorteado é {}'.format(sort))
