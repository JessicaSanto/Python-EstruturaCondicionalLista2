# Faça um programa que pergunte a temperatura atual para o usuário e mostre uma mensagem na tela dizendo se está “quente”, “frio” ou “agradável”.

temperatura = float(input("Digite a temperatura atual em Celsius: "))

if temperatura > 30:
    print("Está quente.")
elif temperatura < 15:
    print("Está frio.")
else:
    print("Está agradável.")