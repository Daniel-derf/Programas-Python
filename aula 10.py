n1 = float(input("Digite a n1: "))
n2 = float(input("Digite a n2: "))
media = (n1+n2)/2
print('A média de notas é {:1}'.format(media))
if media >= 6:
    print('Passou de ano!')
else:
    print('Repetiu!')