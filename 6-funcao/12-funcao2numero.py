import os
os.system("cls")

def calcular_soma(nota1, nota2):
    calculo=nota1 + nota2
    return calculo

def calcular_subtracao(nota1, nota2):
    calculo=nota1 - nota2
    return calculo

def calcular_multiplicacao(nota1, nota2):
    calculo=nota1 * nota2
    return calculo

def calcular_divisao(nota1, nota2):
    calculo=nota1 / nota2
    return calculo

n1=float(input("digite a sua primeria nota:"))
n2=float(input("digite a sua segunda nota:"))

adicao=calcular_soma(n1, n2)
subtracao=calcular_subtracao(n1, n2)
multiplicacao=calcular_multiplicacao(n1, n2)
divisao=calcular_divisao(n1, n2)

print(f"AdIção:{adicao}")
print(f"Subtração:{subtracao}")
print(f"Multiplicação:{multiplicacao}")
print(f"Divisão:{divisao}")