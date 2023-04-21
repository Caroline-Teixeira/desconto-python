#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

p = float(input('Digite o preço do produto para aplicar o desconto de 5%: R$ '))
porcentagem = (p * 5)/100
d = p - porcentagem

print("Você vai pagar R$ {:.2f}".format(d))

