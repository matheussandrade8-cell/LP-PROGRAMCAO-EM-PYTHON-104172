import os 
os.system("cls")

altura =float(input("digite seu altura:"))
sexo=input("escolha seu sexo (M ou F):").upper()

match sexo:
    case "M":
        peso_ideal = (72.7 * altura) - 58
        print(f"Peso ideal: {peso_ideal} kg")

    case "F":
        peso_ideal = (62.1 * altura) - 44.7
        print(f"Peso ideal: {peso_ideal} kg")

    case _:
        print("Sexo inválido!")
