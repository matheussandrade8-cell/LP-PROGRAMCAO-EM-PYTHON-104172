import os
os.system("cls")

def numero_negativo():
    if numero >1:
        resultado= "positivo"
    elif numero == 0:
        resultado= "neutro"
    else:
        resultado= "negativo"
    return resultado

numero=int(input("digite o numero:"))

resultado_final =   numero_negativo()
print(f" O numero {numero} é {resultado_final}")