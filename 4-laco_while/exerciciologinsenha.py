import os
import time
os.system("cls")

print("centro de cadastro")
print("selecione a opção")
print("1- cadastra-se")
print("2-login")


print("ㅤㅤㅤCadastroㅤㅤㅤ")
ccadastro=input("digite seu cadastro:")
csenha=input("digite sua senha:")
print("ㅤcadastro concluido")
time.sleep(1)
os.system("cls")

for i in range(3):
    while True:
        login=input("digite seu login:")
        senha=input("digite sua senha:")
        time.sleep(1.5)
        
        os.system("cls")
        
        if login==ccadastro and csenha==senha:
            print(f"bem vindo {login}!")
            break
        else:
            ("login ou senha invalida")
            break