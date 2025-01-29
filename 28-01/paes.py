'''Uma padaria vende uma certa quantidade de pães franceses e uma quantidade de broas a cada dia.
Cada pãozinho custa R$ 0,12 e a broa custa R$ 1,50. Ao final do dia o dono quer saber quanto arrecadou 
com a venda dos pães e broas (juntos), e quanto deve guardar numa poupança (10% do total arrecadado). 
Você foi contratado para fazer os cálculos para o dono.
Com base nesses fatos, faça um algoritmo para ler as quantidades de pães e broas, e depois calcular 
os dados solicitados.
'''

qtd_pao = int(input('Digite a quantidade de pães vendidos: '))
qtd_broa = int(input('Digite a quantidade de broas vendidas: '))

total = (qtd_pao * 0.12) + (qtd_broa * 1.5)
poupanca = total * (10/100)

print(f"Você vendeu o total de R$ {total:.2f}.")
print(f"Você deve guardar R$ {poupanca:.2f}.")