import os
os.system("cls")
import time
vetor=[]
negativo=0

for i in range(5):
        numero=int(input(f"digite {i+1}º numero:"))
        if numero<0:
            negativo+=1
            numero=0
        else:
            numero=numero
        vetor.append(numero)
print(f"vetor {vetor}")
print(f"quantidade de numero negativo {negativo}")
time.sleep(2)
