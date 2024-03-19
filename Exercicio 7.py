#Ler duas notas de um aluno, efetuar a média aritmética e, se a média for maior ou igual a 7, informar que o aluno foi aprovado; se a média for maior ou igual a 5 mas menor do que 7, informar que o aluno está de exame; se a média for menor do que 5 informar que o aluno foi reprovado.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print("Aluno aprovado!")
elif media >= 5:
    print("Aluno em exame.")
else:
    print("Aluno reprovado.")