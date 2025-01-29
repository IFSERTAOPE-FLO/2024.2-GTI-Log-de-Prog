'''Faça um programa que calcule o IMC de uma pessoa (IMC = massa em kg / altura em metros elevado ao
quadrado) e informe a sua classificação segundo a tabela a seguir, obtida na Wikipédia
'''

kg = float(input('Digite o peso em kg: '))
m = float(input('Digite a altura em metros: '))

imc = kg / (m ** 2)

if imc < 18.5:
    print('Abaixo do peso')
elif imc <= 24.9:
    print('Peso normal')
elif imc <= 29.9:
    print('Peso em excesso')
elif imc <= 34.9:
    print('Obesidade grau I')
elif imc <= 39.9:
    print('Obesidade grau II (severa)')
else:
    print('Obesidade grau III (mórbida)')
