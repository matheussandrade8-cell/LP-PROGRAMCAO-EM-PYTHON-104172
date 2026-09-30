
import os
os.system("cls")
usuario="M"
s=1
while True:
    login=input("digite seu login:")
    senha=input("digite sua senha:")

    if login=="M" and senha=="1":
        print("senha correta")
        break
    else:
        print("senha ou login incorreta, tente novamente")
        input("pressione a tecla para cutinuar")
        os.system("cls")


