maior = 0
menor = 0
for i in range(0,5):
    peso = float(input('Digite o peso da {} pessoa: '.format(i+1)))
    if i == 0:
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O maior peso digitado foi {}\nO menor peso digitado foi {}'.format(maior,menor))