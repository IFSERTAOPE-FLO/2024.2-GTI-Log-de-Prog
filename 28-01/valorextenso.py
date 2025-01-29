'''§ Faça um programa que leia um número inteiro entre 0 e 9999 e escreva o seu valor por extenso
Exemplo: 6574
Unidade:  4 Dezena:  7 Centena:  5 Milhar:  6
'''

numero = int(input('Digite um número inteiro entre 0 e 9999: '))
if numero < 0 or numero > 9999:
    print('Número inválido')
else:
    n1 = numero % 10
    n2 = numero // 10 % 10
    n3 = numero // 100 % 10
    n4 = numero // 1000 % 10
    print(f'''
          Unidade: {n1}
          Dezena: {n2}
          Centena: {n3}
          Milhar: {n4}
          ''')