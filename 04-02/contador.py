num_inicial = int(input("Digite um número: "))
num_final = int(input("Digite outro número: "))
contador_pares = 0
while num_inicial <= num_final:
    if num_inicial % 2 == 0:
        contador_pares = contador_pares + 1
    num_inicial = num_inicial + 1
print(contador_pares)

