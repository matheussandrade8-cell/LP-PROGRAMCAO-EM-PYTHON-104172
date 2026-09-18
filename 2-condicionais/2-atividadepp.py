import os
os.system("cls")

nome=input("digite o seu nome:")
sexo=input("digite o seu sexo (F/M):").upper()
estado_civil=input("digite seu estado civil:").upper()

if sexo== "F" and estado_civil =="CASADA":
    tempo_casada=int(input("digite o seu tempo de casada:"))

    print(f"{nome}")
    print(f"{sexo}")
    print(f"{estado_civil}")

if sexo== "F" and estado_civil =="CASADA":
    print(f"{tempo_casada} anos")