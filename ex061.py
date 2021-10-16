primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
num = 0
while num <= decimo:
    num += (primeiro + razao)
    print(' {} '.format(num),end='-> ')