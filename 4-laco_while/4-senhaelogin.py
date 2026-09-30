
import os
os.system("cls")
import time
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
        time.sleep(1.5)
        os.system("cls")


