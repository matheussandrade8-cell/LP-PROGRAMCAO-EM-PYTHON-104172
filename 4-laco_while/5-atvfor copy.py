import os
os.system("cls")

t=0

while True:
    login=input("digite o seu login:")
    senha=input("digite sua senha:")
    if login=="ze" and senha=="123":
        print("login concluido")
        break
    else:
        t +=1
        print("tente novamente!")
        input("pressione a tecla para cutinuar")
        os.system("cls")

        if t >=3:
            print("voce atingiu o maximo de tentativa")
            os.system("cls")
