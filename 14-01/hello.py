# Faça um programa que leia o nome, a idade, a
# altura, o peso e a nacionalidade do usuário e
# escreva essas informações na forma de um
# parágrafo de apresentação

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
nacionalidade = input("Digite sua nacionalidade: ")

print("Olá, meu nome é", nome, "e tenho", idade, "anos. Tenho", altura, "m de altura e peso", peso, "kg. Sou", nacionalidade, ".")
print(f"Olá, meu nome é {nome} e tenho {idade} anos. Tenho {altura} m de altura e peso {peso} kg. Sou {nacionalidade}.")
print("Olá, meu nome é {} e tenho {} anos. Tenho {} m de altura e peso {} kg. Sou {}.".format(nome, idade, altura, peso, nacionalidade))