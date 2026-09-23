import os
os.system("cls")
QUANTIDADE=3
pares=0
impares=0

for i in range(QUANTIDADE):
    n=int(input("digite um numero:"))
    if i % 2 ==0:
        pares= pares + 1
        # ou +=1
    else:
        impares= impares + 1
        # ou +=1

print(f"quantidade de pares: {pares}:")
print(f"quantidade de impares: {impares}:")

