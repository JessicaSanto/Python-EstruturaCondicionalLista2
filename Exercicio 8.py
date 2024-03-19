#Desenvolva um programa que recebe do usuário o placar de um jogo de futebol (os gols de cada time) e informe se o resultado foi um empate, se a vitória foi do primeiro time ou do segundo time.

# Recebe os gols de cada time do usuário
gols_time1 = int(input("Digite a quantidade de gols do primeiro time: "))
gols_time2 = int(input("Digite a quantidade de gols do segundo time: "))

# Verifica o resultado do jogo
if gols_time1 == gols_time2:
    print("O resultado foi um empate.")
elif gols_time1 > gols_time2:
    print("O primeiro time venceu.")
else:
    print("O segundo time venceu.")