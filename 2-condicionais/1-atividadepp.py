import os
os.system("cls")

a = int(input("digite o valor A:"))
b = int(input("digite o valor B:"))
c = int(input("digite o valor C:"))

resultado = a + b < c

match resultado:
    case True:
        print(" A + B é menor que C")
    case False:
        print("A + B é maior que C")