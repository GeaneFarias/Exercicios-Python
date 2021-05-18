dias = float(input('Quantos dias permaneceu com o carro? '))
km = float(input('Km rodados? '))
d = 60 * dias
k = 0.15 * km
print('O carro foi alugado por {} dias e rodou {}km \nvalor das diarias : R${}\nvalor dos km rodados R${} \ntotal a pagar R${}'.format(dias, km, d, k, d+k))