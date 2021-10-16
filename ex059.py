n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
escolha = 0

while escolha != 5:
    escolha  =  int(input("""
    -------OPÇÕES-------
        [1] Soma
        [2] Multiplicar
        [3] Maior
        [4] Novos Números
        [5] Sair do Programa 
        """))
    if escolha == 1:
        print('A soma dos valores é {}'.format(n1+n2))
    elif escolha == 2:
        print('O produto dos valores é {}'.format(n1*n2))
    elif escolha == 3:
        if n1>n2:
            print('O primeiro número ({}) é maior que o segundo ({})'.format(n1,n2))
        elif n2>n1:
            print('O segundo número ({}) é maior que o primeiro ({})'.format(n2,n1))
        else:
            print('Os números são iguais! (Ambos são {})'.format(n1))
    elif escolha == 4:
        n1 = int(input('Digite o primeiro número novo: '))
        n2 = int(input('Digite o segundo número novo: '))
    else:
        print('Valor Inválido! Digite novamente.')
print('Programa Encerrado!')