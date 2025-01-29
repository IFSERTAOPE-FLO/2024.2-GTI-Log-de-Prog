'''§ Faça um programa que leia um número inteiro de 5 dígitos e indique se ele é palíndromo
Um número palíndromo é aquele que se lido da esquerda para a direita ou da direita para a esquerda
possui o mesmo valor (ex.: 15451)
'''

numero = int(input('Digite um número inteiro de 5 dígitos: '))
if numero < 10000 or numero > 99999:
    print('Número inválido')
else:
    n1 = numero % 10
    n2 = numero // 10 % 10
    n3 = numero // 100 % 10
    n4 = numero // 1000 % 10
    n5 = numero // 10000 % 10
    if n1 == n5 and n2 == n4:
        print('É palíndromo')
    else:
        print('Não é palíndromo')