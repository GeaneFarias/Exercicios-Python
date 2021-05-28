#44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
compra = float(input('Valor da compra? '))
print('FORMAS DE PAGAMENTO \n [ 1 ] Á vista dinheiro/cheque \n [ 2 ] Á vista no cartão \n [ 3 ] 2x no cartão \n [ 4 ] 3x ou mais no cartão')
opçao = int(input("Qual a opção? "))

if opçao == 1:
    print('Sua compra está com o valor de {}R$ '.format(compra))
    des = compra - (compra * 10/100)
    print('Pórem com o pagamento à vista no dinheiro/cheque fica R${} '.format(des))
elif opçao == 2:
    print('Pórem com pagamento a vista no cartão o valor fica R${}'.format(compra - (compra * 5/100)))
elif opçao == 3:
    print('Sua compra está com o valor de R${} '.format(compra))
    print('E será parcelada em 2X de R${} SEM JUROS  '. format(compra / 2))
elif opçao == 4:
    parce = int(input('Quantas parcelas? '))
    juros = compra + (compra * 20/100)
    print('Sua compra será parcelada em {}X de R${} \nSua compra de R${} vai custar R${} no final.'.format(parce, juros / parce, compra, juros))
else:
    print('OPÇÃO DE PAGAMENTO INVALIDA')


