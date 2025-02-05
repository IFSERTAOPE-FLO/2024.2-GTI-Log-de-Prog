'''Um mercado está vendendo produtos com a seguinte tabela de preços:
Total de compras até 10 Kg              Total de compras acima de 10Kg
Carambolas: R$ 5,00 p/Kg                Carambolas: R$ 4,50 p/Kg
Amoras: R$ 3,00 p/Kg                    Amoras: R$ 2,00 p/Kg

Caso o cliente compre mais de 15Kg em frutas ou o valor total da compra ultrapasse R$ 35,00, 
receberá ainda um desconto de 20% sobre esse total. Faça um algoritmo para ler a quantidade 
(em Kg) de carambolas e a quantidade (em Kg) de amoras adquiridas e escreva o valor a ser pago pelo cliente.
'''
carambolas = float(input('Quantidade de carambolas (Kg): '))
amoras = float(input('Quantidade de amoras (Kg): '))

kgs = carambolas + amoras
if kgs <= 10:
    total = (carambolas * 5) + (amoras * 3)
else:
    total = (carambolas * 4.5) + (amoras * 2)
    
if kgs > 15 or total > 35:
    total = total - (total * 0.2)

print(f"O valor a ser pago é R$ {total:.2f}")