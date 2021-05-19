nota1 = float(input('Digite a primera  nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 7:
    print('Sua nota final foi {} PARABENS VOCÊ ESTA APROVADO  '.format(media))
elif media >= 5 and media < 7:
    print('Sua nota final foi {} você esta de recuperação!!'.format(media))
elif media < 5:
    print('Infelizmente você esta reprovado!! sua media final foi {}.'.format(media))