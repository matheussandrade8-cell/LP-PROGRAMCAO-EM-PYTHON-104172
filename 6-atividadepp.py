import os
os.system("cls")

nota1=float(input("digite sua nota 1:"))
nota2=float(input("digite sua nota 2:"))

media= (nota1 + nota2) /2

match media:
    case media if media>= 6.0:
        print("aprovado")
    case media if media >= 4.1:
        print("recuperação")
    case _:
        print("reprovado")
