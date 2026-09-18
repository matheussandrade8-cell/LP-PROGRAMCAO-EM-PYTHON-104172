import os
os.system("cls")

operacao=input("digite a operação(+,-,* ou /):")
A=int(input("digite o valor de A:"))
B=int(input("digite o valor de B:"))

match operacao:
    case "+":
        Resultado= A + B
    case "-":
        Resultado= A - B
    case "*":
        Resultado= A * B
    case "/":
        Resultado= A / B
    case _:
        print("Resultado invalido")
print(f"Resultado {Resultado}")