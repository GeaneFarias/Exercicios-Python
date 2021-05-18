valor = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
ano = int(input('Quantos anos de financiamento? '))
parcela = valor / (ano * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos as parcelas vão ficar em R${:.2f}'. format(valor, ano, parcela))
if parcela > minimo:
    print('Seu financiamento foi NEGADO !!')
elif parcela <= minimo:
    print('Seu financiamento foi APROVADO parabens!!!')
