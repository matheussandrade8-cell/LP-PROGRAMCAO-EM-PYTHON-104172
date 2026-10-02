import os
os.system("cls")


while True:
    nota=float(input("digite a nota entre 0 e 10:"))
    if nota< 0 or nota > 10:
        print("nota invalida")
        print("tente novamente \n")
    else:
        print(f"nota {nota}")
        break
