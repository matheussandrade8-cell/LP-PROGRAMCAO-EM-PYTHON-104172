import os 
os.system("cls")

#Inicip
nome= input("digite seu nome:")
nota1= float(input("digite sua nota 1: "))
nota2= float(input("digite sua nota 2:"))

#processo
media= (nota1 + nota2)/2

#fim.
if media >=9:
    resultado=print(f"O aluno {nome} foi aprovado nota A")
elif media >= 7.5:
    resultado=print(f"O aluno {nome} foi aprovado nota B")
elif media >= 6:
    resultado=print(f"O aluno {nome} foi aprovado nota C")
elif media >= 4:
    resultado=print(f"O aluno {nome} foi reprovado nota D")
else:
    resultado=print(f"O aluno {nome} foi reprovado nota E")

