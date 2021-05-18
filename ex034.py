salario = float(input('Qual o salário do funcinario? R$ '))
if salario <= 1250.00:
    aumento = salario + (salario * 15/100)
    print('Seu salario atua é de {} com aumento ficará {}'.format(salario, aumento))
else:
    novo =salario + (salario * 10/100)
    print('SEU SALARIO ATUAL É {} COM O AUMENTO FICARÁ {}'. format(salario, novo))