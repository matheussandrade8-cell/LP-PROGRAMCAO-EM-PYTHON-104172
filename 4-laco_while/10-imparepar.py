import os
os.system("cls")

pares=0
impares=0
soma_pares=0
soma_total=0

n=int(input("digite um numero:"))
while n !=0:
    soma_total +=n
    if n % 2 ==0:
        pares +=1
        soma_pares +=n
    else:
        impares+=1

        n=int(input("digite um numero:"))

    print(f"pares: {pares}")
    print(f"impares: {impares}")

    if pares > 0:
        print("Media dos pares", soma_pares / pares)
    print("media geral:", soma_total/ (pares+impares))
    break