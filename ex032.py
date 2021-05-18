ano = int(input('Ano para analisar: '))
if ano % 4 == 0:
    print("O ano de {} é BISSEXTO".format(ano))
else:
    print('O ano de {} não é BISSEXTO'. format(ano))