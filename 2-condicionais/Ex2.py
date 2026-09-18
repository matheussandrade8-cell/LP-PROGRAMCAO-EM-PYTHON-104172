import os
os.system("cls")

#Inicio.
nota1 =float(input("nota 1: "))
nota2 =float(input("nota 2: "))
nota3 =float(input("nota 3: "))

#Processo.
media = (nota1 + nota2 + nota3) /3

if media > 7:
    Resultado = "aluno aprovado"
else:
    Resultado = "aluno reprovado"
#fim.
print(F"media: {media}")
print(f"Resultado: {Resultado:.2f}")