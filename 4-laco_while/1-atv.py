import os
os.system("cls")

while True:
    n=float(input("digite sua nota "))
    if n< 0 or n > 10:
        print()
        print("nota invalida")
    else:
        print(f"sua nota é {n} ")
        break
print("fim")
