'''Exemplo: Programa para informar o
número de dias de um mês qualquer
'''

mes = int(input('Entre com um mês (1 a 12): '))

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    print('O mês tem 31 dias')
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    print('O mês tem 30 dias')
elif mes == 2:
    ano = int(input('Entre com um ano(4 dígitos): '))
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print('O mês tem 29 dias')
    else:
        print('O mês tem 28 dias')
else:
    print('Mês inválido')