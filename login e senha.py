import os 
os.system("cls")
#i
usuario=str(input("digite seu login:"))
senha=(input("digite sua senha:"))
#P
if usuario=="matheus" and senha=="008":
    mostre= ("bem vindo matheus")
else:
    mostre=("usuario ou senha invalida")
print(mostre)
