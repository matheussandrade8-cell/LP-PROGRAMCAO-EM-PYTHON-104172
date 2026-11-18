import os
os.system("cls")

def verificar_peso(peso, altura):
    imc= peso/ (altura*altura)
    return imc

#inicio
peso= float(input("digite seu peso: "))
altura= float(input("digite sua altura: "))

#Processo.
imc = verificar_peso(peso, altura)

if imc < 18.5:
    indice=("abaixo do peso")
elif imc < 75.9:
    indice=("peso ideal parabens")
elif imc < 90.9:
    indice=("levemente acima do peso")
elif imc < 120.9:
    indice=("obesidade grau 1")
elif imc < 150.0:
    indice=("obesidade grau 2 ")
else:
    indice=("obesidade morbida")
#fim.
