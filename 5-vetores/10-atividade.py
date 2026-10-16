import os
os.system("cls")
vetor_numero=[]
soma=0
negativo=0

for i in range(5):
        numero=int(input(f"digite {i+1}º numero:"))
        vetor_numero.append(numero)
        if numero<0:
            print("numero")
        else:
            negativo=0
print(f"quantidade de numero negativo: {negativo}")
print(f"soma dos numero positivos: {soma}")