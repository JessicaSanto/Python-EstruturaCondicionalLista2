#- Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

#“Telefonou para a vítima? “
#“Esteve no local do crime?”
#“Mora perto da vítima? “
#“Devia para a vítima? “
#“Já trabalhou com a vítima? “
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como “Suspeita”, entre 3 e 4 como “Cúmplice” e 5 como “Assassino“. Caso contrário, ele será classificado como “Inocente“.

print("Responda às seguintes perguntas com 'sim' ou 'não':")
pergunta1 = input("Telefonou para a vítima? ").lower()
pergunta2 = input("Esteve no local do crime? ").lower()
pergunta3 = input("Mora perto da vítima? ").lower()
pergunta4 = input("Devia para a vítima? ").lower()
pergunta5 = input("Já trabalhou com a vítima? ").lower()

positivas = 0

if pergunta1 == "sim":
    positivas += 1
if pergunta2 == "sim":
    positivas += 1
if pergunta3 == "sim":
    positivas += 1
if pergunta4 == "sim":
    positivas += 1
if pergunta5 == "sim":
    positivas += 1

if positivas == 2:
    print("Suspeita")
elif 3 <= positivas <= 4:
    print("Cúmplice")
elif positivas == 5:
    print("Assassino")
else:
    print("Inocente")