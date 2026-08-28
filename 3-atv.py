import os 
os.system("cls")

numero1 =int(input("digite seu primeiro numero:"))
numero2 = int(input("digite seu segundo numero:"))
numero3 = int(input("digite seu tesceiro numero:"))

maior= max(numero1, numero2, numero3)
menor= min(numero1, numero2, numero3)

print(f"o maior numero {maior} e o menor numero {menor}")
