import os
os.system("cls")

numero1 =float(input("digite o numero 1:"))
numero2 =float(input("digite o numero 2:"))
usar = input("digite um caracter para calculo(+,-,* ou /)")

match usar:
    case "+":
        calculo=print(f"a soma entre {numero1} e o {numero2} é {numero1+numero2}")
    case "-":
        calculo=print(f"a subtração entre {numero1} e o {numero2} é {numero1-numero2}")
    case "*":
        calculo=print(f"a multiplicação entre {numero1} e o {numero2} é {numero1*numero2}")
    case "/":
        calculo=print(f"a divisão entre {numero1} e o {numero2} é {numero1/numero2}")
    case _:
        (":(")
print(calculo)
