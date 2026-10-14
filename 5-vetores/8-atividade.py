import os
os.system("cls")
vetor_numero=[]

pares=0
impares=0

for i in range(6):
    numero=int(input(f"digite {i+1}º seu numero:"))
    vetor_numero.append(numero)
    
    if numero % 2 ==0:
        pares +=1
    else:
        impares+=1
    print(f"pares: {pares}")
    print(f"impares: {impares}")

for posicao, numero in enumerate(vetor_numero, start=1):
        print(f"{posicao}º: {numero}")

