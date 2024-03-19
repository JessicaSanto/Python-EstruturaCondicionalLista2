#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = input("Em que turno você estuda? Digite M para matutino, V para vespertino ou N para noturno: ")

if turno.upper() == 'M':
    print("Bom Dia!")
elif turno.upper() == 'V':
    print("Boa Tarde!")
elif turno.upper() == 'N':
    print("Boa Noite!")
else:
    print("Valor Inválido!")