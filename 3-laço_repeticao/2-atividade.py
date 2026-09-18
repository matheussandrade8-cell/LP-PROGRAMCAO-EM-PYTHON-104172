import os
os.system("cls")

print("Tabuada")
numero=int(input("digite o numero:"))

print("\ndivisão")
for i in range(1,11):
    print(f"{numero} / {i} = {numero / i}")

print("\nsoma")
for i in range(1,11):
    print(f"{numero} + {i} = {numero + i}")

print("\nmultiplicação")
for i in range(1,11):
    print(f"{numero} * {i} = {numero * i}")

print("\nsubtração")
for i in range(1,11):
    print(f"{numero} - {i} = {numero - i}")

