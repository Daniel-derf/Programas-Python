from random import randint
num = randint(0,10)
total = 0
jogada = 0

jogada = int(input('Digite um número entre 0 e 10: '))
if 0 < jogada > 10:
    print('Número Inválido!')
else:
    while jogada != num:
        jogada = int(input('Errou! Tente novamente: '))
        total += 1
    print('Acertou! Total de {} tentativas!'.format(total))