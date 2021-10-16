nome = [0,1,2,3]
idade = [0,1,2,3]
sexo = [0,1,2,3]

homemIdade = 0
totalIdade = 0
mediaIdade = 0
homemNome = str()
muie = 0

for i in range(0,4):

    nome[i] = str(input('Digite o nome da {} pessoa: '.format(i+1)))
    idade[i] = int(input('Digite a idade da {} pessoa: '.format(i+1)))
    sexo[i] = str(input('Digite o sexo (M ou F) da {} pessoa: '.format(i+1))).lower()

    totalIdade += idade[i]

    if sexo[i] == 'f':
        if idade[i] < 20:
            muie+=1


    if sexo[i] == 'm':
        if idade[i] > homemIdade:
            homemIdade = idade[i]
            homemNome = nome[i]


mediaIdade = totalIdade/4
print('\nA média de idades do grupo é {}'.format(mediaIdade))
print('O homem mais velho do grupo tem {} anos e se chama {}'.format(homemIdade,homemNome))
print('{} mulher(es) do grupo tem menos de 20 anos'.format(muie))




#Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, # mostre: a média de idade do grupo, qual é o nome do homem mais
# velho e quantas mulheres têm menos de 20 anos.