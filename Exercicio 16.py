#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

preco_produto1 = float(input("Digite o preço do primeiro produto: "))
preco_produto2 = float(input("Digite o preço do segundo produto: "))
preco_produto3 = float(input("Digite o preço do terceiro produto: "))

if preco_produto1 <= preco_produto2 and preco_produto1 <= preco_produto3:
    print("Você deve comprar o primeiro produto.")
elif preco_produto2 <= preco_produto1 and preco_produto2 <= preco_produto3:
    print("Você deve comprar o segundo produto.")
else:
    print("Você deve comprar o terceiro produto.")