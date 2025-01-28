# Faça um programa para, a partir de um valor informado em centavos, indicar a menor
# quantidade de moedas que representa esse valor

valor = int(input("Digite o valor em centavos: "))

moedas1real = valor // 100
valor = valor % 100
moedas50 = valor // 50
valor = valor % 50
moedas25 = valor // 25
valor = valor % 25
moedas10 = valor // 10
valor = valor % 10
moedas5 = valor // 5
moedas1 = valor % 5

print(f'''{moedas1real} moeda(s) de 1 real
{moedas50} moeda(s) de 50 centavos
{moedas25} moeda(s) de 25 centavos
{moedas10} moeda(s) de 10 centavos
{moedas5} moeda(s) de 5 centavos
{moedas1} moeda(s) de 1 centavo''')

x, y = 5, 10
