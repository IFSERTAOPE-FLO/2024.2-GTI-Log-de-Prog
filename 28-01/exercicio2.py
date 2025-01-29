'''Faça um programa que leia três coordenadas num espaço 2D e indique se formam um
triângulo, juntamente com o seu tipo (equilátero, isósceles e escaleno)
– Equilátero: todos os lados iguais
– Isósceles: dois lados iguais
– Escaleno: todos os lados diferentes
'''

x1 = float(input('Digite a coordenada x1: '))
x2 = float(input('Digite a coordenada x2: '))
x3 = float(input('Digite a coordenada x3: '))

if x1 == x2 and x2 == x3:
    print('Equilátero')
elif x1 == x2 or x2 == x3 or x1 == x3:
    print('Isósceles')
else:
    print('Escaleno')