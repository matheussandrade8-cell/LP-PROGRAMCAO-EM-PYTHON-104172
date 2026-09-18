import os
os.system("cls")

#Inicio.
nota1 =float(input("nota 1: "))
nota2 =float(input("nota 2: "))
nota3 =float(input("nota 3: "))

#Processo.
media = (nota1 + nota2 + nota3) /3

if media > 7:
    print("aluno aprovado")
else:
    print("aluno reprovado")
#fim.
print(F"media: {media}")
