#Faça um programa que pergunte ao usuário se ele quer passar uma temperatura de Fahrenheit para Celsius ou de Celsius para Fahrenheit, e que, a partir da resposta do usuário, faça a devida conversão.

opcao = input("Deseja converter a temperatura de Fahrenheit para Celsius (digite 'FC') ou de Celsius para Fahrenheit (digite 'CF')? ")

if opcao == 'FC':
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"A temperatura em Celsius é: {celsius:.2f} °C")
elif opcao == 'CF':
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f} °F")
else:
    print("Opção inválida. Por favor, digite 'FC' ou 'CF'.")