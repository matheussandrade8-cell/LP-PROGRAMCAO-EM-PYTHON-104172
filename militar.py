import os 
os.system("cls")

sexo=str(input("digite seu sexo"))
ano_de_nascimento=int(input("digite seu ano de nascimento:"))

if sexo=="masculino" and ano_de_nascimento<=2005:
    mostre=("voce pode se alistar")
else:
    mostre=("voce nao pode se alistar")
print(mostre)
