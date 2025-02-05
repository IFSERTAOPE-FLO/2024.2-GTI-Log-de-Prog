import random

num = int(input("Digite um número entre 1 e 10: "))
soma = num_aleatorio = random.randint(1, 10)
print(f"O número sorteado foi {num_aleatorio}")
while num != num_aleatorio:
    num_aleatorio = random.randint(1, 5)
    soma = soma + num_aleatorio
    print(f"O número sorteado foi {num_aleatorio}")

print(f"A soma dos números é {soma}")