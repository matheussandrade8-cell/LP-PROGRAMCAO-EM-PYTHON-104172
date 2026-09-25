import os 
os.system("cls")

pares=0
impar=0
Q=5

for i in range(Q):
    n=int(input("digite o numero:"))
    if  i % 2==0:
        pares=pares +1
    else:
        impar=impar +1

print(f"quantidae de pares: {pares}")
print(f"quantidae de impar: {impar}")