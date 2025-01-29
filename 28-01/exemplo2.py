''' Programa para somar dois números, se o usuário desejar:
'''

op = input("Deseja somar? (S/N)")
if (op == "S"):
    x = float(input('Digite o primeiro numero:'))
    y = float(input('Digite o segundo numero:'))
    resultado = x + y
    print('O resultado da soma é', resultado)
print('Até a próxima!')
