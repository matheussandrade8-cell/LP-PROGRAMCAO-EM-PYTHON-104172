import os 
os.system("cls")
#inicio
peso= float(input("digite seu peso: "))
altura= float(input("digite sua altura: "))

#Processo.
Imc=peso/(altura*altura)

if Imc < 18.5:
    indice=("abaixo do peso")
elif Imc >= 18.5 > 24.9:
    indice=("peso ideal parabens")
elif Imc >= 25.0 > 29.9:
    indice=("levemente acima do peso")
elif Imc >= 30.0 > 34.9:
    indice=("obesidade grau 1")
elif Imc >= 35.0 > 40.0:
    indice=("obesidade grau 2 ")
else:
    indice=("obesidade morbida")
#fim.
print(f"sua condicao é {indice}")