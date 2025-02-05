# Faça um algoritmo que leia as coordenadas de um ponto (x,y) num plano cartesiano e 
# exiba uma mensagem informando se o ponto pertence ao eixo X, ao eixo Y, à origem ou 
# a nenhuma dessas opções.

x = int(input("Digite o valor da coordenada x: "))
y = int(input("Digite o valor da coordenada y: "))

if x == 0 and y == 0:
    print("Os pontos estão na origem")
elif x == 0:
    print("O ponto está no eixo X")
elif y == 0:
    print("O ponto está no eixo Y")
else:
    print("nenhuma dessas opções")