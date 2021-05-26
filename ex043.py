#43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
import math

peso = float(input('Qual seu peso? (kg) '))
altu = float(input('Qual sua altura? (m) '))
imc = peso / (math.pow(altu, 2))

print('O IMC dessa pessoa é de {:.2f}'.format(imc))
if imc < 18.5:
    print('Você esta ABAIXO DO PESO! ')
elif imc >= 18.5 and imc <= 25:
    print('Você esta com o peso IDEAL!')
elif imc >= 25 and imc <= 30:
    print('Você esta com SOBRE PESO')
elif imc >= 30 and imc <= 40:
    print('Você esta com OBSIDADE!')
else:
    print('Você esta com OBSIDADE MÓRBIDA')