'''Um usuário deseja criar um algoritmo onde possa escolher que tipo de média deseja calcular a 
partir de três notas. Faça um algoritmo que leia as notas, a opção escolhida pelo usuário e calcule a média. 
Assuma as seguintes entradas válidas para o tipo de média:

[1] - Média aritmética
[2] – Média ponderada (com pesos 3, 3 e 4, respectivamente)
'''

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
opcao = int(input("Digite a opção desejada: [1] - Média aritmética [2] – Média ponderada: "))

if opcao == 1:
    media = (nota1 + nota2 + nota3) / 3
elif opcao == 2:
    media = ((nota1 * 3) + (nota2 * 3) + (nota3 * 4)) / 10
else:
    print("Opção inválida")
    
print(f"A média é {media:.2f}")