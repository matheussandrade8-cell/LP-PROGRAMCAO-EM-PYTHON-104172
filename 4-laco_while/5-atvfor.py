import os
os.system("cls")
import time
usuario="ze"
senhac=123
tente=0
for i in range(3):
    print(f"tentativas {i+1}")
    login=input("digite o seu login:")
    senha=input("digite sua senha:")
    if login=="ze" and senha=="123":
        print("login concluido")
        break
    else:
        print("tente novamente!")
        time.sleep(0.5)
        os.system("cls")