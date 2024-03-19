#- [ ]  Faça um programa que recebendo um valor inteiro, informe se o número é positivo, negativo ou neutro.

numero = int(input("Digite um número inteiro: "))

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é neutro.")