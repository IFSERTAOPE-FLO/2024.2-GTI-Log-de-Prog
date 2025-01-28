# Faça um programa que informe a distância em quilômetros de um raio para o observador
# – O observador deve informar o tempo (em segundos) transcorrido entre ver o raio e ouvir o trovão
# – Assuma que a velocidade do som é 340 m/s

tempo = int(input("Digite o tempo (em segundos) entre ver o raio e ouvir o trovão: "))
distancia = tempo * 340 / 1000

print(f"A distância do raio é {distancia:.2f} km")